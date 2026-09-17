---
name: training-export
description: Xuất chương trình Markdown đã duyệt thành Word hoặc Excel dễ sử dụng, giữ đúng revision, tiếng Việt và hyperlink từng bài; chỉ xuất khi người dùng chọn định dạng.
---

# Export bản đã duyệt

Đọc [layout contract](../../workflows/export-layout.md), [contract](../../workflows/operating-contract.md), program active/approved và state. Bản draft chưa đủ link/dữ liệu không được báo hoàn chỉnh. Hỏi định dạng nếu user chưa chọn; không tự làm cả hai.

Kiểm tra công cụ: dùng skill documents/spreadsheets của môi trường nếu có và phù hợp, hoặc thư viện docx/xlsx. Không yêu cầu API riêng. Thiếu khả năng tạo file thì báo cụ thể, giữ MD; không gọi bảng chat là artifact. Không tự cài package bằng mạng khi chưa có quyền cần thiết.

Ánh xạ từ MD đã duyệt, giữ program ID/revision/ngày. Tách lịch, dinh dưỡng, quy tắc, ghi thực tế tùy nhu cầu. Tên bài tiếng Anh/hyperlink; phần còn lại tiếng Việt. Tóm gọn quy tắc nhưng giữ condition/action/review và giới hạn quan trọng.

Sau tạo: kiểm tra số buổi/bài và các giá trị so MD, link từng bài, cộng macros/đơn vị, khả năng đọc và ngắt trang. Với công cụ render, xem trang/sheet đại diện và trang dài; không báo đã kiểm tra hình nếu chỉ đọc XML. Nếu không render được, nói giới hạn kiểm tra. Lưu artifact `exports/<program>-r<revision>-<date>.<ext>`, không ghi đè bản cũ khác revision.

Cập nhật state.exports và MD program mục bản xuất. Nếu chương trình đổi sau đó, bản cũ stale; khi user báo sửa trực tiếp Word/Excel, đọc/đối chiếu thay đổi rồi ghi vào MD, không tự coi artifact là nguồn mới nhất.
