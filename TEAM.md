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

## HoangLamMinh-2A202603566

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh**. Phụ trách bản đồ dữ liệu và các phần nối với nó sau khi nhận thẻ S1:

- Câu 2.3 · Phiếu B mục **B3** (`templates/form-b-evaluation-gates.md`): bản đồ dữ liệu của trợ lý hoàn tiền và ví dụ drift trong 3 tháng tới.
- Câu 3.1 (phần riêng thẻ S1) · Phiếu C mục **C3.5** (`templates/form-c-incident.md`): mở lại bản đồ dữ liệu cho các trường của `parcel`.
- Câu 3.2, 3.3 · Phiếu C mục **C5**: specification cho lệnh `file_carrier_fault` và giả định môi trường.

### Đóng góp cụ thể

- **B3:** lập bảng 9 dòng gồm người dùng, việc cần làm, 4 lệnh ghi, dữ liệu đọc lúc chạy và các trường then chốt. Với mỗi trường, ghi rõ là nguồn sự thật hay bản sao. Phát hiện agent chọn chính sách theo cờ `index_active` (bản sao, cập nhật tay) thay vì theo `effective_from/to` (nguồn sự thật).
- **Ví dụ drift (B3):** REFUND-v3 chuyển sang REFUND-v4 ngày 01/12/2026. Đã so sánh v3 và v4 trên từng đơn trong `data/world.json`, chỉ ra các ca bị ảnh hưởng:
  - O-1006 bị ghi lỗi hãng oan cho MKD, vì v4 không còn tính `FORCE_MAJEURE` là lỗi hãng;
  - O-1002, O-1024, O-1016, O-1019 bị hoàn thiếu;
  - hạn mức tự động giảm còn 100.000đ, kéo theo tỉ lệ chuyển người và chi phí.

  Kết luận đây là drift quan hệ vào–ra, kèm đề xuất chỉ số `policy_version_mismatch_count`.
- **C3.5:** 6 dòng cập nhật so với vòng 1.
  - `delivered_date` trống cả khi `status=DELIVERED` (O-2120, O-2121), nên số ngày trễ bị tính theo `as_of`.
  - `status` là trường để phát hiện mâu thuẫn đó.
  - `delay_cause` trống nhưng agent tự gán `CARRIER`.
  - Khách khai số ngày trễ theo cả hai chiều (S1-01…04, S1-07).
  - Bảng lỗi hãng trong ngày, vòng 1 chưa hỏi tới: loạt S1-40…43 vượt trần 2 lỗi/hãng/ngày.
  - `as_of` không được dùng thay ngày giao.
- **C5:** viết specification 4 điều kiện cho việc tự ghi lỗi hãng (đủ dữ liệu, số ngày theo tracking, có nguyên nhân ghi nhận, trong trần theo ngày), giữ khoản hoàn hợp lệ cho khách; ghi cách kiểm trong `write_gate` và dòng report `wrongful_carrier_faults`. Viết giả định môi trường: tracking của hãng và điểm phát luôn đầy đủ, kịp thời; kèm lý do giả định này sai ngoài thực tế.

### Bằng chứng

- Commit `c8bd55d`: *Fill Form B section B3: data map and policy drift example*.
- Commit `8cfee58`: *Fill Form C sections C3.5 (S1 data map) and C5 (spec and environment assumption)*.
- Phiếu B mục B3; Phiếu C mục C3.5 và C5.
- Số liệu dẫn trong C5: mốc prepared `R-S1-prepared-20261118-164604-0dc81f` (15 lỗi hãng oan còn lại), lấy từ C0 của bàn.

### Exit ticket

- **Một điều học được:** phải hỏi từng trường là nguồn sự thật hay bản sao, và trống thì nghĩa là gì. Một giá trị trống (`delivered_date = null`) bị hệ thống lặng lẽ thay bằng ngày hôm nay có thể gây hoàn sai và ghi lỗi oan, mà cổng kiểm tiền vẫn cho qua vì dùng chung phép tính. Ngoài ra, drift kiểu đổi chính sách không làm đổi đầu vào, nên phải theo dõi bằng chỉ số đối chiếu kết quả chứ không bằng phân phối dữ liệu.
- **Một điều còn chưa chắc:** cổng theo specification ở C5 chỉ GIẢM hay thực sự NGĂN được lỗi hãng oan ngoài thực tế. Nó phụ thuộc vào việc `status` và `fault_rows` có đáng tin không, và trên dữ liệu thật tỉ lệ kiện thiếu ngày giao hoặc thiếu nguyên nhân là bao nhiêu. Điều đó cần đo trong pilot.
