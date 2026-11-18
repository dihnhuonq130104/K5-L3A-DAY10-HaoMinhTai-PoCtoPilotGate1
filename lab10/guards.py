"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("Không tìm thấy chính sách có hiệu lực: chuyển người xác minh")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault"):
        return Verdict.allow()
    order = ctx.tools.lookup_order(action.get("order_id"))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not policy or not order.get("parcels"):
        return Verdict.escalate("Thiếu đơn, kiện hoặc chính sách để kiểm chứng lệnh ghi")
    if order.get("customer_id") != ctx.ticket.get("customer_id"):
        return Verdict.escalate("Đơn không thuộc khách đang yêu cầu")
    if ctx.ticket.get("parcel_id") and not any(
        p["parcel_id"] == ctx.ticket["parcel_id"] for p in order["parcels"]
    ):
        return Verdict.escalate("Kiện yêu cầu không thuộc đơn")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    if tool == "issue_refund":
        expected = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        amount = action.get("amount_vnd", 0)
        if amount <= 0 or amount != max(0, expected - paid) or action.get("payer", "LOGIX") != "LOGIX":
            return Verdict.escalate("Khoản hoàn không khớp quyền lợi theo tracking, chính sách và lịch sử hoàn")
        approval_id = action.get("approval_id")
        if approval_id or amount > policy["auto_limit_vnd"]:
            approvals = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
            valid = any(
                a.get("status") == "valid"
                and a.get("order_id") == order["order_id"]
                and a.get("customer_id") == ctx.ticket.get("customer_id")
                and a.get("ticket_id") == ctx.ticket.get("ticket_id")
                and (not ctx.gates.get("operations", {}).get("approver_id") or a.get("approver_id") == ctx.gates["operations"]["approver_id"])
                and a.get("expires_at", "") >= ctx.as_of
                and a.get("max_vnd", 0) >= amount
                for a in approvals
            )
            if not valid:
                return Verdict.escalate("Chưa có phê duyệt hợp lệ cho đúng giao dịch")
    if tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("Tracking và chính sách không đủ căn cứ ghi lỗi hãng")
        if any(action.get(k) != parcel.get(k) for k in ("parcel_id", "carrier_id", "driver_id")) or action.get("delay_days") != delay:
            return Verdict.modify("Ghi lỗi đúng kiện, hãng và số ngày từ tracking",
                                  parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                                  driver_id=parcel.get("driver_id"), delay_days=delay)
    return Verdict.allow()
