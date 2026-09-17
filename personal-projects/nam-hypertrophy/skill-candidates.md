# Ứng viên skill

Agent được tự ghi ứng viên; **tạo hoặc sửa skill phải có đồng ý riêng của user** (AGENTS.md). Tính đến 2026-09-16 **chưa có skill nào được tạo hoặc sửa**.

Mỗi ứng viên lưu ID, vấn đề, trigger/input, cách xử lý, căn cứ, ngoại lệ, các case tương tự/khác, kết quả đã quan sát và unknown. Đề xuất skill mới hay sửa skill hiện có; không chép thông tin cá nhân vào skill chung.

Trạng thái: observed → proposed → approved/declined → implemented → reviewed. Ghi phê duyệt ngày/phạm vi và version khi triển khai; không suy từ số lần gặp rằng đã chứng minh hiệu quả.

---

## SC-01 — Lấy transcript YouTube qua trình duyệt thật

- **Trạng thái:** observed · ghi ngày 2026-09-16 · **chưa đề xuất tạo skill**
- **Đề xuất:** sửa [training-qa](../../training-toolkit/skills/training-qa/SKILL.md), không tạo skill mới. Đây là kỹ thuật lấy nguồn, đúng phạm vi training-qa.

**Vấn đề.** User cung cấp link video làm tài nguyên. Cần transcript để tiếp nhận, nhưng mọi đường tự động đều hỏng.

**Trigger.** User gửi link YouTube và yêu cầu tiếp nhận nội dung làm kiến thức.

**Cách xử lý đã dùng được.**

1. Mở **tất cả** video thành tab riêng trong một session/tab group.
2. Mở sẵn phần mô tả và cuộn nút «Hiện bản chép lời» vào giữa màn hình ở từng tab.
3. **Yêu cầu user tự bấm** nút đó ở mọi tab, một lượt.
4. Đọc DOM từng tab, **có xác minh** đang ở đúng video trước khi đọc.

**Bốn cái bẫy đã gặp — đây là phần đáng ghi nhất.**

| Bẫy | Biểu hiện | Xử lý |
|---|---|---|
| YouTube bỏ qua click tổng hợp | Panel transcript mở nhưng **không nạp nội dung**; `click` và cả CDP `Input.dispatchMouseEvent` đều vô hiệu | Phải để user bấm — click của user là `isTrusted` |
| `find_tab` khớp URL lỏng | Hỏi tab `watch?v=A`, daemon trả về tab `watch?v=B` vì chỉ khớp tới `/watch`. **Kết quả: 4/6 file bị gán nhầm video** | Sau `find_tab`, **poll `location.href` cho tới khi đúng video id** rồi mới đọc; và kiểm tra lại id trong chính kết quả đọc |
| Panel render nội dung hai lần | Transcript dài gấp đôi, nửa sau lặp y nguyên nửa đầu | Khử theo **timestamp**: dừng khi gặp lại timestamp của đoạn đầu tiên |
| Endpoint `timedtext` | Trả HTTP 200 nhưng **body rỗng** | Bỏ hẳn đường này, đi bằng DOM |

**Ngoại lệ / khi không dùng được.** Không có trình duyệt thật hoặc daemon không chạy. Video không có phụ đề. Video riêng tư.

**Đã quan sát.** 6/6 video lấy được, tổng ~80.000 ký tự sau khử trùng lặp. Một lần đọc sai hoàn toàn trước khi thêm bước xác minh tab.

**Chưa biết.** Bẫy `find_tab` là lỗi của phiên bản daemon cụ thể hay hành vi thiết kế. Cấu trúc DOM của YouTube đổi thường xuyên nên selector `ytd-transcript-segment-renderer` có thể hỏng.

---

## SC-02 — Xác minh link bài tập MuscleWiki

- **Trạng thái:** observed · ghi ngày 2026-09-16 · **chưa đề xuất tạo skill**
- **Đề xuất:** sửa [training-qa](../../training-toolkit/skills/training-qa/SKILL.md). Liên quan trực tiếp tới khoảng trống **P0 "Exercise database thực sự"** ở [references/25](../../training-toolkit/references/25-doi-chieu-mau-thuan-va-khoang-trong.md).

**Vấn đề.** Mọi bài trong chương trình hoàn chỉnh phải có link đúng biến thể, ưu tiên MuscleWiki. Contract cấm đoán URL.

**Ba phát hiện.**

