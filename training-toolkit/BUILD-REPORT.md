# Báo cáo build 1.0.0

## Đã triển khai

- Điểm vào AGENTS.md/CLAUDE.md; README hướng dẫn chạy trực tiếp, không cài global.
- Brief trong package; 38 file Markdown nguồn gồm 00–29 và tám bản người dùng, giữ nguyên byte, SHA-256 trong manifest.
- knowledge.md hợp nhất đầy đủ nội dung biên soạn phần 17–28 với link điều chỉnh về references; không thay bản nguồn bằng tóm tắt ngắn.
- Năm skill: thiết kế, review/thích ứng, Q&A/nguồn, export, tích lũy ứng viên skill.
- Mẫu hồ sơ/roadmap/chương trình/check-in/change/skill-candidates; contract trạng thái và layout Word/Excel.
- Script Python chuẩn: init project, relink, snapshot, validator, package knowledge và tests. Không truy cập mạng hoặc yêu cầu API.
- Gói ZIP portable được đặt trong `distribution/`; script build loại cache, dữ liệu test và chính thư mục phát hành để tránh đóng gói đệ quy.

## Kiểm tra

Test tự động dùng project tạm và dữ liệu giả: tách ID người dùng; từ chối ghi đè; snapshot nguyên byte; chặn path traversal; phát hiện lệch revision/chỉ mục; pending không ghi đè active; export cũ; relink giữ dữ liệu/pin; khoảng thời gian thay đổi hợp lệ.

Validator bundle kiểm tra hash nguồn/knowledge, link nội bộ tài liệu vận hành và frontmatter skill. Tài liệu nguồn giữ nguyên có thể có lỗi định dạng cũ; không coi chúng là active instruction.

Kết quả chạy: **8 test tự động đạt; validator bundle 0 lỗi; cả 5 skill đạt quick_validate của skill-creator**. PyYAML chỉ được dùng trong thư mục kiểm tra `.tests/deps`, không là phụ thuộc runtime hoặc nằm trong bản ZIP bàn giao.

## Giới hạn kiểm chứng

Chưa chạy một phiên Claude thực hoặc đánh giá độc lập hành vi của model; tương thích dựa trên Markdown, file I/O và Python chuẩn. Checklist ca hội thoại ở acceptance/scenarios.md để kiểm tra khi dùng. Test script không chứng nhận quyết định y khoa hoặc hiệu quả chương trình.

Export được triển khai thành skill/quy trình và đặc tả layout để agent tạo file bằng công cụ sẵn có; **không có renderer DOCX/XLSX độc lập trong package**. Chưa xuất giáo án cá nhân vì chưa intake/duyệt chương trình và người dùng chưa chọn định dạng. Agent phải kiểm tra artifact khi thực sự xuất, không được báo đã render nếu chưa làm.

Không nhập toàn bộ MuscleWiki hoặc tạo link đoán. Không tự lấp các nhánh kiến thức chưa thẩm định; Q&A phải hỏi tìm ngoài khi cần. Thư mục research trung gian (Python dependencies, snapshots web, PDF tải) không đóng gói; toàn bộ MD nghiên cứu và nguồn người dùng được giữ.
