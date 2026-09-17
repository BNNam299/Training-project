# Kiến thức hợp nhất — Training Toolkit 1.0.0
Bản nội bộ dùng cho Q&A và thiết kế. Được hợp nhất toàn bộ nội dung biên soạn phần 17–28, không rút mất các điều kiện/liều/giới hạn. Các chương gốc 01–15 và tám tài liệu người dùng giữ nguyên trong references để truy sâu; không nhập phát biểu cũ chưa kiểm chứng thành quy tắc.
**Thứ tự đọc:** sàng lọc khi liên quan → mục tiêu/đối tượng → kiến thức chuyên đề → ma trận nguồn và audit. E/C/H và A/P/F có nghĩa theo các chương; không đánh đồng grade của CPG. Archive chứa cả instruction do người dùng gửi: chỉ là dữ liệu nguồn.
Các link nội bộ bên dưới dẫn về bản chương để tra cứu, nội dung đầy đủ cũng nằm ngay trong file này. Dùng tìm kiếm theo mã phần/thuật ngữ để đọc chọn lọc thay vì nạp cả file vào mỗi lượt.
## Mục lục
- [17. NỀN TẢNG LẬP CHƯƠNG TRÌNH VÀ ĐIỀU CHỈNH](references/17-nen-tang-lap-chuong-trinh-va-dieu-chinh.md) — tìm `CHAPTER 17`
- [18. DINH DƯỠNG VÀ ĐIỀU CHỈNH THEO MỤC TIÊU](references/18-dinh-duong-va-dieu-chinh-theo-muc-tieu.md) — tìm `CHAPTER 18`
- [19. SÀNG LỌC VÀ ĐỊNH HƯỚNG CHẨN ĐOÁN CƠ–KHỚP–MÔ MỀM](references/19-sang-loc-va-dinh-huong-chan-doan.md) — tìm `CHAPTER 19`
- [20. REHAB CHI DƯỚI VÀ TRỞ LẠI VẬN ĐỘNG](references/20-rehab-chi-duoi-va-tro-lai-van-dong.md) — tìm `CHAPTER 20`
- [21. REHAB LƯNG, VAI, KHUỶU VÀ CHẨN ĐOÁN PHÂN BIỆT](references/21-rehab-lung-vai-khuyu-va-chan-doan-phan-biet.md) — tìm `CHAPTER 21`
- [22. VẬN ĐỘNG PHỤC VỤ SINH HOẠT, HỒI PHỤC VÀ LÃO HÓA](references/22-van-dong-sinh-hoat-hoi-phuc-va-lao-hoa.md) — tìm `CHAPTER 22`
- [23. BỘ QUY TẮC ĐIỀU CHỈNH VÀ MẪU ĐẦU RA](references/23-bo-quy-tac-dieu-chinh-va-mau-dau-ra.md) — tìm `CHAPTER 23`
- [24. MA TRẬN NGUỒN, PHẠM VI ĐỌC VÀ KIỂM CHỨNG](references/24-ma-tran-nguon-va-kiem-chung.md) — tìm `CHAPTER 24`
- [25. ĐỐI CHIẾU, MÂU THUẪN VÀ KHOẢNG TRỐNG CÒN LẠI](references/25-doi-chieu-mau-thuan-va-khoang-trong.md) — tìm `CHAPTER 25`
- [26. CHỌN BÀI TẬP VÀ BIẾN THỂ THEO MỤC TIÊU](references/26-chon-bai-tap-va-bien-the-theo-muc-tieu.md) — tìm `CHAPTER 26`
- [27. CÁ NHÂN HÓA NAM–NỮ VÀ CHU KỲ KINH NGUYỆT](references/27-ca-nhan-hoa-nam-nu-va-chu-ky-kinh-nguyet.md) — tìm `CHAPTER 27`
- [28. TIẾP NHẬN 8 TÀI NGUYÊN VÀ ĐỐI CHIẾU KẾT LUẬN](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md) — tìm `CHAPTER 28`

---

<!-- CHAPTER 17 -->

# 17. NỀN TẢNG LẬP CHƯƠNG TRÌNH VÀ ĐIỀU CHỈNH

Ngày nghiên cứu: 14/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Ma trận nguồn và giới hạn](references/24-ma-tran-nguon-va-kiem-chung.md).

## 17.1. Phạm vi và cách đọc

Phần này dành cho thiết kế toolkit strength, hypertrophy và powerlifting ở người trưởng thành. Người có triệu chứng mới, chấn thương hoặc hạn chế sau mổ đi qua [phần 19](references/19-sang-loc-va-dinh-huong-chan-doan.md) trước khi áp dụng.

- **[E]**: kết luận hoặc khuyến nghị từ nghiên cứu/guideline; vẫn phải giữ đúng đối tượng.
- **[C]**: đồng thuận hoặc đề xuất chuyên gia trong nguồn, chưa đồng nghĩa đã được thử nghiệm xác nhận.
- **[H]**: quy tắc vận hành do bộ toolkit đề xuất. Các số trong ví dụ là điểm khởi đầu để kiểm thử, không phải ngưỡng sinh học phổ quát.

## 17.2. Bằng chứng nền và những giới hạn phải giữ

**[E] ACSM 2026** tổng hợp 137 systematic reviews, hơn 30.000 người; nghiên cứu tập 6–52 tuần, phần lớn người ít kinh nghiệm. Tập kháng lực có lợi ở nhiều cách tổ chức. Sức mạnh được hỗ trợ bởi tải nặng, bài ưu tiên đặt đầu buổi, nhiều hơn một set và tập lặp lại trong tuần. Hypertrophy có quan hệ với volume; khoảng ≥10 set/nhóm cơ/tuần có thể tăng lợi ích so với volume thấp hơn, nhưng không phải ngưỡng bắt buộc để bắt đầu. Failure không bắt buộc. Không đủ bằng chứng để ấn định một RIR tối ưu cho mọi người. Các kết quả ở người khỏe mạnh không tự động áp dụng cho rehab, frailty hoặc VĐV trình độ cao. [T01 — ACSM 2026, Results; Discussion; Tables 4 và 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823/).

