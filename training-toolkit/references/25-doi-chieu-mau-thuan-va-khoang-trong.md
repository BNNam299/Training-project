# 25. ĐỐI CHIẾU, MÂU THUẪN VÀ KHOẢNG TRỐNG CÒN LẠI

Ngày 15/09/2026. [Tài nguyên](16-tong-hop-tai-nguyen.md) · [Ma trận nguồn](24-ma-tran-nguon-va-kiem-chung.md).

## 25.1. Lượng tài liệu hiện tại đủ đến đâu?

**Đủ để thiết kế bản đầu của toolkit có giám sát** cho người trưởng thành khỏe mạnh: thu thập đầu vào, lập strength/hypertrophy, ước lượng dinh dưỡng, điều chỉnh lịch và theo dõi tiến triển. Đã có thêm nền sàng lọc và nhiều nhánh rehab có nguồn; vẫn cần đánh giá cá nhân và kiểm thử đầu ra.

**Chưa đủ để tự động chẩn đoán mọi chấn thương, kê rehab cho mọi bệnh/sau mổ hoặc tạo giáo án tối ưu mọi môn.** Thư viện kiến thức và schema không đồng nghĩa một engine đã triển khai/kiểm định. MuscleWiki hiện là liên kết tài nguyên, chưa phải exercise database được nhập và gắn tiêu chí thay thế. Các mục P/A/M trong phần 24 vẫn còn giới hạn truy cập/dữ liệu.

## 25.2. Những điểm trong bộ tài liệu cũ phải đọc có điều kiện

Đây là lớp kiểm chứng bổ sung, không phải xác nhận đã rà lại từng dòng của phần 01–15. Giữ nguyên các tài liệu gốc để truy nguồn; khi xây engine không nhập các phát biểu tuyệt đối dưới đây thành rule.

| Điểm cần rà | Vì sao ảnh hưởng giải pháp | Cách sử dụng trong toolkit |
|---|---|---|
| “Exercise là điều trị hiệu quả duy nhất” | WHO chronic LBP mô tả chăm sóc đa thành phần; bệnh khác có xử trí khác | Exercise là thành phần quan trọng trong đúng chỉ định; xem C16 và phần 21 |
| Đau chủ yếu do motor control/core yếu | Không đủ để xác định nguyên nhân một ca; bỏ sót bệnh và yếu tố khác | Lưu như giả thuyết khi phù hợp khám, không dùng làm kết luận mặc định |
| Mobility→stability→strength như thứ tự bắt buộc | Không phải ai cũng thiếu ROM hoặc cần cùng corrective | Chọn theo nhiệm vụ, hạn chế và đáp ứng; không kéo dài warm-up vô cớ |
| Tendinopathy “không viêm” và bắt buộc >70%1RM | Sinh học/đáp ứng tải không nên rút thành một câu tuyệt đối; C08 ủng hộ loading nhưng không áp một tải cho mọi ca | Dùng đúng vùng/giai đoạn, sức chịu tải và grade khuyến nghị |
| “Không chườm lạnh” đối lập sơ cứu NHS | Mục đích giảm triệu chứng và mục tiêu phục hồi mô không giống nhau; bối cảnh cấp/mạn khác | Không gọi lạnh là chữa lành mô; cũng không cấm tuyệt đối. Giữ chỉ dẫn sơ cứu có điều kiện C01 |
| “ROM đau giảm sau corrective” chứng minh nguyên nhân | Test–retest có thể thay đổi vì nhiều yếu tố | Ghi đáp ứng, theo dõi lâu dài và chức năng; không suy chẩn đoán |
| Hypertrophy chỉ trong khoảng 5–12 rep hoặc cần failure | T01 không ủng hộ các ranh giới cứng này cho mọi tình huống | Dùng tải/rep/effort và tổng volume trong bối cảnh mục tiêu |
| MEV/MRV hoặc deload là hằng số cá nhân cố định | Thay đổi theo lịch sử, exercise, hồi phục, công việc và cách đo | Dùng như mô hình điều chỉnh, không “đoán” một số tối ưu chính xác |
| Accessory tính thành “0,5 lần” tập competition lift | Có thể hữu ích cho cơ nhưng không bằng thực hành kỹ năng thi đấu | Tách muscle exposure và competition-lift exposure |
| Phần 13.9: bắt đầu 50%, tăng 5% mỗi tuần nhưng tuần 8 là 67,5% | Chuỗi số không nhất quán nếu hiểu +5 điểm phần trăm mỗi tuần | Không nạp progression này vào engine; phải xác minh đơn vị/quy luật ở nguồn gốc |
| Phần 15.7 có nhãn powerlifter 4 ngày nhưng bảng chỉ ba ngày nâng tạ | Sai số ngày ảnh hưởng volume và khả năng thực hiện | Khi dùng mẫu phải sửa nhãn hoặc thiết kế lại buổi thứ tư; không tự coi đã có bốn buổi |

