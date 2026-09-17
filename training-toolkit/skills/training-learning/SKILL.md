---
name: training-learning
description: Ghi nhận cách giải quyết lặp lại thành ứng viên skill và chuẩn bị đề xuất tạo/cập nhật skill cho người dùng duyệt; không tự thay skill chung.
---

# Học từ quá trình sử dụng

Đọc project skill-candidates và [contract](../../workflows/operating-contract.md). Tự ghi vấn đề, trigger/input, giải pháp, lý do, exception, các case tương tự/khác, outcome thực đã quan sát, unknown và đề xuất. Một lần hợp lý chưa là hiệu quả đã kiểm chứng.

Không giữ thông tin định danh trong skill dùng chung. Dữ liệu chi tiết ở project; chỉ khái quát có căn cứ khi đề xuất. Tách giải pháp huấn luyện khỏi guideline lâm sàng cần thẩm định.

Khi đủ giá trị tái sử dụng, so skill hiện có để tránh trùng. Chuẩn bị đề xuất cụ thể/diff: tên, trigger, phạm vi, nội dung, điều kiện không áp dụng, ảnh hưởng, căn cứ và cách kiểm tra. **Hỏi user trước khi tạo hoặc sửa skill.** Lưu approval với ngày/phạm vi; pending/declined không được thực hiện.

Sau khi được duyệt: dùng quy trình skill-creator của môi trường nếu có; viết SKILL.md có name/description, chỉ dẫn ngắn và reference cần thiết. Kiểm tra ca thành công, ngoại lệ và missing data. Ghi version/changelog, cập nhật candidate status và không tự migrate chương trình cá nhân.
