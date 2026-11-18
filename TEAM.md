## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HaoMinhTai
- Lớp: `L3A`
- Repo của bàn: https://github.com/dihnhuonq130104/K5-L3A-DAY10-HaoMinhTai-PoCtoPilotGate1.git
- Thẻ sự cố đã bốc (S1–S8): S1

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |Đinh Thị Hường           |    2A202603569  |     Kỹ sư cổng|  x           |
|   2 |Hoàng Lam Minh    |    2A202603566|Sản phẩm và kinh doanh     |             |
|   3 |Nguyễn Thị Thanh Thúy     |      2A202603523|   Vận hành và pháp lý|           |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenThiThanhThuy-2A202603523

### Phần việc phụ trách

Vận hành và pháp lý: Phiếu A câu 1.2, câu 1.4; Phiếu B câu 2.4, checklist go-live, cổng `operations`/`legal`, runbook phần 1–3 và giờ cao điểm; với thẻ S1, Phiếu C mục C3.5, C4, C11 và thông tin nộp bài.

### Đóng góp cụ thể

Soạn mục tiêu cho kế toán đối soát và trưởng ca; thiết kế telemetry phát hiện payload gửi hãng còn chứa trường PII bị cấm. Đặt ngưỡng SLA 60 phút, công suất 6 ca/giờ và điều kiện dừng; cấu hình PIC/người duyệt, kiểm mẫu 10%, ghi chú quyết định; chặn `customer_note`/`recipient_contact` và yêu cầu cause tracking được ghi nhận. Với S1, bổ sung phân tích HAZOP về lời khách lệch tracking, thiếu `delivered_date` và trần lỗi cộng dồn theo hãng/ngày; mở lại bản đồ dữ liệu và checklist/runbook sau sự cố. Đã dùng trợ lý AI để rà soát repo và soạn phần này. Các ngưỡng vận hành, kênh báo tin và người dự phòng cần nhóm xác nhận trước pilot thật.

### Bằng chứng

`config/operating_gates.json`; Phiếu A A1.2/A2; Phiếu B B4/B5/B7.5/B7.6; Phiếu C C3.5/C4. Tiêu chí đã ký ở commit `618d9d5` (hash `4c1f8793`); baseline `R-base-before-20261118-152709-bde05c`; S1 prepared `R-S1-prepared-20261118-164604-0dc81f` và grade `R-S1-grade-20261118-164604-0dc81f`. Grade S1 còn FAIL integrity/visible/monitor; chưa có kết quả `after`, nên chưa kết luận pilot đạt. C4 được commit trong `1c3c28b`.

### Exit ticket

Học được rằng người trực cũng là một giới hạn năng lực có thể định lượng bằng SLA và throughput. Chưa chắc kênh cảnh báo và người dự phòng nào sẽ được dùng thật; cần chốt trước pilot.
