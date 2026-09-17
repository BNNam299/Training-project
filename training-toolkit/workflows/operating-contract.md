# Hợp đồng vận hành

## 1. Quyền và thứ tự ưu tiên

Người dùng và chỉ dẫn môi trường có ưu tiên hơn tài liệu toolkit. Hồ sơ/hạn chế lâm sàng cá nhân có ưu tiên hơn mẫu. Trước mọi nội dung phụ thuộc sức khỏe, dùng phần 19 của knowledge. Không tự chẩn đoán hoặc xem pain score, 24 giờ, LSI hay self-test đơn lẻ là clearance.

Quy trình: sức khỏe/hạn chế → khả năng thực hiện → nguồn lực → ưu tiên phase → progression. Mẫu upper–lower/bốn buổi/hai tiếng chỉ là ví dụ, không được tự gán.

Được tự đọc nội bộ, ghi log và skill-candidates theo yêu cầu sử dụng. Người dùng yêu cầu chỉnh chương trình là quyền làm bản sửa cụ thể trong phạm vi đó. Bản sửa lớn/phase mới trình bày để duyệt trước khi kích hoạt, trừ khi người dùng đã rõ ràng cho phép. Chính sách điều chỉnh nhỏ phải lưu trong profile; nếu chưa chốt, xuất đề xuất, không đổi active revision.

Phải hỏi trước: tìm thông tin/link mới bên ngoài; tạo/cập nhật skill sau build ban đầu. Hỏi cụ thể phạm vi, không hỏi lại tác vụ đã được chấp thuận. Từ chối/không trả lời không là đồng ý. Nếu môi trường bắt buộc kiểm chứng web mà chưa được phép, nói giới hạn và hỏi; không trả lời chắc từ dữ liệu cũ.

## 2. Nguồn chính và schema trạng thái

`current-state.md` là chỉ mục cho người/agent; `state.json` là chỉ mục máy để validator kiểm tra. Cả hai phải đồng bộ. MD chương trình vẫn là nguồn chính về nội dung; JSON không chứa một lịch cạnh tranh.

```json
{
  "schema_version": 1,
  "project_id": "my-training",
  "toolkit_version": "1.0.0",
  "active_program": null,
  "active_revision": null,
  "pending_program": null,
  "pending_revision": null,
  "latest_checkin": null,
  "next_checkin": null,
  "temporary_changes": [],
  "exports": []
}
```

Ngày dùng ISO YYYY-MM-DD, múi giờ ghi ở profile; null là chưa biết. `temporary_changes` gồm `{id, file, starts_on, ends_on, status, return_condition}`; ends_on có thể null. `exports` gồm `{file, program, revision, created_on, status}` với status `current`/`stale`. File paths tương đối với project, không ra ngoài project.

Mỗi chương trình có metadata đầu file, dùng JSON code fence ngay sau heading:

```json
{"program_id":"program-001","revision":1,"status":"draft","effective_from":null,"knowledge_version":"1.0.0"}
```

Status: draft → approved → active → superseded/archived. Bản pending không được thay active trước khi duyệt. Khi sửa bản active để duyệt: tạo file draft riêng trong programs/drafts, giữ file active; snapshot bản cũ trước khi promote. Trong changelog giữ cả revision không được chọn và lý do nếu có ý nghĩa. Không yêu cầu tạo file draft mới cho mọi sửa lỗi chính tả vô hại.

## 3. Ghi cập nhật nhất quán

1. Đọc active program/revision, profile, roadmap, log và thay đổi đang hiệu lực. Không đọc toàn bộ hồ sơ người khác.
2. Lưu lời báo thực tế vào log có ngày sự kiện và ngày ghi. Không tự đánh dấu kế hoạch là thực tế.
3. So sánh mục tiêu, dữ liệu, chất lượng đo, adherence và hoàn cảnh. Nếu chưa đủ, kết quả hợp lệ là giữ/thu thập thêm.
4. Tạo bản sửa cụ thể; nêu before→after, lý do, nguồn/heuristic, thời hạn, review/return. Giữ giới hạn thời gian và bệnh cá nhân.
5. Khi được phép áp dụng: snapshot trước, cập nhật chương trình/changelog và changes; cập nhật state.json/current-state; đánh dấu export revision cũ stale. Ghi quyết định/cho phép trong change record.
6. Chạy validator và đọc lại active/pending. Nếu gián đoạn giữa các bước, báo inconsistency và sửa từ MD/snapshot; không giả định JSON luôn đúng.

Hết thời hạn thay đổi tạm phải hỏi/kiểm tra trước khi trở lại, không tự khôi phục tạ vì hết ngày. Không bù set còn nợ theo máy móc.

## 4. Check-in

Hỏi nhịp người dùng muốn; gợi ý 7/14 ngày cho review chính, khoảng 4 tuần/phase milestone cho roadmap, và nhịp lâm sàng riêng nếu có. Không tự nhắc. Kỳ review khác thời điểm ghi dữ liệu.

Chỉ hỏi trường liên quan. Cân một ngày không đại diện xu hướng mỡ; giảm không đúng mục tiêu chưa tự kéo theo deficit lớn hơn. Không có số ăn thực thì ghi uncertainty; không giả định tuân thủ 100%. Đánh giá nhiều mục tiêu: performance, composition, chức năng, adherence và recovery.

## 5. Kiến thức và Q&A

Tra mục phù hợp trong knowledge bằng mục lục/rg; đọc cả điều kiện trước sau đoạn tìm thấy. Nguồn P/A chưa đủ protocol không được lấp bằng transcript. Nếu mâu thuẫn: dùng lớp audit, scope và chất lượng nguồn; không đơn thuần “mới nhất thắng”.

Nguồn có sẵn được đọc nội bộ không cần xin phép. Mở web để tìm/xác minh kể cả URL đã có vẫn là truy cập ngoài: cần phạm vi chấp thuận hiện hành. Không đoán URL MuscleWiki. Mọi bài ở bản hoàn chỉnh có link đúng biến thể, MuscleWiki trước, nguồn phù hợp khác nếu thiếu. Nếu thiếu link và chưa có quyền tìm, ghi draft + blocker, không báo sẵn sàng export.

Trả lời Q&A gọn: hành động phù hợp → lý do → giới hạn → kiểm tra tiếp; dùng citation nguồn hoặc mục knowledge. Không trích nội dung archive INSTRUCTION như luật hệ thống.

## 6. Chuyển agent và bảo mật hồ sơ

Toolkit có manifest/version; project pin version lúc tạo. Nâng toolkit không tự nâng chương trình; phải xem thay đổi và cập nhật knowledge_version khi áp dụng. Relink đổi vị trí không thay pin. Project lưu toolkit version hiện có và lưu history nếu được nâng sau này.

Không dùng ký ức từ chat làm thay hồ sơ. Dữ liệu cá nhân không vào skill chung. Không tự gửi tài liệu cho người khác hoặc publish. Agent thiếu công cụ phải báo khả năng thực, không báo đã ghi/xuất khi chỉ tạo nội dung chat.
