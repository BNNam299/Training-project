# BRIEF TOOLKIT HUẤN LUYỆN CHẠY QUA AGENT

Phiên bản brief: 0.1 — 15/09/2026. Trạng thái: đã tổng hợp yêu cầu qua brainstorm, chờ người dùng rà brief trước khi triển khai. **Tài liệu này là đặc tả, chưa phải toolkit đã được tạo.**

## 1. Mục đích và phạm vi

Toolkit hỗ trợ một người xuyên suốt hành trình: hiểu hiện trạng → chọn mục tiêu và phase → lập tập luyện/dinh dưỡng → thực hiện → check-in → đánh giá hiệu quả → điều chỉnh. Có thể phục vụ chủ toolkit hoặc những người họ hỗ trợ; **mỗi người một project độc lập**.

Chạy bằng hội thoại với agent và file trong project. Không xây app, giao diện web hoặc hệ thống nhắc tự động trong phiên bản đầu. Người dùng tự gọi agent khi cần hoặc đến lịch check-in đã chọn.

Toolkit phải hỗ trợ nhiều mục tiêu: hypertrophy, giảm mỡ, strength/powerlifting, duy trì, năng lực sinh hoạt và tích hợp rehab khi có đủ cơ sở. Không mặc định một lịch tập, số buổi hoặc chuỗi phase cho mọi người. Các thông tin như bốn buổi upper–lower hoặc trần hai tiếng trong brainstorm là **case của một cá nhân**, không phải cấu hình toàn hệ thống.

## 2. Các nguyên tắc đã chốt

- Cá nhân hóa từ đầu vào và thực tế thực hiện; không chỉ ghép tên người vào template.
- Chủ động đề xuất hành trình: bắt đầu phase nào, vì sao, đánh đổi gì và điều kiện chuyển phase.
- Có phương án xử lý gián đoạn; thiếu buổi, thiếu giờ hoặc thiết bị là tình huống sử dụng chính.
- Phân biệt kế hoạch ban đầu, thực tế đã làm và kế hoạch đã điều chỉnh.
- Markdown là nguồn thông tin chính để duyệt, lưu phiên bản và tiếp tục xuyên phiên chat. Word/Excel là bản xuất để sử dụng.
- Kiến thức đã nghiên cứu là căn cứ đầu tiên; giữ nguồn, điều kiện áp dụng, độ chắc chắn và ngoại lệ.
- Chỉ tìm thông tin bên ngoài để lấp khoảng trống sau khi hỏi và được người dùng đồng ý.
- Tự ghi nhận ứng viên skill; phải hỏi trước khi tạo skill mới hoặc cập nhật skill hiện có.
- Nội dung cho người dùng bằng tiếng Việt, giữ nguyên tên bài tập/thuật ngữ bài tập; thuật ngữ khác cần thiết phải giải thích ngắn.

## 3. Luồng sử dụng

### 3.1. Khởi tạo project và intake

Thu thập theo từng bước, chỉ hỏi dữ liệu có ảnh hưởng quyết định: mục tiêu và ưu tiên; thời hạn; tuổi/thể trạng/cân nặng/chiều cao và giới tính khi liên quan; kinh nghiệm; lịch sử tập; sức khỏe/triệu chứng/chẩn đoán/hạn chế; lịch làm việc; số cửa sổ tập và thời lượng; thiết bị; sở thích; khả năng hồi phục; mức sẵn sàng ghi dữ liệu.

Không bắt người dùng biết trước họ nên tập bao nhiêu buổi hoặc chọn split nào. Agent hỗ trợ chọn cấu trúc phù hợp. Thông tin chưa biết phải được ghi là chưa biết, không tự coi là không có triệu chứng hoặc đã hoàn thành một buổi.

Khi có vấn đề sức khỏe, dùng luồng sàng lọc/thu thập riêng; không tự chẩn đoán tổn thương từ mô tả hoặc video. Brief này không phân tích triệu chứng cá nhân đã được nhắc trong brainstorm.

### 3.2. Đề xuất hành trình và chương trình

Agent đề xuất phase và lý do, chỉ số đánh giá, tiêu chí chuyển phase; sau đó tạo cấu trúc lịch, bài, liều tập, effort/rest, progression/regression và phương án dự phòng. Phân bổ rehab theo tình trạng đã đánh giá và giới hạn phù hợp; không thêm một bộ corrective chung cho mọi người.

