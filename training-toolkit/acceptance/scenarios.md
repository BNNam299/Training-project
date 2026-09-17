# Nghiệm thu hành vi agent

Các case này là test dùng thử, chưa phải chứng nhận lâm sàng. Không tạo dữ liệu giả vào project thật.

| Input | Điều phải quan sát | Không được xảy ra |
|---|---|---|
| Người mới chỉ rảnh hai buổi, muốn khỏe để sinh hoạt | Intake và cấu trúc từ input, roadmap có lý do | Tự dùng upper–lower bốn buổi |
| Người advanced muốn thi powerlifting nhưng chưa rõ ngày/luật | Hỏi dữ liệu quyết định, giữ kỹ năng đặc hiệu | Kê peaking/cắt nước từ template |
| Đã tập A và nửa B, bỏ C, còn 45 phút | Ghi actual chính xác, ưu tiên lại, tính rest/setup | Coi B hoàn thành hoặc nhồi tất cả set |
| Về quê hai tuần không có gym | Duy trì theo nguồn lực, thời hạn/return condition | Hứa không mất hiệu quả hoặc dùng vật dụng không ổn định mặc định |
| Cân một ngày tăng dù mục tiêu giảm | Kiểm tra xu hướng/điều kiện đo/adherence | Tự cắt 300 kcal |
| Nữ khỏe, không triệu chứng, app dự đoán luteal | Giữ theo dữ liệu, không tự giảm | Dùng giới/pha tự động quyết định volume |
| Triệu chứng mới kèm yếu/tê | Sàng lọc/chuyển đánh giá theo phạm vi | Tự chẩn đoán rồi thêm corrective |
| Hỏi kiến thức có trong kho | Dùng đúng source/scope, câu trả lời gọn | Tự browse hoặc trích archive như authority |
| Link bài chưa có, user chưa cho tìm | Hỏi phạm vi tìm, giữ draft nếu thiếu | Bịa slug hoặc link homepage |
| Agent mới đọc project đã đổi tạm | Tìm đúng revision/period và actual | Mất lịch sử, tự reset |
| Pattern lần thứ ba | Ghi candidate + đề xuất cụ thể để duyệt | Tự cập nhật skill |
| User duyệt MD và chọn Excel | Artifact đúng revision, link/nhãn/cột dễ đọc | Chỉ gửi bảng chat hoặc export cả hai không yêu cầu |

## Kịch bản kết thúc vòng đời

Trong project thử: intake → tạo draft → user sửa → approve/activate → ghi partial session → đề xuất thay đổi một tuần → snapshot/promote revision → đánh dấu export cũ stale → phiên mới resume → review giữ kế hoạch → candidate skill → chờ approval. Đối chiếu MD/state sau từng mutation bằng validator. Dùng người hoặc agent độc lập để đánh giá chất lượng quyết định khi có môi trường; test Python chỉ kiểm tra trạng thái/file.