1. **musclewiki.com trả HTTP 403 cho fetch tự động.** Xác minh gián tiếp qua chỉ mục tìm kiếm là khả thi (URL + tiêu đề khớp tên bài) nhưng **phải ghi rõ là gián tiếp** — chưa đối chiếu được video/biến thể bằng mắt. Trình duyệt thật thì vào được bình thường và trang còn trả về metadata có cấu trúc: `Difficulty · Force · Grips · Mechanic`.
2. **Slug không suy ra được từ tên bài.** Ví dụ thật: bài cáp face pull nằm ở `/exercise/machine-face-pulls`; walking lunge là `lunge-walking` chứ không phải `walking-lunge`; machine hip thrust chỉ có ở đường dẫn dài `/exercise/machine/male/glutes/machine-hip-thrust`. **Đây là bằng chứng cụ thể cho luật "không đoán URL".**
3. **Có API chính thức** tại `api.musclewiki.com` — 1.900+ bài, 7.700+ video, OpenAPI 3.1, free tier, commercial use allowed, có MCP server. Yêu cầu header `X-API-Key`, tức cần user tự đăng ký. **Đây là đường đúng để lấp P0**, không phải cào trang.

**Ngoại lệ.** Một số bài không có trang đúng biến thể (ví dụ ab wheel rollout độc lập) — phải ghi "chưa tìm được", không thay bằng bài gần giống mà không nói.

**Đã quan sát.** 55 link lấy được qua chỉ mục tìm kiếm; 3 bài lệch biến thể phải ghi chú; 26 bài thay thế vẫn chưa tra.

**Chưa biết.** Điều khoản API cho phép gì cụ thể. Chất lượng metadata của API so với trang web.

---

## SC-03 — Tiếp nhận nguồn hạng thấp (transcript, vlog) mà không phá phân hạng knowledge

- **Trạng thái:** observed · ghi ngày 2026-09-16 · **chưa đề xuất tạo skill**
- **Đề xuất:** **không tạo skill mới.** Quy trình đã có ở [references/25.5](../../training-toolkit/references/25-doi-chieu-mau-thuan-va-khoang-trong.md) và mẫu U01–U08 ở [references/28](../../training-toolkit/references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md). Nếu muốn, chỉ bổ sung một mục ngắn vào [training-learning](../../training-toolkit/skills/training-learning/SKILL.md).

**Vấn đề.** User đưa nguồn phổ thông (video YouTube) và muốn "cào thêm kiến thức". Rủi ro là đổ nội dung chưa kiểm chứng vào `knowledge.md` và phá lớp phân hạng [E]/[C]/[H].

**Cách xử lý đã dùng.** Chia kết quả làm đúng ba rổ: **trùng** (tăng tin cậy cho quyết định đang dùng) · **mâu thuẫn** (nêu ra, giải thích, **không tự đổi** theo video) · **chưa đủ căn cứ** (ghi lại kèm việc cần làm để nhập). Lưu tài nguyên trong **project**, không đưa vào toolkit dùng chung vì toolkit có `manifest.json` kiểm tra sha256 và nâng knowledge phải bump version.

**Bốn dấu hiệu cần đánh dấu ở nguồn phổ thông.** Xung đột lợi ích (bán sách/app/dịch vụ) · tuổi tài liệu so với nguồn đang có trong kho · phát biểu không truy được nghiên cứu gốc · công thức thô bỏ qua biến quan trọng.

**Kết quả đã quan sát.** 6 tài nguyên, phần lớn **xác nhận** chương trình; chỉ 3 chi tiết nhỏ được sửa; 1 công thức bị bác bỏ vì ra mức thâm hụt 21–34%; 4 phát biểu xếp diện chưa đủ căn cứ. **Không nội dung nào được nâng lên knowledge chung.**

**Chưa biết.** Tỷ lệ "xác nhận / mâu thuẫn" này có lặp lại với bộ nguồn khác không. Một lần quan sát không chứng minh quy trình hiệu quả.

---

## Không phải ứng viên skill

Ghi lại để lần sau không nhầm là vấn đề của toolkit:

- **Console Windows mặc định cp1252** nên `print` tiếng Việt gây `UnicodeEncodeError`. Xử lý: `sys.stdout.reconfigure(encoding='utf-8')`. Đây là môi trường, không phải nghiệp vụ.
- **Heredoc trong Bash làm hỏng nội dung dài có ký tự đặc biệt.** Xử lý: ghi script ra file rồi chạy. Cũng là môi trường.
- Cả hai nên nằm ở ghi chú môi trường nếu có, **không** nhét vào skill nghiệp vụ tập luyện.