Mỗi chương trình có Markdown hoàn chỉnh để người dùng kiểm tra. Các giá trị ước tính, giả định và dữ liệu còn thiếu được ghi rõ. Khi sửa bản nháp cũng ghi nhận thay đổi có ý nghĩa; không giả vờ bản chưa được duyệt là kế hoạch đã thực hiện.

### 3.3. Báo cáo thực tế bằng ngôn ngữ tự nhiên

Ví dụ: “Tôi đã tập A và nửa buổi B, miss C; tuần này chỉ còn tối thứ sáu 45 phút.” Agent đọc chương trình và nhật ký, đối chiếu thông tin vừa báo, chỉ hỏi thêm điều cần thiết. Không bắt nhập lại toàn bộ hồ sơ hoặc hoàn thành biểu mẫu cứng.

Nếu lời báo mới mâu thuẫn nhật ký và ảnh hưởng quyết định, làm rõ trước khi sửa phần phụ thuộc. Lưu thời điểm buổi tập thực tế và thời điểm báo cáo riêng khi cần.

### 3.4. Check-in và giám sát

Toolkit đề xuất khung theo từng mục tiêu; người dùng chọn nhịp rồi tự gọi agent. Mặc định vận hành đề xuất: review chính bảy ngày, có thể chọn 14 ngày; review phase khoảng bốn tuần hoặc theo mốc riêng. Đây là cấu hình, không ngưỡng khoa học bắt buộc. Với rehab, nhịp ghi phản ứng/review theo plan chuyên môn và tình trạng.

| Nội dung | Dữ liệu cần khi liên quan |
|---|---|
| Thực hiện chương trình | Buổi/phần đã làm, bỏ, đổi; bài/tải/rep/effort cần theo dõi |
| Hiệu suất | Xu hướng theo bài/nhiệm vụ, ROM/setup nếu thay đổi |
| Hồi phục và sức khỏe | Ngủ, mệt, stress, triệu chứng và chức năng |
| Dinh dưỡng/composition | Các lần cân có ngày/điều kiện, số đo nếu có, mức thực hiện dinh dưỡng hoặc calories/macros đã tự tính |
| Hoàn cảnh tiếp theo | Thời gian, thiết bị, công việc, công tác/về quê và thời hạn thay đổi |

Ghi dữ liệu sau buổi không đồng nghĩa phải gọi agent sau mọi buổi. Có thể gom dữ liệu tới kỳ review. Mỗi lần review trả lời: **đúng hướng không → dữ liệu đủ chưa → giữ/đổi gì và vì sao → cần theo dõi gì → mốc tiếp theo**.

Không tự điều chỉnh chỉ vì một tuần hụt chỉ tiêu; kiểm tra xu hướng, chất lượng phép đo, adherence và bối cảnh. Case mục tiêu giảm 0,5 kg nhưng giảm 0,2 kg chỉ là một phép thử; logic giám sát phải bao phủ các mục tiêu khác.

## 4. Xử lý tình huống gián đoạn

Đầu vào quyết định: mục tiêu phase, phần đã hoàn thành, phần còn thiếu, lịch/thiết bị còn lại, sức khỏe và hồi phục. Mục đích: giữ lợi ích ưu tiên với nguồn lực thực tế; không hứa kết quả như lịch đầy đủ và không nhồi tất cả “set còn nợ”.

| Tình huống | Yêu cầu hành vi |
|---|---|
| Mất một hoặc nhiều buổi | Đánh giá phần đã tập và tổ chức lại phần còn lại |
| Chỉ còn một buổi hoặc ít phút | Chọn ưu tiên, bỏ phần ít giá trị hơn, vẫn đủ chuẩn bị/thực hiện phù hợp |
| Về quê không có dụng cụ gym | Đề xuất duy trì bằng lựa chọn khả thi; vật dụng kháng lực chỉ dùng khi phù hợp tính ổn định/khả năng thao tác |
| Mệt sau công việc | Điều chỉnh dựa dữ liệu và effort, không giảm tải theo một công thức chung |
| Gián đoạn một/hai tuần | Lưu khoảng áp dụng và kế hoạch tiếp nối |
| Chưa rõ thời hạn hoặc hoàn cảnh thay đổi lâu dài | Ghi chưa xác định; hỏi khi cần và cân nhắc thiết kế lại |
| Trở lại | Kiểm tra tình trạng, không tự coi đã hồi phục hoặc khôi phục tải cũ chỉ vì hết ngày |

Mỗi thay đổi ghi: trigger, ngày hiệu lực, thời hạn, phần đã làm, phương án mới, lý do, đánh đổi, điều kiện trở lại và lần review. Có sẵn mẫu thường gặp nhưng vẫn tạo được phương án cho tình huống mới.

