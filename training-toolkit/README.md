# Toolkit tập luyện qua agent

Phiên bản 1.0.0. Chạy bằng hội thoại và file; không có app, tài khoản hoặc nhắc tự động. Dùng với Codex, Claude hoặc agent có khả năng đọc/ghi file. Chỉ dẫn không thay quy định của môi trường đang chạy.

## Bắt đầu

Đưa cả thư mục này cho agent và nói:

> Đọc AGENTS.md và workflows/operating-contract.md trong training-toolkit. Khởi tạo project riêng cho tôi; hỏi đầu vào từng bước rồi đề xuất hành trình. Chưa dựng chương trình cá nhân khi thiếu dữ liệu quyết định.

Có thể khởi tạo khung bằng Python 3 (thư viện chuẩn, không cần mạng):

```text
python scripts/init_project.py --project ../personal-projects/my-training --name "Tên hiển thị"
```

Sau đó mở thư mục project trong agent. `AGENTS.md`/`CLAUDE.md` của project dẫn về toolkit. Nếu di chuyển toolkit/project, chạy lại liên kết:

```text
python scripts/relink_project.py --project ../personal-projects/my-training --toolkit .
```

Project khác phải có đường dẫn khác. Khởi tạo từ chối ghi vào thư mục đã tồn tại. Không tạo sẵn hồ sơ thật dựa trên ví dụ brainstorm.

## Tiếp tục và check-in

> Đọc current-state.md của project, chương trình hiện hành và các log gần nhất. Tôi đã tập A và một phần B; tuần này chỉ còn tối thứ sáu 45 phút. Hãy tổ chức lại phần còn lại và lưu thay đổi cùng phạm vi hiệu lực.

> Đến kỳ check-in. Hãy dùng khung đã thống nhất, hỏi phần còn thiếu và đánh giá trước khi quyết định có cần sửa chương trình.

> Giải thích vì sao chọn bài này, dùng kiến thức nội bộ trước. Nếu thiếu căn cứ, hãy hỏi tôi trước khi tìm bên ngoài.

## Tài liệu và skill

| Việc cần làm | Đọc |
|---|---|
| Toàn bộ yêu cầu sản phẩm | [brief.md](brief.md) |
| Quyền, trạng thái, ghi lịch sử | [Operating contract](workflows/operating-contract.md) |
| Intake, roadmap, chương trình và dinh dưỡng | [training-plan](skills/training-plan/SKILL.md) |
| Check-in, lịch gián đoạn, đổi phase | [training-review](skills/training-review/SKILL.md) |
| Q&A, nguồn, link từng bài | [training-qa](skills/training-qa/SKILL.md) |
| Xuất Word/Excel sau duyệt | [training-export](skills/training-export/SKILL.md) |
| Ghi nhận và đề xuất skill mới | [training-learning](skills/training-learning/SKILL.md) |
| Kiến thức hợp nhất | [knowledge.md](knowledge.md) |
| Tài liệu chi tiết và bản người dùng | [references/16-tong-hop-tai-nguyen.md](references/16-tong-hop-tai-nguyen.md) |
| Phạm vi chưa đủ kiến thức | [references/25-doi-chieu-mau-thuan-va-khoang-trong.md](references/25-doi-chieu-mau-thuan-va-khoang-trong.md) |
| Tình huống nghiệm thu hành vi | [acceptance/scenarios.md](acceptance/scenarios.md) |

Tên bài tiếng Anh; hướng dẫn tiếng Việt. Kho nguồn đầy đủ không đồng nghĩa đã kiểm chứng mọi phát biểu. File MD hợp nhất giữ lớp kiến thức đã biên soạn/đối chiếu; các phần gốc 01–15 và tám tài liệu người dùng vẫn nằm nguyên trong references để tra sâu.

## Công cụ và kiểm tra

- Python 3: khởi tạo, đổi liên kết, snapshot và kiểm tra trạng thái; không dùng mạng.
- Agent có trình duyệt: chỉ sử dụng khi đã được cho phép tìm/kiểm chứng bên ngoài cho tác vụ đó.
- Word/Excel: dùng công cụ artifact của agent hoặc thư viện tương ứng; layout contract/template đi kèm. Không yêu cầu plugin riêng.
- Không tự cài global skill hay thay cấu hình Codex/Claude. Đọc skill bằng đường dẫn là cách chạy mặc định.

```text
python scripts/validate.py
python scripts/validate.py --project ../personal-projects/my-training
python scripts/snapshot_program.py --project ../personal-projects/my-training --program programs/program-001.md
```

Snapshot phải tạo trước khi sửa kế hoạch đã tồn tại. Validator kiểm tra cấu trúc, liên kết và trạng thái; không chứng minh tính đúng y khoa hoặc hiệu quả giáo án. Xem [BUILD-REPORT.md](BUILD-REPORT.md) để biết đã kiểm tra gì và giới hạn.

## Gói bàn giao

Toàn bộ brief, kiến thức, nguồn, skill, mẫu và script nằm trong chính thư mục `training-toolkit/`; xem [PACKAGE-CONTENTS.md](PACKAGE-CONTENTS.md). File ZIP phát hành nằm trong `distribution/` và được tạo lại bằng:

```text
python scripts/build_release.py
```

Script từ chối ghi đè để tránh thay một bản phát hành mà không nhận biết. Khi phát hành phiên bản mới, cập nhật version/manifest và dùng tên ZIP mới. Project cá nhân được tạo bên ngoài thư mục toolkit và không đưa vào package dùng chung.