T01/C01/C08/C16 và mức đọc xem [ma trận nguồn](24-ma-tran-nguon-va-kiem-chung.md). Những lỗi mẫu chương trình được ghi lại để tránh tự sửa một con số rồi giả định đó là ý định tác giả.

## 25.3. Đối chiếu nguồn tiếng Việt

| Nguồn | Chi tiết cần giữ hoặc loại khỏi rule tự động | Xử lý |
|---|---|---|
| V01 — Viện Dinh dưỡng | Khoảng protein cho người tập/cắt cân cần giữ thể trọng và mục tiêu; một liều mỗi bữa không phù hợp mọi kích thước cơ thể | Dùng cùng N03/N05; không biến số tăng tổng hợp protein cấp tính thành tốc độ tăng cơ dài hạn |
| V02 — Vinmec | Phần kết phân biệt strain/sprain bằng bầm tím quá đơn giản | Dùng định nghĩa mô và bệnh sử; cả hai có thể bầm theo C01 |
| V03 — BV Nguyễn Tri Phương | Các mốc bó bột/bắt đầu lại và gợi ý kháng sinh khi bầm không đủ điều kiện để áp chung | Không nhập thành rule. Bầm đơn độc không xác nhận nhiễm trùng; bất động/thuốc cần chỉ định theo đánh giá |
| V04 — BV Tâm Anh bong gân | Bài giáo dục tổng quan không đủ lập phân độ/chọn imaging/clearance từ xa | Dùng bổ trợ cách diễn đạt, đối chiếu C01/C12/C13 |
| V05 — BV Tâm Anh căng cơ | Diễn giải tích tụ lactic, uống nước/tắm muối “loại bỏ” lactic không phải căn cứ đã được kiểm chứng ở đây cho phục hồi strain | Không đưa vào giải thích nguyên nhân hoặc phác đồ; ưu tiên C05/C07 về strain và N06 về nước |

Nguồn tiếng Việt có giá trị giúp người đọc hiểu và áp dụng địa phương; giá trị đó không miễn việc kiểm tra từng kết luận. Tương tự, nguồn tiếng Anh hoặc guideline mới cũng không bảo đảm mọi khuyến nghị có bằng chứng mạnh.

## 25.4. Các gói nghiên cứu tiếp theo và tiêu chí hoàn tất