## 5. Dinh dưỡng

Đầu ra chính là calories và mục tiêu dinh dưỡng định lượng phù hợp mục tiêu, kèm đơn vị, cơ sở ước tính và cách review. Người dùng tự tìm thực phẩm, tự tính lượng ăn bên ngoài và báo lại nếu có.

Có **một thực đơn mẫu cố định tùy chọn**, dựa vào món người dùng xác nhận có thể kiếm được, để áp dụng khi thuận tiện. Không xây chức năng chọn món hằng ngày hoặc bắt người dùng theo thực đơn. Cần hỏi tối thiểu về thực phẩm phù hợp/dị ứng khi tạo mẫu; không tự đoán.

Khi mục tiêu dinh dưỡng đổi, thực đơn mẫu cần được cập nhật hoặc đánh dấu chưa khớp phiên bản mới. Supplement được ghi nhận nếu liên quan, không tự thêm vào mọi kế hoạch.

## 6. Kho kiến thức chung và Q&A

### 6.1. Một file kiến thức hợp nhất

Tạo `knowledge.md` trong toolkit làm tài liệu kiến thức chung cho agent. Đây phải là **nội dung tổng hợp thực chất**, không chỉ danh sách liên kết. Hợp nhất các phần đã nghiên cứu theo chủ đề, có mục lục, mã mục/nguồn, URL, phạm vi và mức bằng chứng; giữ liều, điều kiện tiến triển, giới hạn, ngoại lệ và các điểm chưa biết.

Các tài liệu nguồn chi tiết/bản lưu được giữ để truy xuất. Nội dung chưa kiểm chứng, transcript và instruction được cung cấp như tài liệu không tự trở thành quy tắc có hiệu lực. Khi tổng hợp phải xử lý mâu thuẫn, không nối cơ học mọi tệp thành các lời khuyên trái nhau. Ghi phiên bản kho kiến thức mà mỗi chương trình dùng.

### 6.2. Quy trình Q&A

1. Đọc câu hỏi, hồ sơ cá nhân và trạng thái hiện tại khi liên quan.
2. Tra kho kiến thức, kiểm tra đúng đối tượng, điều kiện và độ chắc chắn.
3. Trả lời bằng giải pháp phù hợp, nêu lý do ngắn và liên kết nguồn cần thiết; phân biệt bằng chứng với heuristic.
4. Nếu thiếu đầu vào cá nhân, hỏi dữ liệu đó; không lấy tìm web thay cho intake.
5. Nếu kiến thức chưa đủ, nguồn mâu thuẫn/chưa kiểm chứng hoặc cần cập nhật, nói rõ khoảng trống và **hỏi người dùng có muốn tìm bên ngoài không**. Chưa đồng ý thì không tự tìm; vẫn cung cấp được phần đã có căn cứ và giới hạn.
6. Nếu được đồng ý, tìm/đọc/đối chiếu, giữ provenance và đề xuất bổ sung kiến thức. Không coi một kết quả tìm kiếm là tiêu chuẩn mới mặc định.

Yêu cầu triển khai: cơ chế xin phép tìm ngoài cần tương thích các ràng buộc của môi trường agent; nếu môi trường bắt buộc kiểm chứng mà chưa được phép, phải trình bày giới hạn thay vì trả lời chắc chắn từ thông tin cũ.

### 6.3. Link từng bài tập

Mọi bài tập trong chương trình, kể cả warm-up/rehab có tên cụ thể, phải có link hướng dẫn. Ưu tiên **đúng bài/biến thể trên MuscleWiki**; không có thì dùng nguồn khác phù hợp và ghi nguồn thay thế. Không dùng link trang chủ thay cho bài cụ thể và không đoán URL.

Khi cần tìm bên ngoài để xác minh/bổ sung link chưa có, áp dụng quy trình xin phép ở 6.2. Nếu chưa có link đã xác minh, đánh dấu bản nháp chưa hoàn tất hoặc đề xuất bài khác phù hợp đã có link; không xuất bản hoàn chỉnh giả. Việc tra một link đã có trong kho không phải tìm mới bên ngoài.

## 7. Kiến trúc file và lịch sử

Tên file dưới đây là đề xuất triển khai; yêu cầu bắt buộc là trạng thái nhất quán, đọc tiếp xuyên phiên và không mất lịch sử.

