# Team

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
|   3 |Nguyễn Thanh Thúy     |      2A202603523|   Vận hành và pháp lý|           |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## DinhThiHuong-2A202603569

### Phần việc phụ trách

Tôi là trưởng nhóm, phụ trách vai Kỹ sư cổng: thiết lập repo, ký và lưu tiêu chí sau khi thống nhất; chạy eval/gate/trace, phân tích ca lỗi, tổ chức phần code cổng và monitor. Các phần liên quan gồm Phiếu A; Phiếu B B0–B2, B6–B8; Phiếu C C0–C2, C6 và phần tổng hợp sau sửa. Minh và Thúy thực hiện các phần theo phân công, thể hiện qua commit riêng; tôi phối hợp tổng hợp hồ sơ.

### Đóng góp cụ thể

- Chuẩn bị repo nhóm, kiểm tra 13 test công khai và thực hiện ký/commit tiêu chí trước lần đánh giá đầu tiên.
- Chọn eval card và PRD v1.1 từ Lab 9 của tôi làm tài liệu chung; rà soát và chấp nhận bộ ngưỡng đề xuất trước khi ký, không sửa tiêu chí theo kết quả chạy.
- Trực tiếp chạy baseline, gate và trace T-002@55; cung cấp output để phân tích lỗi lời khách đè dữ kiện tracking. Nhận thẻ S1, chạy grade và hai trace prepared S1-07@11, S1-20@11.
- Phối hợp phân tích ba lỗ hổng: từ chối oan ngoài nhánh chi tiền, trạng thái DELIVERED thiếu ngày giao và vượt trần lỗi tự động/hãng/ngày. Yêu cầu triển khai, kiểm tra và tổng hợp cổng vòng 1/vòng 2, monitor, Phiếu C và bộ submission.
- Giữ kết luận Cải tiến thêm khi S1 hết ticket sai nhưng chi phí/ROI chưa đạt; ghi nhận integrity còn lỗi cần Lab Coach xác minh, không coi bộ nộp đủ thành phần là đã đạt mọi kiểm tra.

**Sử dụng AI:** Tôi dùng ChatGPT/Codex để giải thích yêu cầu, soạn Phiếu A và JSON tiêu chí, soạn các phần phiếu thuộc công việc của tôi và phần tổng hợp, đọc code/trace, trực tiếp hỗ trợ sửa guards.py, thêm monitor, chạy kiểm tra và gom submission. Không trình bày các phần AI soạn hoặc chạy thay là tôi tự viết/chạy hoàn toàn. Nội dung này là bản tổng hợp có AI hỗ trợ; tôi cần rà soát và giải thích được các ngưỡng, cổng và quyết định khi demo.

### Bằng chứng

- Commit ký tiêu chí: `618d9d5`; hash tiêu chí `4c1f87936146`.
- Baseline: `R-base-before-20261118-152709-bde05c`, pass_rate 0.9909, hoàn sai 20.000đ, một lỗi hãng oan; Phiếu B B0–B2.
- Chốt vòng 1: hash `ae2e5687`; prepared `R-base-prepared-20261118-160153-0dc81f`, pass_rate/pass_k=1.0, không lỗi an toàn.
- Commit phần phân tích S1 C0–C2/C6: `6521787`; nhận thẻ S1: `f468124`.
- Grade trước sửa S1: `R-S1-grade-20261118-164604-0dc81f`; trace S1-07@11 và S1-20@11 ở mốc prepared.
- Grade sau sửa: `R-S1-grade-20261118-172233-7feb82`; S1 65/65 và bộ nền 110/110 đúng, 13 public tests OK, monitor mới hoạt động. S1 cost 8.246đ/ticket, ROI 0,21 chưa đạt; integrity còn lỗi. Thay đổi vòng 2 chưa có mã commit tại thời điểm viết mục này.

### Exit ticket

*Bản gợi ý để tôi rà soát, sửa theo trải nghiệm thực tế trước khi nộp:*

- **Một điều học được:** Cổng chỉ kiểm lúc hoàn tiền vẫn có thể bỏ sót việc từ chối oan. Cần kiểm cả quyết định không chi tiền và tính nhất quán của dữ liệu nguồn; tỉ lệ đúng cao không thay thế kiểm tiền, quyền lợi đối tác và chi phí vận hành.
- **Một điều còn chưa chắc:** Khi nhiều yêu cầu cùng ghi lỗi cho một hãng trong production, cần thiết kế kiểm trần và ghi sổ nguyên tử như thế nào để không vượt trần; đồng thời làm sao giảm chi phí xác minh mà vẫn giữ các ngưỡng an toàn đã ký.