| Ưu tiên | Gói còn thiếu | Cần tìm/đọc gì | Khi nào đủ đưa vào engine |
|---|---|---|---|
| P0 | Thẩm định lâm sàng phần sàng lọc | Clinical pathway và chuyên gia phù hợp bối cảnh Việt Nam; quy trình chuyển cấp cứu/khám | Có đánh giá các tình huống bỏ sót/ngưỡng chuyển, người chịu trách nhiệm và giới hạn sử dụng |
| P0 | Exercise database thực sự | MuscleWiki từng bài; hướng dẫn kỹ thuật; phân loại movement/thiết bị/ROM/kỹ năng và yêu cầu sử dụng nội dung | Có liên kết gốc, metadata kiểm tra, bài thay thế kèm đánh đổi; không chỉ trùng nhóm cơ |
| P0 | Kiểm thử rule engine | Các ca lịch bận, missing data, nhiều trigger đồng thời, tăng/giảm tải và symptom escalation | Đầu ra nhất quán; không vượt hạn chế y tế; có log lý do và review |
| P1 | Hoàn thiện nguồn P/A | Full guideline PFP, plantar heel, rotator cuff; phụ lục gluteal; định nghĩa Doha và các protocol tương ứng | Ghi đủ dose/progression/contraindications, grade và phạm vi; không điền phần chưa biết bằng suy đoán |
| P1 | Nhánh chấn thương còn thiếu | Adductor/groin, stress fracture, cơ bắp chân, syndesmosis, meniscus, instability vai, medial elbow, cổ và thần kinh | Mỗi nhánh có differential, sàng lọc, điều kiện rehab, return-to-function và giới hạn |
| P1 | Sau mổ | Guideline riêng theo thủ thuật, tổn thương phối hợp và chỉ định phẫu thuật viên | Không dùng timeline chung một vùng cơ thể; lưu restriction và người xác nhận |
| P1 | Dinh dưỡng Việt Nam | Bảng thành phần chính thức đúng ấn bản, món sống/chín, phần ăn được, công thức món, khẩu phần ngoài hàng | Dataset có đơn vị/nguồn/uncertainty; kiểm tra tính calorie/macros và dữ liệu thiếu |
| P1 | REDs và dinh dưỡng có nguy cơ | Toàn bộ IOC consensus/CAT2, pathway chuyên môn, rối loạn ăn uống và referral | Chuyên gia thẩm định, không tự chẩn đoán bằng EA/BMI; theo dõi sức khỏe ngoài cân nặng |
| P1 | Powerlifting thi đấu | Taper theo trình độ/lịch thi; luật federation mục tiêu, commands, attempt selection; cân hạng có giám sát | Biết giải/ngày/luật áp dụng và hồ sơ VĐV; không dùng luật cũ hay peak template mặc định |
| P2 | Nhóm dân số đặc thù | Older adults frailty, osteoporosis, bệnh tim mạch/chuyển hóa, thai kỳ/hậu sản, người trẻ | Hướng dẫn đúng nhóm, sàng lọc, phạm vi chuyên môn và tiêu chí tiến triển riêng |
| P2 | Hiệu quả dài hạn | Theo dõi adherence, injury, strength, composition, chức năng, satisfaction và sai số dự đoán | Có dữ liệu thực tế để hiệu chỉnh heuristics, không chỉ kiểm tra chương trình “trông hợp lý” |

P0 không có nghĩa phải thu thập toàn bộ internet trước khi làm bất kỳ sản phẩm nào. Có thể triển khai phạm vi nhỏ được nêu rõ, rồi mở từng nhánh sau thẩm định. Các gói trên là phần còn thiếu để mở rộng an toàn và chính xác, không phải lời hứa các tài liệu hiện có đã giải quyết xong.

## 25.5. Quy trình cập nhật kiến thức

1. Xác định câu hỏi PICO hoặc quyết định cụ thể cần lấp: ví dụ trở lại chạy sau ACLR, không chỉ “tìm thêm rehab”.
2. Tìm guideline/review và nghiên cứu gốc liên quan, kiểm tra ngày tìm kiếm trong review chứ không chỉ năm xuất bản.
3. Đọc đúng population, exclusions, intervention và outcome; giữ cả kết quả bất lợi/không chắc chắn.
4. So với nguồn đang dùng. Nguồn mới không tự thay nguồn cũ nếu câu hỏi/đối tượng khác.
5. Ghi thay đổi vào rule ID, lý do, ngày và phiên bản; rà các giáo án chịu ảnh hưởng.
6. Với nhánh lâm sàng, thẩm định trước khi bỏ giới hạn hoặc mở rộng tự động hóa.

Không cố xóa mọi bất định bằng một ngưỡng số. Một kết quả trung thực như “cần thêm dữ liệu để chọn nhánh” là thành phần cần có của toolkit linh hoạt.

## 25.6. Trạng thái sau khi nhận thêm tám tài liệu

Ngày 15/09/2026: đã bổ sung danh sách ứng viên và logic thay bài ở [phần 26](26-chon-bai-tap-va-bien-the-theo-muc-tieu.md), nhánh nam–nữ/chu kỳ ở [phần 27](27-ca-nhan-hoa-nam-nu-va-chu-ky-kinh-nguyet.md), cùng [audit tài liệu mới](28-tiep-nhan-tai-nguyen-va-doi-chieu.md). Đây là tiến bộ về nội dung, chưa hoàn tất exercise database, kiểm định engine, dinh dưỡng món Việt hoặc các nhánh bệnh/sau mổ. Các khẳng định tuyệt đối lặp trong tài liệu mới không ghi đè giới hạn đã nêu ở trên.