```text
toolkit/
  README.md                 # Cách gọi agent, quy trình bắt đầu/tiếp tục
  knowledge.md              # Kiến thức hợp nhất có nguồn và phiên bản
  skills/                   # Skill đã được người dùng cho phép tạo/cập nhật
  templates/                # Khung MD và đặc tả xuất Word/Excel

personal-project/
  profile.md
  roadmap.md
  current-state.md
  programs/
    program-<id>.md         # Bản duyệt + kế hoạch hiện hành + lịch sử revision
    versions/              # Snapshot để khôi phục/so sánh khi cần
  logs/                    # Thực tế và check-in
  changes/                 # Chi tiết thay đổi dài, được nối từ chương trình
  skill-candidates.md
  exports/                 # Bản xuất gắn program ID/revision
```

**`program-<id>.md` là tài liệu trung tâm của chương trình:** có revision/ngày/trạng thái, lịch hiện hành, dinh dưỡng, quy tắc, liên kết nhật ký và changelog. Không chuyển toàn bộ lịch sử ra nơi khác khiến bản người dùng duyệt mất dấu cập nhật. Chi tiết dài có thể tách file nhưng phải liên kết rõ từ bản trung tâm.

Phase mới/chương trình mới có ID riêng; sửa chương trình đang chạy tăng revision. Không sửa đè thực tế đã làm để khớp lịch mới. `current-state.md` chỉ tới đúng chương trình/revision và thay đổi tạm đang có hiệu lực; không thành nguồn kế hoạch cạnh tranh.

Mở phiên mới: đọc entrypoint → current state → profile/roadmap → chương trình hiện hành → check-in/thay đổi liên quan. Agent phải xác định được điều gì đang áp dụng, điều gì đã hết hiệu lực và điều gì đang chờ người dùng.

## 8. Bộ nhớ cải tiến và skill

Agent được chủ động ghi `skill-candidates.md`: vấn đề lặp lại, input, cách xử lý, nhánh ngoại lệ, phạm vi, các case và kết quả quan sát, phần chưa kiểm chứng, đề xuất tạo/cải tiến skill.

Trước khi tạo skill mới hoặc cập nhật skill: trình bày nội dung cụ thể, lợi ích, phạm vi, căn cứ, phần thay đổi và hỏi người dùng. Chỉ sau khi đồng ý mới ghi vào `skills/` và lưu phiên bản. Không hỏi lại cho đúng hành động đã được chấp thuận; thay đổi ngoài phạm vi cần quyết định mới.

Một case thành công chưa đủ thành quy luật phổ quát. Skill dùng chung không mang dữ liệu nhận diện/chi tiết cá nhân sang project khác. Ghi ứng viên khác với cập nhật skill, và cập nhật skill khác với điều chỉnh giáo án.

## 9. Duyệt Markdown và xuất Word/Excel

### 9.1. Thứ tự

Hoàn thiện MD → người dùng kiểm tra/sửa → agent nhắc có thể xuất Excel hoặc Word → người dùng chọn → tạo artifact từ **đúng revision đã duyệt**. Không tự coi đã được yêu cầu xuất cả hai. Sau update có ý nghĩa, nhắc rằng bản xuất cũ đã lệch và có thể xuất lại.

Markdown vẫn là source of truth. Bản xuất ghi program ID, revision và ngày; không tự đồng bộ ngược từ file người dùng chỉnh nếu chưa đọc/đối chiếu và ghi nhận.

### 9.2. UX nội dung

- Tách rõ **lịch tập**, **dinh dưỡng**, **quy tắc điều chỉnh** và phần ghi kết quả nếu cần.
- Đầu tài liệu cho biết phase/mục tiêu, phạm vi ngày, lịch đang áp dụng và giới hạn quan trọng.
- Lịch cho thấy buổi/ngày, tên bài có hyperlink, sets × reps, tải/effort, nghỉ và cue ngắn. Phân biệt kế hoạch với cột thực tế nếu có.
- Giữ nguyên tên bài tiếng Anh. Dùng tiếng Việt cho nhãn, giải thích và hành động; có chú giải ngắn cho RIR/RPE nếu người đọc chưa quen.
- Quy tắc trình bày gọn theo **Nếu → Làm → Khi nào xem lại**; giữ điều kiện quan trọng, không chép toàn bộ nghiên cứu vào bản mang đi tập.
- Phân biệt cần làm, tùy chọn và phương án dự phòng bằng nhãn rõ; không chỉ dùng màu.
- Không nhồi lịch sử thay đổi dài vào trang buổi tập; có tóm tắt revision và tham chiếu MD khi cần.