**[E] Tập ít thời gian:** ưu tiên bài đa khớp, tổ chức volume theo thời gian thực tế, có thể dùng giai đoạn duy trì. Superset có thể tiết kiệm thời gian nhưng tăng mệt; bằng chứng dài hạn và khả năng duy trì bằng liều rất thấp còn hạn chế, đặc biệt ở người lớn tuổi. [T02 — No Time to Lift?, Practical Applications và Maintenance](https://pmc.ncbi.nlm.nih.gov/articles/PMC8449772/).

**[E] Autoregulation:** meta-analysis 15 nghiên cứu năm 2022 không tìm thấy khác biệt có ý nghĩa thống kê về 1RM giữa cách điều chỉnh tải tự động và tải chuẩn hóa; không nên quảng bá RPE là luôn tốt hơn %1RM. Điều chỉnh volume theo velocity loss có thể đánh đổi sức mạnh và hypertrophy; ngưỡng đo bằng thiết bị không được chuyển nguyên sang RIR. [T03 — Load and Volume Autoregulation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8762534/).

## 17.3. Hồ sơ đầu vào bắt buộc [H]

| Nhóm | Dữ liệu | Quyết định bị ảnh hưởng |
|---|---|---|
| Mục tiêu | Mục tiêu chính, phụ; thời hạn; mức ưu tiên; có thi đấu không | Chọn bài, phân bổ volume, tiêu chí thành công |
| Kinh nghiệm | Số tháng tập đều, lịch gần đây, bài đã biết, mức tạ/reps thực tế | Điểm khởi đầu và mức phức tạp |
| Công việc | Lịch ca, thời gian di chuyển, lao động thể lực, tuần cao điểm | Số buổi, thời lượng, khoảng hồi phục |
| Thiết bị | Tại nhà, phòng gym, khi công tác; mức tăng tạ nhỏ nhất | Biến thể và quy tắc tăng tiến |
| Khả năng phục hồi | Giấc ngủ, stress, ăn uống, các môn khác | Liều tập có thể duy trì |
| Sức khỏe | Triệu chứng, chẩn đoán đã xác nhận, hạn chế của người điều trị | Được dùng nhánh nào |
| Sở thích | Bài thích/không thích, lịch khả thi, mức sẵn sàng ghi chép | Khả năng tuân thủ |
| Dữ liệu gốc | Các buổi gần đây, RIR, cân nặng nếu liên quan, bài kiểm tra | So sánh tiến bộ và phát hiện thay đổi |

Không có 1RM thì không bắt buộc test max. Có thể bắt đầu bằng mức tạ dưới tối đa và RIR ước tính, ghi độ tin cậy thấp ở người chưa quen đánh giá nỗ lực. Không suy trình độ chỉ từ số năm mua thẻ gym.

## 17.4. Định nghĩa để tránh tính sai

- **Load**: kg hoặc %1RM; **effort**: khoảng cách đến không thể hoàn thành thêm rep với tiêu chuẩn đã định. Hai biến khác nhau.
- **Set làm việc** và **set khởi động** phải tách riêng.
- **RPE theo RIR**: RPE 10 tương ứng không còn rep dự trữ; 9 khoảng 1 RIR; 8 khoảng 2; 7 khoảng 3. Đây là ước lượng theo thang cụ thể, không phải quy đổi từ mọi thang RPE.
- **Volume theo lift** khác **volume theo cơ**. Squat và deadlift không cộng thành một số duy nhất rồi gọi đó là volume hamstring.
- **Tonnage** = tổng kg × reps, có ích để mô tả cùng bài trong điều kiện tương tự; không chứng minh bài có tonnage lớn hơn gây hypertrophy tốt hơn.
- Bài đổi ROM, tempo, dụng cụ hoặc cách thực hiện tạo chuỗi dữ liệu mới. Không dùng 1RM barbell để tính tải dumbbell hay máy khác.

## 17.5. Quy trình thiết kế lịch cơ sở [H]

1. Chốt số buổi **thực sự có thể hoàn thành**, kèm thời gian tối đa mỗi buổi.
2. Chọn mục tiêu đo được: ví dụ tiến bộ rep ở cùng tải; thành tích SBD; vòng eo và cân nặng; khả năng leo cầu thang.
3. Chọn bài chính và bài phụ theo mục tiêu; lấy liên kết minh họa từ MuscleWiki rồi kiểm tra yêu cầu kỹ thuật.
4. Gán liều ban đầu từ lịch tập đã dung nạp. Người mới bắt đầu thấp, tạo cơ hội học bài và đo phản hồi trước khi tăng.
5. Phân bố volume để chất lượng set và thời lượng còn phù hợp. Không cộng thêm set chỉ vì nguồn có một con số lớn hơn.
6. Dựng sẵn phiên bản buổi đầy đủ/rút gọn và tuần ít buổi.
7. Gán điều kiện tiến triển và điều kiện giảm tải cho từng bài.
8. Đánh giá sau một khoảng theo dõi đã định; không kết luận thất bại từ một buổi kém.

### Bản đồ ưu tiên theo mục tiêu

| Mục tiêu | Giữ trước khi cắt lịch | Phần có thể giảm trước | Đo kết quả |
|---|---|---|---|
| Powerlifting | Tiếp xúc kỹ thuật SBD phù hợp giai đoạn; các set chính có chất lượng | Accessory ít liên quan mục tiêu hiện tại | Thành tích/rep ở kỹ thuật chuẩn; mức nỗ lực |
| Hypertrophy | Kích thích nhóm cơ ưu tiên và độ bao phủ toàn thân | Bài trùng vai trò, kỹ thuật tăng cường không cần thiết | Reps/tải; số đo chuẩn hóa; xu hướng cân |
| Sức khỏe | Các kiểu vận động chính và hoạt động aerobic | Chuyên biệt hóa nhỏ | Khả năng sinh hoạt, mức hoàn thành, sức bền |
| Duy trì trong tuần bận | Những bài quen có giá trị cao nhất | Volume thêm để tối ưu tốc độ tiến bộ | Giữ được năng lực và thói quen |

Đây là ưu tiên thiết kế, không có nghĩa chỉ tập ba lift sẽ đáp ứng mọi nhu cầu cơ thể.

## 17.6. Hai ví dụ tăng tiến đủ rõ để triển khai [H]

### Double progression cho bài phụ

Ví dụ đã chọn: 3 set × 8–12 reps, mục tiêu khoảng 2 RIR, cùng ROM và thiết bị.

- Hoàn thành 12/12/12, RIR và kỹ thuật đúng trong hai lần tập liên tiếp → tăng mức tạ nhỏ nhất hợp lý, trở lại phần thấp của dải reps.
- Hoàn thành 12/10/9 đúng RIR → giữ tạ; lần sau thử thêm rep ở set chưa đạt trần.
- Chạm 12 rep nhưng phải rút ROM hoặc đến failure ngoài kế hoạch → chưa đạt điều kiện tăng.
- Không đạt 8 rep ngay set đầu dù đã nghỉ/khởi động phù hợp → điều chỉnh tạ trong buổi; ghi nguyên nhân, không xem là “thiếu ý chí”.
- Mức tăng nhỏ nhất của máy quá lớn → tiếp tục dải reps phù hợp hoặc đổi cách tăng tiến; không buộc tăng tạ bằng mọi giá.

Điều kiện “hai lần liên tiếp” là lựa chọn vận hành để giảm nhiễu, không phải phát hiện của ACSM.

### Tải kế hoạch kèm giới hạn effort cho bài chính

Ví dụ: một khoảng tải dự kiến từ lịch gần đây, kèm mục tiêu rep và RPE trần.

- Khởi động và set đầu nằm trong khoảng effort → thực hiện số set kế hoạch.
- Set đầu nặng hơn mục tiêu rõ rệt → kiểm tra nghỉ, sai tải, kỹ thuật và triệu chứng; nếu chỉ là readiness thấp, giảm một bước tải rồi đánh giá lại.
- Sau điều chỉnh vẫn lệch effort hoặc kỹ thuật tiếp tục giảm → cắt set còn lại hoặc chuyển phiên bản buổi nhẹ hơn.
- Có triệu chứng mới đáng lo → nhánh sức khỏe ưu tiên, không tiếp tục tìm mức tạ “vượt qua đau”.

Không chuyển RPE thành một tỷ lệ giảm kg cố định cho mọi bài. Mức giảm khởi đầu phải phù hợp bước tạ và dữ liệu cá nhân.

## 17.7. Chững tiến bộ và deload

**[H] Trình tự điều tra:** kiểm tra số buổi thực hiện → độ nhất quán của kỹ thuật/đo lường → effort thực tế → khả năng hồi phục → năng lượng ăn vào → mức kích thích → thay đổi chương trình.

| Quan sát | Giả thuyết cần kiểm tra | Hành động thử nghiệm |
|---|---|---|
| Ít hoàn thành buổi, thường hết giờ | Lịch vượt khả năng thực hiện | Rút gọn hoặc giảm số ngày rồi phân bổ lại |
| Hoàn thành đều, set quá dễ | Liều/nỗ lực chưa phù hợp | Tăng reps/tải theo quy tắc |
| Nhiều bài cùng giảm thành tích, mệt tích lũy | Hồi phục kém hoặc bệnh/thiếu năng lượng | Sàng lọc sức khỏe; thử giảm stress tập |
| Chỉ một bài chững | Kỹ thuật, bài chọn, đặc tính riêng của lift | Giữ phần đang hiệu quả; điều chỉnh cục bộ |
| Cân giảm ngoài kế hoạch, tập xuống sức | Ăn thiếu hoặc vấn đề sức khỏe | Đánh giá dinh dưỡng và triệu chứng |

Deload là giảm stress tập có chủ đích, khác nghỉ bệnh và khác taper thi đấu. Ví dụ có thể giảm số set trước, giữ kỹ thuật ở tải dung nạp; không bắt buộc cứ tuần 4 phải deload. Ghi thời hạn thử nghiệm và đánh giá đáp ứng trước khi trở lại volume cũ. Nếu triệu chứng dai dẳng, không lặp vô hạn các tuần deload để trì hoãn đánh giá chuyên môn.

## 17.8. Powerlifting: periodization và peaking

**[E]** Tổng quan về taper năm 2020 đề xuất xem xét giảm volume khoảng 30–70%, trong 1–2 tuần; intensity có thể giữ cao hoặc giảm tùy giai đoạn; một số cách dùng 2–7 ngày ngừng tập cuối. Bằng chứng gồm nhiều nhóm strength/power, mẫu nhỏ và không đồng nhất, nên không phải công thức đảm bảo PR. [T04 — Tapering and Peaking, Conclusion và Tables 2–4](https://pmc.ncbi.nlm.nih.gov/articles/PMC7552788/).

**[H] Cách chuyển sang toolkit:** lịch thi đấu là đầu vào; xác định block xây nền, phát triển strength và thể hiện thành tích theo nhu cầu. Chọn taper dựa trên lần tập cuối từng lift, fatigue và trải nghiệm trước; không ép cả ba lift có cùng số ngày nghỉ. Nếu công việc làm mất một tuần tập sát giải, không tự động “bù volume” vào taper. Tạo lại kế hoạch và kỳ vọng thi đấu.

Các nhánh còn cần dữ liệu riêng trước khi dùng cho thi đấu: luật liên đoàn, commands, tiêu chuẩn động tác, thiết bị được phép, thời gian cân, lựa chọn attempts và quản lý hạng cân. Không dùng module dinh dưỡng giảm mỡ để sinh quy trình cắt nước.

## 17.9. Điều kiện xuất một giáo án

Mỗi giáo án phải chỉ rõ: đối tượng; mục tiêu; thời gian; bài/sets/reps/tải hoặc effort/nghỉ; cách thay bài; lý do phân bổ; phiên bản ít thời gian; cách tăng/giảm; thời điểm review. Nguồn chỉ hỗ trợ nguyên lý nào phải ghi đúng nguyên lý đó, không gán cả lịch minh họa cho tác giả nguồn.

## 17.10. Bổ sung từ tài nguyên người dùng: chu kỳ hóa và chuẩn hóa tiến bộ [H]

Tiếp nhận có điều kiện từ U01/U06/U08, [hồ sơ phần 28](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md). Đây là mô hình tổ chức, không phải chứng minh mô hình nào tốt nhất theo cấp độ người tập.

| Mô hình | Cách tổ chức | Khi có thể phù hợp | Không được mặc định |
|---|---|---|---|
| Linear | Thay đổi có hướng qua thời gian, thường tăng tải tương đối và giảm reps/volume | Có giai đoạn ưu tiên rõ và muốn cấu trúc dễ theo dõi | Mọi novice phải dùng, hoặc mỗi tuần phải tăng kg |
| DUP | Thay đổi nội dung/rep range trong một chu kỳ ngắn | Cần phân bố nhiều mục tiêu hoặc nhiều lần tiếp xúc lift | Thay đổi rep tự chứng minh tránh được “neural accommodation” |
| Block | Mỗi khối ưu tiên một phẩm chất, giữ phần khác ở liều phù hợp | Deadline hoặc ưu tiên cần quản lý qua các giai đoạn | Mọi người phải hypertrophy→strength→peaking hoặc bỏ hết phẩm chất khác |
| Conjugate/Westside-style | Phối hợp max/dynamic effort và thay biến thể theo hệ thống | Mục tiêu, kinh nghiệm và khả năng theo dõi phù hợp | Nhãn “advanced” tự đủ lý do chọn; xoay bài luôn có lợi |

Macrocycle là kế hoạch dài hạn; mesocycle là khối; microcycle là vòng lặp ngắn. Các ví dụ một năm/3–6 tuần/7 ngày trong nguồn là cách bố trí, không định nghĩa bắt buộc. Người làm ca có thể dùng vòng A/B/C; xem W07 phần 23.

**Chuẩn hóa để biết đã tiến bộ:** ghi cả tải, reps, ROM, tempo nếu quy định, effort và thiết bị. Tăng reps cùng tải/ROM/effort là một dạng tiến bộ; đổi ROM hoặc tempo là thay đổi nhiệm vụ và có thể cần baseline mới. Giảm rest không tự là hypertrophy tốt hơn nếu chất lượng/rep giảm. Tránh gọi mọi biến thể khó hơn là overload phù hợp mục tiêu.

**Specificity:** có thể tăng thực hành lift mục tiêu khi gần kiểm tra/thi đấu, nhưng không bắt thay mọi isolation bằng compound. Xét tổng stress, giới hạn cá nhân và phần kỹ năng cần giữ. Danh sách bài và đánh đổi ở [phần 26](references/26-chon-bai-tap-va-bien-the-theo-muc-tieu.md).


---

<!-- CHAPTER 18 -->

# 18. DINH DƯỠNG VÀ ĐIỀU CHỈNH THEO MỤC TIÊU

Ngày nghiên cứu: 14/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Ma trận nguồn](references/24-ma-tran-nguon-va-kiem-chung.md).

**Phạm vi:** nền tảng cho người trưởng thành hoạt động thể lực. Công thức và ví dụ không thay thế kế hoạch lâm sàng cho bệnh thận, đái tháo đường cần thuốc, thai kỳ, trẻ em, rối loạn ăn uống hoặc tình trạng sau mổ. **[E]** là bằng chứng nguồn; **[H]** là cách vận hành đề xuất cho toolkit.

## 18.1. Đầu vào và thứ tự xử lý [H]

Thu thập tuổi, chiều cao, cân nặng, xu hướng cân, mục tiêu, lịch tập và công việc, thói quen ăn, dị ứng, thực phẩm kiêng, ngân sách, khả năng nấu, triệu chứng tiêu hóa, bệnh/thuốc có liên quan. Nếu dùng khối nạc phải lưu phương pháp ước tính và sai số. Không tự điền body-fat từ ảnh.

Thứ tự: **phạm vi sức khỏe → năng lượng → protein → fat và carbohydrate → chất lượng khẩu phần/vi chất → timing → supplement → theo dõi và hiệu chỉnh**. Một kế hoạch không thể thực hiện trong lịch làm việc thực tế chưa phải kế hoạch tốt.

## 18.2. Năng lượng: ước tính khác với đo lường

**[E] Mifflin–St Jeor** dự đoán năng lượng lúc nghỉ, không phải tổng năng lượng trong ngày:

```text
REE nam   = 10 × cân nặng kg + 6,25 × chiều cao cm − 5 × tuổi + 5
REE nữ    = 10 × cân nặng kg + 6,25 × chiều cao cm − 5 × tuổi − 161
```

Nguồn gốc là nghiên cứu người khỏe mạnh, không phải công thức riêng cho VĐV hoặc người đang bị bệnh. [N01 — Mifflin et al., 1990, abstract có công thức](https://pubmed.ncbi.nlm.nih.gov/2305711/).

**[H] TDEE khởi đầu:** dùng REE và một giả định hoạt động được ghi rõ; cung cấp một khoảng thay vì độ chính xác giả. Nếu đã có lịch ăn và cân ổn định, ưu tiên dữ liệu thực tế có chất lượng. Không vừa nhân hệ số đã bao gồm tập vừa cộng toàn bộ calories đồng hồ báo.

Ví dụ tính toán: nam 30 tuổi, 75 kg, 175 cm → REE 1.698,75 kcal/ngày. Giả định hoạt động 1,5 → TDEE khoảng 2.550 kcal/ngày. Hệ số 1,5 ở đây chỉ là giả định minh họa; cân nặng và phản hồi sẽ kiểm tra nó.

## 18.3. Chọn mục tiêu năng lượng

**[E]** Giảm mỡ đòi hỏi thâm hụt năng lượng kéo dài; nhiều kiểu ăn có thể hiệu quả nếu tạo thâm hụt và được duy trì. Đo thành phần cơ thể có sai số; tốc độ giảm nên xét mức mỡ, khối nạc, năng lực tập và mức tuân thủ. [N02 — ISSN Diets and Body Composition, Position Statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC5470183/).

**[E] Off-season bodybuilding:** narrative review đề xuất surplus khoảng 10–20% cho người mới/trung cấp, mục tiêu tăng khoảng 0,25–0,5% cân/tuần; người nâng cao thận trọng hơn. Bằng chứng dài hạn trực tiếp ở bodybuilder còn thiếu. Đây là khoảng tham khảo, không phải lý do buộc mọi người ăn surplus lớn. [N03 — Off-season Nutrition, Energy và Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC6680710/).

**[E] Physique preparation:** giảm cân chậm, đặc biệt khi đã lean, giúp quản lý đánh đổi về khối nạc, thành tích và sức khỏe. Contest prep và hồi phục sau giải là tình huống chuyên biệt; cần theo dõi sinh lý, tâm lý và hành vi ăn, không chỉ số cân. [N04 — Nutritional Recommendations for Physique Athletes](https://pmc.ncbi.nlm.nih.gov/articles/PMC7052702/).

**[H] Lựa chọn vận hành minh họa:** với người khỏe mạnh giảm mỡ không thi đấu, có thể thử thâm hụt nhẹ, theo dõi tốc độ và khả năng tập; nếu muốn con số để kiểm thử, dùng 10–15% làm giả định ban đầu và ghi rõ chưa phải quy tắc phổ quát. Duy trì là lựa chọn hợp lệ trong tuần stress, rehab hoặc khi không đủ dữ liệu. “Recomp” được theo dõi bằng nhiều chỉ số, không hứa chắc giảm mỡ và tăng cơ đồng thời cho mọi người.

## 18.4. Protein: giữ đúng mẫu số

**[E] ISSN 2017:** khoảng 1,4–2,0 g/kg cân nặng/ngày phù hợp đa số người tập; khoảng 20–40 g hoặc 0,25 g/kg mỗi lần là hướng tham khảo cho protein chất lượng cao. Tổng ngày và phân bố đều quan trọng hơn một cửa sổ vài phút. Khoảng 2,3–3,1 g/kg **khối nạc** được thảo luận cho người tập kháng lực trong thâm hụt; không nhân nhầm với tổng cân nặng. [N05 — Protein and Exercise, Position Stand](https://pmc.ncbi.nlm.nih.gov/articles/PMC5477153/).

**[E] Nguồn Việt:** Viện Dinh dưỡng trình bày 1,2–2,0 g/kg/ngày cho vận động viên, 1,6–2,4 g/kg khi giảm cân, và lưu ý nhu cầu khi có chấn thương. Bài cập nhật 2025 nhưng tham chiếu bài năm 2016; không coi năm đăng web là năm của bằng chứng gốc. [V01 — Nhu cầu protein đối với người hoạt động thể lực](https://viendinhduong.vn/vi/professional-activities/nhung-loi-khuyen-dinh-duong/67dcedfc3770b9299302c692).

**[H] Quy tắc:** lưu `protein_basis = body_weight` hoặc `fat_free_mass`; hiển thị phép tính. Người không biết khối nạc dùng phương án không cần khối nạc. Với béo phì hoặc bệnh ảnh hưởng dinh dưỡng, không tự nhân cực cao theo cân thực rồi gọi là cá nhân hóa. Whey là lựa chọn tiện lợi để đạt mục tiêu, không bắt buộc. Ăn chay cần thiết kế đa dạng nguồn và đủ tổng lượng; không loại tự động mọi protein thực vật.

## 18.5. Fat, carbohydrate và ví dụ kiểm tra tổng năng lượng

**[E]** Review off-season gợi ý fat khoảng 0,5–1,5 g/kg/ngày; carbohydrate nhận phần năng lượng còn lại, thường xét khoảng ≥3–5 g/kg khi nhu cầu và năng lượng cho phép. Đây không phải mức tối thiểu bắt buộc khi đang cut hay ít vận động. [N03](https://pmc.ncbi.nlm.nih.gov/articles/PMC6680710/).

**[H] Ví dụ thực hành, không phải thực đơn cá nhân:** 75 kg, chọn 2.300 kcal; protein 150 g, fat 70 g:

```text
Năng lượng protein = 150 × 4 = 600 kcal
Năng lượng fat     = 70 × 9  = 630 kcal
Carbohydrate       = (2.300 − 600 − 630) / 4 = 267,5 g
Kiểm tra           = 600 + 630 + 1.070 = 2.300 kcal
```

Khi các khoảng protein/fat/carb và tổng kcal không đồng thời khả thi, toolkit phải báo xung đột, xét lại mục tiêu và mức năng lượng; không xuất các số cộng lại sai. Quy đổi 4/4/9 là cách tính gần đúng; nhãn thực phẩm và dữ liệu có thể chênh vì làm tròn, chất xơ và phương pháp tính.

Ngày tập và ngày nghỉ có thể dùng cùng mức ăn để dễ tuân thủ. Nếu phân kỳ, giữ tổng năng lượng và protein trong kế hoạch, phân bố carbohydrate theo nhu cầu; việc bỏ một buổi không tự động dẫn đến nhịn bữa.

## 18.6. Nước và điện giải

**[E] NATA:** nhu cầu khác theo mồ hôi, thời tiết, thời lượng và dung nạp tiêu hóa; cần đủ nhưng tránh uống quá mức. Đo trước/sau tập có ích để xây chiến lược cá nhân. Không có một số lít áp dụng cho mọi người. [N06 — Fluid Replacement Position Statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC5634236/).

**[H] Công thức ghi chép thực địa gần đúng:**

```text
Mồ hôi mất (L) ≈ cân trước − cân sau (kg) + nước uống (L) − nước tiểu (L)
Tốc độ mồ hôi ≈ lượng mất / số giờ tập
```

Cân cùng điều kiện và quần áo khô tương tự. Đây là ước tính, không phải đo chính xác mất natri. Không bù lại bằng uống thật nhanh một lượng lớn nước lọc. Nếu có bệnh/thuốc yêu cầu hạn chế dịch hoặc điện giải, dùng kế hoạch của người điều trị. Môi trường nóng và lao động ngoài trời là phần tải của ngày, không chỉ buổi gym.

## 18.7. Supplement và giới hạn

**[E] Creatine monohydrate:** có bằng chứng hỗ trợ các hoạt động cường độ cao và thích nghi tập luyện. Có thể dùng 3–5 g/ngày để tăng dự trữ dần, không bắt buộc loading. Loading và chế độ duy trì là các phương án khác nhau; không cộng cả hai vô thời hạn. [N07 — ISSN Creatine Position Stand](https://pmc.ncbi.nlm.nih.gov/articles/PMC5469049/).

**[H] Mặc định toolkit:** ưu tiên thực phẩm; supplement là module tùy chọn có mục đích và cách theo dõi. Không tự thêm sắt/vitamin D liều điều trị, chất “đốt mỡ”, hormone hoặc thuốc giảm đau để hoàn thành buổi. Khi dùng creatine, ghi thời điểm bắt đầu để không hiểu nhầm thay đổi nước/cân là tăng mỡ. Caffeine cần cân nhắc giấc ngủ, công việc theo ca, bệnh/thuốc và dung nạp; phần này chưa đặt liều tự động.

## 18.8. Thiếu năng lượng tương đối trong thể thao (REDs)

**[E] IOC 2023:** chẩn đoán cần đánh giá lâm sàng và nhiều chỉ dấu, không chỉ tính calories. Sức khỏe xương, chức năng sinh sản, chuyển hóa, tâm lý và hiệu suất có thể liên quan đến thiếu năng lượng có vấn đề. [N08 — IOC REDs 2023; trong đợt này chỉ đọc được phần nội dung được lập chỉ mục, chưa kiểm chứng toàn bộ CAT2](https://doi.org/10.1136/bjsports-2023-106994).

**[H] Nhánh dừng tự động giảm ăn:** có giảm cân ngoài ý muốn, rối loạn kinh nguyệt, chấn thương xương do stress tái diễn, mệt kéo dài, hành vi ăn đáng lo hoặc sa sút chức năng → đề nghị đánh giá phù hợp; không tự kết luận REDs. Không dùng “dưới 30 kcal/kg khối nạc” làm bộ chẩn đoán nhị phân. Không có đủ dữ liệu để triển khai toàn bộ công cụ IOC trong toolkit này.

## 18.9. Review và điều chỉnh [H]

| Tình huống | Kiểm tra trước | Hành động đề xuất |
|---|---|---|
| Cân thay đổi mạnh trong 1–3 ngày | Muối, carbohydrate, tiêu hóa, chu kỳ kinh, creatine, điều kiện cân | Giữ kế hoạch; chưa coi là thay đổi mỡ |
| Xu hướng không đúng mục tiêu | Độ đầy đủ nhật ký, mức vận động, đủ thời gian quan sát chưa | Nếu dữ liệu đủ, đổi một bước nhỏ rồi theo dõi |
| Cân giảm nhưng strength ổn, sinh hoạt tốt | Tốc độ có nằm trong mục tiêu đã thống nhất? | Tiếp tục, không giảm ăn thêm chỉ vì muốn nhanh |
| Cân giảm nhanh và nhiều bài xuống sức | Thiếu ăn, thiếu ngủ, bệnh, volume quá cao | Giảm độ quyết liệt; đánh giá sức khỏe nếu cần |
| Tuần làm việc ít vận động hơn | Thay đổi có kéo dài không? | Không giảm kcal theo phản xạ; kiểm tra xu hướng |
| Tăng cân nhưng vòng eo tăng nhanh, tập không tiến | Surplus, chất lượng tập, cách đo | Xem lại surplus và chương trình |
| Nhật ký thiếu nhiều | Không đủ cơ sở kết luận | Giữ hoặc dùng kế hoạch đơn giản hơn; yêu cầu dữ liệu tối thiểu |

Ví dụ kỹ thuật để kiểm thử: xem trung bình cân theo tuần trong 2–3 tuần; điều chỉnh 100–200 kcal/ngày mỗi lần nếu cần. Đây là **heuristic**, không thích hợp mọi đối tượng và không áp khi có triệu chứng đáng lo. Người theo dõi cân gây căng thẳng có thể dùng cách đánh giá khác cùng chuyên gia. Không đổi kcal, cardio và volume tập cùng lúc nếu mục tiêu là xác định nguyên nhân.

## 18.10. Dữ liệu thực phẩm Việt Nam

Đã xác định [N09 — Vietnamese Food Composition Table trong danh mục FAO](https://www.fao.org/food-composition/tables-and-databases/detail/%28viet-nam--2007%29-vietnamese-food-composition-table/en) và [N10 — USDA FoodData Central](https://fdc.nal.usda.gov/data-documentation.html). Danh mục không đồng nghĩa đã kiểm tra từng giá trị hoặc nhập database.

Schema đề xuất: tên thực phẩm; mã nguồn; phiên bản; phần ăn được; sống/chín; cách chế biến; đơn vị; giá trị/100 g; nutrient thiếu dữ liệu; ngày truy cập. **Thiếu dữ liệu khác 0.** Với món hỗn hợp, lưu nguyên liệu, khối lượng trước/sau nấu, số phần, dầu/nước sốt; không coi “một bát cơm” có khối lượng cố định.

Toolkit có thể xuất kế hoạch theo nhóm thực phẩm khi chưa có dữ liệu món Việt đủ tốt, nhưng phải nói rõ đó là ước tính và chưa thể hứa một thực đơn gram chính xác.


---

<!-- CHAPTER 19 -->

# 19. SÀNG LỌC VÀ ĐỊNH HƯỚNG CHẨN ĐOÁN CƠ–KHỚP–MÔ MỀM

Ngày nghiên cứu: 14/09/2026. [Nguồn và mức độ đã đọc](references/24-ma-tran-nguon-va-kiem-chung.md) · [Rehab chi dưới](references/20-rehab-chi-duoi-va-tro-lai-van-dong.md) · [Lưng và chi trên](references/21-rehab-lung-vai-khuyu-va-chan-doan-phan-biet.md).

## 19.1. Chức năng của module

Module cần giúp người dùng mô tả triệu chứng, nhận ra mức cần chăm sóc y tế và hiểu cách chuyên gia phân biệt các khả năng. Nó không được tự khẳng định “rách gân độ II”, “thoát vị đĩa đệm” hoặc kê điều trị chỉ từ vị trí đau hay một self-test.

**Chấn thương mô mềm** trong phạm vi này gồm cơ, gân, dây chằng và cấu trúc mô mềm quanh khớp. Đau tại một vùng còn có thể liên quan xương, thần kinh, viêm hệ thống hoặc nội tạng. Vết thương hở, nhiễm trùng, bỏng và chấn thương lớn cần nhánh chăm sóc riêng.

**[E]** thông tin từ nguồn; **[H]** cấu trúc ứng dụng đề xuất; mọi quyết định chẩn đoán chuyên môn do người có chuyên môn thực hiện.

## 19.2. Từ ngữ phải phân biệt

| Thuật ngữ | Ý nghĩa cần giữ | Không được suy ra |
|---|---|---|
| Strain | Tổn thương đơn vị cơ–gân do kéo/tải; có thể từ nhẹ đến rách | Mọi cảm giác căng đều là rách cơ |
| Sprain / bong gân | Tổn thương dây chằng | Đồng nghĩa trật khớp hay viêm gân |
| Tendinopathy | Hội chứng đau/rối loạn chức năng liên quan gân, thường với tải | Chỉ là viêm; hoặc tuyệt đối không có vai trò viêm |
| Dislocation / trật khớp | Mất tương quan khớp bình thường | Có thể tự nắn theo video |
| DOMS | Đau cơ xuất hiện muộn sau kích thích tập, thường sau bài lạ | Mọi đau sau tập đều là DOMS |
| Radicular/neuropathic symptoms | Đau lan, tê, yếu hoặc thay đổi cảm giác gợi ý cần khám thần kinh | Tất cả tê đều do “cơ căng” |
| Osteoarthritis | Bệnh khớp cần đánh giá trong bối cảnh lâm sàng | Khớp phải bất động vĩnh viễn |

Nguồn giáo dục đối chiếu: [C01 — NHS Sprains and Strains](https://www.nhs.uk/conditions/sprains-and-strains/), [V02 — Vinmec: Phân biệt căng cơ–bong gân](https://www.vinmec.com/vie/bai-viet/phan-biet-cang-co-bong-gan-huong-dan-cach-so-cuu-vi). Những từ này dùng để tổ chức thông tin, không thay thế khám.

## 19.3. Bảng tiếp nhận triệu chứng [H]

| Câu hỏi | Chi tiết cần ghi | Tại sao quan trọng |
|---|---|---|
| Đau ở đâu? | Bên, điểm đau, diện rộng, đường lan | Tránh chỉ ghi “đau chân” |
| Khởi đầu thế nào? | Đột ngột hay tăng dần; tai nạn/va chạm; bài tập; có tiếng pop | Phân loại hướng đánh giá |
| Bao lâu? | Ngày bắt đầu, diễn biến, lần tái phát | Giai đoạn và nhu cầu khám |
| Mất chức năng gì? | Đi lại, chịu trọng lượng, nâng tay, cầm đồ, ngủ | Mức ảnh hưởng quan trọng hơn điểm đau đơn lẻ |
| Dấu tại chỗ? | Sưng, bầm, nóng, đỏ, biến dạng, vết hở | Nhận diện khả năng tổn thương cần chăm sóc |
| Thần kinh/mạch máu? | Tê mới, yếu mới, chi lạnh/đổi màu | Có thể thay đổi mức khẩn cấp |
| Toàn thân? | Sốt, mệt bất thường, sụt cân không chủ ý | Không mặc định là quá tải tập |
| Liên quan tải? | Khi tập, ngay sau, sáng hôm sau; công việc; môn khác | Xác định tổng stress thực tế |
| Điều trị trước? | Chẩn đoán, phẫu thuật, thuốc, giới hạn chịu tải/ROM | Không ghi đè chỉ định cá nhân |
| Bối cảnh | Bệnh nền, tiền sử gãy/rách, osteoporosis, thuốc có liên quan | Điều chỉnh mức nghi ngờ và chuyển chuyên gia |

Cho phép câu trả lời “không biết”. Không có dữ liệu không đồng nghĩa không có dấu hiệu.

## 19.4. Những tình huống cần hành động ngay

| Dấu hiệu | Hướng xử lý cho toolkit | Căn cứ |
|---|---|---|
| Đau lưng kèm mới xuất hiện rối loạn tiểu/đại tiện, tê vùng sinh dục/hậu môn, triệu chứng hai chân | Dừng chương trình; hướng dẫn đến cấp cứu ngay | [C02 — NHS Back Pain](https://www.nhs.uk/conditions/back-pain/) |
| Khớp đau dữ dội, sưng nóng đột ngột, khó vận động/chịu tải; có thể có sốt | Đánh giá y tế khẩn, không “thử tập cho nóng” | [C03 — NHS Septic Arthritis](https://www.nhs.uk/conditions/septic-arthritis/) |
| Đau cơ vượt xa mức dự kiến, yếu bất thường hoặc nước tiểu sẫm sau gắng sức | Chăm sóc y tế ngay vì cần loại trừ tiêu cơ vân; không chỉ bù nước tại nhà | [C04 — CDC Rhabdomyolysis](https://www.cdc.gov/niosh/rhabdo/signs-symptoms/index.html) |
| Sau chấn thương có biến dạng, tê hoặc chi lạnh/đổi màu | Cấp cứu, không tự nắn hoặc kéo giãn | [C01 — NHS Sprains and Strains](https://www.nhs.uk/conditions/sprains-and-strains/) |
| Đau ngực, ngất, khó thở nặng hoặc chấn thương lớn | Ngừng tập, gọi hỗ trợ y tế khẩn tại nơi đang ở | Nhánh cấp cứu chung; không dùng module cơ xương khớp để loại trừ |

Không đợi đủ mọi triệu chứng trong một hàng mới xử lý. Sốt có thể không xuất hiện trong viêm khớp nhiễm trùng; nước tiểu bình thường không loại trừ tiêu cơ vân. Toolkit không chẩn đoán các bệnh trên; nó nhận ra lý do cần đánh giá ngay.

**[H] Phân tầng tiếp theo:** mất chức năng rõ sau chấn thương, tiếng pop kèm yếu đáng kể, sưng/bầm tăng hoặc không chịu tải được → khám sớm/khẩn tùy biểu hiện. Đau dai dẳng/tái phát, tê, yếu, khó ngủ hoặc không cải thiện với kế hoạch phù hợp → hẹn chuyên gia; không lặp self-test vô thời hạn.

## 19.5. Logic chẩn đoán phân biệt

Không xây luật “đau ở vị trí X = bệnh Y”. Dùng chuỗi:

1. Loại trừ tình huống cấp cứu và tổn thương cần bảo vệ.
2. Bệnh sử/cơ chế tạo danh sách khả năng.
3. Khám chuyên môn đánh giá vận động chủ động/thụ động, sức mạnh, cảm giác, phản xạ, độ vững hoặc dấu đặc hiệu khi phù hợp.
4. Test làm thay đổi mức nghi ngờ; một test không phải đáp án cuối.
5. Cận lâm sàng khi có câu hỏi cụ thể có thể thay đổi xử trí.
6. Đánh giá lại khi diễn biến không phù hợp giả thuyết ban đầu.

**Ví dụ [E]:** đau mặt sau đùi có thể là hamstring strain, tổn thương gân gần ụ ngồi, đau gân khởi phát dần, đau liên quan cột sống hoặc tổn thương adductor. Cơ chế và vị trí giúp phân biệt nhưng cần khám. MRI có thể làm rõ vị trí và phạm vi; phân loại MRI chi tiết không luôn dự đoán thời điểm trở lại tốt hơn khám. [C05 — Hamstring Strain Injury Rehabilitation, Differential Diagnosis và MRI](https://pmc.ncbi.nlm.nih.gov/articles/PMC8876884/).

## 19.6. Đau và hình ảnh học

**[E] NICE NG59:** không chụp thường quy cho đau lưng/sciatica ở cơ sở không chuyên khoa; cân nhắc ở chuyên khoa nếu kết quả có khả năng thay đổi quản lý. Điều này không áp dụng để bỏ qua dấu bệnh nghiêm trọng. [C06 — NICE NG59, 1.1.4–1.1.6](https://www.nice.org.uk/guidance/NG59/chapter/recommendations).

**[H] Mỗi yêu cầu chụp nên gắn câu hỏi:** nghi gãy? nghi đứt gân? cần đánh giá cấu trúc trước can thiệp? có diễn biến khác dự kiến? Không gán “MRI bình thường → không đau thật”, cũng không “MRI có bất thường → nguyên nhân chắc chắn”. Không dùng ảnh chụp để xếp lịch trở lại thể thao mà thiếu chức năng thực tế.

Trong module phục vụ người dùng, các nghiệm pháp đặc hiệu nên được mô tả về **vai trò và giới hạn**, không hướng dẫn tự thực hiện thao tác gây đau mạnh để “xác nhận bệnh”. Các số sensitivity/specificity chỉ được dùng khi giữ đúng mẫu nghiên cứu, người thực hiện và cách định nghĩa test.

## 19.7. Sơ cứu, giảm triệu chứng và tải sớm

**[E] NHS** hướng dẫn bảo vệ, nghỉ tương đối giai đoạn đầu, chườm lạnh có lớp ngăn da, băng ép và kê cao; vận động trở lại khi đau không ngăn cản để tránh cứng. Chườm lạnh là công cụ kiểm soát triệu chứng, không bằng chứng bảo đảm mô lành nhanh. [C01](https://www.nhs.uk/conditions/sprains-and-strains/).

**[H] Áp dụng:** sau khi đã loại trừ tình huống cần cấp cứu, ưu tiên bảo vệ vùng tổn thương và hướng dẫn khám khi cần. Không lấy “rest” thành nghỉ mọi hoạt động nhiều tuần. Cũng không lấy “early loading” thành nâng nặng ngay sau tai nạn. Vùng chưa được xác định tổn thương không được nhận protocol gân mạn tính.

Các phương pháp thụ động, thuốc và thủ thuật phải được xem theo từng tình trạng, hiệu quả ngắn/dài hạn, chống chỉ định và vai trò hỗ trợ. Toolkit không tự kê thuốc hoặc gợi ý dùng giảm đau để che triệu chứng rồi test max.

## 19.8. Theo dõi đau đúng cách [H]

Ghi điểm đau cùng **nhiệm vụ cụ thể**, thời điểm và điều kiện. “3/10 khi đi bộ 10 phút” khác “3/10 khi ngồi nghỉ”; không ghép chung thành điểm tuần. Theo dõi cả sưng, ROM, sức mạnh, thời gian hoạt động, giấc ngủ và mức tự tin.

Một số chương trình tendinopathy dùng pain-monitoring với ngưỡng số cụ thể; không chuyển sang mọi chấn thương, đau thần kinh, gãy xương hoặc sau mổ. Việc đau giảm sau khởi động chỉ là một quan sát, chưa đủ chứng minh có thể tập hết lịch.

Mẫu:

```text
Triệu chứng nền trước buổi:
Nhiệm vụ/tải gây triệu chứng:
Đáp ứng trong buổi:
Đáp ứng sau buổi và sáng hôm sau:
Thay đổi chức năng/sưng:
Giới hạn người điều trị đã đặt:
Quyết định và ngày đánh giá lại:
```

## 19.9. Đầu ra hợp lệ

Một bản định hướng phải có: thông tin đã biết/chưa biết; mức khẩn cấp; nhóm khả năng cần phân biệt; thông tin cần khám thêm; giới hạn tạm thời; theo dõi và điều kiện quay lại. Chẩn đoán đã được xác nhận phải lưu người xác nhận, ngày, bên/vùng và hạn chế liên quan.

Không dùng sự chắc chắn về một bài tập để thay thế sự chưa chắc chắn về tình trạng bệnh.

## 19.10. Điều kiện khi dùng “24 giờ”, entry point và isometric

Bổ sung đối chiếu U01/U07/U08 ngày 15/09/2026; [hồ sơ](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md).

**[H]** Mốc sáng hôm sau/khoảng 24 giờ là cửa sổ thu thập đáp ứng, không phải phép xác nhận mọi mô đã hồi phục. Đau trở lại baseline chưa đủ nếu sưng, chức năng hoặc sức mạnh vẫn giảm. Phản ứng xấu cũng không tự chứng minh đã gây tổn thương mới; xem liều và đánh giá lại. Giữ rule riêng của chẩn đoán/plan thay vì bắt mọi ca cùng một mốc.

**[E] C23:** review 10 nghiên cứu tendinopathy, phần lớn chất lượng thấp, không cho thấy isometric vượt isotonic trong quản lý tendinopathy mạn; đáp ứng thay đổi giữa người và tình trạng. Có thể là thành phần của progressive loading, không bảo đảm giảm đau ngay. Đã đọc abstract. [Clifford et al., 2020](https://pubmed.ncbi.nlm.nih.gov/32818059/).

**[H]** Co tĩnh vẫn tạo lực; không mô tả là “không có áp lực lên khớp”. Entry point là nhiệm vụ/liều phù hợp sau sàng lọc, không bắt buộc isometric trước rồi HSR 3 giây xuống/3 giây lên. Các kiểu co, ROM và tốc độ được chọn theo mục tiêu và hạn chế của tình trạng; protocol đúng vùng ở phần 20–21 ưu tiên hơn lộ trình chung trong tệp gửi.


---

<!-- CHAPTER 20 -->

# 20. REHAB CHI DƯỚI VÀ TRỞ LẠI VẬN ĐỘNG

Ngày nghiên cứu: 14/09/2026. Dùng sau [sàng lọc phần 19](references/19-sang-loc-va-dinh-huong-chan-doan.md). [Ma trận nguồn](references/24-ma-tran-nguon-va-kiem-chung.md).

**[E]** bằng chứng/guideline; **[C]** đề xuất đồng thuận; **[H]** cấu trúc triển khai cần chuyên gia duyệt. Các giai đoạn là tiêu chí chức năng, không lịch chữa khỏi được bảo đảm. Chẩn đoán cụ thể và hạn chế hậu phẫu được ưu tiên hơn mẫu này.

## 20.1. Hamstring strain: tổn thương cơ–gân sau đùi

### Cơ chế, đánh giá và điều cần giữ

**[E]** Tổn thương thường xảy ra khi chạy nhanh hoặc kéo dài hamstring mạnh. CPG 2022 khuyến nghị đánh giá lực gấp gối bằng dụng cụ khi có thể, ROM, khả năng đi/chạy và tiền sử tái chấn thương. Eccentric theo dung nạp kết hợp các bài sức mạnh, ổn định, chạy tiến triển là thành phần quan trọng; agility và trunk stabilization có thể được tích hợp. Không quyết định trở lại chỉ vì đã hết đau. [C07 — Hamstring CPG 2022, CPG2 và phần Interventions](https://www.orthopt.org/uploads/content_files/files/Hamstring_Strain_Injury_in_Athletes_2022.pdf).

CPG liên quan vận động viên; không tự áp cho đứt/bong điểm bám gân gần ụ ngồi hoặc mọi đau đùi. Đau dữ dội gần ụ ngồi, bầm nhiều và mất lực sau cơ chế kéo mạnh cần đánh giá khác với strain thông thường.

### Lộ trình đề xuất để ghi vào hồ sơ [H]

| Giai đoạn | Mục đích | Thành phần được chuyên gia lựa chọn | Điều kiện review |
|---|---|---|---|
| Bảo vệ và phục hồi chức năng cơ bản | Đi lại và vận động dung nạp | Co cơ/liều nhẹ, ROM phù hợp, duy trì vùng khác | Đau, dáng đi, chức năng không xấu dần |
| Tăng khả năng chịu lực | Khôi phục knee flexion và hip extension | Slider, bridge, hip extension, RDL/biến thể; tăng theo năng lực | Chất lượng, force và đáp ứng sau buổi |
| Tăng tốc độ và chiều dài chịu tải | Chuẩn bị yêu cầu môn | Eccentric ở chiều dài phù hợp; chạy tăng dần | Dung nạp tốc độ hiện tại, không có phản ứng xấu kéo dài |
| Trở lại nhiệm vụ/môn | Đáp ứng chạy nhanh, đổi hướng, đá hoặc nâng | Tiếp xúc đặc hiệu tăng dần; buổi tập hoàn chỉnh | Kết hợp triệu chứng, lực, ROM, tự tin và nhiệm vụ |

**[E]** Review 2022 nêu bài slider hai chân có thể tiến tới một chân và Nordic theo năng lực; tăng tốc chạy gần tối đa phải thận trọng vì nhu cầu lực tăng mạnh. Không chỉ dùng bài gập gối nhẹ để chứng minh đã sẵn sàng sprint. [C05 — Rehabilitation, Running và Eccentric Loading](https://pmc.ncbi.nlm.nih.gov/articles/PMC8876884/).

**[H]** Liều cụ thể phải ghi từ kế hoạch điều trị: bài, tải, ROM, số lần/tuần, khoảng cách buổi và điều kiện tăng. Không tự điền “3×15 hàng ngày” cho tất cả các pha. Nếu đau khu trú mới, lực giảm đột ngột hoặc bầm/sưng tăng, quay lại đánh giá thay vì tăng bài.

## 20.2. Achilles tendinopathy

### Phân biệt vị trí

**Midportion** và **insertional** là hai nhánh khác nhau. Guideline 2024 đã đọc tập trung **midportion**; không mở rộng toàn bộ khuyến nghị sang điểm bám, đứt gân hoặc sau khâu gân. Ghi rõ vị trí, đau theo tải, cứng buổi sáng và khả năng heel rise.

### Khuyến nghị cốt lõi [E]

- Tendon-loading exercise với tải cao trong khả năng dung nạp là lựa chọn đầu tay nếu không nghi cấu trúc gân mong manh.
- Tập tải gân ít nhất 3 lần/tuần là khuyến nghị **grade E** trong CPG; không gọi đây là bằng chứng mạnh tương đương khuyến nghị tập tải **grade A**.
- Giáo dục kết hợp tập; không chỉ định nghỉ hoàn toàn cho mọi ca midportion.
- Heel lift có thể dùng tạm để giảm dorsiflexion; không có kết luận chắc cho orthoses do bằng chứng mâu thuẫn.
- Không dùng low-level laser; không dùng ultrasound đơn độc như điều trị chính.

[C08 — Achilles 2024, bảng CPG2; Diagnosis CPG8; Interventions CPG10–17](https://www.orthopt.org/uploads/content_files/files/Achilles_Pain_revision_2024.pdf).

### Các mức tải và điều kiện tiến triển

**[E]** Review 2020 mô tả bắt đầu heel rise trên sàn, hai chân hoặc có hỗ trợ nếu cần; tiến tới một chân và tải ngoài khi mức trước không còn khó. Với đau điểm bám, hạn chế nén do xuống gót sâu dưới bậc trong giai đoạn dễ kích thích. Tốc độ nhanh và tải đàn hồi cần chuẩn bị ở pha sau; isometric chưa được chứng minh luôn tốt hơn mọi kiểu co cơ. [C09 — Conservative Management of Achilles Tendinopathy, Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC7249277/).

**[H] Bảng kiểm trước khi đổi mức:**

| Dữ liệu | Giữ/tăng trong kế hoạch | Cần giảm hoặc đánh giá lại |
|---|---|---|
| Đau và cứng sáng | Ổn định trong giới hạn cá nhân | Tăng rõ qua nhiều ngày |
| Heel rise | Đủ chiều cao, kiểm soát và số lần đã đặt | Chiều cao/lực giảm, bù trừ tăng |
| Tải sinh hoạt | Đi lại/cầu thang dung nạp | Công việc tăng tải làm vượt khả năng |
| Buổi trước | Trở lại mức nền theo kế hoạch theo dõi | Phản ứng kéo dài hoặc mất chức năng |
| Nhiệm vụ kế tiếp | Chỉ thêm một yêu cầu mới | Đồng thời tăng kg, reps, tốc độ và chạy |

Không tự dùng calf raise nặng để kiểm tra một trường hợp có tiếng pop, mất khả năng đẩy chân hoặc nghi đứt gân. Không dùng “gân phải tập >70% 1RM” làm luật tuyệt đối; “as tolerated” có điều kiện lâm sàng.

## 20.3. Patellar tendinopathy

**[E]** Đau gân bánh chè thường khu trú, liên quan tải gân; có thể cùng tồn tại với patellofemoral pain. Tập tải tiến triển và điều chỉnh hoạt động là nền. Review trình bày chuỗi quản lý triệu chứng → phục hồi → xây lại tải → trở lại môn. Một mẫu dùng isometric 5 lần giữ 30–60 giây, sau đó bài isotonic và tải nặng chậm; đây là ví dụ có yêu cầu cá nhân hóa. Pain-monitoring được mô tả cho phép đến 5/10 trong/sau tập, phải dưới 5 ngày sau; triệu chứng tăng qua các tuần cần giảm hoạt động. [C10 — Clinical Management of Patellar Tendinopathy, Table 2 và Load Management](https://pmc.ncbi.nlm.nih.gov/articles/PMC9528703/).

**[H] Những chi tiết không được bỏ khi chuyển thành giải pháp:**

1. Đây không phải ngưỡng an toàn 5/10 cho mọi chấn thương.
2. Xác định trước bài/tải gây kích thích: số lần nhảy, chạy, squat, công việc; tổng tải không chỉ nằm trong buổi rehab.
3. Giảm phần kích thích nhưng giữ hoạt động dung nạp; ví dụ tập kỹ thuật môn không nhảy ở giai đoạn phù hợp.
4. Khi tăng tải, ghi biến thay đổi và phản hồi ngày sau.
5. Chuyển sang nhảy nhanh, hãm, đổi hướng phải có khả năng chịu tải tương ứng; squat chậm tốt chưa chứng minh sẵn sàng chơi môn.
6. Nếu không đáp ứng, xem lại chẩn đoán, tuân thủ, liều, tải ngoài buổi và yếu tố sức khỏe; không mặc định chỉ cần tăng eccentric.

## 20.4. Patellofemoral pain: đau quanh/sau bánh chè

**[E]** Best-practice guide 2024 đặt giáo dục và bài tập hướng gối, có thể kết hợp hướng hông, làm nền. Các hỗ trợ như taping, orthoses đúc sẵn, manual therapy hoặc chỉnh động tác cần lựa chọn theo đánh giá và nhu cầu. [C11 — PFP Best Practice 2024](https://pubmed.ncbi.nlm.nih.gov/39401870/). Trong đợt này xác nhận abstract và truy cập được bản PDF nhưng việc đọc toàn văn không ổn định; không trích liều chi tiết từ phần chưa kiểm chứng.

**[H]** Hỏi đau khi cầu thang, squat, chạy, ngồi lâu; ghi mức gập gối và tổng tải. Thử điều chỉnh ROM/tải/bài theo mục tiêu dưới hướng dẫn. Không suy “valgus = nguyên nhân duy nhất”, hoặc “hông yếu = chẩn đoán”. Cần phân biệt gân bánh chè, chấn thương cấp, khớp sưng, khóa gối và tình trạng khác. Quy tắc tiến triển phải xét việc đi cầu thang/làm việc lẫn gym.

## 20.5. Bong gân cổ chân và mất vững tái diễn

Sau chấn thương, trước hết xác định có cần đánh giá gãy, trật, syndesmosis hoặc tổn thương khác. Khả năng bước đi và vị trí đau xương là thông tin cho người khám, không tự đưa Ottawa rules vào app mà chưa kiểm tra đầy đủ đối tượng/ngoại lệ.

**[E]** Meta-analysis 14 RCT, 2.182 người cho thấy rehab bằng exercise có thể giảm tái bong gân so với chăm sóc thông thường; kết quả còn nhạy với chất lượng nghiên cứu, chưa xác định liều/nội dung tối ưu. [C12 — Exercise-based Rehabilitation after Ankle Sprain](https://pmc.ncbi.nlm.nih.gov/articles/PMC8824326/).

**[C] PAASS** là khung đồng thuận gồm: đau; ROM/sức mạnh/sức bền/power cổ chân; tự tin và sẵn sàng tâm lý; kiểm soát cảm giác–vận động/thăng bằng; thực hiện chức năng/môn và buổi tập đầy đủ. Đây là các miền đánh giá, không phải bộ điểm cắt đã được xác nhận cho tất cả vận động viên. [C13 — PAASS 2021, abstract](https://pubmed.ncbi.nlm.nih.gov/34158354/).

**[H]** Lộ trình ghi hồ sơ: bảo vệ/chịu tải theo đánh giá → phục hồi ROM và sức mạnh → thăng bằng và điều khiển → nhảy/đổi hướng → toàn buổi. Cần ghi nẹp/băng hỗ trợ được chỉ định và điều kiện tháo. Không dùng “đã đủ 8 tuần” làm giấy phép quay lại; không mặc định bó bột mọi bong gân 4 tuần. Guideline cổ chân 2021 đã xác định, chưa đọc được toàn văn nên chưa nhập liều/khuyến nghị grade từ đó.

## 20.6. Sau tái tạo ACL

**[E]** Aspetar xem exercise là nền, nhưng bằng chứng liều–đáp ứng còn ít. Điều kiện quay lại chạy và thể thao trong guideline có phần là đề xuất chuyên gia, chưa được xác nhận bằng nghiên cứu như một bộ dự báo an toàn tuyệt đối. [C14 — Aspetar ACLR Guideline](https://pmc.ncbi.nlm.nih.gov/articles/PMC11785408/).

**[C] Tiêu chí quay lại chạy được đề xuất trong Box 5:**

- Knee flexion ROM đạt 95%; duỗi gối đầy đủ. Khi ghi kết quả, nêu rõ ROM đo và mốc tham chiếu của người đánh giá; không hiểu 95% thành 95 độ.
- Không hoặc chỉ rất ít tràn dịch.
- Limb symmetry index (LSI) >80% cho sức mạnh quadriceps.
- LSI >80% cho **eccentric impulse trong countermovement jump**, không phải mọi chỉ số nhảy đều có thể thay cho nhau.
- Aqua jogging và chạy Alter-G không đau.
- Repeated single-leg hopping kiểu “pogos” không đau.

Nguồn mô tả đây là tiêu chí đề xuất khi thiếu nghiên cứu xác nhận. Thiết bị không có tại phòng tập không có nghĩa được tự đánh dấu đạt; cần người phụ trách lựa chọn đánh giá thích hợp và ghi giới hạn.

**[C] Box 5 còn có bộ tiêu chí khác cho VĐV chuyên nghiệp rời clinic để bắt đầu trở lại tập với đội**, rồi tăng dần đến tham gia đầy đủ: không đau/sưng, ROM đủ, khớp ổn định qua khám; chức năng tự báo cáo và readiness tâm lý; sức mạnh isokinetic quadriceps/hamstrings ở 60°/s đạt 100% đối xứng cho môn pivoting yêu cầu cao, đồng thời phục hồi giá trị tuyệt đối và chuẩn môn. Các phép nhảy xét >90% đối xứng chiều cao và concentric/eccentric impulse; có đánh giá biomechanics nhảy/chạy và hoàn thành chương trình đặc hiệu. Đây không phải một ngưỡng LSI duy nhất để tự clearance. Chi tiết test và chuẩn môn phải tra toàn bộ Box 5 cùng chuyên gia trước khi dùng.

**[H] Không bỏ những giới hạn sau:**

- Chạy khác thi đấu môn xoay/đổi hướng; đạt ngưỡng chạy không phải đạt return-to-sport.
- LSI có thể đẹp khi cả hai chân yếu; cần xét giá trị tuyệt đối, dữ liệu trước mổ và nhu cầu môn.
- Loại graft, tổn thương kèm, khâu meniscus và chỉ định surgeon có thể thay đổi kế hoạch.
- Lịch công việc không cho phép tăng tải nhanh hơn thời gian bảo vệ sinh học.
- Sau khi được rời clinic vẫn cần tiến triển ngoài sân/hoạt động đặc hiệu, không lập tức thi đấu hết cường độ.

## 20.7. Đau gan gót và bàn chân

**[E]** CPG plantar fasciitis 2023 khuyến nghị stretching đặc hiệu cân gan chân và cơ bắp chân; có thể dùng resistance training và các hỗ trợ trong kế hoạch phối hợp. Night splint 1–3 tháng được đề cập cho người đau bước đầu buổi sáng thường xuyên. [C15 — Heel Pain CPG 2023, nội dung khuyến nghị được lập chỉ mục](https://doi.org/10.2519%2Fjospt.2023.0303). Chưa đọc toàn bộ guideline trong đợt này.

**[H]** Ghi vị trí đau, bước đầu buổi sáng, tải đứng/đi ở công việc, giày và mức tăng vận động. Phân biệt đau gót liên quan xương, thần kinh, đệm mỡ hoặc tổn thương khác trước khi gán plantar fasciitis. Không bắt mọi người bỏ orthotics hoặc chuyển barefoot. Chọn giày là phần quản lý dung nạp, không lời hứa sửa cấu trúc chân.

## 20.8. Bộ dữ liệu chung để tránh protocol “mù” [H]

```text
Tình trạng đã được đánh giá/chẩn đoán:
Phạm vi protocol áp dụng và loại trừ:
Giai đoạn hiện tại và lý do:
Bài, tải, ROM, tốc độ, sets/reps, lịch:
Ngưỡng triệu chứng theo kế hoạch cá nhân:
Đáp ứng sau tập/sáng hôm sau:
Tải công việc và môn thể thao:
Tiêu chí tiến triển / lùi mức / khám lại:
Người phụ trách và ngày review:
```

Nếu một trường quyết định an toàn còn thiếu, output hợp lệ là “cần đánh giá thêm”, không phải tự điền một protocol chung.


---

<!-- CHAPTER 21 -->

# 21. REHAB LƯNG, VAI, KHUỶU VÀ CHẨN ĐOÁN PHÂN BIỆT

Nghiên cứu 14–15/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Nguồn và mức độ đọc](references/24-ma-tran-nguon-va-kiem-chung.md).

Đọc [sàng lọc phần 19](references/19-sang-loc-va-dinh-huong-chan-doan.md) trước. **[E]** là bằng chứng/khuyến nghị trong đúng phạm vi nguồn; **[C]** là đồng thuận chuyên gia; **[H]** là cách tổ chức toolkit đề xuất. Các biến thể bài tập dưới đây là lựa chọn để thử sau đánh giá, không phải bằng chứng xác nhận nguyên nhân đau.

## 21.1. Lưng dưới: phân loại trước, không tự gán mọi đau cho disc hoặc core yếu

**[E]** NICE NG59 không khuyến nghị chụp thường quy ở tuyến không chuyên khoa; ở chuyên khoa, cân nhắc khi kết quả có thể thay đổi xử trí. Duy trì hoạt động và lựa chọn exercise theo khả năng, nhu cầu; manual therapy nếu dùng nên nằm trong gói có exercise. Nguồn này đã đối chiếu các khuyến nghị liên quan, chưa rà toàn bộ evidence reviews. [C06 — NICE NG59](https://www.nice.org.uk/guidance/NG59/chapter/recommendations).

**[E]** WHO 2023 dành cho **chronic primary low back pain**, thường kéo dài trên ba tháng và không do bệnh nền khác giải thích. Chăm sóc có thể phối hợp giáo dục, exercise, hỗ trợ tâm lý, một số trị liệu vật lý và thuốc do người có chuyên môn lựa chọn. Không có cơ sở từ hướng dẫn này để khẳng định exercise là phương pháp hiệu quả duy nhất, hoặc tất cả mọi người cần cùng một bộ bài core. Khuyến nghị không dùng thường quy đai hỗ trợ điều trị đau lưng không tương đương cấm belt trong thi đấu. [C16 — WHO, thông cáo hướng dẫn 2023](https://www.who.int/news/item/07-12-2023-who-releases-guidelines-on-chronic-low-back-pain).

### Hồ sơ cần phân biệt [H, dựa quy trình C06/C16 và phần 19]

| Kiểu trình bày | Cần làm rõ | Hệ quả với giáo án |
|---|---|---|
| Đau lưng khu trú, liên quan vận động | Khởi phát, tải mới, hoạt động tăng/giảm đau; khám khi cần | Có thể tìm hoạt động dung nạp được; chưa được kết luận mô tổn thương chỉ từ hướng gây đau |
| Đau lan chân, tê hoặc yếu | Phân bố cảm giác, sức cơ, tiến triển; khám thần kinh | Không gộp vào DOMS; thiếu hụt tăng dần cần đánh giá y tế |
| Sau ngã/chấn thương, có nguy cơ gãy | Cơ chế, sức khỏe xương, thuốc, khả năng chịu lực | Chưa thử deadlift để “test xem có ổn không” |
| Đau kéo dài kèm sợ vận động, ngủ kém, khó làm việc | Chức năng, niềm tin, tâm trạng, điều kiện công việc | Theo dõi nhiều đầu ra, không chỉ sửa tư thế |
| Dấu báo động thần kinh/toàn thân | Xem phần 19 | Nhánh y tế ưu tiên hơn mọi chương trình tập |

### Lộ trình xây lại khả năng vận động [H]

1. Chọn 2–3 việc người tập muốn lấy lại: ngồi làm việc, đi bộ, nhấc đồ, squat. Ghi thời lượng/tải hiện chịu được và phản ứng sau đó.
2. Tạm điều chỉnh yếu tố gây khó chịu: tải, ROM, số set, nhịp độ hoặc hỗ trợ. Đổi từng yếu tố để hiểu đáp ứng; không đồng thời thêm nhiều “corrective”.
3. Giữ các vận động khác dung nạp được. Một lựa chọn có thể là squat tới ghế, hip hinge nhẹ, row có tựa hoặc đi bộ; lựa chọn theo phản ứng cá nhân.
4. Khi buổi tập và hoạt động hôm sau ổn định, tăng một biến ở lần tiếp theo. Khi chức năng xấu đi, quay lại liều đã dung nạp và đánh giá lại nguyên nhân.
5. Đưa dần yêu cầu thực tế trở lại: tầm với, vật ở độ cao khác nhau, tải không đối xứng, thời gian làm việc. Không suy từ làm được bird dog sang đã sẵn sàng deadlift tối đa.

Không lấy đau bằng 0 trong một test làm tiêu chí duy nhất. Nhật ký cần có đau, chức năng, tải, sự tự tin và xu hướng qua nhiều lần tiếp xúc. Đau kéo dài/diễn biến khác dự kiến cần xem lại đánh giá, không mặc định do người tập thiếu kiên trì.

## 21.2. Vai: rotator cuff tendinopathy khác với rách cấp, mất vững hoặc đau từ cổ

**[E]** CPG 2025 bao gồm tendinopathy, có thể kèm vôi hóa hoặc rách bán phần; không dùng nguyên chương trình cho rách toàn phần hay sau mổ. Đánh giá dựa bệnh sử và khám; không chụp thường quy ngay để xác nhận tendinopathy. Nếu chưa cải thiện sau quản lý bảo tồn phù hợp, hướng dẫn nêu cân nhắc hình ảnh trong tối đa 12 tuần; chấn thương nghi tổn thương lớn cần xử trí sớm hơn. Active rehabilitation với motor control và/hoặc resistance training là lựa chọn ban đầu; chưa rõ tải cao hay một bài đặc hiệu luôn tốt hơn. Quay lại thể thao cần đánh giá khả năng chịu tải và chức năng. Đã đọc các phần được lập chỉ mục về khám, hình ảnh, exercise và return to sport; trang toàn văn trực tiếp bị chặn. [C17 — Rotator cuff CPG 2025, khuyến nghị 9–13, 24–25, 35–36](https://doi.org/10.2519/jospt.2025.13182).

### Các nhánh không được gộp [H]

| Tình huống | Điều toolkit cần thu thập/chuyển đánh giá |
|---|---|
| Đau tăng khi đưa tay hoặc đẩy/kéo | Vị trí, ROM chủ động/thụ động, sức mạnh, yếu tố tải và khám phân biệt |
| Chấn thương rồi yếu rõ hoặc mất khả năng nâng tay | Đánh giá tổn thương cấp; không chờ đủ một block rehab |
| Cảm giác trượt khớp, tiền sử trật | Cần đánh giá mất vững; không tự kéo giãn mạnh |
| Hạn chế nhiều hướng, kể cả khi được hỗ trợ | Cần xem các nguyên nhân hạn chế khớp; không mặc định thiếu scapular stability |
| Đau cổ kèm lan tay/tê/yếu | Sàng lọc thần kinh và cổ; không mặc định toàn bộ là rotator cuff |

### Cấu trúc một trial exercise [H]

- Chọn mục tiêu đo được: nâng đồ lên kệ, mặc áo, bench hoặc overhead press.
- Chọn một bài sức mạnh trong ROM dung nạp, ví dụ external rotation có kháng lực hoặc scaption; thêm bài đẩy/kéo phù hợp mục tiêu khi dung nạp được. Tên bài là ví dụ thiết kế, không phải phác đồ trích từ CPG.
- Ghi resistance, set, rep, ROM, effort, pain trong/sau tập và ngày hôm sau. Nếu không có các trường này, không thể nói bài “không hiệu quả”.
- Tiến từ nhiệm vụ dễ kiểm soát tới tốc độ, ROM và tải yêu cầu của hoạt động. Một biến thể dumbbell/landmine có thể hữu ích, nhưng không tự động tương đương competition bench hoặc overhead sport.
- Xem lại nếu đau/chức năng xấu dần hoặc không có tiến triển dù tuân thủ. Đổi chẩn đoán làm việc hoặc kế hoạch khi dữ liệu không phù hợp, thay vì chỉ tăng volume scapula.

## 21.3. Lateral elbow tendinopathy: tải cả trong gym lẫn công việc

**[E]** CPG 2022 khuyến nghị isometric, concentric và/hoặc eccentric cho wrist extensors ở giai đoạn bán cấp/mạn (grade B). Đo PRTEE/DASH và chức năng riêng của người bệnh; theo dõi ROM, pain-free grip và maximum grip. Tập vai/scapula là bổ sung khi phát hiện thiếu hụt, không mặc định cần cho mọi người. Tiến theo giai đoạn để trở lại việc đòi hỏi cao là khuyến nghị chuyên gia (E). Ergonomics cũng ở mức E; không nên quảng bá một bàn phím hoặc tư thế là chữa được bệnh. [C18 — CPG 2022, CPG2–3](https://www.orthopt.org/uploads/content_files/files/lucado_et_al_2022_lateral_elbow_pain_and_muscle_function_impairments.pdf).

**Chẩn đoán phân biệt:** đau ngoài khuỷu có thể cần phân biệt chèn ép thần kinh, radiculopathy cổ hoặc bệnh lý khớp; vị trí đau không đủ xác nhận LET. CPG có phần differential diagnosis và decision tree; toolkit không tự dùng một resisted test để kết luận. [C18 — CPG12–14 và CPG43].

### Quy trình vận hành [H]

1. Tính cả công việc dùng chuột, dụng cụ, mang vác, chơi vợt và bài kéo/curl; ghi hoạt động nào thực sự làm triệu chứng tăng.
2. Giảm hoặc chia nhỏ tiếp xúc gây đau, thử thay cách cầm/thiết bị nếu phù hợp. Straps có thể thay nhu cầu grip trong một số bài, nhưng không phải điều trị chung và không dùng để vượt qua đau chưa đánh giá.
3. Chọn resistance và ROM wrist extension dung nạp được. Không áp đặt eccentric-only; ghi effort và phản ứng như các bài sức mạnh khác.
4. Khi nhiệm vụ cơ bản ổn, tăng dần thời gian cầm nắm, tải, tốc độ và thao tác giống công việc/thể thao.
5. Đánh giá thành công bằng chức năng và grip ở cùng điều kiện đo; không chỉ bằng đau sau massage.

Đau mặt trong khuỷu, tê ngón, yếu bàn tay hoặc đau sau chấn thương cần nhánh đánh giá riêng. Chưa có trong đợt này một phác đồ đầy đủ cho medial elbow, distal biceps/triceps rupture hoặc sau mổ.

## 21.4. Hông bên và bẹn: tránh gọi tất cả là cơ căng hoặc impingement

**[C]** Doha phân loại groin pain thành các nhóm liên quan adductor, iliopsoas, inguinal, pubic; nhóm liên quan khớp hông; và nguyên nhân khác. Đây là hệ thuật ngữ dựa bệnh sử/khám, không phải thuật toán tự chẩn đoán hoặc chương trình rehab hoàn chỉnh. Đã đọc abstract ở kho học thuật, chưa đọc toàn bộ định nghĩa khám. [C21 — Doha agreement 2015](https://wrap.warwick.ac.uk/id/eprint/104765/).

**[E]** RCT gluteal tendinopathy 2018 so sánh education + exercise, một lần corticosteroid injection và wait-and-see. Education + exercise có kết quả global improvement tốt hơn hai nhóm còn lại ở 52 tuần; khác biệt đau so với injection không có ý nghĩa ở thời điểm đó. Không suy thành mọi đau hông đều do gluteal tendon hoặc mọi injection đều vô ích. Đợt này đọc phương pháp/kết quả qua phần lập chỉ mục; chưa trích đầy đủ liều tập trong phụ lục. [C22 — Mellor et al., BMJ 2018](https://www.bmj.com/content/361/bmj.k1662).

**[H] Dữ liệu để chọn nhánh:** vị trí trước/bên/sau hông; đau khi nằm nghiêng, đi bộ, lên cầu thang hay đổi hướng; khởi phát đột ngột hay tăng dần; đau lan từ lưng; tiền sử chấn thương; khả năng chịu lực. Không ép stretch hông sâu chỉ vì test ROM giảm. Lộ trình adductor trở lại chạy/đổi hướng cần nguồn riêng trước khi đưa thành protocol tự động.

## 21.5. Thoái hóa khớp và cổ: phạm vi hiện có

**[E]** NICE NG226 ưu tiên therapeutic exercise cá thể hóa, có thể gồm tăng sức mạnh tại chỗ và aerobic; giáo dục và quản lý cân nặng nếu phù hợp. Đau có thể tăng khi bắt đầu, nhưng tập đều hỗ trợ chức năng dài hạn. Điều này không có nghĩa bỏ qua khớp nóng đỏ, sưng mới hoặc đau cấp chưa đánh giá. [C20 — NICE NG226, 1.3.1–1.3.4](https://www.nice.org.uk/guidance/NG226/chapter/recommendations).

Đối với cổ, đợt nghiên cứu mới đủ nguồn để nhận diện cần khám khi có triệu chứng thần kinh; chưa đủ xây protocol cervical radiculopathy/myelopathy. [C19 — NHS neck pain](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/). Toolkit phải hiển thị **“chưa có protocol đã thẩm định cho nhánh này”**, thay vì tự chọn các bài giãn cổ từ thư viện.

## 21.6. Tiêu chí bàn giao vào engine [H]

Mỗi hồ sơ vùng cơ thể cần có: chẩn đoán đã xác nhận hoặc giả thuyết đang đánh giá; người đánh giá; hạn chế hiện tại; liều đã dung nạp; tiêu chí tăng tải; điều kiện cần khám lại; nhiệm vụ cần trở lại; phép đo và ngày review. Sau mổ cần lưu chỉ định người mổ, loại thủ thuật và hạn chế riêng. Không lấy số tuần của nghiên cứu trên người không mổ làm quyền tăng tải sau phẫu thuật.


---

<!-- CHAPTER 22 -->

# 22. VẬN ĐỘNG PHỤC VỤ SINH HOẠT, HỒI PHỤC VÀ LÃO HÓA

Nghiên cứu 14–15/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Nguồn](references/24-ma-tran-nguon-va-kiem-chung.md).

## 22.1. Sức khỏe cần nhiều hơn tổng squat–bench–deadlift

**[E]** WHO khuyến nghị người trưởng thành tích lũy 150–300 phút aerobic cường độ vừa hoặc 75–150 phút cường độ mạnh mỗi tuần, hoặc phối hợp tương đương; tập sức mạnh các nhóm cơ chính ít nhất hai ngày. Người lớn tuổi thêm vận động đa thành phần nhấn mạnh thăng bằng chức năng và sức mạnh ít nhất ba ngày để tăng năng lực chức năng và phòng té ngã. Có vận động tốt hơn không vận động; tăng theo khả năng và giảm thời gian ít vận động. Đây là mục tiêu sức khỏe cộng đồng, không phải liều rehab cho một chấn thương. [T06 — WHO Physical activity](https://www.who.int/news-room/fact-sheets/detail/physical-activity).

### Bản đồ mục tiêu thực tế [H]

| Nhu cầu | Năng lực cần phát triển | Cách theo dõi cụ thể |
|---|---|---|
| Lên cầu thang, đi xa | Aerobic, sức mạnh chân, chịu tải | Số tầng hoặc quãng đường, thời gian, mức gắng sức, triệu chứng |
| Đứng dậy, xuống sàn rồi đứng lên | Sức mạnh và ROM phù hợp, thăng bằng | Mức hỗ trợ cần dùng; chất lượng và sự tự tin |
| Mang đồ, bế con | Sức mạnh nâng/mang, grip, sức bền | Khối lượng, quãng đường, thời gian, phản ứng hôm sau |
| Với đồ trên cao | ROM vai và khả năng chịu tải ở tầm với | Độ cao, tải, số lần, triệu chứng |
| Đi địa hình không bằng phẳng | Thăng bằng, phản ứng bước, năng lực chân | Nhiệm vụ tăng dần có hỗ trợ phù hợp |
| Làm việc ngồi lâu | Khả năng đổi tư thế và duy trì hoạt động | Thời gian làm việc dung nạp, số lần đứng/đi, ảnh hưởng tới công việc |

Đây là phép theo dõi nội bộ, không phải các test chẩn đoán hoặc điểm cắt nguy cơ té ngã đã được xác thực. Với người có tiền sử té ngã, chóng mặt, suy yếu hoặc bệnh nền, chọn đánh giá chuyên môn trước khi thử nhiệm vụ khó.

## 22.2. Phối hợp cardio và tập tạ

**[E]** Meta-analysis 43 nghiên cứu không tìm thấy ảnh hưởng bất lợi đáng kể tổng thể lên hypertrophy và maximal strength khi phối hợp aerobic với cùng chương trình strength. Explosive strength có thể tăng kém hơn, rõ hơn khi cùng buổi; phân nhóm cách nhau ít nhất ba giờ không cho thấy cùng tín hiệu đó. Không suy ra ba giờ là ngưỡng bảo đảm hoặc VĐV elite không có đánh đổi. [T05 — Concurrent training meta-analysis 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8891239/).

**[H] Cách bố trí theo ưu tiên:**

- Sức khỏe chung: chọn cardio dễ duy trì; ghép sau tập tạ hoặc ngày khác theo lịch thực tế.
- Powerlifting: đặt buổi squat/deadlift quan trọng khi ít mệt; theo dõi ảnh hưởng của chạy, đạp xe và lao động chân trước đó. Nếu hiệu suất giảm lặp lại, thử đổi lịch/liều cardio trước khi kết luận “cardio làm mất cơ”.
- Power/sprint: nếu có thể, tách nội dung sức mạnh bùng nổ và endurance gây mệt; giữ chất lượng các lần thực hiện nhanh.
- Rehab chân: chọn phương thức cardio dựa hạn chế của tổn thương và đáp ứng, không mặc định đạp xe luôn an toàn cho mọi gối/hông.

Ghi **thời gian × mức gắng sức × phương thức** thay vì chỉ số buổi. Một buổi chạy interval không tương đương một buổi đi bộ cùng thời lượng.

## 22.3. Mobility có mục tiêu

**[H]** Xác định nhiệm vụ cần ROM nào trước khi kê bài mobility. Lưu ROM hiện tại, cảm giác giới hạn, mức hỗ trợ và kết quả test–retest. Cải thiện tức thời sau warm-up là dữ liệu về đáp ứng, không chứng minh nguyên nhân đau hoặc sửa được cấu trúc.

Nếu ROM hiện đủ cho nhiệm vụ và không gây khó chịu, không tự thêm 20 phút corrective. Nếu hạn chế rõ, chọn biện pháp rồi kiểm tra cả tác động tới nhiệm vụ và khả năng giữ kết quả lâu dài. Nếu có đau, chấn thương hoặc giới hạn sau mổ, chuyển sang nhánh đánh giá thay vì ép ROM.

Tài liệu Squat University hữu ích để tra kỹ thuật và ý tưởng thử; các giả thuyết như joint-by-joint cần đi kèm giới hạn tại [phần 25](references/25-doi-chieu-mau-thuan-va-khoang-trong.md).

## 22.4. Ngủ, ca làm việc và mệt

**[E]** CDC nêu người 18–60 tuổi cần ít nhất 7 giờ ngủ/ngày; 61–64 tuổi 7–9 giờ và từ 65 tuổi 7–8 giờ. Chất lượng và tính đều đặn cũng quan trọng. Đây không phải công thức “thiếu một giờ ngủ giảm chính xác bao nhiêu % tạ”. [T07 — CDC About Sleep](https://www.cdc.gov/sleep/about/).

**[H]** Ghi tổng ngủ 24 giờ, chất lượng chủ quan, ca làm, mức buồn ngủ, khả năng tập trung và kết quả warm-up. Một đêm kém nhưng warm-up bình thường có thể chỉ cần bỏ mục tiêu PR và theo dõi; mất ngủ kéo dài hoặc giảm chức năng cần xử lý nguyên nhân và cân nhắc đánh giá y tế. Nếu buồn ngủ đến mức không bảo đảm thao tác an toàn, chọn nghỉ hoặc hoạt động đơn giản phù hợp thay cho free-weight nặng.

Không kê lịch buổi sáng cố định cho người vừa hết ca đêm. Toolkit cần biết **cửa sổ thời gian sau giấc ngủ chính**, không chỉ thứ trong tuần. Xem bảng quyết định phần 23.

## 22.5. Một tuần minh họa cho người khỏe mạnh bận rộn [H]

Đây là thiết kế minh họa, không phải chương trình thử nghiệm trong nguồn. Giả định người đã dung nạp vận động, không có triệu chứng cần khám; có ba cửa sổ tập tạ 35–45 phút.

| Ngày | Strength/năng lực | Aerobic vừa, tích lũy |
|---|---|---|
| Thứ hai | Squat pattern, push, pull | Đi bộ nhanh 20 phút |
| Thứ ba | Không bắt buộc buổi tạ | Đi bộ nhanh 30 phút |
| Thứ tư | Hinge, push/pull khác, carry | Đi bộ nhanh 20 phút |
| Thứ năm | Bài thăng bằng phù hợp nếu cần | Đi bộ nhanh 30 phút |
| Thứ sáu | Chân đơn, push, pull; kỹ năng còn thiếu | Đi bộ nhanh 20 phút |
| Thứ bảy | Hoạt động lựa chọn | Đi bộ nhanh 30 phút |
| Chủ nhật | Review, hồi phục theo nhu cầu | Tùy khả năng |

Tổng ví dụ 150 phút aerobic vừa; thời gian đi lại rất nhẹ không tự động tính tương đương. Người mới có thể bắt đầu ít hơn rồi tăng dần. Set/rep/effort chọn theo phần 17, không điền một liều giống nhau cho mọi người. Người cao tuổi cần bố trí rõ ít nhất ba lần vận động đa thành phần/thăng bằng theo khả năng; bảng này không tự hoàn thành điều đó chỉ vì có ba buổi tạ.

## 22.6. Nhánh chưa được phép tự động hóa

Chưa xây đầy đủ bài toán frailty, osteoporosis/gãy xương, tim mạch, tăng huyết áp chưa kiểm soát, thai kỳ/hậu sản, bệnh thần kinh hoặc giới hạn sau phẫu thuật. Nguồn healthy-adult strength không đủ thay hướng dẫn cho từng nhóm. Đợt này đặt cấu trúc và đường chuyển đánh giá; xem danh mục research ưu tiên ở phần 25.

## 22.7. Warm-up, stretching và tempo: bổ sung điều kiện

**[E] T13:** review stretching ở người khỏe hoạt động ghi tác động hiệu suất phụ thuộc liều/bối cảnh; phân nhóm static stretch ≥60 giây mỗi nhóm cơ giảm hiệu suất trung bình nhiều hơn <60 giây. Đây không phải ranh giới “29 giây an toàn tuyệt đối, 46 giây gây hại”, cũng không là ngưỡng chấn thương. Đã đọc abstract và phần liều được lập chỉ mục. [Behm et al., 2016](https://pubmed.ncbi.nlm.nih.gov/26642915/).

**[H] Tiếp nhận U01/U08:** dùng warm-up để chuẩn bị nhiệm vụ: vận động nhẹ nếu cần, ROM liên quan, rồi ramp-up sets bài chính. Không bắt mọi buổi có foam rolling/stretch/activation đủ ba bước hoặc xong trong đúng 5–10 phút. Ghi tổng thời gian stretch trên nhóm cơ, cường độ, bài tiếp sau và tác động tới nhiệm vụ.

Tempo chậm có thể là cách thực hành kiểm soát và chuẩn hóa ROM; không suy time-under-tension càng lâu càng tăng cơ. Nếu đổi từ rep bình thường sang eccentric ba giây, đánh giá lại tải/effort và baseline. Khi mục tiêu power, tốc độ/ý định phát lực là yêu cầu khác; không ép mọi concentric chậm. Chi tiết tiếp nhận và các phát biểu chưa đủ chứng cứ ở [phần 28](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md).


---

<!-- CHAPTER 23 -->

# 23. BỘ QUY TẮC ĐIỀU CHỈNH VÀ MẪU ĐẦU RA

Biên soạn 15/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Nguồn](references/24-ma-tran-nguon-va-kiem-chung.md).

## 23.1. Quy ước: rõ ràng không có nghĩa giả vờ chính xác

Các bảng dưới đây là **[H] — đặc tả vận hành đề xuất**, chưa phải thuật toán được kiểm định trên người dùng. Nền tảng lấy từ [lập chương trình](references/17-nen-tang-lap-chuong-trinh-va-dieu-chinh.md), [dinh dưỡng](references/18-dinh-duong-va-dieu-chinh-theo-muc-tieu.md), [sàng lọc](references/19-sang-loc-va-dinh-huong-chan-doan.md) và rehab phần 20–21. Các mốc thời gian, số lần review và phần trăm điều chỉnh trong ví dụ phải được lưu là cấu hình, không gán thành ngưỡng y khoa.

Một rule hoàn chỉnh phải có: **ID → đối tượng → điều kiện → ưu tiên → hành động → giới hạn → dữ liệu kiểm tra lại → thời điểm → điều kiện quay lại → căn cứ**. Không dùng một “readiness score” tổng để che mất dấu hiệu cần khám.

## 23.2. Thứ tự xử lý khi nhiều điều kiện đồng thời xảy ra

1. **Sàng lọc y tế:** dấu hiệu cấp cứu hoặc triệu chứng mới cần đánh giá.
2. **Giới hạn đã được chỉ định:** sau mổ, tổn thương đã chẩn đoán, điều kiện tăng tải của người điều trị.
3. **Khả năng thực hiện an toàn trong ngày:** tỉnh táo, thiết bị, kỹ năng, triệu chứng và warm-up.
4. **Nguồn lực thực tế:** thời gian, số ngày, địa điểm, công việc.
5. **Mục tiêu và tiến triển:** strength/hypertrophy/duy trì, dinh dưỡng và ưu tiên phụ.

Ví dụ: thiếu thời gian **và** có dấu thần kinh mới → xử lý nhánh sức khỏe trước, không xuất “buổi nhanh 20 phút”. Có rehab plan **và** thiếu máy → chỉ chọn bài thay đáp ứng giới hạn rehab; không tự thay bằng bài cùng nhóm cơ.

## 23.3. Dữ liệu tối thiểu và xử lý khi thiếu

| Dữ liệu | Nếu thiếu |
|---|---|
| Triệu chứng mới, hạn chế y tế/sau mổ | Hỏi trước khi tạo nội dung phụ thuộc; không coi để trống là “không có” |
| Thời gian hôm nay và số ngày khả dụng | Xuất lịch tạm với giả định hiển thị; hỏi để chọn phiên bản |
| Kinh nghiệm, bài quen, tải gần đây | Bắt đầu bằng đánh giá kỹ thuật/tải dưới tối đa; không đoán 1RM |
| Effort/RIR | Hướng dẫn cách ghi; dùng khoảng rep và điều kiện dừng kỹ thuật, tránh chính xác giả |
| Cân nặng/mục tiêu dinh dưỡng | Có thể hướng dẫn cấu trúc bữa; chưa tính gram/kg hoặc calorie cá thể |
| Diễn biến triệu chứng sau buổi trước | Không tự động tăng tải rehab; thu thập lại phản ứng |

## 23.4. Rule theo công việc và lịch tập [H]

| ID / điều kiện | Hành động | Giới hạn | Review và trở lại |
|---|---|---|---|
| W01: còn ≥ thời gian của lịch cơ sở | Giữ buổi đã lên, áp dụng kiểm tra sức khỏe/effort | Không tăng thêm vì cảm thấy có thời gian nếu vượt kế hoạch | Review cuối buổi và tuần |
| W02: chỉ còn khoảng 30 phút | Chọn phiên bản rút gọn đã chuẩn bị: warm-up riêng bài, bài ưu tiên, phần bổ trợ quan trọng nhất | Bỏ phần ưu tiên thấp; không ép tất cả set bằng cách cắt rest của lift nặng | Buổi sau dùng lịch bình thường nếu thời gian đủ; không trả “nợ set” |
| W03: chỉ còn khoảng 15 phút | Phiên bản tối thiểu đã định: một nhiệm vụ sức mạnh hoặc rehab ưu tiên có thể thực hiện trọn vẹn | Nếu không đủ warm-up/thực hiện an toàn thì chọn hoạt động đơn giản hoặc bỏ buổi | Ghi việc đã làm, tiếp tục thứ tự buổi |
| W04: bỏ lỡ một buổi | Dời buổi theo thứ tự A→B→C nếu hồi phục và lịch cho phép; nếu không thì bỏ phần ưu tiên thấp | Không gộp hai buổi đầy đủ vào một ngày | Review cuối tuần; trở lại lịch khi cửa sổ thời gian ổn |
| W05: từ 4 xuống 2 ngày trong vài tuần | Tạo lại hai buổi toàn thân, giữ mục tiêu chính và giảm tổng volume thực tế | Không giữ nguyên mọi set của 4 ngày bằng cách nhồi vào 2 ngày | Review sau tuần đầu; thêm lại volume từng bước khi lịch mở |
| W06: công tác/thiếu thiết bị | Dùng thư viện thay thế đã kiểm tra; có thể chuyển mục tiêu ngắn hạn sang duy trì | Không gọi bodyweight squat là thay thế hoàn toàn kỹ năng competition squat | Buổi trở lại dùng tải theo effort thực tế; không mặc định giữ PR cũ |
| W07: ca đêm hoặc lịch đổi liên tục | Dùng chu kỳ buổi A/B/C, đặt sau giấc ngủ chính và theo khả năng | Không buộc hoàn thành vào đúng thứ; xem rule mệt bên dưới | Review mỗi chu kỳ hoặc mỗi tuần |
| W08: công việc chân/tay tăng rõ | Ghi loại việc và vùng chịu tải; giảm phần trùng gây mệt nếu hiệu suất/triệu chứng xấu | Lao động không được đổi cơ học thành số hypertrophy set tương đương | Đối chiếu các ngày làm việc và warm-up; phục hồi từng phần khi đáp ứng ổn |

Các mốc 15/30 phút là các phiên bản sản phẩm, không phải liều tối thiểu có tác dụng cho mọi người. Căn cứ nguyên tắc tiết kiệm thời gian và duy trì: [T02](https://pmc.ncbi.nlm.nih.gov/articles/PMC8449772/).

## 23.5. Rule theo effort, hiệu suất và hồi phục [H]

| ID / điều kiện | Hành động | Giới hạn | Review / quay lại |
|---|---|---|---|
| F01: ngủ kém một đêm, tỉnh táo, warm-up như thường | Tập theo effort cap; bỏ yêu cầu lập PR nếu độ sẵn sàng không chắc | Không có công thức cố định giờ ngủ→% tạ | Đánh giá từng bài; hôm sau theo tình trạng mới |
| F02: buồn ngủ, mất tập trung hoặc thao tác không chắc | Bỏ nội dung đòi hỏi kiểm soát tải cao; nghỉ hoặc chọn hoạt động phù hợp | Không dùng stimulant để ép hoàn thành chương trình | Chỉ trở lại khi tỉnh táo và kiểm soát vận động phù hợp |
| F03: warm-up nặng bất thường nhưng không có triệu chứng mới | Giảm tải từng nấc nhỏ để về effort mục tiêu; nếu vẫn không đạt thì giảm set/bỏ bài ưu tiên thấp | Không cố giữ %1RM khi effort đã vượt cap | Ghi tải, rep, RIR thực tế; xem có lặp lại không |
| F04: đạt đầu trên rep range ở mọi set, effort/ROM đúng trong hai lần liên tiếp | Tăng nấc tải nhỏ nhất hợp lý lần tiếp theo | Theo ví dụ double progression phần 17; hai lần là cấu hình heuristic, không đồng thời tăng mọi biến | Nếu rep rơi dưới đáy khoảng hoặc effort vượt cap, giữ/giảm lại |
| F05: không đạt rep/effort mục tiêu một lần | Giữ hoặc điều chỉnh buổi theo F03; kiểm tra bối cảnh | Chưa gọi là plateau hay overtraining | Review lần tiếp xúc tiếp theo |
| F06: giảm hiệu suất lặp lại qua ≥2 lần ở điều kiện tương tự | Kiểm tra adherence, ăn/ngủ, đau, bệnh, tải công việc, volume và độ phù hợp bài | Hai lần là trigger review của toolkit, không chẩn đoán overtraining | Chỉ tăng volume nếu thực sự có lý do; có thể giảm tải/volume tạm và kiểm tra lại |
| F07: bước vào tuần nhẹ đã quyết định | Giảm volume/effort theo lý do và lịch; ghi rõ bài nào giữ để luyện kỹ năng | Không bắt buộc deload mỗi số tuần cố định cho mọi người | Kết thúc theo phục hồi chức năng/hiệu suất, không chỉ hết ngày |

Ví dụ cấu hình F03: giảm khoảng 5% rồi đánh giá lại set, thay vì đặt một con số tuyệt đối theo giấc ngủ. Đây là ví dụ huấn luyện cần kiểm thử; chưa có nghiên cứu xác nhận engine này. Nguồn nền và giới hạn autoregulation: [T03](https://pmc.ncbi.nlm.nih.gov/articles/PMC8762534/).

## 23.6. Rule triệu chứng và rehab

| ID / điều kiện | Hành động | Review / điều kiện quay lại |
|---|---|---|
| S01: có dấu báo động trong phần 19 | Ngừng nhánh tập liên quan, hướng tới mức đánh giá y tế tương ứng | Theo kết quả đánh giá; không cho engine tự clearance |
| S02: đau mới sau chấn thương, sưng/giảm chức năng đáng kể hoặc chưa rõ nguyên nhân | Dừng bài gây triệu chứng, chuyển sàng lọc; chưa xuất protocol chẩn đoán cụ thể | Khi đã đánh giá và có giới hạn phù hợp |
| S03: có chẩn đoán và rehab plan | Dùng pain/response rule riêng của plan, gồm phản ứng sau buổi và hôm sau | Tăng tải chỉ khi đạt tiêu chí của giai đoạn |
| S04: đau trong ngưỡng plan nhưng hôm sau chức năng giảm hoặc sưng tăng | Không tăng; giảm về liều dung nạp hoặc liên hệ người điều trị tùy mức độ | Review trước lần tải tiếp theo, khám lại nếu diễn biến không phù hợp |
| S05: đau thấp nhưng sức mạnh/khả năng hoạt động chưa đạt | Tiếp tục xây năng lực, chưa cho phép quay lại toàn bộ | Đạt tiêu chí nhiệm vụ và readiness; không dựa đau đơn độc |
| S06: vận động không liên quan vẫn dung nạp | Có thể giữ để duy trì thể lực trong giới hạn plan | Theo dõi tác động gián tiếp lên vùng đang rehab |
| S07: sau mổ, thiếu thông tin thủ thuật/hạn chế | Yêu cầu thông tin trước nội dung phụ thuộc | Không suy protocol từ tên vùng đau |
| S08: sốt/bệnh cấp hoặc triệu chứng toàn thân mới | Hoãn phần tập gắng sức, đánh giá tình trạng; dấu nặng theo phần 19 | Không đặt thời hạn trở lại chung khi chưa rõ bệnh |

**Không dùng chung “đau ≤3/10” hoặc “≤5/10” cho mọi tổn thương.** Ví dụ pain-monitoring patellar tendon trong phần 20 phải giữ điều kiện ngày hôm sau và diễn biến tuần; không chuyển sang nghi gãy xương, tổn thương thần kinh hoặc hậu phẫu.

## 23.7. Rule dinh dưỡng [H]

| ID / điều kiện | Hành động | Giới hạn và review |
|---|---|---|
| N01: cân nhảy lên/xuống một ngày | Giữ kế hoạch, xem nước, muối, carbohydrate, chu kỳ kinh, tiêu hóa và điều kiện cân | Không suy ngay thay đổi mỡ; dùng xu hướng nhiều ngày |
| N02: có 2–3 tuần dữ liệu tương đối nhất quán, xu hướng lệch mục tiêu | Kiểm tra adherence và hoạt động; sau đó mới chỉnh năng lượng nhỏ nếu cần | Ví dụ 100–200 kcal/ngày là nấc vận hành; review lại thay vì chỉnh hằng ngày |
| N03: giảm ngày tập | Xem thay đổi tổng hoạt động và xu hướng cân, giữ protein phù hợp | Không trừ máy móc calorie một buổi từ đồng hồ |
| N04: bận không nấu được | Dùng bữa thay theo protein, năng lượng và khẩu phần có thể ước tính | Ghi độ không chắc của món ngoài; không báo macro chính xác giả |
| N05: giảm cân kèm hiệu suất/sức khỏe xấu kéo dài hoặc dấu thiếu năng lượng | Dừng mục tiêu ép deficit để đánh giá lại; cân nhắc chuyên gia dinh dưỡng/y tế | Không chẩn đoán REDs bằng một ngưỡng calorie hoặc một triệu chứng |
| N06: cân không đổi nhưng vòng eo/chức năng thay đổi theo hướng mong muốn | Xem lại mục tiêu composition và sai số đo trước khi giảm calorie thêm | Không đồng nhất cân không đổi với thất bại |

Công thức và điều kiện áp dụng ở phần 18. Các rule này không thay chế độ dinh dưỡng điều trị bệnh hoặc rối loạn ăn uống.

## 23.8. Ví dụ xử lý đồng thời

**A — Powerlifter thường tập 4 ngày, tuần này chỉ có 2 × 45 phút, không đau:** W05 tạo hai buổi mới. Một buổi ưu tiên squat + bench, buổi kia deadlift + bench hoặc lift ưu tiên thực tế; accessory chọn theo thời gian còn lại. Set/effort từ lịch sử dung nạp, không gộp đủ volume bốn ngày. Mục tiêu tuần có thể là duy trì kỹ năng và năng lực. Không gọi đây là chương trình peaking nếu chưa biết lịch thi đấu.

**B — Hypertrophy, ngủ ít và warm-up vẫn bình thường:** F01 giữ effort cap, theo dõi; không tự cắt 30% mọi bài. Nếu set đầu vượt cap thì F03 điều chỉnh. Chưa tăng volume chỉ vì buổi ngắn.

**C — Achilles đã có plan, chỉ còn 20 phút:** kiểm tra S03/S04 trước W03. Nếu chưa đạt phản ứng hôm sau thì không tăng calf loading; ưu tiên liều rehab được phép. Không tự đổi sang nhảy dây để “tiết kiệm thời gian”.

**D — Cutting, cân tăng sau bữa ngoài, bỏ một buổi do công việc:** N01 giữ kế hoạch và theo dõi; W04 sắp lại buổi. Không đồng thời cắt mạnh thức ăn và thêm cardio để bù một ngày.

**E — Đau vai mới sau ngã, còn ít thời gian:** S02 ưu tiên. Không chọn MuscleWiki rồi xuất buổi vai ngắn trước khi sàng lọc.

## 23.9. Mẫu đầu ra bắt buộc cho một giáo án

```yaml
status: draft_requires_individual_inputs
goal:
  primary: null
  secondary: []
  review_date: null
assumptions: []
health:
  screening_completed: false
  confirmed_diagnoses: []
  clinician_restrictions: []
availability:
  sessions_per_cycle: null
  minutes_per_session: []
  equipment: []
program:
  base_sessions: []
  short_versions: []
  minimum_versions: []
exercise_record_fields:
  - exercise_and_source_url
  - purpose
  - sets_reps_load_effort_rest_rom
  - allowed_substitutions_and_tradeoffs
  - progression_and_regression
  - symptom_response_rule_if_applicable
nutrition:
  energy_estimate_and_uncertainty: null
  protein_fat_carbohydrate_and_units: null
  review_rule: null
adaptation:
  applicable_rule_ids: []
  actions_taken_and_reason: []
follow_up:
  during_session: []
  next_day: []
  weekly: []
provenance:
  evidence_sources: []
  expert_consensus: []
  toolkit_heuristics: []
```

Đây là schema để thiết kế, không phải file cấu hình đã được một ứng dụng triển khai. Một đầu ra tốt phải giải thích **vì sao đổi, đổi phần nào, mất/giữ lợi ích gì và khi nào quay lại**. Đánh giá cuối tuần dùng cả adherence, hiệu suất, triệu chứng, chức năng và mục tiêu dinh dưỡng; không chỉ số buổi hoàn thành.

## 23.10. Mẫu review kỹ thuật bổ sung từ U01 [H]

1. **Bối cảnh:** bài/biến thể, mục tiêu, tải, reps, effort, triệu chứng và thiết bị. Video cần thấy các phần liên quan và nhiều rep; nếu góc quay che thì ghi chưa quan sát được.
2. **Quan sát:** mô tả điều nhìn thấy, như “hông lên trước ngực ở các rep cuối”, không chuyển ngay thành “glutes không hoạt động”.
3. **Giả thuyết:** chỉ nêu những yếu tố có cơ sở từ dữ liệu; không bắt đủ hai hay bốn nguyên nhân khi chưa biết. Có thể là tải/mệt, setup, kỹ năng hoặc giới hạn khác.
4. **Một thay đổi để thử:** giảm tải hoặc thay một yếu tố setup/cue; ưu tiên một đến hai cue ngắn. Ghi phần đánh đổi nếu đổi bài/ROM.
5. **Review:** cùng góc quay, ROM và mức effort phù hợp; xem nhiệm vụ có cải thiện, triệu chứng và phản ứng sau đó. Không chẩn đoán tổn thương từ test–retest.
6. **Kế hoạch tiếp:** giữ nếu hữu ích, thử cách khác hoặc chuyển đánh giá khi cần; thời hạn 2–4 tuần trong U01 chỉ là mẫu, không phải lịch khỏi bệnh.

Phương án chọn/thay bài: [phần 26](references/26-chon-bai-tap-va-bien-the-theo-muc-tieu.md). Khi cần cá nhân hóa theo chu kỳ, dùng M01–M05 tại [phần 27](references/27-ca-nhan-hoa-nam-nu-va-chu-ky-kinh-nguyet.md) dưới thứ tự ưu tiên sức khỏe ở 23.2; không ghi đè S01–S08 bằng dự đoán pha chu kỳ.


---

<!-- CHAPTER 24 -->

# 24. MA TRẬN NGUỒN, PHẠM VI ĐỌC VÀ KIỂM CHỨNG

Nghiên cứu 14–15/09/2026. [Trang tài nguyên](references/16-tong-hop-tai-nguyen.md).

## 24.1. Phương pháp và giới hạn

Đợt này tìm theo khoảng trống của toolkit: resistance training, hypertrophy/powerlifting, autoregulation, lịch bận, dinh dưỡng, hoạt động sức khỏe, chẩn đoán phân biệt, rehab và return to sport. Dùng Kimi Bridge để mở/đọc các trang công khai trong trình duyệt; bổ sung công cụ tìm kiếm để tìm nguồn gốc và đối chiếu khi trang chặn truy cập. PDF công khai được trích văn bản; trang tóm tắt khuyến nghị Achilles, hamstring và elbow được xem hình để tránh đọc lẫn hai cột.

Ưu tiên guideline, consensus, systematic review, nghiên cứu gốc và cơ quan chuyên môn. Nguồn tiếng Việt được đọc để đối chiếu thuật ngữ, hướng dẫn cho người bệnh và dinh dưỡng địa phương; không tự coi uy tín tên bệnh viện là bảo đảm cho từng mệnh đề. Đây là **nghiên cứu có cấu trúc theo chủ đề**, không phải systematic review đăng ký trước và không thể khẳng định đã đọc hết mọi nguồn Anh–Việt hoặc mọi tài liệu tham khảo trong từng bài.

### Mã trạng thái

- **F:** truy cập toàn văn, đọc các phần liên quan được ghi trong bảng. Không có nghĩa từng phụ lục và mọi bài được trích dẫn đều đã đọc.
- **P:** chỉ đọc được một phần/khuyến nghị được lập chỉ mục; giữ giới hạn, không suy liều còn thiếu.
- **A:** abstract/metadata; dùng để định hướng, chưa đủ nhập toàn bộ protocol.
- **M:** mới xác nhận nguồn/catalog; chưa có dữ liệu để sử dụng tính toán.
- **X:** truy cập không thành công hoặc không dùng làm căn cứ vận hành.

**F/P/A là mức truy cập, không phải chất lượng bằng chứng.** [E]/[C]/[H] trong các phần 17–23 lần lượt phân biệt bằng chứng/khuyến nghị, đồng thuận chuyên gia và quy tắc do toolkit đề xuất. Grade A–F trong CPG là hệ riêng của CPG, không được đánh đồng với các nhãn truy cập ở đây.

## 24.2. Lập chương trình và sức khỏe

| ID | Nguồn / năm / ngôn ngữ | Loại, trạng thái và phần đã đọc | Ứng dụng, giới hạn |
|---|---|---|---|
| T01 | [ACSM: Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults, 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823/) · EN | Overview of reviews; **F**: abstract, methods, results, bảng 4/6, discussion/limitations | Nền strength/hypertrophy; 137 reviews, phần lớn người ít kinh nghiệm. Không ngoại suy nguyên sang rehab/elite/frailty |
| T02 | [No Time to Lift? Designing Time-Efficient Training Programs for Strength and Hypertrophy, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8449772/) · EN | Narrative review; **F**: phần thực hành, superset, maintenance | Giảm thời gian và duy trì; liều thấp không phải bảo đảm cho mọi tuổi/trình độ |
| T03 | [The Effects of Load and Volume Autoregulation on Muscular Strength and Hypertrophy, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8762534/) · EN | Systematic review/meta-analysis; **F**: methods, kết quả và kết luận | RPE/velocity; không chứng minh autoregulation luôn hơn fixed loading |
| T04 | [Tapering and Peaking Maximal Strength for Powerlifting Performance, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7552788/) · EN | Review; **F**: bảng nghiên cứu, taper/cessation, kết luận | Taper powerlifting; mẫu nhỏ, khác đối tượng, chưa đủ quyết định attempts/cắt cân |
| T05 | [Compatibility of Concurrent Aerobic and Strength Training, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8891239/) · EN | Updated systematic review/meta-analysis; **F**: PICO, 43 studies, results, moderators, discussion | Cardio + strength; explosive strength có đánh đổi, ba giờ không phải ngưỡng chắc chắn |
| T06 | [WHO Physical activity](https://www.who.int/news-room/fact-sheets/detail/physical-activity) · EN | Khuyến nghị sức khỏe cộng đồng; **F**: adult/older adult recommendations | Aerobic, strength, balance, sedentary time; không phải protocol bệnh riêng |
| T07 | [CDC About Sleep, 2024](https://www.cdc.gov/sleep/about/) · EN | Cơ quan y tế; **F**: thời lượng theo tuổi và chất lượng ngủ | Đầu vào hồi phục; không quy đổi trực tiếp giờ ngủ thành % tải |

## 24.3. Dinh dưỡng

| ID | Nguồn | Loại/trạng thái, nội dung dùng | Giới hạn |
|---|---|---|---|
| N01 | [Mifflin et al., A new predictive equation for resting energy expenditure in healthy individuals, 1990](https://pubmed.ncbi.nlm.nih.gov/2305711/) · EN | Nghiên cứu gốc; **A**: phương trình trong abstract | Ước lượng REE, không phải TDEE đo được hoặc calorie chính xác |
| N02 | [ISSN position stand: diets and body composition, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5470183/) · EN | Position stand; **F**: cân bằng năng lượng, các chế độ, đo composition và giới hạn | Adherence, deficit/surplus; phương pháp khác nhau có thể phù hợp khác nhau |
| N03 | [Nutrition Recommendations for Bodybuilders in the Off-Season, 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6680710/) · EN | Narrative review; **F**: năng lượng, macros, timing, bảng kết luận | Surplus/gain rate là khoảng đề xuất theo đối tượng; không bắt buộc cho người advanced |
| N04 | [Nutritional Recommendations for Physique Athletes, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7052702/) · EN | Review; **F**: abstract và các phần deficit/contest/recovery liên quan | Bối cảnh thi thể hình không đồng nhất giảm cân sức khỏe; chưa xây peak-week protocol |
| N05 | [ISSN position stand: protein and exercise, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5477153/) · EN | Position stand; **F**: khuyến nghị, tổng protein, phân bố và deficit | Giữ đơn vị theo cân nặng hay FFM; người bệnh cần nhánh riêng |
| N06 | [NATA Position Statement: Fluid Replacement for the Physically Active, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5634236/) · EN | Position statement; **F**: cá thể hóa nước, mồ hôi, nguy cơ uống quá mức | Không kê một số lít cố định cho mọi người |
| N07 | [ISSN position stand: safety and efficacy of creatine supplementation, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5469049/) · EN | Position stand; **F**: dosing và phạm vi an toàn liên quan | 3–5 g/day maintenance; không coi supplement bắt buộc hoặc ngoại suy mọi bệnh nền |
| N08 | [IOC consensus statement on REDs, 2023](https://bjsm.bmj.com/content/57/17/1073) · EN | Consensus; **P**: abstract/khuyến nghị lập chỉ mục về đánh giá đa yếu tố | Trang trực tiếp bị chặn; **chưa triển khai IOC REDs CAT2**, không dùng ngưỡng EA đơn độc để chẩn đoán |
| N09 | [FAO catalog: Vietnamese Food Composition Table, 2007](https://www.fao.org/food-composition/tables-and-databases/detail/%28viet-nam--2007%29-vietnamese-food-composition-table/en) · EN, tài nguyên VN | Catalog; **M** | Chưa có bảng thành phần đã nhập/kiểm chứng; cần xác minh ấn bản, đơn vị, edible portion, sống/chín |
| N10 | [USDA FoodData Central documentation](https://fdc.nal.usda.gov/data-documentation.html) · EN | Tài liệu dữ liệu; **F**: tổng quan loại dữ liệu, FAQ/API liên quan | Thiết kế schema; chưa nhập dataset món Việt; missing không được biến thành zero |

## 24.4. Chấn thương, chẩn đoán phân biệt và rehab

| ID | Nguồn | Loại / mức đọc | Phạm vi phải giữ |
|---|---|---|---|
| C01 | [NHS Sprains and strains](https://www.nhs.uk/conditions/sprains-and-strains/) · EN | Giáo dục người bệnh; **F** | Sơ cứu, vận động trở lại, khi nào cần khám; không thay phân độ tổn thương |
| C02 | [NHS Back pain](https://www.nhs.uk/conditions/back-pain/) · EN | Giáo dục người bệnh; **F**: tự chăm sóc và dấu cần trợ giúp | Dấu thần kinh/cấp cứu; không dùng để xác định mô gây đau |
| C03 | [NHS Septic arthritis](https://www.nhs.uk/conditions/septic-arthritis/) · EN | Giáo dục người bệnh; **F** | Khớp đau/sưng cấp cần đánh giá; không chờ đủ mọi triệu chứng |
| C04 | [CDC/NIOSH Signs and Symptoms of Rhabdomyolysis, 2025](https://www.cdc.gov/niosh/rhabdo/signs-symptoms/index.html) · EN | Cơ quan y tế; **F** | Đau cơ bất thường, yếu, nước tiểu sẫm; cần xét nghiệm/đánh giá, không tự loại trừ |
| C05 | [Hamstring Strain Injury Rehabilitation, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8876884/) · EN | Clinical review; **F**: khám, differential, loading, running/RTS | Strain khác avulsion/proximal tendinopathy/đau lan; không đặt lịch sprint cố định |
| C06 | [NICE NG59: Low back pain and sciatica in over 16s](https://www.nice.org.uk/guidance/NG59/chapter/recommendations) · EN | Guideline; **P**: khuyến nghị đánh giá, imaging, activity/exercise/manual therapy | Trang trực tiếp hạn chế; không tuyên bố đã đọc mọi evidence review |
| C07 | [Hamstring Strain Injury in Athletes CPG, 2022](https://www.orthopt.org/uploads/content_files/files/Hamstring_Strain_Injury_in_Athletes_2022.pdf) · EN | CPG, PDF 44 trang; **F**: summary, assessment, prevention/rehab liên quan | Phân biệt grade bằng chứng; Nordic prevention không thay toàn bộ rehab |
| C08 | [Achilles Pain, Stiffness, and Muscle Power Deficits: Midportion Achilles Tendinopathy Revision, 2024](https://www.orthopt.org/uploads/content_files/files/Achilles_Pain_revision_2024.pdf) · EN | CPG, PDF 32 trang; **F**: summary, scope/methods, loading và adjuncts | **Midportion**; loading grade A, tần suất ≥3 lần/tuần grade E; không gán cùng mức chắc chắn |
| C09 | [Current Clinical Concepts: Conservative Management of Achilles Tendinopathy, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7249277/) · EN | Clinical review; **F**: phân loại, loading, bảng progression | Insertional cần lưu ý compression/ROM; không cho heel drop sâu tự động |
| C10 | [Clinical Management of Patellar Tendinopathy, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9528703/) · EN | Clinical review; **F**: differential, pain monitoring, bảng phase/loading | Ngưỡng đau cần giữ phản ứng hôm sau/xu hướng tuần; mốc tuần là mẫu |
| C11 | [Best practice guide for patellofemoral pain, 2024](https://pubmed.ncbi.nlm.nih.gov/39401870/) · EN | Best practice synthesis; **A/P**: abstract và phần truy cập được | Education + knee exercise ± hip, bổ trợ cá thể; PDF repository truy cập không ổn định, chưa trích protocol chi tiết |
| C12 | [Exercise-based rehabilitation reduces reinjury following acute lateral ankle sprain, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC8824326/) · EN | Systematic review/meta-analysis; **F**: 14 RCT, results/sensitivity, limitations | Tín hiệu giảm tái chấn thương, độ chắc thay đổi qua sensitivity; chưa xác định liều tối ưu |
| C13 | [PAASS return-to-sport framework, 2021](https://pubmed.ncbi.nlm.nih.gov/34158354/) · EN | International consensus; **A/P**: abstract và mô tả domains lập chỉ mục | Năm domains, không có điểm cắt clearance phổ quát; BJSM trực tiếp chặn |
| C14 | [Aspetar clinical practice guideline on rehabilitation after ACL reconstruction, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11785408/) · EN | CPG; **F**: methods, exercise, Box 5 running/RTS, limitations | Tiêu chí chạy/RTS phần lớn đề xuất chuyên gia; không chỉ thời gian; không áp dụng nguyên cho mọi thủ thuật phối hợp |
| C15 | [Heel Pain—Plantar Fasciitis CPG Revision, 2023](https://doi.org/10.2519/jospt.2023.0303) · EN | CPG; **P**: khuyến nghị lập chỉ mục | Stretching/loading và night splint có điều kiện; chưa đọc toàn bộ PDF |
| C16 | [WHO releases guidelines on chronic low back pain, 2023](https://www.who.int/news/item/07-12-2023-who-releases-guidelines-on-chronic-low-back-pain) · EN | Thông cáo chính thức; **F** | Chronic primary LBP; đây không phải đã đọc toàn bộ guideline/evidence profiles |
| C17 | [Rotator Cuff Tendinopathy Diagnosis, Nonsurgical Medical Care, and Rehabilitation CPG, 2025](https://doi.org/10.2519/jospt.2025.13182) · EN | CPG; **P**: scope, imaging, education/exercise, RTS được lập chỉ mục | Không full tear/post-op; chưa biết liều tối ưu, không dựng một protocol duy nhất |
| C18 | [Lateral Elbow Pain and Muscle Function Impairments CPG, 2022](https://www.orthopt.org/uploads/content_files/files/lucado_et_al_2022_lateral_elbow_pain_and_muscle_function_impairments.pdf) · EN | CPG, PDF 111 trang; **F**: summary CPG2–3, differential và therapeutic exercise liên quan | Tập wrist extensors cho subacute/chronic LET; chưa rà tất cả phụ lục hoặc bệnh khuỷu khác |
| C19 | [NHS Neck pain and stiff neck](https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/) · EN | Giáo dục người bệnh; **P**: khi nào cần khám | Mới dùng định hướng, chưa đủ protocol radiculopathy/myelopathy |
| C20 | [NICE NG226: Osteoarthritis in over 16s, 2022](https://www.nice.org.uk/guidance/NG226/chapter/recommendations) · EN | Guideline; **P**: exercise, education, weight management | OA khác khớp sưng cấp chưa rõ nguyên nhân; chưa rà mọi nhánh thuốc/phẫu thuật |
| C21 | [Doha agreement on groin pain in athletes, 2015](https://wrap.warwick.ac.uk/id/eprint/104765/) · EN | Consensus; **A** tại kho Warwick | Phân loại thuật ngữ; chưa đủ protocol adductor/inguinal/hip |
| C22 | [Education plus exercise versus corticosteroid injection versus wait-and-see for gluteal tendinopathy, 2018](https://www.bmj.com/content/361/bmj.k1662) · EN | RCT; **P**: methods/results lập chỉ mục | Global improvement khác pain score; chưa nhập liều phụ lục, không áp dụng mọi lateral hip pain |

## 24.5. Nguồn tiếng Việt và tài nguyên bài tập

| ID | Nguồn | Đã đọc và vai trò | Lưu ý kiểm chứng |
|---|---|---|---|
| V01 | [Viện Dinh dưỡng: Những lời khuyên dinh dưỡng, 11/04/2025](https://viendinhduong.vn/vi/professional-activities/nhung-loi-khuyen-dinh-duong/67dcedfc3770b9299302c692) · VI | **F**: bài về protein/người tập, có dẫn Egan 2016 | Đối chiếu khoảng protein và cách diễn đạt VN; không biến một con số mỗi bữa thành chuẩn mọi thể trọng |
| V02 | [Vinmec: Phân biệt căng cơ, bong gân, hướng dẫn sơ cứu](https://www.vinmec.com/vie/bai-viet/phan-biet-cang-co-bong-gan-huong-dan-cach-so-cuu-vi) · VI | **F**: giải thích, triệu chứng, sơ cứu | Phần kết luận phân biệt bằng bầm tím không đủ tin cậy; cả hai có thể bầm |
| V03 | [BV Nguyễn Tri Phương: Bong gân và cách xử trí](https://bvnguyentriphuong.com.vn/chan-thuong-chinh-hinh/bong-gan-va-cach-xu-tri) · VI | **F**: nội dung xử trí | Không nhập thành rule chung các mốc bó bột/trở lại hoặc kháng sinh do bầm; xem phần 25 |
| V04 | [BV Tâm Anh: Bong gân](https://tamanhhospital.vn/benh/bong-gan/) · VI | **P**: đã lấy toàn văn, đối chiếu phần triệu chứng/định hướng | Chưa kiểm chứng mọi mệnh đề và chỉ định trong bài; dùng như giáo dục người bệnh |
| V05 | [BV Tâm Anh: Căng cơ](https://tamanhhospital.vn/benh/cang-co/) · VI | **P**: đã lấy toàn văn, đọc phần nguyên nhân/xử trí/dinh dưỡng liên quan | Không nhập diễn giải lactate, tắm muối hoặc thuốc thành protocol; xem phần 25 |
| V06 | [Trang hướng dẫn tập luyện TDTT: Dinh dưỡng cho người luyện tập](https://huongdantapluyen.tdtt.gov.vn/dinh-duong/ID/17084/Dinh-duong-cho-nguoi-luyen-tap-the-duc-the-thao) · VI | **X**: trang không đọc được nội dung đầy đủ | Không dùng làm căn cứ tính khẩu phần |
| R01 | [MuscleWiki](https://musclewiki.com/) · EN | Trang thư viện; vai trò và schema tại phần 16 | Đã bổ sung liên kết; **chưa nhập toàn bộ bài/video**, chưa có bảng thay thế đã thẩm định |
| R02 | [Squat University Blog](https://squatuniversity.com/featured-links/blog/) · EN, bản tổng hợp VI trong kho | Bộ nguồn có trước; đợt này đối chiếu cấu trúc/một số mệnh đề trong phần 00, 13–15 | Không tuyên bố đã kiểm chứng lại toàn bộ 98 bài hoặc mọi khuyến nghị của bản tổng hợp cũ |

## 24.6. Cách lưu một kết luận để không mất chi tiết quyết định

Mỗi kết luận khi đưa vào cơ sở dữ liệu cần lưu: source ID/URL/DOI, năm và ngày kiểm tra, đối tượng, thiết kế nghiên cứu, intervention/comparator, outcome và thời điểm đo, effect/uncertainty nếu dùng, grade của nguồn, ngoại lệ, mức đọc, cách diễn giải tiếng Việt và rule đang sử dụng nó. Liều tập cần đủ frequency/intensity/type/time/volume/progression và điều kiện dừng.

Nếu chỉ có abstract thì để liều chưa biết là `unknown`; không lấp bằng protocol từ video. Nếu một CPG ghi “may” hoặc expert opinion thì bản tiếng Việt không đổi thành “bắt buộc”. Nếu kết quả sensitivity analysis không còn ý nghĩa thống kê, giữ chi tiết đó. Nếu kết quả là giảm đau ngắn hạn, không đổi thành sửa mô hoặc giảm tái chấn thương dài hạn.

## 24.7. Dấu vết nghiên cứu

Thư mục `research/` giữ script truy cập và bản chụp văn bản/PDF phục vụ kiểm tra tại máy. Một snapshot ngắn có thể là trang bị chặn, không phải bài đã đọc. Bảng trên và citation trong phần 17–23 là hồ sơ sử dụng; không lấy số file tải xuống làm số tài liệu đã thẩm định. Bản thảo là diễn giải và tổng hợp, không phải bản dịch toàn văn các nguồn. Các file tải và thư viện Python phụ trợ được tách khỏi nội dung xuất bản bằng `.gitignore` trong thư mục research.

Các khoảng trống còn lại, mâu thuẫn và mức đủ dùng: [phần 25](references/25-doi-chieu-mau-thuan-va-khoang-trong.md).

## 24.8. Bổ sung từ tám tài liệu người dùng, 15/09/2026

U01–U08 là tài liệu người dùng cung cấp, không phải tám nghiên cứu độc lập. Đã đọc toàn bộ nội dung được gửi, lưu nguyên văn và phân loại tại [28.2 — Hồ sơ tiếp nhận](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md). Không tự nhận đã đọc toàn bộ nguồn/video mà các bản này nhắc tới.

| ID | Nguồn tra thêm | Mức đọc / nơi dùng |
|---|---|---|
| T08 | [Maeo et al., triceps overhead vs neutral, 2023](https://pubmed.ncbi.nlm.nih.gov/35819335/) | A; phần 26.5 |
| T09 | [Plotkin et al., hip thrust vs squat, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10593473/) | P; phần 26.5 |
| T10 | [Refalo et al., sex differences in hypertrophy, 2025](https://peerj.com/articles/19042.pdf) | A/P; phần 27.2 |
| T11 | [Judge & Burke, bench press recovery, 2010](https://pubmed.ncbi.nlm.nih.gov/20625191/) | A; phần 27.3 |
| T12 | [Colenso-Semple et al., menstrual cycle and resistance training, 2023](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1054542/full) | F phần liên quan; phần 27.4 |
| T13 | [Behm et al., acute stretching effects, 2016](https://pubmed.ncbi.nlm.nih.gov/26642915/) | A/P; phần 22.7 |
| C23 | [Clifford et al., isometric exercise in tendinopathy, 2020](https://pubmed.ncbi.nlm.nih.gov/32818059/) | A; phần 19.10 |

Phạm vi, lý do sửa kết luận và thông tin nguồn còn thiếu xem phần 28.3–28.5. Tài liệu biên soạn mới không xác nhận toàn bộ danh sách bài/tier trong U02 hoặc protocol lâm sàng trong U05–U08.


---

<!-- CHAPTER 25 -->

# 25. ĐỐI CHIẾU, MÂU THUẪN VÀ KHOẢNG TRỐNG CÒN LẠI

Ngày 15/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Ma trận nguồn](references/24-ma-tran-nguon-va-kiem-chung.md).

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

T01/C01/C08/C16 và mức đọc xem [ma trận nguồn](references/24-ma-tran-nguon-va-kiem-chung.md). Những lỗi mẫu chương trình được ghi lại để tránh tự sửa một con số rồi giả định đó là ý định tác giả.

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

Ngày 15/09/2026: đã bổ sung danh sách ứng viên và logic thay bài ở [phần 26](references/26-chon-bai-tap-va-bien-the-theo-muc-tieu.md), nhánh nam–nữ/chu kỳ ở [phần 27](references/27-ca-nhan-hoa-nam-nu-va-chu-ky-kinh-nguyet.md), cùng [audit tài liệu mới](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md). Đây là tiến bộ về nội dung, chưa hoàn tất exercise database, kiểm định engine, dinh dưỡng món Việt hoặc các nhánh bệnh/sau mổ. Các khẳng định tuyệt đối lặp trong tài liệu mới không ghi đè giới hạn đã nêu ở trên.


---

<!-- CHAPTER 26 -->

# 26. CHỌN BÀI TẬP VÀ BIẾN THỂ THEO MỤC TIÊU

Cập nhật 15/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Hồ sơ tiếp nhận](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md).

## 26.1. Phần nào được tiếp nhận?

Nguồn chính là [U02 — Best Exercises for Each Muscle](references/tai-nguyen-nguoi-dung/2026-09-15/U02-best-exercises.md), kết hợp tiêu chí chọn bài từ [U01](references/tai-nguyen-nguoi-dung/2026-09-15/U01-instruction-ai.md). U02 là bản tổng hợp transcript, chưa có URL/tác giả video để xác minh từng nhận định. Các nhãn S/A/F-tier được giữ trong bản lưu gốc nhưng **không dùng làm thứ hạng khoa học hay danh sách cấm trong toolkit**.

Phần dưới là **[H] — danh sách ứng viên và tiêu chí lựa chọn**, không phải chứng minh bài này tốt hơn mọi bài khác. Nơi có nghiên cứu trực tiếp được tách riêng ở 26.5. Chọn bài cho rehab phải qua phần 19–21, không đi thẳng từ vị trí đau sang bảng bài.

## 26.2. Thứ tự lựa chọn [H]

1. **Mục tiêu:** hypertrophy của cơ nào, thành tích lift nào hay nhiệm vụ sinh hoạt nào?
2. **Ràng buộc:** hạn chế y tế, thiết bị, không gian, thời gian setup, kỹ năng và sở thích.
3. **Khả năng thực hiện:** ROM, kiểm soát, phản ứng triệu chứng, điểm dừng an toàn.
4. **Yếu tố giới hạn set:** cơ mục tiêu, grip, thăng bằng, khó thở, đau, setup hay kỹ thuật?
5. **Theo dõi được:** cùng setup/ROM, bước tăng tải khả thi, có thể ghi reps/effort.
6. **Độ trùng lặp và chi phí:** bài có bổ sung chức năng/nhóm cơ còn thiếu hay chỉ tăng thêm mệt và thời gian?

Pump, soreness và cảm giác “ăn cơ” được ghi như phản hồi; không dùng riêng để kết luận hypertrophy. Một bài ổn định có thể giúp tập trung vào mục tiêu cơ bắp, nhưng nhu cầu thăng bằng có thể chính là mục tiêu của bài khác. Không coi tension là một đại lượng “thất thoát” đơn giản giữa các cơ.

## 26.3. Danh sách ứng viên theo vùng [H, biên soạn từ U02]

Các bài trong cùng hàng là lựa chọn để cân nhắc, **không phải yêu cầu tập tất cả**. Phân vùng cơ là mô tả mục đích, không hứa cô lập hoàn toàn một đầu cơ hoặc thay đổi hình dạng cơ tùy ý.

| Vùng / vai trò | Ứng viên | Điều kiện chọn và điểm cần ghi | Khi thay bài cần giữ/xem lại |
|---|---|---|---|
| Glutes — hip extension | Machine/Barbell Hip Thrust | Đệm, chiều cao ghế, ROM và setup hợp cơ thể | Ghi lại tải theo bài mới; số kg không quy đổi trực tiếp sang squat |
| Glutes — squat/lunge | Walking Lunge; Bulgarian Split Squat; Front-Foot-Elevated Smith Lunge | Độ dài bước, hỗ trợ tay, độ cao kê và mức dung nạp | Có thể dùng biến thể tại chỗ khi thiếu diện tích; không bắt bước dài/nghiêng thân đúng 30° |
| Glutes — hinge | Romanian Deadlift; 45-Degree Back Extension | ROM hip hinge, tải và yếu tố giới hạn grip/lưng | Không dùng “lower glute tie-in” làm hứa hẹn giảm mỡ cục bộ |
| Hip abduction | Machine Hip Abduction; Cable Hip Abduction | Tư thế máy, ROM chủ động, kiểm soát thân | Không đồng nhất glute medius/minimus với toàn bộ “upper glutes” hoặc xem đây là chữa knee cave |
| Biceps — curl có tựa | Dumbbell/Machine Preacher Curl | Góc ghế, vị trí khuỷu, ROM và trọng lượng khởi đầu | Không đánh đồng mọi máy preacher có cùng resistance profile |
| Biceps — vai ở sau thân | Face-Away Bayesian Cable Curl; Incline Dumbbell Curl | Vị trí vai và pulley; dung nạp vai/khuỷu | Không ép vai ra sau để đạt stretch; hai bài có đường lực khác nhau |
| Elbow flexors — grip trung tính | Hammer Curl; Preacher Hammer Curl | Grip, vị trí cánh tay và ROM | Không cam kết tạo “biceps peak”; giữ mục tiêu elbow flexion và xem response |
| Curl ít setup | Standing Dumbbell Curl; EZ-Bar Curl; Standard Cable Curl | Thiết bị sẵn, bước tải, tư thế cổ tay thoải mái | Không bỏ bài đang tiến triển chỉ vì tier thấp hơn |
| Side delts | Cable Lateral Raise; Dumbbell Lateral Raise; Machine Lateral Raise | Vị trí pulley/cuff, đường tay và ROM | Không gọi dumbbell raise vô dụng khi không có cable |
| Rear delts | Reverse Pec Deck; Reverse Cable Crossover; Face Pull | Máy có vừa người, đường khuỷu/tay và yêu cầu phối hợp | Face pull có vai trò khác reverse fly; không mặc định tương đương từng set |
| Front delts / overhead strength | Machine/Dumbbell Shoulder Press | Tải pressing hiện có, mục tiêu overhead, dung nạp | Front raise có thể dư ở người này nhưng cần ở người khác; xem mục tiêu trước |
| Quads — squat ổn định | Hack Squat; Pendulum Squat; Smith Squat | Thiết kế máy, vị trí chân, ROM, chốt an toàn | Không mặc định mọi gym có máy hoặc mọi máy cho cùng ROM |
| Quads / kỹ năng squat | High-Bar Back Squat; Front Squat | Mục tiêu lift, setup, mức kỹ năng, rack/safeties | Machine squat không thay hoàn toàn kỹ năng competition squat |
| Quads — một chân | Bulgarian Split Squat; Supported Split Squat; Step-Up | Hỗ trợ thăng bằng, độ cao bục, công việc một chân | Step-up không bị loại chỉ vì U02 xếp thấp cho hypertrophy; hữu ích tùy nhiệm vụ |
| Quads — knee extension | Leg Extension | Góc tựa, trục máy, ROM và giới hạn cá nhân | Ghi góc hông/ghế; không thêm knee extension sau mổ trái chỉ định |
| Quads — thiết bị hạn chế | Goblet Squat; Reverse Nordic; Split Squat | Reverse Nordic có yêu cầu sức mạnh/ROM riêng, không mặc định cho người mới | Khi tăng reps/depth vẫn không đủ mục tiêu, đổi cách tạo kháng lực |
| Triceps — overhead | Overhead Cable Extension; Dumbbell Overhead Extension | Dung nạp overhead/khuỷu, handle và ROM | Không bắt buộc bar tốt hơn rope; xem setup thực tế |
| Triceps — tay cạnh thân | Cable Pressdown; Cable Kickback | ROM khuỷu, tư thế vai, mức dễ tăng tải | Đổi vị trí vai làm đổi yêu cầu; không gộp mọi biến thể thành cùng bài |
| Triceps — free-weight/press | EZ-Bar/Dumbbell Skullcrusher; Close-Grip Bench Press | Kỹ năng, safeties, pressing volume và cổ tay | Close-grip bench có mục tiêu kỹ năng/compound riêng, không thay 1:1 isolation |
| Chest — press | Machine Chest Press; Flat Dumbbell Press; Bench Press; Smith Press | Máy/ghế vừa người, ROM và đường đẩy dung nạp | Giữ bench nếu cần kỹ năng bench; không phải mọi machine press “an toàn tuyệt đối” |
| Chest — incline | Incline Dumbbell/Barbell/Smith Press | Ghi góc ghế và mục tiêu, theo dõi tải | Không tự kết luận lower chest không cần tập từ sở thích của tác giả |
| Chest — isolation | Seated Cable Flye; Pec Deck; Cable Crossover | ROM và đường máy/cable, thời gian setup | Không ép deep stretch hoặc coi cable tension bằng moment tại khớp |
| Chest — tại nhà | Push-Up; Deficit Push-Up khi phù hợp | Độ cao tay/chân, ROM, tải bổ sung và sự ổn định | Deficit là thay đổi yêu cầu, không mặc định tốt hơn khi gây khó chịu |
| Lats — vertical pull | Neutral/Wide-Grip Pulldown; Pull-Up; Assisted Pull-Up | Grip, ROM, mức hỗ trợ, lực nắm | Không gán wide grip chắc chắn tăng hypertrophy hơn neutral grip |
| Back — row có tựa | Chest-Supported Row; Supported One-Arm Dumbbell Row | Góc ghế, đường khuỷu, ROM, lực nắm | Tựa ngực giảm yêu cầu giữ thân nhưng không thay mọi mục tiêu erector/hinge |
| Back — cable/unilateral | Cable Row; Wide-Grip Cable Row; Half-Kneeling One-Arm Pulldown; Meadows Row | Đường kéo, hỗ trợ thân, setup và kỹ năng | Không ghép ba bài trùng vai trò chỉ để đủ danh sách “best picks” |
| Lat accessory | Cable Pullover; Dumbbell Pullover | Đường lực khác nhau, ROM và dung nạp vai | Không coi hai dụng cụ tạo resistance profile tương đương |

**Phạm vi thiếu:** U02 không có chương riêng đầy đủ cho hamstrings, calves, adductors, abdominals, forearms, neck hoặc conditioning. RDL xuất hiện trong nhóm glutes không biến danh sách này thành chương trình toàn thân hoàn chỉnh. Các mục tiêu đó cần bổ sung nguồn/bài riêng khi thiết kế.

## 26.4. Đổi bài theo tình huống, không đổi theo tier [H]

| Nếu | Có thể thử | Điều kiện đánh giá lại |
|---|---|---|
| Hack squat bận nhưng cần stimulus chân | Leg press/Smith/split squat quen thuộc tùy thiết bị | Warm-up tìm tải mới; giữ effort mục tiêu; không lấy kg của hack squat |
| Row bị giới hạn bởi khả năng giữ thân, mục tiêu chính là back hypertrophy | Chest-supported row | Xem reps/effort, thoải mái và chất lượng; đau mới cần sàng lọc riêng |
| Cable raise mất nhiều thời gian setup | Dumbbell/machine lateral raise | Cùng mục tiêu cơ, nhưng tạo baseline mới vì profile khác |
| Overhead extension không dung nạp | Dừng biến thể gây triệu chứng; xem pressdown hoặc bài khác nếu phù hợp đánh giá | Không ép overhead vì nghiên cứu nhóm trung bình; triệu chứng mới theo phần 19 |
| Muốn power/conditioning hoặc kỹ năng mang vác | Giữ swing, jump hoặc carry khi phù hợp kế hoạch | Không loại vì bảng hypertrophy đánh giá thấp |
| Muốn competition deadlift | Giữ tiếp xúc kỹ năng lift theo giai đoạn | Không thay hết bằng row chỉ vì deadlift không là bài lat ưu tiên |

## 26.5. Hai đối chiếu nghiên cứu trực tiếp

**T08 — Triceps:** 21 người tập extension một tay overhead, tay kia neutral trong 12 tuần; 5 × 10, hai buổi/tuần, khởi đầu 70% 1RM theo điều kiện. MRI ghi tăng thể tích triceps lớn hơn ở overhead, đặc biệt long head. Đây là so sánh hai điều kiện cụ thể, không chứng minh bar hơn rope, không xác nhận an toàn cho vai đau và không buộc dùng liều này trong mọi giáo án. Đã đọc abstract. [Maeo et al., 2023, online 2022](https://pubmed.ncbi.nlm.nih.gov/35819335/).

**T09 — Glutes:** nghiên cứu chín tuần ở người ít kinh nghiệm, số set được cân bằng, ghi hypertrophy glutes tương tự giữa squat và hip thrust; squat tăng cơ đùi nhiều hơn, strength tăng theo bài đã tập. Điều này không đủ xếp walking lunge đứng đầu mọi người hoặc biến EMG/pump thành bảng xếp hạng tăng cơ. Đã đọc phần methods/results được lập chỉ mục của bản công bố. [Plotkin et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10593473/).

## 26.6. Schema cho exercise record [H]

```yaml
exercise_id: null
canonical_name: null
aliases: []
source_material: [U02]
original_video_url: null
musclewiki_url: null
verification_status: candidate_not_fully_validated
goal_roles: []
movement_pattern: null
target_muscles: []
equipment_and_setup: []
rom_and_joint_positions: null
resistance_profile_notes: null
skill_and_balance_requirements: null
likely_set_limiters: []
progression_options: []
substitutions_and_tradeoffs: []
symptom_or_clinician_constraints: []
evidence_for_specific_claims: []
```

`null` nghĩa là chưa xác minh, không phải không cần. Chưa có URL bài MuscleWiki cụ thể thì để trống; không tạo link đoán từ tên. Khi đưa bài vào giáo án, thêm liều, effort, rest, điều kiện tăng/giảm và review theo phần 17/23. Bản lưu U02 vẫn giữ đầy đủ các ứng viên và nhận xét chưa nhập, để truy lại khi có thêm nguồn.


---

<!-- CHAPTER 27 -->

# 27. CÁ NHÂN HÓA NAM–NỮ VÀ CHU KỲ KINH NGUYỆT

Cập nhật 15/09/2026. [Tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Nguồn tiếp nhận và kiểm chứng](references/28-tiep-nhan-tai-nguyen-va-doi-chieu.md).

## 27.1. Phạm vi và cách đọc nguồn mới

[U03](references/tai-nguyen-nguoi-dung/2026-09-15/U03-male-female-adaptations.md) là bài tổng quan được dán, không có tác giả/URL/năm đầy đủ. [U04](references/tai-nguyen-nguoi-dung/2026-09-15/U04-transcript-male-female.md) là đoạn transcript khoảng 5:49–13:57, thiếu mở đầu và liên kết video. Không coi hai tài liệu là hai thử nghiệm độc lập; cả hai nhắc một nghiên cứu bench press năm 2010.

Các nguồn nghiên cứu phân nhóm male/female theo định nghĩa của từng nghiên cứu. Không dùng kết quả nhóm để đoán giải phẫu, hormone, chu kỳ, sở thích hoặc năng lực của một người cụ thể. Thai kỳ/hậu sản, menopause, dùng hormone và bệnh liên quan cần nguồn riêng; đợt bổ sung này chưa xây protocol cho các nhóm đó.

## 27.2. Tăng cơ tương đối khác với tăng cơ tuyệt đối

**[E] T10:** meta-analysis 2025 gồm 29 nghiên cứu, người khỏe mạnh 18–45 tuổi cùng tập một can thiệp. Tăng kích thước cơ tuyệt đối hơi nghiêng về nam; tăng tương đối so baseline tương tự giữa hai nhóm. Không diễn giải thành mọi nam/nữ tăng cùng số kg cơ hoặc cùng tốc độ cá nhân. Đã đọc abstract và thông tin phương pháp/kết quả được lập chỉ mục, chưa toàn văn. [Refalo et al., 2025](https://peerj.com/articles/19042.pdf).

**[H] Ví dụ phép tính:** kích thước cơ giả định từ 100 lên 110 và từ 60 lên 66 đều tăng 10%, nhưng mức tăng tuyệt đối là 10 và 6 đơn vị. Đây chỉ là minh họa, không phải dữ liệu nghiên cứu hoặc chuẩn kích thước theo giới.

**Ứng dụng [H]:** dùng chung quy trình xác định mục tiêu, chọn bài, effort, progressive overload và hồi phục; bắt đầu theo năng lực đo được. Không tự kê tạ nhẹ/high reps cho nữ, hoặc upper-body ưu tiên cho nam. “Bulky” là mô tả sở thích cần hỏi rõ, không phải một outcome khoa học có thể bảo đảm không xảy ra.

## 27.3. Hồi phục: sửa chi tiết nghiên cứu bench press 2010

**[E] T11:** Judge và Burke nghiên cứu 20 người, có nhóm athlete và sinh viên đối sánh; ba tuần làm quen, rồi kiểm tra sau 4/24/48 giờ. Outcome là **1RM ước tính từ reps ở mức 5RM cảm nhận**. Nam giảm estimated 1RM ở cả 4 và 24 giờ; nữ không ghi khác biệt qua các mốc. Vì vậy diễn đạt “nam hồi phục ở 24 giờ” trong transcript không đúng kết quả abstract. Nghiên cứu không thử dài hạn một giáo án nữ bench mỗi bốn giờ. Đã đọc abstract gốc. [Judge & Burke, 2010](https://pubmed.ncbi.nlm.nih.gov/20625191/).

**[H] Quy tắc:** khoảng cách buổi dựa trên bài, liều, effort, lịch sử và đáp ứng người tập. Không gắn `female = recovered_after_4h` hoặc tự tăng tần suất. Phân biệt mệt trong một set, khả năng lặp lại các set, hồi phục một phép thử và thích nghi nhiều tuần; chúng không là cùng outcome.

## 27.4. Chu kỳ kinh nguyệt: theo triệu chứng và dữ liệu, không mặc định chia giáo án theo lịch

**[E] T12:** umbrella review 2023 nhận thấy kết quả không nhất quán, hạn chế về xác định pha chu kỳ và phương pháp. Chưa đủ căn cứ kết luận dao động hormone ngắn hạn tạo ảnh hưởng đáng kể để kê resistance training theo pha cho mọi người. Phạm vi tìm kiếm tập trung người trẻ khỏe, chu kỳ tự nhiên đều, không dùng tránh thai hormone. Không suy thành triệu chứng cá nhân không tồn tại. Đã đọc methods và kết luận liên quan. [Colenso-Semple et al., 2023](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1054542/full).

U03 nêu tăng frequency/volume ở follicular và giảm ở luteal. Trong toolkit, đây là **giả thuyết chưa đủ để làm mặc định**, không phải yêu cầu đã kiểm chứng. Không lấy lịch 28 ngày hoặc ngày app dự đoán làm xác nhận nồng độ hormone/rụng trứng.

### Dữ liệu tùy chọn [H]

Chỉ thu thập khi liên quan và người dùng muốn theo dõi: ngày tự ghi nhận, triệu chứng, mức ảnh hưởng sinh hoạt, giấc ngủ, effort/performance, tình trạng dùng tránh thai hormone nếu họ muốn cung cấp. Có lựa chọn “không theo dõi”; vẫn xây được chương trình dựa trên các đầu vào khác. Không suy thông tin chu kỳ từ tên hoặc giới tính.

### Bảng quyết định [H]

| ID / nếu | Thì | Review và giới hạn |
|---|---|---|
| M01: không có triệu chứng ảnh hưởng, warm-up như thường | Giữ kế hoạch theo effort | Không giảm/tăng chỉ vì ngày chu kỳ |
| M02: khó chịu quen thuộc làm giảm khả năng tập, không có dấu cần đánh giá | Dùng phiên bản nhẹ/ngắn hơn hoặc đổi thời điểm theo lựa chọn cá nhân | Kiểm tra lại từng buổi; không đặt % giảm cố định |
| M03: pattern khó chịu/hiệu suất lặp lại qua các lần theo dõi | Dự phòng cửa sổ linh hoạt, dời buổi quan trọng nếu có lợi | Theo dõi xem thay đổi giúp adherence/hiệu suất không; đây là thử nghiệm cá nhân |
| M04: triệu chứng mới, tăng rõ, ảnh hưởng lớn, mất kinh hoặc có dấu thiếu năng lượng | Chuyển đánh giá phù hợp, áp dụng phần 19/18.8 theo tình huống | Không coi là bằng chứng cần “cycle syncing” hoặc tự chẩn đoán REDs |
| M05: không biết pha, không muốn ghi chu kỳ hoặc dùng hormone | Dùng triệu chứng, lịch và effort; giữ dữ liệu chưa biết | Không tự gán pha sinh lý từ lịch |

Không tự động đổi calorie/macros chỉ vì pha được dự đoán. Quy tắc dinh dưỡng vẫn xét mục tiêu, xu hướng, mức vận động, sức khỏe và khả năng thực hiện ở phần 18.

## 27.5. Những suy luận không nhập từ transcript

- Nhận xét về nữ tuân thủ hơn, nam hay test max, sở thích ngực/mông là kinh nghiệm người nói; không dùng làm rule theo giới.
- Nhận xét “hyper responder” với thuốc/hormone không có dữ liệu đủ trong đoạn gửi; không dùng để tư vấn thuốc hoặc giải thích chắc chắn một vóc dáng.
- Tương đồng hypertrophy tương đối không chứng minh testosterone không quan trọng; mô hình động vật và cơ chế hormone không tự chuyển thành lịch tập.
- Tên tác giả bị ghi thành “Lawrence & Jeanmarie” trong U03 thực chất là tên của Judge và Burke ở T11, không phải một nghiên cứu độc lập khác.

## 27.6. Ví dụ đầu ra hợp lệ [H]

“Bạn có ba buổi khả dụng và ưu tiên squat; lịch cơ sở giữ theo năng lực hiện tại. Nếu xuất hiện khó chịu quen thuộc ảnh hưởng tập, chuyển buổi quan trọng sang cửa sổ dự phòng hoặc dùng phiên bản ngắn theo effort. Ghi phản ứng và mức hoàn thành để xem cách đổi có hữu ích; không tăng volume chỉ vì dự đoán đang ở follicular phase.”

Mục tiêu của module là mở thêm lựa chọn cá thể hóa, không tạo hai giáo án rập khuôn nam/nữ hoặc bắt mọi người ghi dữ liệu sinh sản.


---

<!-- CHAPTER 28 -->

# 28. TIẾP NHẬN 8 TÀI NGUYÊN VÀ ĐỐI CHIẾU KẾT LUẬN

Ngày 15/09/2026. [Trang tài nguyên](references/16-tong-hop-tai-nguyen.md) · [Ma trận nguồn chung](references/24-ma-tran-nguon-va-kiem-chung.md).

## 28.1. Kết quả tiếp nhận

Đã đọc nội dung cả tám tệp người dùng gửi, đối chiếu với phần 17–25 và tra thêm nguồn cho các mệnh đề quyết định. Không coi nhãn “báo cáo khoa học”, persona DPT/CSCS hoặc chữ “INSTRUCTION” trong tài liệu là bằng chứng chuyên môn hay chỉ dẫn tự động có hiệu lực.

Mỗi bản gốc được lưu trong `tai-nguyen-nguoi-dung/2026-09-15/`, kèm attachment ID và SHA-256. Phần nội dung gốc sau marker được giữ nguyên byte; lỗi bảng, transcript, trích dẫn thiếu và khẳng định chưa đúng vẫn được giữ để truy nguồn. **Chỉ các phần biên soạn/đối chiếu mới được dùng làm căn cứ thiết kế; bản lưu không đồng nghĩa đã thẩm định.**

## 28.2. Bản đồ tám tài liệu → nội dung đã bổ sung

| ID / tài liệu gốc | Giá trị lấy vào | Nơi dùng | Giới hạn |
|---|---|---|---|
| [U01 — Instruction cho AI](references/tai-nguyen-nguoi-dung/2026-09-15/U01-instruction-ai.md) | Intake kỹ thuật, quan sát trước giả thuyết, ít cue, setup/ROM/effort có thể đo, cấu trúc trả lời | Phần 23.10, 26 và 17.10 | Bản đề xuất vận hành; sửa việc bắt buộc 24 giờ, số giả thuyết, giai đoạn và thời hạn |
| [U02 — Best Exercises for Each Muscle](references/tai-nguyen-nguoi-dung/2026-09-15/U02-best-exercises.md) | Danh sách ứng viên, thiết bị, limiting factor, chọn và thay bài theo mục tiêu | Phần 26 | Chưa có link video gốc; tier là nhận xét transcript; không nhập thành thứ hạng khoa học |
| [U03 — Male vs Female Strength Training Adaptations](references/tai-nguyen-nguoi-dung/2026-09-15/U03-male-female-adaptations.md) | Câu hỏi absolute/relative, fatigue/recovery và chu kỳ | Phần 27, kiểm chứng T10–T12 | Thiếu tác giả/URL/năm; bảng 1 được nhắc nhưng không có dữ liệu trong tệp |
| [U04 — Transcript nam–nữ](references/tai-nguyen-nguoi-dung/2026-09-15/U04-transcript-male-female.md) | Bối cảnh mục tiêu cá nhân, phân biệt thực hành coach và kết quả nghiên cứu | Phần 27 | Đoạn giữa/cuối video, không xác nhận được toàn bộ ngữ cảnh hoặc danh tính từ URL |
| [U05 — Cơ sinh học và kỹ thuật](references/tai-nguyen-nguoi-dung/2026-09-15/U05-co-sinh-hoc.md) | Checklist setup, cue và thông số cần ghi khi phân tích | Phần 23.10; bảng đối chiếu dưới | Trích dẫn dạng “i” thiếu thư mục đầy đủ; không nhận các chuỗi nhân quả chắc chắn |
| [U06 — Lập trình và chu kỳ hóa](references/tai-nguyen-nguoi-dung/2026-09-15/U06-lap-trinh-chu-ky-hoa.md) | Thuật ngữ macro/meso/micro, cách chọn linear/DUP/block/conjugate, specificity | Phần 17.10 | Các tên nguồn cuối bài chưa có URL; mẫu %/sets không là lịch áp dụng chung |
| [U07 — Rehab và quản lý chấn thương](references/tai-nguyen-nguoi-dung/2026-09-15/U07-rehab-chan-thuong.md) | Demand/capacity như mô hình trao đổi, entry point, ghi phản ứng sau buổi | Phần 19.10; liên kết về 20–21 | Không tiếp nhận chuỗi rehab năm pha cho mọi bệnh hoặc isometric luôn không kích ứng |
| [U08 — Hypertrophy và tối giản](references/tai-nguyen-nguoi-dung/2026-09-15/U08-hypertrophy-toi-gian.md) | Tách phần ưu tiên/tùy chọn, xem chi phí fatigue, tempo theo mục đích | Phần 17.10, 22.7 và 26 | MEV 10–12, tăng set mỗi tuần, bắt buộc RPE 9–10 rồi deload đều là mẫu cần điều kiện |

Nội dung trùng phần 17–25 được nối tới phần đó thay vì chép thêm một bản khẳng định khác. Tám tệp có nhiều nội dung lặp; không tính số lần lặp lại như nhiều nguồn bằng chứng độc lập.

## 28.3. Những kết luận được sửa điều kiện hoặc chưa nhập

| Mệnh đề trong tệp gửi | Vấn đề khi chuyển thành giải pháp | Quy tắc biên soạn thay thế |
|---|---|---|
| Một bài là “best of the best” hoặc F-tier cho toàn bộ người tập | Trộn mục tiêu hypertrophy, power, kỹ năng và rehab | Chọn theo mục tiêu/ràng buộc; giữ tier chỉ trong bản gốc U02 |
| Cable tạo tension đều nên moment tại khớp đều | Đường lực và cánh tay đòn thay đổi theo setup/góc | Ghi pulley, tư thế, ROM; chưa có đo lường thì không gán profile định lượng |
| Bài compound không cần vì máy ổn định hơn | Hypertrophy và kỹ năng competition lift khác nhau | Tách mục tiêu cơ và lift; phần 26 |
| Cơ dài hơn/full ROM luôn tốt nhất; stretch càng sâu càng tốt | Chiều dài cơ, ROM khớp và moment không phải cùng đại lượng; kết quả có tính đặc hiệu | Không suy từ một nghiên cứu triceps sang mọi cơ; giữ ROM dung nạp và mục tiêu |
| Pump/EMG cao xác nhận tăng cơ cao nhất | Outcome cấp tính khác thay đổi kích thước dài hạn | Dùng nghiên cứu longitudinal khi xếp hiệu quả; không dùng cảm giác đơn độc |
| Upper/middle/lower glutes là ba cơ độc lập; hammer curl tạo peak chắc chắn | Trộn tên cơ, vùng cơ và hình dáng thẩm mỹ | Ghi mục tiêu giải phẫu đúng mức; không hứa thay đổi hình dạng hoặc giảm mỡ cục bộ |
| Mọi người bắt đầu MEV 10–12 và tăng 1–2 set mỗi tuần | Con số động không phải ngưỡng đo được chỉ từ intake | Bắt đầu theo lịch sử/liều phù hợp; chỉ tăng khi có lý do và hồi phục |
| Giảm volume “xuống 40–60%” và “giảm 40–60%” được dùng lẫn | Là hai cách mô tả khác; nếu khoảng đối xứng có thể tình cờ trùng nhưng nghĩa vẫn khác | Ghi số set trước→sau; ví dụ 10→5 là giảm 50% |
| Deload luôn giữ nguyên tải để giữ thần kinh/tissue stiffness | Không phù hợp mọi nguyên nhân mệt/đau | Chọn volume, effort và tải theo lý do deload; không chỉ nhìn %1RM |
| Linear tốt nhất cho novice, DUP tốt nhất intermediate, block bắt buộc advanced | Trình độ không đủ quyết định mô hình | Xem deadline, mục tiêu, lịch, kỹ năng và phản hồi; phần 17.10 |
| GAS/SRA chứng minh bắt buộc periodization hoặc stimulus phải đều | Mô hình khái niệm không xác nhận một lịch duy nhất | Dùng để trao đổi về thích nghi/mệt; không suy superiority |
| Knee cave = glute medius yếu; good-morning squat = mất Lombard | Quan sát video không xác định cơ yếu hoặc mô tổn thương | Mô tả hiện tượng, xem tải/mệt/setup/giải phẫu; nêu giả thuyết có giới hạn |
| Hip stiffness là nguyên nhân chính mọi đau lưng | Tương quan/khung quan sát không chứng minh nguyên nhân cá nhân | Giữ sàng lọc và đánh giá đa yếu tố phần 19/21 |
| 5-inch test là cutoff cho tất cả; tệp ghi lúc từ gót, lúc từ mũi | Phép đo không nhất quán, dễ tạo kết luận sai | Ghi điểm mốc, chân, gót có nhấc không và phương pháp; không nhập cutoff để chẩn đoán |
| Không cải thiện ngay sau mobility → bài vô hiệu | Không phân biệt tác dụng tức thời và mục tiêu dài hạn | Review nhiệm vụ ngay và xu hướng qua thời gian; không lặp vô hạn bài không có ích |
| Static stretch <30 giây chắc chắn không ảnh hưởng, >45 giây chắc chắn giảm power | Ngưỡng cứng bỏ qua tổng thời lượng/nhóm cơ và warm-up sau đó | Bổ sung điều kiện ở phần 22.7, nguồn T13 |
| Isometric không có chuyển động nên không gây áp lực/kích ứng | Không có chuyển động khớp không nghĩa không có lực | Chọn theo tổn thương/liều/đáp ứng; nguồn C23 và phần 19.10 |
| Mọi ca đi theo isometric→HSR→full ROM→thi đấu | Các tình trạng và hậu phẫu có yêu cầu khác | Dùng protocol đúng vùng/chẩn đoán; không bắt đi hết các pha |
| Đau quay baseline trong 24 giờ chứng minh an toàn | Là quan sát theo dõi, không đủ xác nhận cấu trúc/clearance | Dùng khoảng review riêng plan và cả chức năng/sưng; phần 19.10 |
| Nữ hồi phục 4 giờ, nam 24 giờ; follicular tự động tăng volume | Mệnh đề nguồn và ứng dụng bị mở rộng; dữ liệu còn bất định | Phần 27 kiểm chứng và dùng rule theo triệu chứng/hiệu suất |

Các hàng cơ sinh học là **giới hạn suy luận và tiêu chuẩn nhập dữ liệu**, không phải khẳng định đã đọc mọi nghiên cứu liên quan từng cơ hoặc từng test. Nếu cần dùng một nhận định để dự đoán tổn thương hoặc xếp bài theo hiệu quả, phải thêm nguồn trực tiếp và thẩm định tương ứng.

## 28.4. Nguồn tra thêm trong đợt này

Mã tiếp nối ma trận phần 24. **A:** abstract; **P:** phần truy cập/lập chỉ mục; **F:** đọc các phần liên quan của toàn văn, không có nghĩa đọc mọi tài liệu được trích dẫn.

| ID | Nguồn và mức đọc | Dùng ở đâu |
|---|---|---|
| T08 | [Maeo et al., triceps overhead vs neutral, 2023; online 2022](https://pubmed.ncbi.nlm.nih.gov/35819335/) — nghiên cứu can thiệp, **A** | 26.5 |
| T09 | [Plotkin et al., hip thrust vs squat, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10593473/) — nghiên cứu can thiệp, **P** methods/results lập chỉ mục, bản công bố | 26.5 |
| T10 | [Refalo et al., sex differences in muscle-size changes, 2025](https://peerj.com/articles/19042.pdf) — meta-analysis, **A/P** | 27.2 |
| T11 | [Judge & Burke, bench press recovery, 2010](https://pubmed.ncbi.nlm.nih.gov/20625191/) — nghiên cứu gốc, **A** | 27.3 |
| T12 | [Colenso-Semple et al., menstrual cycle and resistance training, 2023](https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1054542/full) — umbrella review, **F** phần methods/kết luận, chưa rà mọi nghiên cứu thành phần | 27.4 |
| T13 | [Behm et al., acute stretching effects, 2016](https://pubmed.ncbi.nlm.nih.gov/26642915/) — systematic review, **A/P** abstract và phần liều lập chỉ mục | 22.7 |
| C23 | [Clifford et al., isometric exercise in tendinopathy, 2020](https://pubmed.ncbi.nlm.nih.gov/32818059/) — systematic review/meta-analysis, **A** | 19.10 |

Không ghi các nghiên cứu chỉ được nhắc trong U03/U06 thành “đã đọc”. Một số tài liệu thiếu liên kết gốc vẫn được lưu như đầu mối research; không tự đoán URL hoặc tác giả.

## 28.5. Khoảng trống sau tiếp nhận

- U02 bổ sung danh sách ứng viên, **chưa hoàn thành nhập MuscleWiki** hay kiểm chứng từng cue, grip, góc ghế và tier.
- U03/U04 mở nhánh nam–nữ/chu kỳ, chưa đủ protocol thai kỳ/hậu sản, menopause, tránh thai hormone hoặc hormone therapy.
- Các báo cáo rehab bổ sung cách tổ chức đầu ra nhưng không thay hồ sơ chẩn đoán và protocol hậu phẫu còn thiếu trong phần 25.
- Chưa có thực đơn/dataset dinh dưỡng Việt Nam mới từ tám tài liệu; phần 18 vẫn giữ phạm vi hiện tại.

Khi có video/URL gốc, bổ sung vào source record và kiểm tra lại các mệnh đề chưa xác minh; không cần viết lại mất dấu bản đã tiếp nhận.