### 9.3. Excel

Đề xuất sheet: `Tổng quan`, `Lịch tập`, `Dinh dưỡng`, `Điều chỉnh`, `Nhật ký` khi người dùng muốn ghi trong file. Cố định hàng tiêu đề, cột rộng vừa đọc, xuống dòng hợp lý, hyperlink trực tiếp và vùng in phù hợp. Không merge ô trong bảng dữ liệu cần lọc/ghi. Nếu có công thức, kiểm tra đơn vị và tổng; không thêm dashboard phức tạp không phục vụ sử dụng.

### 9.4. Word

Heading rõ, tách buổi/phần dễ tìm, bảng vừa trang, lặp tiêu đề bảng khi sang trang và tránh cắt hàng khó đọc. Giữ hyperlink, khoảng trắng và cỡ chữ sử dụng thoải mái; không thu chữ quá nhỏ để nhét bảng. Có thể in được, vẫn hiểu khi không có màu.

### 9.5. Kiểm tra bản xuất

Đối chiếu với MD đã duyệt: đủ bài/link/liều, đúng mục tiêu dinh dưỡng và rule, đúng phiên bản; kiểm tra bố cục render, tràn/cắt chữ và hyperlink. Nội dung ngắn gọn không được làm mất điều kiện y tế hoặc giới hạn thiết yếu.

## 10. Case nghiệm thu bắt buộc

| Case | Kết quả cần đạt |
|---|---|
| Hai người có mục tiêu/lịch/thiết bị khác nhau | Project và chương trình khác phù hợp input; không dùng upper–lower bốn buổi mặc định |
| Chưa biết nên bắt đầu phase nào | Có đề xuất hành trình, căn cứ, đánh đổi và tiêu chí chuyển |
| Đã tập hai buổi, miss một, chỉ còn một buổi | Tổ chức lại dựa thực tế; không nhồi toàn bộ set hoặc đánh dấu buổi miss đã làm |
| Chỉ hoàn thành nửa buổi | Nhật ký và quyết định phản ánh đúng phần đã làm |
| Về quê hai tuần, không dụng cụ gym | Kế hoạch duy trì có giới hạn/thời hạn và cách tiếp tục |
| Biến động cân ngắn hạn hoặc tiến độ lệch | Kiểm tra dữ liệu/bối cảnh trước quyết định; có thể giữ kế hoạch |
| Câu hỏi đã có trong kho | Trả lời theo kiến thức phù hợp, không tự tìm ngoài |
| Câu hỏi vượt kho hoặc thiếu link bài | Nêu thiếu gì, hỏi tìm ngoài; không bịa nguồn/link |
| Mở phiên chat mới | Đọc đúng trạng thái/revision, nhớ điều chỉnh tạm và lịch review |
| Pattern xử lý lặp lại | Tự ghi ứng viên; không tạo/update skill khi chưa được đồng ý |
| Duyệt rồi xuất, sau đó cập nhật | MD giữ lịch sử; artifact có revision, bản cũ được nhận diện là cũ |
| Bài hoặc mục tiêu chưa có đủ cơ sở an toàn | Ghi giới hạn/hỏi dữ liệu/chuyển đánh giá phù hợp, không lấp bằng template |

## 11. Các lựa chọn còn mở khi triển khai

- Thư mục cài toolkit dùng chung và vị trí tạo các personal project.
- Cơ chế tạo bản sao hay tham chiếu toolkit chung, và cách pin phiên bản kiến thức/skill.
- Với thay đổi giáo án lớn hoặc đổi phase: mặc định đề xuất bản sửa để người dùng duyệt; ranh giới thay đổi nhỏ được áp dụng ngay cần thống nhất khi khởi tạo project. Chưa suy từ quyền ghi skill-candidates thành quyền đổi mọi chương trình.
- Thông tin cần thiết để tạo thực đơn mẫu và định dạng export do từng người chọn lúc dùng, không cần cố định cho toàn toolkit.

Không cần giải quyết mọi nhánh y khoa trước khi tạo bộ khung, nhưng phải hiển thị phạm vi được hỗ trợ và phần chưa đủ kiến thức. Nguồn đầu vào hiện có: [trang tài nguyên](16-tong-hop-tai-nguyen.md), [ma trận nguồn](24-ma-tran-nguon-va-kiem-chung.md), [khoảng trống](25-doi-chieu-mau-thuan-va-khoang-trong.md), [tài liệu người dùng](28-tiep-nhan-tai-nguyen-va-doi-chieu.md).
