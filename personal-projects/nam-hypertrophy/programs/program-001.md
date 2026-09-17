# Chương trình program-001 — Recomp hypertrophy-led, 12 tuần

```json
{"program_id":"program-001","revision":1,"status":"active","effective_from":"2026-09-16","knowledge_version":"1.0.0"}
```

## Mục tiêu và giả định

**Phase:** Phase 1 của [roadmap](../roadmap.md). Khối 12 tuần, không peaking, không test 1RM.

**Ưu tiên, theo đúng thứ tự khi xung đột:**

1. Giữ cơ và giữ sức (user chốt 2026-09-16).
2. **Độ nét thân trên, đặc biệt mặt trước: ngực và bụng.** (User siết lại mục tiêu 2026-09-16.)
3. **Thân dưới: chỉ cần to lên.** Độ nét thân dưới không phải mục tiêu.
4. **Giữ các bài competition (Squat/Bench/Deadlift)** để không quên kỹ thuật và không mất sức mạnh — user nêu rõ.
5. Giảm mỡ, theo dõi bằng vòng eo.

> **Điều này đổi gì và không đổi gì.** Độ nét ở một khối lượng cơ cho trước vẫn gần như hoàn toàn là hàm của lớp mỡ — **đòn bẩy lớn nhất vẫn là giảm mỡ, không đổi**. Phần tập chỉ đổi ở một chỗ có thật: **cùng một mức mỡ, ngực và bụng dày hơn thì lộ rõ hơn**. Nên thay đổi là về **thứ tự ưu tiên khi phải cắt bớt**, không phải nhồi thêm volume — bạn đang ăn thâm hụt, thêm volume là thêm chi phí hồi phục.
>
> Các bài competition **không phục vụ mục tiêu thẩm mỹ** — chúng phục vụ kỹ năng và giữ sức mạnh, là một mục tiêu riêng. Vì vậy chúng **không bị đưa vào diện cắt**, kể cả khi thân dưới bị hạ ưu tiên thẩm mỹ.

**Tiêu chí thành công cuối tuần 12** — phải đạt cả ba, không chỉ nhìn số cân:

- Đường e1RM của Squat/Bench/Deadlift **đi ngang hoặc nhích 2–5%**. Trong thâm hụt, giữ nguyên e1RM đã là thành công.
- Vòng eo giảm dần đều. Đích dài hạn user nêu: từ ~20% xuống **~15% mỡ** ("nét vừa phải") — xem *Mục tiêu 15% mỡ* ở mục Dinh dưỡng. Đích này cần **12–16 tuần**, tức có thể vượt quá khối 12 tuần này.
- Logbook accessory: tăng reps hoặc tải ở cùng RIR so với tuần 1.
- **Riêng nhóm ưu tiên (ngực, bụng):** Machine Chest Press, Incline Bench, Cable Crunch và Hanging Knee Raise phải tăng reps hoặc tải. Nếu ba nhóm khác chững mà bốn bài này vẫn tiến, khối vẫn coi là thành công theo mục tiêu đã đặt.

**Tiêu chí chuyển phase:** xem bảng [roadmap](../roadmap.md). Quyết định nhánh 2a/2b/2c vào cuối tuần 12.

**Đối tượng và giới hạn:** nam 25 tuổi, 170 cm, 76 kg, trên 2 năm tập đều, nền powerlifting, không khai báo triệu chứng tại 2026-09-16. Chương trình này **không dành cho** người có triệu chứng mới, chấn thương đang hoạt động hoặc hạn chế sau mổ — các trường hợp đó đi qua knowledge phần 19 trước.

**Dữ liệu chưa biết — không giả vờ cá nhân hóa:**

- 1RM 170/130/200 là số user tự báo, **chưa rõ ngày đo và phương pháp**. Toàn bộ kg in trong ma trận suy ra từ ba số này, nên là **điểm khởi hành chứ không phải mệnh lệnh** — RPE thắng kg.
- Chưa có baseline vòng eo và cân trung bình 7 ngày. Tuần 1–2 là tuần thu thập baseline, **chưa diễn giải tốc độ giảm**.
- Chưa có dữ liệu giấc ngủ, stress, lịch làm việc thực tế. Đây là ba biến phải kiểm tra đầu tiên khi hiệu suất tụt (knowledge 17.7), trước khi đổi chương trình.
- Chưa có ước tính khối nạc. Protein tính theo **cân nặng**, không theo khối nạc (`protein_basis = body_weight`).

**Điểm vào: TUẦN 5, không phải tuần 1.** User đã chạy xong tuần 1–4 của chính ma trận này trước khi project được tạo (xác nhận 2026-09-16). Chạy lại từ tuần 1 là vứt bỏ 4 tuần tiến bộ. Khi kích hoạt, `effective_from` ứng với **tuần 5** của ma trận; tuần 1–4 coi như đã hoàn thành ngoài project và **không có log trong `logs/`** — đây là khoảng trống dữ liệu đã biết, không phải lỗi đồng bộ.

**Phản hồi thực tế đã được đưa vào thiết kế:** qua 4 tuần, user báo toàn bộ chương trình dung nạp được **trừ một chỗ** — tuần tăng BO Squat từ 2 lên 3 hiệp gây hết sức ngay từ bài đầu. Đã sửa: xem *Vì sao BO Squat bị chặn ở 2 hiệp*. Bench và Deadlift không đổi vì user xác nhận hai bài đó ổn.

**Nguồn kế thừa:** cấu trúc buổi, ma trận 12 tuần và quy tắc Top set/Back-off kế thừa từ plan "POWERBUILDING RECOMP 12 TUẦN" user đang chạy (user cung cấp 2026-09-16). Toolkit giữ nguyên phần đã dung nạp được và bổ sung: số dinh dưỡng cụ thể, buổi 5 riêng, abs 2 lần/tuần, nhịp check-in 7 ngày, bảng dự phòng, và các giới hạn ở mục Nguồn. Cấu trúc buổi được dựng lại 2026-09-16 khi user đổi sang khung sáng.

## ⚠ Bản điều chỉnh tạm thời — triệu chứng gối và lưng

| | |
|---|---|
| **Hiệu lực từ** | 2026-09-16 |
| **Đánh giá lại** | **2026-10-07** (3 tuần) |
| **Điều kiện trở lại** | Chỉ gỡ từng mục khi nhật ký cho thấy triệu chứng **về mức nền trong 24 giờ** ở nhiệm vụ đó, **liên tục 2 tuần**. **Không tự khôi phục vì hết ngày.** |
| **Nhật ký bắt buộc** | [logs/nhat-ky-trieu-chung.md](../logs/nhat-ky-trieu-chung.md) |

**Bối cảnh.** User khai bổ sung hai cụm triệu chứng ngày 2026-09-16 (xem [profile](../profile.md)). Sàng lọc dấu báo động knowledge 19.4: **âm tính cả hai cụm**. User **chưa đi khám được** và muốn tiếp tục tập.

**Giới hạn của bản này — đọc trước khi dùng.** Đây **không phải phác đồ phục hồi**. Knowledge 19.7: *vùng chưa được xác định tổn thương không được nhận protocol*. Toàn bộ mục dưới đây chỉ làm hai việc: **giảm những thứ user báo là gây triệu chứng**, và **thu thập dữ liệu theo nhiệm vụ**. Nó không điều trị gì cả, và nó **không thay được một buổi khám**.

### A. Lưng — giảm tải gập cột sống

User báo: **cong lưng dưới (gập) gây đau**; các tư thế thấy đỡ đều ở hướng ngược lại; ngồi làm việc lâu cũng gây triệu chứng.

| Bài | Bình thường | Trong 3 tuần này |
|---|---|---|
| **45° Back Extension** | Cue "cuộn nhẹ lưng trên để dồn glute" | **Bỏ cue cuộn.** Giữ cột sống trung tính toàn bộ tầm. Đây là hip hinge, không phải bài gập lưng |
| **ABS B1 — Hanging Knee Raise** | Cue "**cuộn xương chậu lên**" | **Bỏ phần cuộn chậu.** Chỉ gập hông tới ~90°, cột sống trung tính. Mất một phần kích thích rectus dưới — chấp nhận đánh đổi |
| **ABS A — Cable Crunch** | 3 × 10–15 | **Giữ nguyên.** User xác nhận cuộn abs **không** gây đau. Vẫn ghi nhật ký mỗi buổi |
| **Deadlift · Squat · RDL** | Theo ma trận | **Chạy bình thường theo ma trận** — đã sửa 2026-09-16, xem ghi chú dưới |

> **Đã sửa 2026-09-16 — tôi siết quá tay ở bản đầu.** Bản trước bắt dừng tăng Deadlift, hạ trần RPE Squat và đóng băng RDL. User phản hồi: **kỹ thuật ổn, không vòng lưng dưới; tải của hai bài đó lưng hoàn toàn ổn; và đi tập còn thấy đỡ đau hơn ở nhà.**
>
> Phản hồi đó đúng, và quan trọng hơn — nó khớp với chính knowledge. Mục 21.1 dẫn NICE NG59: **duy trì hoạt động**, chọn bài theo khả năng và nhu cầu; bước 3 của lộ trình ghi rõ **"giữ các vận động khác dung nạp được"**. Mục 19.7 cảnh báo không biến "nghỉ tương đối" thành nghỉ mọi thứ nhiều tuần. Deadlift và Squat, theo báo cáo của user, **là hoạt động dung nạp được** — nên cắt chúng là làm ngược hướng dẫn.
>
> **Thay bằng cơ chế đã có sẵn trong chương trình:** tiến độ chạy bình thường theo ma trận, **có điều kiện qua quy tắc 24 giờ**. Sáng hôm sau lưng về mức nền → tuần sau tiến tiếp theo ô ma trận. **Không về mức nền ở 2 buổi liên tiếp** → lúc đó mới giữ tải và xem lại. Đây là đúng logic mà chương trình vốn dùng cho RPE, chỉ thêm một biến đầu ra mới. Điều kiện duy nhất để nó hoạt động: **phải ghi nhật ký**.

**Tripwire, không phải chỉnh kỹ thuật.** User xác nhận kỹ thuật ổn và không vòng lưng, nên luật sau về nguyên tắc sẽ không bao giờ kích hoạt: rep nào lưng dưới bắt đầu tròn ra thì kết thúc hiệp ngay tại đó. Nó tồn tại cho **ngày tệ** — ngủ kém, ăn thiếu, tuần stress — chứ không phải vì nghi ngờ kỹ thuật.

**Ngoài phòng tập — nhiều khả năng là yếu tố lớn nhất.** User làm văn phòng và tự nhận thấy ngồi lâu gây triệu chứng. Ngồi chính là gập thắt lưng duy trì. **Đứng dậy đi lại 2–3 phút mỗi 30–45 phút.** Đây không phải lời khuyên chung chung — nó là biến tải lớn nhất trong ngày của user, lớn hơn bất cứ bài nào trong chương trình.

### B. Gối — giảm tích lũy trong buổi và bỏ tư thế gây triệu chứng

User báo: squat **không** đau, nhưng **các bài sau trong buổi** mới bó nhức → gợi ý tích lũy. Gập gối sâu kiểu chân sau kê bục/ghế gây căng bó.

| Bài | Bình thường | Trong 3 tuần này |
|---|---|---|
| **Leg Extension** (B1) | 2–3 × 12–15 | **TẠM DỪNG.** B1 hiện có 3 bài knee-dominant liên tiếp (Squat → Hack Squat → Leg Extension). Bỏ bài này còn 2. Đây cũng là bài rẻ nhất để cắt vì thẩm mỹ thân dưới đã bị hạ ưu tiên |
| **Walking Lunge** (B3) | 3–4 × 8–12 bước/chân | **Giảm tầm**: bước ngắn lại, gối sau **không hạ sâu**. Nếu vẫn bó → đổi sang Step-Up tầm thấp |
| **Bulgarian Split Squat** | Bài thay thế ưu tiên 2 | **Loại khỏi danh sách thay thế** trong 3 tuần — đúng tư thế user mô tả là gây triệu chứng |
| **Hack Squat** | 3–4 × 8–12 | Giữ, nhưng ghi nhật ký. Nếu triệu chứng xuất hiện ở bài này → lần sau giảm tầm trước, giảm tải sau |

**Một thử nghiệm có chủ đích: ngừng chủ động bẻ gối cho kêu "độp" trong 3 tuần.** User mô tả chu kỳ *tích tụ khó chịu → cố duỗi căng → kêu → đỡ*. Chưa biết việc bẻ khớp lặp lại đang giúp hay đang duy trì chu kỳ đó. Ba tuần không bẻ sẽ trả lời câu hỏi đó — và đó là dữ liệu hữu ích để mang đi khám. Nếu quá khó chịu thì cứ bẻ, **nhưng ghi lại ngày nào có bẻ**.

### C. Abs — tăng liều mà không tăng gập thắt lưng

Câu hỏi của user: 3 bài abs/tuần là thiếu. **Đúng là thiếu so với mục tiêu thẩm mỹ.** Nhưng cách bù không thể là nhân đôi bài gập cột sống khi lưng đang có triệu chứng chưa rõ nguyên nhân.

| Buổi | Trong 3 tuần này |
|---|---|
| **B2** | Cable Crunch 3 × 10–15 · **+ Cable Pallof Press 2 × 8–12/bên** *(thêm mới)* |
| **B5** | Hanging Knee Raise **trung tính** 3 × 10–20 · Cable Pallof Press 2 × 8–12/bên |

Từ 6 hiệp phì đại + 2 hiệp chống xoay → **6 + 4**. Tăng tiếp xúc, **không tăng một hiệp gập thắt lưng nào**. Khi lưng được đánh giá và ổn định, mới bàn tới việc lên 12 hiệp như [U14](../tai-nguyen/2026-09-16/U14-nippard-get-abs.md) kê.

### D. Mobility, giãn cơ và foam roller

User nêu rõ: khai triệu chứng ra là để **nhận bài phục hồi, giãn, foam roller** — không phải để bị cắt bài. Phần này trả lời đúng yêu cầu đó.

**Nguyên tắc bắt buộc trước khi đọc bảng (knowledge 22.3):** xác định **nhiệm vụ cần ROM nào** trước, rồi mới kê bài. Nếu ROM đã đủ cho nhiệm vụ và không khó chịu thì **không tự thêm 20 phút corrective**. Và 22.7: không bắt mọi buổi phải đủ ba bước foam rolling + stretch + activation.

#### Foam roller — 8–10 phút, **sau buổi tập** hoặc ở buổi 5

| Vùng | Liều | Căn cứ |
|---|---|---|
| **Đùi trước (quad)** | 60–90 giây/bên | Meta-analysis ghi foam rolling **có** tăng ROM khi áp lên hamstring và quadriceps. Chương trình có nhiều bài quad |
| **Đùi sau (hamstring)** | 60–90 giây/bên | Như trên |
| **Mông và hông ngoài** | 60–90 giây/bên | User mô tả triệu chứng "như mỏi cơ mông" |
| **Cột sống ngực** | 8–10 lượt lăn chậm, có thể ưỡn nhẹ qua con lăn | Đối kháng tư thế ngồi cả ngày. Nằm **xa vùng thắt lưng đang có triệu chứng**. Cũng phục vụ trực tiếp wall angel và setup bench |
| **Thắt lưng** | **KHÔNG lăn** | Vùng đang có triệu chứng **chưa được đánh giá**. Không tự ép mô ở vùng chưa biết đang bị gì |
| **Bắp chân — nếu mục tiêu là cải thiện knee-to-wall** | **Không dùng cho mục tiêu này** | Cùng meta-analysis: lăn triceps surae **không** cải thiện dorsiflexion cổ chân. Dùng goblet squat mobilization mà chương trình đã có |

**Kỳ vọng đúng:** cùng meta-analysis ghi hiệu quả ROM **rõ hơn ở các can thiệp kéo dài trên 4 tuần** so với từ 4 tuần trở xuống. Nghĩa là foam rolling là **thói quen tích lũy**, không phải liều chữa cháy trước buổi tập. Nó cũng **không** thay đổi cấu trúc mô — nó đổi cảm giác và ROM tạm thời.

#### Giãn tĩnh — liều theo thời điểm

| Khi nào | Liều | Vì sao |
|---|---|---|
| **Trước buổi nặng** | **Dưới 60 giây/nhóm cơ** | Review của Behm 2016: phân nhóm giãn tĩnh **≥60 giây/nhóm cơ giảm hiệu suất nhiều hơn** nhóm dưới 60 giây. Đây không phải ranh giới tuyệt đối, nhưng đủ để chọn phía an toàn trước buổi Squat/Deadlift |
| **Sau buổi, hoặc ngày riêng** | Thoải mái 60 giây trở lên | Không còn buổi nặng phía sau để bị ảnh hưởng |

#### Chống lại việc ngồi — hằng ngày, kể cả ngày không tập

Đây nhiều khả năng là phần có tác động lớn nhất tới thứ đang làm phiền sinh hoạt của user.

- **Đứng dậy đi lại 2–3 phút mỗi 30–45 phút.** Ngồi là gập thắt lưng duy trì — đúng hướng user báo là gây triệu chứng.
- **Thoracic extension qua foam roller**, 1–2 lượt trong ngày làm việc.
- **Các tư thế user tự thấy dễ chịu** (nằm ngửa xoay hai chân vào trong; nằm kê thân trên thả hông và chân xuống) — dùng được khi thấy cần. Ghi vào nhật ký như **quan sát cá nhân**, không phải bài được kê theo chẩn đoán.

#### Luật test–retest — áp cho **mọi** mục ở trên

Knowledge 22.3: cải thiện tức thời sau warm-up là **dữ liệu về đáp ứng**, không chứng minh nguyên nhân đau và không sửa được cấu trúc.

1. Làm bodyweight squat 3 rep (hoặc knee-to-wall / wall angel tùy vùng) — ghi cảm giác
2. Làm bài mobility
3. Test lại **ngay**
4. **Không cải thiện → bỏ bài đó.** Đừng làm tiếp chỉ vì nó phổ biến

#### Buổi 5 vẫn không phải rehab

Tôi **không kê bộ bài phục hồi cho gối hay lưng**, vì chưa có đánh giá và knowledge 19.7 cấm áp protocol cho vùng chưa xác định tổn thương. Bảng trên là **mobility chung cho người ngồi văn phòng nhiều** cộng phần tránh vùng đang có triệu chứng — khác hẳn một phác đồ nhắm vào một chẩn đoán.

Buổi 5 giữ: ba phép thử mỗi tuần một lần (ghi kết quả) · zone 2 đi bộ 20–30 phút · foam roller theo bảng trên.

### E. Theo dõi chức năng sinh hoạt

User nói rõ vấn đề nằm ở **sinh hoạt hàng ngày**, không ở việc tập. Nên thước đo của bản điều chỉnh này là ba chức năng đó, không phải con số tạ:

**F1** phút ngồi liên tục trước khi lưng khó chịu · **F2** xuống cầu thang (0–10) · **F3** số lần/ngày cần bẻ gối cho kêu.

Bảng ghi và cách tiến từng bước nằm ở [nhật ký triệu chứng](../logs/nhat-ky-trieu-chung.md). **Tuần đầu là tuần đo baseline**, không phải tuần cải thiện.

### H. Khi nào phải dừng và đi khám — không chờ hết 3 tuần

Toàn bộ danh sách ở [nhật ký triệu chứng](../logs/nhat-ky-trieu-chung.md). Tóm tắt: gối kẹt cứng hoặc khuỵu · sưng/nóng/đỏ · tê, yếu mới, đau lan xuống chân · rối loạn tiểu-đại tiện hoặc tê vùng yên ngựa **(cấp cứu ngay)** · đau tăng dần 2 tuần liên tiếp dù đã giảm tải · sáng hôm sau không về mức nền ở 3 buổi liên tiếp.

**Ngay cả khi mọi thứ đỡ hơn:** lưng đang ở xu hướng **nặng dần so với trước** theo chính nhận xét của user, và cụm gối đã kéo dài vượt xa mốc 6 tuần mà [NHS](https://www.nhs.uk/symptoms/knee-pain/) nêu là khoảng thời gian đa số vấn đề gối tự dịu. Ba tuần này là **để có dữ liệu mang đi khám**, không phải để thay thế việc đi khám.

## Lịch hiện hành

**Vì sao 5 buổi, và vì sao buổi 5 ngắn** (cấu trúc lại 2026-09-16 sau khi user đổi sang khung sáng):

Khung sáng 6h00–7h30 có trần **cứng** 90 phút, không co giãn như khung chiều cũ. Ở cấu trúc 4 buổi, buổi 2 và buổi 4 chạm 77–84 phút — chỉ còn 6–13 phút đệm. Những bài nằm cuối hai buổi đó (lateral raise, facepull, curl, tricep) là nhóm bị cắt đầu tiên mỗi khi trễ giờ. Tức là chúng có mặt trên giấy nhưng không có mặt trong thực tế.

Tách buổi 5 giải quyết đúng chỗ đó: **tổng volume tuần gần như không đổi, chỉ trải ra**. Bốn buổi chính xuống 70–76 phút (đệm 14–20 phút), và những bài hay bị cắt được đưa vào một buổi riêng, ngắn, không có compound nặng.

**Buổi 5 không phải buổi volume thứ 5.** Nó không thêm bài compound và không tăng tổng tải. Trong lúc ăn thâm hụt, khả năng hồi phục mới là biến giới hạn chứ không phải thời gian rảnh — nên nếu tuần đó mệt thì bỏ hẳn buổi 5, bốn buổi chính vẫn đủ liều.

**Vì sao upper/lower luân phiên:** mỗi lift thi đấu có đúng 1 buổi nặng cộng khoảng 72 giờ hồi phục, và mọi nhóm cơ đạt 2 lần/tuần — kiểm tra đầy đủ ở bảng *Kiểm tra tần suất* cuối mục này. Deadlift luôn xếp sau ngày nghỉ.

**Thứ tự buổi:** Buổi 1 – Buổi 2 – nghỉ – Buổi 3 – Buổi 4 – Buổi 5 – nghỉ.

Ví dụ: **T2** Lower A · **T3** Upper A · **T4** nghỉ · **T5** Lower B · **T6** Upper B · **T7** Vai/Tay/Abs · **CN** nghỉ.

Cách xếp này đặt hai buổi abs cách nhau 4 ngày rồi 3 ngày (T3 và T7) — đều, không dồn cục. Deadlift ở T5 rơi ngay sau ngày nghỉ T4. Vỡ lịch thì **giữ đúng thứ tự buổi**, không giữ đúng thứ trong tuần.

**Cửa sổ thời gian: 6h00–7h30 buổi sáng — trần cứng 90 phút** (user đổi từ buổi chiều sang buổi sáng, 2026-09-16). Cột "Thời gian" là ước tính đã gồm warm-up, nghỉ giữa hiệp và setup. Xem mục *Tập buổi sáng* để biết điều chỉnh bắt buộc đi kèm.

> **Về cột link (L1 — đã gỡ 2026-09-16).** Cả 25 bài chính đều có link MuscleWiki đã tra, ghi kèm ngày kiểm tra và ghi chú biến thể ở [exercise-links.md](../exercise-links.md).
>
> Hai điều cần biết khi mở link: (1) xác minh là **gián tiếp** — musclewiki.com chặn fetch trực tiếp (HTTP 403), nên URL và tiêu đề lấy từ chỉ mục tìm kiếm, chưa đối chiếu video bằng mắt; (2) ba bài **lệch biến thể** — Leg Extension (program yêu cầu ngả lưng ghế), Cable Lateral Raise (program yêu cầu cáp ngang tầm tay), Wide-Grip Cable Row (program yêu cầu grip rộng). Ở ba bài đó, **cue trong bảng này thắng nội dung trang link**.

### Buổi 1 — Lower A (Squat + quad/đùi sau) · ~72 phút

| Buổi | Bài tập và link | Mục đích | Sets × reps | Load/effort | Nghỉ | ROM/tempo/cue | Thời gian |
|---|---|---|---|---|---|---|---|
| 1 | Warm-up Lower (mục Khởi động) | Tăng nhiệt, mobilize, ramp-up | — | RPE ≤4 | — | Knee-to-wall, 90/90, glute bridge | 12 phút |
| 1 | **Competition Squat — Top set** — [MuscleWiki](https://musclewiki.com/exercise/barbell-low-bar-squat) | Kỹ năng lift thi đấu + dung nạp tải nặng | 1 × 6 (tuần 1) | @130 kg • **RPE 7** • trần 8,5 • sàn 4 rep | 3–4 phút | Bracing 360° trước khi hạ | 14 phút |
| 1 | **Competition Squat — Back-off** | Volume quad/glute trong cùng bài | **2 × 8 — trần 2 hiệp cả khối** | = Top −10% (@120 kg) • hiệp cuối RIR 2–3 | **3 phút** | Cùng tải mọi hiệp. Muốn 3 hiệp thì phải hạ xuống Top −15% | 8 phút |
| 1 | **Romanian Deadlift** — [MuscleWiki](https://musclewiki.com/exercise/barbell-romanian-deadlift) | Trụ volume hip hinge | 3 × 8 | RIR 3 • gợi ý 100–110 kg | 2–3 phút | Hạ 2–3 giây; hinge, không squat xuống | 12 phút |
| 1 | **Hack Squat** — [MuscleWiki](https://musclewiki.com/exercise/machine-hack-squat) | Quad-biased — **gánh phần volume cắt khỏi BO Squat** | 3 × 8 | RIR 3 | 2–3 phút | Xuống sâu trong tầm kiểm soát | 12 phút |
| 1 | **Leg Extension** (ngả lưng ghế) — [MuscleWiki](https://musclewiki.com/exercise/machine-leg-extension) | Rectus femoris, hông duỗi | 2 × 12 | RIR 2 | 90–120 giây | Ngả lưng ghế để cố định hông | 7 phút |
| 1 | **Calf Raise** — [MuscleWiki](https://musclewiki.com/exercise/machine-standing-calf-raises) | Bắp chân lần 1/tuần | 2 × 12 | RIR 2 | 90–120 giây | Dừng 1 giây ở đáy stretch | 6 phút |

### Buổi 2 — Upper A (ngực/lưng + tay sau + abs) · ~76 phút

| Buổi | Bài tập và link | Mục đích | Sets × reps | Load/effort | Nghỉ | ROM/tempo/cue | Thời gian |
|---|---|---|---|---|---|---|---|
| 2 | Warm-up Upper | T-spine, bả vai, ramp-up | — | RPE ≤4 | — | Band pull-apart, scap push-up | 10 phút |
| 2 | **Competition Bench — Top set** — [MuscleWiki](https://musclewiki.com/exercise/barbell-bench-press) | Kỹ năng lift thi đấu | 1 × 6 (tuần 1) | @97,5 kg • **RPE 7** • trần 8,5 • sàn 4 rep | 3–4 phút | Leg drive là cơ chế **neo bả vai**, lực đi ngang | 14 phút |
| 2 | **Competition Bench — Back-off** | Volume ngực/tay sau | 2 → 4 × 8 theo ma trận | = Top −10% (@87,5 kg) • hiệp cuối RIR 2–3 | 2–3 phút | **Không đổi** — user xác nhận bài này dung nạp tốt qua tuần 4 | 10 phút |
| 2 | **Chest-Supported Row** — [MuscleWiki](https://musclewiki.com/exercise/machine-chest-supported-t-bar-row) | Lưng giữa lần 1/tuần; cho ngực nghỉ trước bài kế | 3 × 8 | RIR 3 | 2–3 phút | Ngực tì đệm, không giật thân | 11 phút |
| 2 | **Machine Chest Press** — [MuscleWiki](https://musclewiki.com/exercise/machine-chest-press) | Ngực — nhóm ưu tiên | 3 × 8 | RIR 3 | 2–3 phút | Deep stretch, hạ 2–3 giây | 11 phút |
| 2 | **Cable Lateral Raise** — [MuscleWiki](https://musclewiki.com/exercise/cable-low-bilateral-lateral-raise) | Vai bên lần 1/tuần — nhóm ưu tiên | 2 × 12 | RIR 2 | 90–120 giây | Không vung | 7 phút |
| 2 | **Overhead Cable Triceps Ext** — [MuscleWiki](https://musclewiki.com/exercise/cable-rope-overhead-tricep-extension) | Tay sau lần 1/tuần, long head | 2 × 12 | RIR 2 | 90 giây | Tay qua đầu, stretch tối đa | 6 phút |
| 2 | **ABS A — Cable Crunch** — [MuscleWiki](https://musclewiki.com/exercise/cable-row-bar-kneeling-crunch) | **Gập cột sống** — rectus abdominis, phì đại có tải | 3 × 10–15 | **Có tải • RIR 1–2** | 90 giây | Cuộn xương sườn về phía xương chậu. **Hông không di chuyển.** Cho cột sống duỗi nhẹ ở đầu rep | 7 phút |

### Buổi 3 — Lower B (Deadlift + glute/đùi sau) · ~70 phút

| Buổi | Bài tập và link | Mục đích | Sets × reps | Load/effort | Nghỉ | ROM/tempo/cue | Thời gian |
|---|---|---|---|---|---|---|---|
| 3 | Warm-up Lower | Hông, cổ chân, bracing | — | RPE ≤4 | — | Test-retest nếu có vùng cứng | 12 phút |
| 3 | **Competition Deadlift — Top set** — [MuscleWiki](https://musclewiki.com/exercise/barbell-deadlift) | Kỹ năng lift; xếp sau ngày nghỉ | 1 × 5 (tuần 1) | @155 kg • **RPE 7** • trần 8,5 • **sàn 3 rep** | 3–4 phút | Thanh sát cẳng chân — mỗi cm rời xa đều tăng cánh tay đòn lên thắt lưng | 13 phút |
| 3 | **Competition Deadlift — Back-off** | Giữ groove, nuôi erector | 2 × 5 | = Top −10% (@135 kg) • hiệp cuối **RIR 3–4** | 2–3 phút | **Không đổi** — cố ý để nhẹ | 7 phút |
| 3 | **Walking Lunge** — [MuscleWiki](https://musclewiki.com/exercise/lunge-walking) | Glute + quad lần 2/tuần | 3 × 8 (bước/chân) | RIR 2–3 | 2–3 phút | Bước dài, nghiêng thân ~30° | 12 phút |
| 3 | **Seated / Lying Leg Curl** — [MuscleWiki](https://musclewiki.com/exercise/seated-leg-curl) | Hamstring ở nhiệm vụ gập gối | 2 × 12 | RIR 2 | 90–120 giây | Không hất mông khỏi đệm | 7 phút |
| 3 | **Machine Hip Thrust** — [MuscleWiki](https://musclewiki.com/exercise/machine/male/glutes/machine-hip-thrust) | Glute — nhóm ưu tiên | 2 × 10 | RIR 2–3 | 90–120 giây | Cằm thu, xương sườn xuống | 8 phút |
| 3 | **45° Back Extension** — [MuscleWiki](https://musclewiki.com/exercise/machine-45-degree-back-extension) | Glute + erectors | 2 × 12 | RIR 2 | 90 giây | Cuộn nhẹ lưng trên để dồn glute | 7 phút |
| 3 | **Calf Raise** (lần 2/tuần) — [MuscleWiki](https://musclewiki.com/exercise/machine-standing-calf-raises) | Bắp chân | 2 × 12 | RIR 2 | 90 giây | Bỏ trước nếu thiếu giờ | 6 phút |

### Buổi 4 — Upper B (đẩy dọc/lưng + tay trước) · ~70 phút

**Bài 1 giữ Incline Bench Press cả 12 tuần** (sửa 2026-09-16). Trước đây bài này luân phiên sang Machine Shoulder Press ở Meso 2, làm ngực rơi xuống 1 lần/tuần từ tuần 7 — không chấp nhận được khi ngực là nhóm ưu tiên thẩm mỹ số 1. Machine Shoulder Press **chuyển sang buổi 5** trong Meso 2.

| Buổi | Bài tập và link | Mục đích | Sets × reps | Load/effort | Nghỉ | ROM/tempo/cue | Thời gian |
|---|---|---|---|---|---|---|---|
| 4 | Warm-up Upper | T-spine, bả vai | — | RPE ≤4 | — | — | 10 phút |
| 4 | *Tùy chọn:* **Bench kỹ thuật** — [MuscleWiki](https://musclewiki.com/exercise/barbell-bench-press) | Giữ groove — Bench chỉ 1 buổi nặng/tuần | 3 × 3 | @90 kg • **RPE ≤6** | 2 phút | Không tính volume; bỏ ở tuần deload | 8 phút |
| 4 | **Incline Bench Press** — [MuscleWiki](https://musclewiki.com/exercise/barbell-incline-bench-press) | **Ngực trên — ưu tiên thẩm mỹ số 1.** Giữ cả 12 tuần | 3 × 8 | RIR 3 • gợi ý 75–80 kg | 2–3 phút | Không đổi bài giữa khối | 12 phút |
| 4 | **Wide-Grip Lat Pulldown** — [MuscleWiki](https://musclewiki.com/exercise/cable-lat-pulldown) | Kéo dọc, độ rộng lưng | 3 × 8 | RIR 3 | 2–3 phút | Kéo khuỷu xuống, stretch ở đỉnh | 11 phút |
| 4 | **Wide-Grip Cable Row** — [MuscleWiki](https://musclewiki.com/exercise/machine-seated-cable-row) | Mid traps / midback | 3 × 8 | RIR 3 | 2–3 phút | Siết bả vai ở cuối | 11 phút |
| 4 | **Reverse Cable Crossover** — [MuscleWiki](https://musclewiki.com/exercise/cable-high-reverse-fly) | Vai sau lần 1/tuần | 2 × 12 | RIR 2 | 90 giây | Giữ khuỷu gần thẳng | 7 phút |
| 4 | **EZ Bar Curl** — [MuscleWiki](https://musclewiki.com/exercise/ez-bar-curl) | Tay trước lần 1/tuần, mid-range | 2 × 12 | RIR 2 | 90 giây | Grip ngoài đỡ cổ tay | 6 phút |

### Buổi 5 — Vai / Tay / Abs · **bản chạy sẵn**

Buổi ngắn nhất, **rẻ nhất về mệt mỏi toàn thân** — không compound nặng, không cần bracing. Đây là chỗ chứa những bài vốn nằm cuối buổi 2 và 4, tức đúng những bài bị cắt đầu tiên khi thiếu giờ.

**Làm theo đúng thứ tự dưới đây, không phải chọn.** Tổng: **~57 phút** (Meso 1) · **~69 phút** (Meso 2).

#### Bước 0 — Ba phép thử · 3 phút · **chỉ 1 lần/tuần**

Làm khi còn tươi, trước warm-up, để số liệu so sánh được giữa các tuần. Ghi vào [nhật ký](../logs/nhat-ky-trieu-chung.md).

| Phép thử | Ghi gì |
|---|---|
| **Knee-to-wall** | Khoảng cách mũi chân tới tường khi gót vẫn chạm sàn — **cm, từng bên** |
| **Wall Angel** | Giữ được tiếp xúc lưng/mông/đầu/mu bàn tay khi tay lên quá đầu — **có / không** |
| **Bodyweight Squat 3 rep** | Cảm giác và độ sâu — **1 câu** |

Thứ đáng theo dõi là **thay đổi của chính bạn theo tuần** và **chênh lệch hai bên**, không phải một ngưỡng chuẩn nào.

#### Bước 1 — Warm-up · 6 phút

| Nội dung | Liều |
|---|---|
| Xe đạp hoặc đi bộ dốc | 3 phút, RPE 3 |
| [Band Pull Apart](https://musclewiki.com/exercise/band-pull-apart) | 2 × 15 |
| Xoay vai ngoài với dây, tay áp thân | 2 × 12/bên |

#### Bước 2 — Khối tạ nhẹ · 31 phút (Meso 1) / 43 phút (Meso 2)

| # | Bài | Hiệp × rep | Effort | Nghỉ | Cue |
|---|---|---|---|---|---|
| **2.0** | *Chỉ tuần 7–11:* [Machine Shoulder Press](https://musclewiki.com/exercise/machine-overhand-overhead-press) | 3 → 4 × 8–12 | RIR 2–3 | 2–3 phút | Ép lưng vào đệm, đẩy tới gần duỗi khuỷu, không khóa cứng |
| **2.1** | [Cable Lateral Raise](https://musclewiki.com/exercise/cable-low-bilateral-lateral-raise) — lần 2/tuần | 2 → 4 × 12–15 | RIR 2 | 90 giây | Nâng tới ngang vai, **không vung thân**. Vai bên là nhóm ưu tiên |
| **2.2** | [Rope Facepull](https://musclewiki.com/exercise/machine-face-pulls) | 2 → 4 × 12–15 | RIR 2 | 90 giây | Quét rope ra hai bên đầu, **không giật**. Khuỷu cao ngang vai |
| **2.3** | [Bar Pressdown](https://musclewiki.com/exercise/cable-bar-pushdown) | 2 → 3 × 12–15 | RIR 2 | 90 giây | "T-Rex arms" — khuỷu **dán sát thân**. Vai cuộn ra trước = tải quá nặng |
| **2.4** | [Incline Dumbbell Curl](https://musclewiki.com/exercise/dumbbell-incline-curl) | 2 → 4 × 12–15 | RIR 2 | 90 giây | Ghế 45–60°, tay **buông thõng ra sau thân**, không đưa khuỷu ra trước |

Số hiệp chính xác của từng tuần đọc ở [ma trận buổi 5](#buổi-5--vai--tay--abs). Tuần đầu tập bài nào thì **tự chọn tải đạt đúng rep ở RIR quy định rồi ghi logbook**.

#### Bước 3 — Abs · 14 phút

| # | Bài | Hiệp × rep | Effort | Nghỉ | Cue |
|---|---|---|---|---|---|
| **3.1** | [Hanging Knee Raise](https://musclewiki.com/exercise/hanging-knee-raises) | 3 × 10–20 | RIR 1–2 | 90 giây | **Bản điều chỉnh tạm thời: KHÔNG cuộn xương chậu.** Chỉ gập hông tới ~90°, cột sống trung tính. Chậm, **không lấy đà**. Đạt 3×20 mới kẹp tạ giữa chân |
| **3.2** | [Cable Pallof Press](https://musclewiki.com/exercise/cables/male/obliques/cable-pallof-press) | 2 × 8–12/bên | RIR 2 | 60 giây | Cáp ngang ngực, đứng nghiêng, đẩy tay thẳng ra trước và **chống lại lực xoay**. Đẳng trường — thân không xoay theo |

Chưa treo xà được hoặc grip là điểm giới hạn → [Reverse Crunch](https://musclewiki.com/bodyweight/male/abdominals/reverse-crunch), cùng hiệp × rep.

#### Bước 4 — Foam roller · 9 phút · **sau khi tập xong**

| Vùng | Liều |
|---|---|
| Đùi trước | 60–90 giây/bên |
| Đùi sau | 60–90 giây/bên |
| Mông và hông ngoài | 60–90 giây/bên |
| Cột sống ngực | 8–10 lượt chậm, ưỡn nhẹ qua con lăn |
| **Thắt lưng** | **Không lăn** — vùng đang có triệu chứng chưa được đánh giá |

Sau khi lăn quad và mông, **test lại bodyweight squat 3 rep**. Không cải thiện → tuần sau bỏ phần đó, đừng lăn tiếp vì nó phổ biến.

#### Bước 5 — Zone 2 · **tách ra khỏi buổi tập**

**Không** làm ở phòng gym sau buổi 5. Chuyển thành **đi bộ 20–30 phút giờ nghỉ trưa hoặc buổi tối**, RPE 3–4 (nói thành câu được).

Hai lý do: giữ buổi 5 dưới 70 phút kể cả ở Meso 2; và đi bộ giữa ngày làm việc **đánh trúng vấn đề ngồi lâu** — thứ bạn tự nhận thấy gây triệu chứng lưng.

#### Bản rút gọn — khi chỉ còn 25–30 phút

Bỏ theo đúng thứ tự này: **Bước 5 → Bước 0 → 2.3 → 2.4 → Bước 4**.

Giữ lại bằng mọi giá: **2.1 Cable Lateral Raise** (vai là nhóm ưu tiên, và đây là lần thứ 2 duy nhất trong tuần) · **2.2 Rope Facepull** (vai sau lần 2) · **Bước 3 Abs** (bụng là ưu tiên thẩm mỹ, và đây cũng là lần thứ 2 duy nhất).

**Mệt, ngủ kém, hoặc DOMS chưa hết → bỏ hẳn buổi 5.** Bốn buổi chính vẫn mang đủ liều cho ngực, lưng và bụng. Bỏ buổi 5 **không tạo "nợ"** phải bù.

### Kiểm tra tần suất — mọi nhóm cơ 2 lần/tuần

| Nhóm cơ | Lần 1 | Lần 2 |
|---|---|---|
| Quad | B1 Squat + Hack + Leg Extension | B3 Walking Lunge |
| Hamstring | B1 Romanian Deadlift | B3 Leg Curl |
| Glute | B1 Squat + RDL | B3 Hip Thrust + Back Extension |
| Bắp chân | B1 | B3 |
| **Ngực** ← ưu tiên #1 | B2 Bench + Machine Chest Press | B4 Incline Bench **(cả 12 tuần)** |
| Lưng | B2 Chest-Supported Row | B4 Pulldown + Cable Row |
| **Vai bên** | B2 Cable Lateral Raise | **B5** Cable Lateral Raise |
| **Vai sau** | B4 Reverse Cable Crossover | **B5** Rope Facepull |
| Tay sau | B2 Overhead Cable Extension | **B5** Bar Pressdown |
| Tay trước | B4 EZ Bar Curl | **B5** Incline DB Curl |
| **Abs** ← ưu tiên #1 | **B2** Cable Crunch *(gập cột sống)* | **B5** Hanging Knee Raise *(gập hông)* |
| Vai trước / đẩy dọc | B2 + B4 (gián tiếp qua đẩy ngang) | **B5** Machine Shoulder Press *(chỉ Meso 2)* |

**Lỗ hổng ngực ở Meso 2 — đã vá 2026-09-16.** Bản trước cho bài 1 của buổi 4 đổi sang Machine Shoulder Press từ tuần 7, khiến ngực rơi xuống 1 lần/tuần đúng nửa sau của khối. Khi ngực là ưu tiên thẩm mỹ số 1 thì đó là lỗi không chấp nhận được. Cách vá: **Incline ở lại buổi 4 cả 12 tuần**, Machine Shoulder Press chuyển sang buổi 5 trong Meso 2. Tổng volume không tăng — chỉ đổi chỗ.

### Thứ tự cắt khi thiếu giờ hoặc thiếu hồi phục

Luật cũ "cắt bài cuối buổi" là luật chung. Với ưu tiên hiện tại, dùng thứ tự này thay thế:

| Cắt trước | Nội dung |
|---|---|
| 1 | **Calf Raise** (lần 2 ở B3), **Leg Extension** — phụ trợ thân dưới, thẩm mỹ thân dưới không phải mục tiêu |
| 2 | **45° Back Extension**, **Machine Hip Thrust** — giữ lại nếu còn giờ, nhưng cắt trước phần thân trên |
| 3 | **Walking Lunge** (giảm còn 2 hiệp trước khi bỏ hẳn) |
| 4 | Bài cuối của buổi upper |
| **Không bao giờ cắt** | **Top set + Back-off của Squat/Bench/Deadlift** — đây là phần giữ kỹ thuật và sức mạnh, user nêu rõ là bắt buộc giữ · **Machine Chest Press và Incline** — ưu tiên thẩm mỹ số 1 · **ABS A và ABS B** |

Lưu ý: thân dưới bị hạ ưu tiên **thẩm mỹ**, không bị hạ ưu tiên **sức mạnh**. Squat và Deadlift ở nguyên vị trí bài 1 của buổi 1 và buổi 3, ramp-up đầy đủ, tập khi sung sức nhất.

### Luật riêng cho abs

Abs tuân theo đúng luật double progression của bài cô lập, **không phải** kiểu tập đến rát.

- **Phải có tải.** Cable crunch có tải, hanging knee raise kẹp tạ khi bodyweight đã quá dễ. Bài không tăng tải được thì không có đường tăng tiến.
- **Buổi abs đầu tiên:** tự chọn tải đạt đúng rep ở RIR quy định rồi **ghi vào logbook** — giống luật bài máy. Vì abs là bài mới thêm từ tuần 5, cột này bắt đầu từ baseline riêng chứ không nhảy vào giữa ma trận.
- **Tăng tiến — hai bài khác dải rep:**
  - **ABS A (Cable Crunch, có tải sẵn):** đạt 15 rep cả 3 hiệp ở RIR 1–2 trong **hai buổi liên tiếp** → tăng một bậc tải nhỏ nhất, quay về 10 rep.
  - **ABS B (Hanging Knee Raise, bodyweight):** kéo dài dải rep **10 → 20** trước, chỉ thêm tải (kẹp tạ giữa chân) sau khi đạt 3×20. Lý do: thêm tải sớm khi kỹ thuật cuộn chậu chưa vững sẽ biến bài thành động tác hip flexor.
- **Không tập tới failure ở abs.** [U14](../tai-nguyen/2026-09-16/U14-nippard-get-abs.md) yêu cầu set cuối tới failure; chương trình này **giữ RIR 1–2** vì knowledge 17.2 (ACSM 2026) ghi rõ failure không bắt buộc và chưa đủ bằng chứng để ấn định một RIR tối ưu cho mọi người — thêm nữa bạn đang ăn thâm hụt, nơi chi phí hồi phục của failure cao hơn.
- Phải rút ROM hoặc lấy đà mới đủ rep → **chưa đạt điều kiện tăng**.
- **Không tập oblique nặng có tải** (side bend cầm tạ nặng). Cơ liên sườn dày lên có thể làm rộng phần eo — ngược mục tiêu của bạn. Pallof press an toàn vì là bài đẳng trường chống xoay.

## Khởi động (5–10 phút + ramp-up)

1. **Tăng nhiệt:** 3–5 phút xe đạp / đi bộ nhanh / nhảy dây nhẹ.
2. **Mobilize — chỉ vùng thật sự hạn chế**, quyết định bằng ba phép thử dưới, và test-retest ngay sau:
   - Buổi Lower: cổ chân knee-to-wall; hông 90/90 hoặc deep squat hold 30–45 giây.
   - Buổi Upper: T-spine với peanut/foam roller; giãn lat/pec dưới 30 giây nếu bó cứng.
3. **Activate:** Lower — glute bridge 2×10 hoặc lateral band walk 1–2 vòng. Upper — band pull-apart 2×15, scap push-up 1×10.
4. **Ramp-up bài đầu buổi (SBD):** đòn ×10 → 45% Top ×5 → 65% ×3 → 80% ×2 → 90% ×1 → vào Top set.
   *Ví dụ Squat tuần 1 (Top 130):* 20×8 → 70×5 → 95×3 → 115×1 → 130×6.
   Giữ ramp-up gọn — mỗi rep thừa trước Top set là một rep bị lấy khỏi back-off. Bài 2 trở đi: 1–2 hiệp dẫn nhẹ là đủ.

### Ba phép thử nhanh (≤3 phút, làm ở khởi động)

| Phép thử | Cách làm | Đạt khi | Nếu không đạt |
|---|---|---|---|
| Knee-to-wall | Mũi chân cách tường ~12–13 cm, gối đẩy thẳng chạm tường, gót **không nhấc** | Chạm được cả hai bên và cân nhau | Goblet squat mobilization 30–45 giây/bên, rồi test lại |
| Wall Angel | Áp lưng, mông, đầu và mu bàn tay vào tường, trượt tay lên xuống | Giữ tiếp xúc khi tay lên quá đầu | Peanut dọc hai bên cột sống ngực + prayer stretch, rồi test lại |
| Bodyweight Squat (test-retest) | Squat tay không 3 rep, trước và ngay sau bài mobility | Cảm giác/độ sâu cải thiện rõ | **Bỏ bài mobility đó.** Chuyển sang exposure dần với tải nhẹ |

Không coi một ngưỡng duy nhất là chuẩn cho mọi cơ thể. Thứ đáng theo dõi là **sự thay đổi của chính bạn theo tuần** và chênh lệch giữa hai bên.

## Tập buổi sáng 6h00–7h30

User chuyển sang khung sáng từ 2026-09-16. Trần 90 phút là **cứng**, không co giãn như khung chiều cũ.

**Thời lượng có vừa không:** vừa, nhưng buổi 2 và buổi 4 không còn đệm.

| Buổi | Ước tính | Đệm còn lại trong 90 phút |
|---|---|---|
| 1 — Lower A | ~72 phút | ~18 phút |
| 2 — Upper A | ~76 phút | ~14 phút |
| 3 — Lower B | ~70 phút | ~20 phút |
| 4 — Upper B | ~70 phút | ~20 phút |
| 5 — Vai/Tay/Abs | ~52 phút (+25 nếu làm cardio) | ~38 phút |

Sau khi tách buổi 5, mọi buổi đều còn ít nhất 14 phút đệm trong trần 90 phút — trước khi tính phần tiết kiệm được nhờ gym vắng, không phải đợi máy. Nếu một hôm vẫn vượt giờ: cắt bài **cuối** buổi, không cắt Top set/BO.

**Khởi động phải dài hơn khung chiều.** Sáng sớm thân nhiệt thấp và cột sống vừa qua một đêm nằm.

- Tăng nhiệt **8–10 phút** thay vì 3–5.
- Thêm **một bước** vào ramp-up SBD: đòn ×10 → 40% ×5 → 55% ×5 → 70% ×3 → 82% ×2 → 90% ×1 → Top set.
- Ba phép thử ở mục Khởi động càng đáng làm hơn vào buổi sáng, đặc biệt knee-to-wall trước buổi Lower.

**Hai tuần đầu sau khi đổi giờ: hạ trần RPE Top set đi 0,5** (ô ghi RPE 7 → tập ở 6,5; ô ghi RPE 8 → 7,5) và **không chạy theo kg in trong ma trận**. Đổi giờ tập là một biến số mới. Nếu vừa đổi giờ vừa ép kg thì khi hiệu suất tụt sẽ không biết nguyên nhân là giờ giấc, giấc ngủ hay tải — knowledge 18.9: không đổi nhiều biến cùng lúc khi mục tiêu là xác định nguyên nhân.

**Ăn trước tập.** Bắt đầu 6h00 nên không còn chỗ cho bữa lớn.

| Buổi | Phương án khuyến nghị | Nội dung |
|---|---|---|
| 1 và 3 (Squat / Deadlift) | **Có ăn nhẹ** | 5h20–5h30: ~30–40 g carb + 20–25 g protein (ví dụ chuối hoặc 1–2 lát bánh mì + 1 scoop whey). Tải nặng lên cột sống thì không nên vào buổi với dạ dày trống |
| 2 và 4 (Upper) | Ăn nhẹ **hoặc** fasted | Nếu fasted: 20–30 g whey + 20–30 g carb nhanh uống **trong** buổi, rồi ăn bữa lớn ngay sau 7h30 |

Phân bổ lại 165 g protein cho lịch dậy sớm — 4 cữ khoảng 40 g: **5h30** (pre) · **8h00** (sau tập, cữ lớn nhất) · **12h30** · **19h00**. Tổng ngày và phân bố đều quan trọng hơn cửa sổ vài phút.

> **Rủi ro lớn nhất của việc đổi giờ không phải là buổi tập — là giấc ngủ.**
>
> Có mặt ở gym 6h00 nghĩa là dậy khoảng 5h00–5h15. Để đủ 7–8 giờ ngủ, bạn phải lên giường **trước 21h30–22h00**. Nếu đổi giờ tập mà **không** dời giờ ngủ sớm tương ứng, bạn đang cắt 1–1,5 giờ ngủ mỗi đêm trong lúc đang ăn thâm hụt. Đó là cách nhanh nhất để phá cả e1RM lẫn khối nạc — tức là phá đúng hai thứ bạn xếp ưu tiên số 1.
>
> **Nếu giờ ngủ không dời được, đừng đổi sang tập sáng.** Giữ khung chiều tốt hơn.
>
> Bắt buộc theo dõi trong 2 tuần đầu sau khi đổi: giờ lên giường, giờ dậy, tổng giờ ngủ. Ngủ dưới 7 giờ từ 3 đêm trở lên trong tuần → xử lý như tín hiệu ở bảng dự phòng (ăn duy trì hoặc kéo deload sớm), không cố chạy theo ma trận.

## Cách đọc lịch và luật tăng tiến

### Top set (SBD)

- Kg trong ma trận là **điểm khởi hành, không phải mệnh lệnh** — RPE thắng kg. Tải in sẵn tính từ 1RM 170/130/200; trong thâm hụt, %1RM cũ sẽ "nói dối" dần từ tuần 4–5, còn RPE đọc đúng tình trạng hôm đó.
- Đủ rep mà RPE **thấp hơn** mức ghi → tuần sau +2,5 kg so với số in.
- Đúng RPE ghi → tuần sau theo đúng số in.
- **Vượt** RPE ghi → giữ nguyên tải, lặp lại tuần sau, bỏ qua mức tăng của ma trận.
- **Sàn rep:** Squat/Bench 4, Deadlift 3. **Trần RPE:** 8,5. Không xuống 2 rep, không lên RPE 9+ — đó là ranh giới giữ khối này là hypertrophy chứ không lén thành peaking.
- Ký hiệu ¹: chỉ nhận mức tải đó khi tuần trước hoàn thành đủ rep ở RPE ≤ mức ghi. Không đạt → giữ tải cũ.

### Back-off (BO)

- BO = tải Top set hôm đó **−10%**, làm tròn bậc 2,5 kg. Top lên thì BO tự lên theo — chỉ quản lý một đường tiến độ.
- RIR ghi ở back-off áp cho **hiệp cuối**, không phải hiệp đầu. Nếu hiệp đầu đã đúng bằng RIR ghi thì tải đang quá nặng cho số hiệp đó → **cắt 1 hiệp và giữ tải**, đừng hạ tải để cố đủ hiệp.
- **Cùng một mức tạ cho tất cả các hiệp BO** (straight sets). Chọn tải sao cho hiệp cuối rơi đúng RIR ghi; các hiệp trước nhẹ hơn và đó là bình thường. Không dùng drop set hay giảm tải dần qua từng hiệp.
- **Thêm hiệp không đi kèm thêm tạ.** Tuần 2 lên 3 hiệp nhưng vẫn 120 kg — chính hiệp thứ ba làm hiệp cuối nặng hơn, đó là quá tải lũy tiến của tuần đó.
- Hiệu chỉnh tải BO sau mỗi buổi: hiệp cuối ra RIR 4 → tuần sau +2,5 kg. Đúng RIR ghi → giữ nguyên. RIR 0 hoặc sập → tuần sau −2,5 kg.
- **Trần hiệp BO Squat: 2 hiệp cho cả khối** (sửa 2026-09-16 theo phản hồi thực tế ở tuần 2–4). Lý do và số liệu ở mục *Vì sao BO Squat bị chặn ở 2 hiệp* bên dưới. Muốn 3 hiệp thì **phải hạ tải xuống Top −15%** thay vì −10% — con số cụ thể đã in sẵn trong ma trận (ô "hoặc 3×6 @…").
- BO Bench và BO Deadlift **giữ nguyên** như cũ: user xác nhận hai bài này dung nạp tốt qua tuần 4.

### Vì sao BO Squat bị chặn ở 2 hiệp

Phản hồi thực tế của user sau 4 tuần chạy: mọi thứ dung nạp được, **trừ tuần tăng BO Squat từ 2 lên 3 hiệp** — hết sức ngay từ bài đầu, các bài sau của buổi bị ảnh hưởng.

Kiểm tra lại con số thì đây là lỗi thiết kế chứ không phải vấn đề của người tập:

| | Tuần 2 (bản cũ) |
|---|---|
| Top set | 132,5 kg × 6 @RPE 7,5 |
| BO | 3 × 8 @120 kg |
| 120 kg theo %1RM | **70,6%** của 1RM 170 |
| 70% khi tươi | ≈ 12RM → 8 rep = RIR ~4 |
| Thực tế sau ramp-up + Top set | hiệp 1 ≈ RIR 3 → hiệp 2 ≈ RIR 1–2 → **hiệp 3 ≈ RIR 0** |
| Tổng rep ở ≥70% 1RM trong **một bài** | **30 rep** |

Gốc lỗi: quy tắc `BO = Top − 10%` trừ 10% theo **kg của top set**, không theo %1RM. Top set nằm ở 76–87% 1RM nên BO vẫn rơi vào 68–78% 1RM — quá nặng cho 8 rep × 3 hiệp straight set. Luật bảo vệ sẵn có (*"hiệp đầu đã đúng RIR ghi → cắt 1 hiệp"*) chỉ bắt được khi **hiệp 1** đã nặng; nó không bắt được kiểu tích lũy đến **hiệp 3** mới sập.

Bench không gặp vấn đề vì BO ở 67,3% 1RM (87,5/130) — nhẹ hơn Squat khoảng 3 điểm phần trăm và không có tải lên cột sống như squat. Deadlift BO cố ý để RIR 3–4. Vì vậy **chỉ sửa Squat**.

**Volume quad không mất đi:** Hack Squat đã lên 4 hiệp từ tuần 3, cộng RDL 4 hiệp, Walking Lunge 4 hiệp và Leg Extension. Phần bị cắt là các hiệp squat nặng có chi phí mệt mỏi cao nhất nhưng kích thích phì đại chồng lấn với những bài trên — đúng với ưu tiên hypertrophy và giữ sức của bạn.

### Bài máy và cô lập

- Ô ma trận ghi hiệp × rep • RIR. **Tuần 1:** tự chọn tải đạt đúng rep ở RIR quy định rồi **ghi vào logbook** — từ tuần 2 ma trận tự dẫn tiến độ theo rep/RIR. Máy khác hãng chênh 30–50% nên không in kg cho nhóm này.
- "(đạt → +tải Tx)": hoàn thành đủ hiệp × rep ở đúng RIR → tuần ghi chú tăng 1 bậc nhỏ nhất (2,5 kg hoặc 1 nấc máy). Không đạt → giữ tải, lặp lại.
- **THÊM 1 HIỆP** chỉ nhận khi đủ **cả bốn** điều kiện: hiệu suất tuần trước giữ hoặc tăng; DOMS hết trước buổi kế; không đau khớp tăng; ngủ ổn. Thiếu một điều → giữ số hiệp cũ.
- **Nghỉ giữa hiệp:** Top set SBD 3–4 phút; BO và compound 2–3 phút; máy/cô lập 90–120 giây. Thiếu giờ thì cắt bài **cuối** buổi, không cắt Top set/BO.

### Bài thay thế (theo thứ tự ưu tiên)

Chọn từ trên xuống theo thiết bị sẵn có, áp nguyên hiệp × rep × RIR của tuần hiện tại; đã đổi thì **giữ hết meso** (đổi bài giữa chừng làm hỏng chuỗi dữ liệu logbook).

| Bài gốc | Ưu tiên 1 | Ưu tiên 2 | Ưu tiên 3 |
|---|---|---|---|
| Competition Squat | High-Bar Squat | Smith Machine Squat | Pendulum Squat |
| Romanian Deadlift | 45° Back Extension | Good Morning nhẹ | Dumbbell RDL |
| Hack Squat | Pendulum Squat | Smith Machine Squat | 45° Leg Press (ROM sâu) |
| Leg Extension | Reverse Nordic | 45° Leg Press nhẹ ROM sâu | — |
| Calf Raise | Seated Calf Raise | — | — |
| Competition Bench | Smith Machine Bench | Machine Chest Press (nặng 6–8 rep) | — |
| Chest-Supported Row | Meadows Row | Cable Row | 1-Arm Dumbbell Row |
| Machine Chest Press | Flat Dumbbell Press | Dips | Deficit Push-Up (đeo tạ) |
| Cable Lateral Raise | Cable Y-Raise | Behind-the-Back Cuffed Raise | Lean-In DB Lateral Raise |
| Rope Facepull | Reverse Pec Deck (ngồi nghiêng) | Floor-Seated Rope Face-Pull | — |
| Overhead Cable Triceps Ext | Skullcrusher (EZ bar) | 1-Arm DB Overhead Extension | Katana Extension |
| EZ Bar Curl | 45° DB Preacher Curl | Machine Preacher Curl | Hammer Curl |
| Competition Deadlift | Trap-Bar Deadlift | Block / Elevated Pull | — |
| Walking Lunge | Front-Foot-Elevated Smith Lunge | Bulgarian Split Squat (2 hiệp) | Step-Up |
| Leg Curl | Nordic có hỗ trợ | RDL nhẹ | — |
| Machine Hip Thrust | Barbell Hip Thrust | Single-Leg DB Hip Thrust | — |
| 45° Back Extension | Cable Kickback (đá chéo lên–ra) | Hip Thrust nhẹ | — |
| Incline Bench Press | Incline Dumbbell Press | Incline Smith Press | — |
| Wide-Grip Lat Pulldown | Neutral-Grip Pulldown | Half-Kneeling 1-Arm Pulldown | Pull-Up (đeo tạ) |
| Wide-Grip Cable Row | Cable Row | Meadows Row | — |
| Reverse Cable Crossover | Reverse Pec Deck (ngồi nghiêng) | Rope Facepull | — |
| Incline Dumbbell Curl | 45° DB Preacher Curl | Bayesian Cable Curl | Machine Preacher Curl |
| Bar Pressdown | Close-Grip Bench Press | Cable Kickback | Skullcrusher |

## Ma trận 12 tuần

Dòng **DELOAD** = tuần giảm tải. **THÊM 1 HIỆP** = tuần bài đó được thêm hiệp, chỉ nhận khi đủ 4 điều kiện ở mục trên. Ký hiệu ¹ = chỉ tăng khi tuần trước đạt. Kg của Top/BO là điểm khởi hành — RPE thắng kg.

### Buổi 1 — Lower A

| Tuần | Competition Squat (Top + BO) | Romanian Deadlift | Hack Squat | Leg Extension | Calf Raise |
|---|---|---|---|---|---|
| 1 | Top 1×6 @130 • RPE 7 · BO 2×8 @120 • hiệp cuối RIR 2–3 | 3×8 • RIR 3 | 3×8 • RIR 3 | 2×12 • RIR 2 | 2×12 • RIR 2 |
| 2 | Top 1×6 @132,5 • RPE 7,5 · BO **2**×8 @120 • RIR 2 — *đã sửa: không thêm hiệp* | 3×10 (cùng tải) • RIR 2 | 3×10 (cùng tải) • RIR 2 | 2×14 (cùng tải) • RIR 2 | 2×14 (cùng tải) • RIR 2 |
| 3 | Top 1×6 @135 • RPE 8 · BO **2**×8 @122,5 • RIR 2 | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 2×15 • RIR 1–2 (đạt → +tải T4) | 2×15 • RIR 1–2 (đạt → +tải T4) |
| 4 | Top 1×5 @137,5 • RPE 7,5 · BO **2**×7 @125 • RIR 2 | 4×10 • RIR 2 | 4×10 • RIR 2 | 2×12 (tải mới) • RIR 2 | 2×12 (tải mới) • RIR 2 |
| 5 | Top 1×5 @140 • RPE 8–8,5 · BO **2**×6 @125 • RIR 2 — *hoặc 3×6 @120* | 4×12 • RIR 1–2 (đạt → +tải T7) | 4×12 • RIR 1–2 (đạt → +tải T7) | 2×14 • RIR 1–2 | 2×14 • RIR 1–2 |
| **6** | **DELOAD** — Top 1×5 @122,5 • RPE ≤6 · BO 2×6 @105 | 2×8 • RIR 4 | 2×8 • RIR 4 | 1×12 • RIR 4 | 1×12 • RIR 4 |
| 7 | Top 1×5 @137,5 • RPE 7,5 · BO **2**×7 @125 • RIR 2 | 4×8 (tải mới) • RIR 2 | 4×8 (tải mới) • RIR 2 | 2×12 • RIR 2 | 2×12 • RIR 2 |
| 8 | Top 1×5 @140 • RPE 8 · BO **2**×7 @125 • RIR 2 — *hoặc 3×7 @120* | 4×10 • RIR 2 | 4×10 • RIR 2 | 2×14 • RIR 1–2 | 2×14 • RIR 1–2 |
| 9 | Top 1×4 @142,5 • RPE 8 · BO **2**×6 @127,5 • RIR 2 — *hoặc 3×6 @120* | 4×11 • RIR 1–2 | 4×11 • RIR 1–2 | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 2 — **THÊM 1 HIỆP** |
| 10 | Top 1×4 @145¹ • RPE 8,5 · BO **2**×6 @130 • RIR 1–2 — *hoặc 3×6 @122,5* | 4×12 • RIR 1 (đạt → +tải T11) | 4×12 • RIR 1 (đạt → +tải T11) | 3×14 • RIR 1 | 3×14 • RIR 1 |
| 11 | Top 1×4 @145 • RPE 8,5 (đạt → 147,5) · BO **2**×6 @130 • RIR 1–2 — *hoặc 3×6 @122,5* | 4×8 (tải mới) • RIR 1–2 | 4×8 (tải mới) • RIR 1–2 | 3×15 • RIR 1 (đạt → +tải khối sau) | 3×15 • RIR 1 (đạt → +tải khối sau) |
| **12** | **DELOAD** — 2×5 @120 + AMRAP @RPE 8 tùy chọn (ước e1RM) | 2×8 nhẹ | 2×8 nhẹ | 1×12 nhẹ | 1×12 nhẹ |

### Buổi 2 — Upper A

| Tuần | Competition Bench (Top + BO) | Chest-Supported Row | Machine Chest Press | Cable Lateral Raise | OH Cable Triceps Ext | **ABS A** — Cable Crunch |
|---|---|---|---|---|---|---|
| 1 | Top 1×6 @97,5 • RPE 7 · BO 2×8 @87,5 • RIR 2–3 (hiệp 1 ra RIR ≤2 → hạ 85 ngay) | 3×8 • RIR 3 | 3×8 • RIR 3 | 2×12 • RIR 2 | 2×12 • RIR 2 | 3×10 • RIR 2 — *buổi đầu: tự chọn tải, ghi logbook* |
| 2 | Top 1×6 @100 • RPE 7,5 · BO 3×8 @87,5 • RIR 2 — **THÊM 1 HIỆP** | 3×10 (cùng tải) • RIR 2 | 3×10 (cùng tải) • RIR 2 | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 2 |
| 3 | Top 1×6 @102,5 • RPE 8 · BO 3×8 @90 • RIR 2 | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 3×14 • RIR 2 | 3×14 • RIR 2 | 3×15 • RIR 1–2 (đạt → +tải) |
| 4 | Top 1×5 @105 • RPE 7,5 · BO 3×7 @92,5 • RIR 2 | 4×10 • RIR 2 | 4×10 • RIR 2 | 3×15 • RIR 1–2 (đạt → +tải T5) | 3×15 • RIR 1–2 (đạt → +tải T5) | 3×10 (tải mới) • RIR 2 |
| 5 | Top 1×5 @107,5 • RPE 8–8,5 · BO 4×6 @95 • RIR 2 — **THÊM 1 HIỆP** | 4×12 • RIR 1–2 (đạt → +tải T7) | 4×12 • RIR 1–2 (đạt → +tải T7) | 3×12 (tải mới) • RIR 1–2 | 3×12 (tải mới) • RIR 1–2 | 3×12 • RIR 1–2 |
| **6** | **DELOAD** — Top 1×5 @92,5 • RPE ≤6 · BO 2×6 @82,5 | 2×8 • RIR 4 | 2×8 • RIR 4 | 1×12 • RIR 4 | 1×12 • RIR 4 | 2×10 • RIR 4 |
| 7 | Top 1×5 @105 • RPE 7,5 · BO 3×7 @92,5 • RIR 2 | 4×8 (tải mới) • RIR 2 | 4×8 (tải mới) • RIR 2 | 3×12 • RIR 2 | 3×12 • RIR 2 | 3×12 • RIR 2 |
| 8 | Top 1×5 @107,5 • RPE 8 · BO 4×7 @95 • RIR 2 — **THÊM 1 HIỆP** | 4×10 • RIR 2 | 4×10 • RIR 2 | 3×14 • RIR 1–2 | 3×14 • RIR 1–2 | 3×15 • RIR 1–2 (đạt → +tải) |
| 9 | Top 1×4 @110 • RPE 8 · BO 4×6 @97,5 • RIR 2 | 4×11 • RIR 1–2 | 4×11 • RIR 1–2 | 4×12 • RIR 2 — **THÊM 1 HIỆP** | 4×12 • RIR 2 — **THÊM 1 HIỆP** | 3×10 (tải mới) • RIR 2 |
| 10 | Top 1×4 @112,5¹ • RPE 8,5 · BO 4×6 @100 • RIR 1–2 | 4×12 • RIR 1 (đạt → +tải T11) | 4×12 • RIR 1 (đạt → +tải T11) | 4×14 • RIR 1 | 4×14 • RIR 1 | 3×12 • RIR 1 |
| 11 | Top 1×4 @112,5 • RPE 8,5 (đạt → 115) · BO 4×6 @100 • RIR 1–2 | 4×8 (tải mới) • RIR 1–2 | 4×8 (tải mới) • RIR 1–2 | 4×15 • RIR 1 (đạt → +tải khối sau) | 4×15 • RIR 1 | 3×15 • RIR 1 (đạt → +tải khối sau) |
| **12** | **DELOAD** — 2×5 @90 + AMRAP @RPE 8 tùy chọn | 2×8 nhẹ | 2×8 nhẹ | 1×12 nhẹ | 1×12 nhẹ | 2×10 nhẹ |
> **Đọc cột ABS khác với các cột còn lại.** Bạn vào khối này ở **tuần 5**, nhưng abs là bài **mới thêm** nên chưa có baseline. Buổi abs đầu tiên của bạn đọc ở ô **"Tuần 1"** của cột ABS, buổi thứ hai đọc ô "Tuần 2", và cứ thế đi xuống — trong khi mọi cột khác vẫn đọc theo đúng số tuần của khối. Hai cột ABS (buổi 2 và buổi 5) đi cùng nhịp với nhau. Khi cột ABS chạy hết ô "Tuần 11" thì lặp lại từ "Tuần 7" với tải mới.

### Buổi 3 — Lower B

| Tuần | Competition Deadlift (Top + BO) | Walking Lunge | Leg Curl | Machine Hip Thrust | 45° Back Extension | Calf Raise |
|---|---|---|---|---|---|---|
| 1 | Top 1×5 @155 • RPE 7 · BO 2×5 @135 • RIR 3–4 | 3×8 • RIR 2–3 | 2×12 • RIR 2 | 2×10 • RIR 2–3 | 2×12 • RIR 2 | 2×12 • RIR 2 |
| 2 | Top 1×5 @160 • RPE 7,5 · BO 2×5 @137,5 • RIR 3 | 3×10 (cùng tải) • RIR 2 | 2×14 (cùng tải) • RIR 2 | 3×10 • RIR 2 — **THÊM 1 HIỆP** | 2×14 (cùng tải) • RIR 2 | 2×14 (cùng tải) • RIR 2 |
| 3 | Top 1×5 @162,5 • RPE 8 · BO 2×5 @140 • RIR 3 | 3×12 • RIR 2 (đạt → +tải T4) | 2×15 • RIR 1–2 (đạt → +tải T4) | 3×12 • RIR 2 | 2×15 • RIR 1–2 (đạt → +tải T4) | 2×15 • RIR 1–2 (đạt → +tải T4) |
| 4 | Top 1×4 @165 • RPE 7,5 · BO 2×5 @142,5 • RIR 3 | 3×8 (tải mới) • RIR 2 | 2×12 (tải mới) • RIR 2 | 3×15 • RIR 1–2 (đạt → +tải T5) | 2×12 (tải mới) • RIR 2 | 2×12 (tải mới) • RIR 2 |
| 5 | Top 1×4 @167,5 • RPE 8 · BO 2×5 @145 • RIR 3 | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 2×14 • RIR 1–2 | 3×10 (tải mới) • RIR 2 | 2×14 • RIR 1–2 | 2×14 • RIR 1–2 |
| **6** | **DELOAD** — Top 1×4 @145 • RPE ≤6 · BO 1×5 @120 | 1×8 • RIR 4 | 1×12 • RIR 4 | 1×10 • RIR 4 | 1×12 • RIR 4 | 1×12 • RIR 4 |
| 7 | Top 1×4 @165 • RPE 7,5 · BO 2×4 @145 • RIR 3 | 3×10 • RIR 2 | 2×12 • RIR 2 | 3×10 • RIR 2 | 2×12 • RIR 2 | 2×12 • RIR 2 |
| 8 | Top 1×4 @167,5 • RPE 8 · BO 2×4 @147,5 • RIR 3 | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 2×14 • RIR 1–2 | 3×12 • RIR 1–2 | 2×14 • RIR 1–2 | 2×14 • RIR 1–2 |
| 9 | Top 1×3 @172,5 • RPE 8 · BO 2×4 @150 • RIR 3 | 4×10 • RIR 1–2 | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×15 • RIR 1 (đạt → +tải T10) | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 2 — **THÊM 1 HIỆP** |
| 10 | Top 1×3 @175¹ • RPE 8,5 · BO 2×4 @152,5 • RIR 3 | 4×12 • RIR 1 (đạt → +tải T11) | 3×14 • RIR 1 | 3×10 (tải mới) • RIR 1–2 | 3×14 • RIR 1 | 3×14 • RIR 1 |
| 11 | Top 1×3 @175 • RPE 8,5 (đạt → 177,5) · BO 2×4 @155 • RIR 2–3 | 4×8 (tải mới) • RIR 1–2 | 3×15 • RIR 1 (đạt → +tải khối sau) | 3×12 • RIR 1 | 3×15 • RIR 1 | 3×15 • RIR 1 |
| **12** | **DELOAD** — 1×3 @140 · BO 1×4 @120 | 1×8 nhẹ | 1×12 nhẹ | 1×10 nhẹ | 1×12 nhẹ | 1×12 nhẹ |

### Buổi 4 — Upper B

Bài 1 = **Incline Bench Press cả 12 tuần** (không còn luân phiên sang Machine Shoulder Press — xem *Lỗ hổng ngực ở Meso 2*). Bench kỹ thuật 3×3 @90 RPE ≤6 tùy chọn trước bài 1 (bỏ ở tuần 6 và 12).

| Tuần | Incline Bench Press | Wide-Grip Lat Pulldown | Wide-Grip Cable Row | Reverse Cable Crossover | EZ Bar Curl |
|---|---|---|---|---|---|
| 1 | 3×8 • RIR 3 | 3×8 • RIR 3 | 3×8 • RIR 3 | 2×12 • RIR 2 | 2×12 • RIR 2 |
| 2 | 3×10 (cùng tải) • RIR 2 | 3×10 (cùng tải) • RIR 2 | 3×10 (cùng tải) • RIR 2 | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 2 — **THÊM 1 HIỆP** |
| 3 | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 4×8 • RIR 2 — **THÊM 1 HIỆP** | 3×14 • RIR 2 | 3×14 • RIR 2 |
| 4 | 4×10 • RIR 2 | 4×10 • RIR 2 | 4×10 • RIR 2 | 3×15 • RIR 1–2 (đạt → +tải T5) | 3×15 • RIR 1–2 (đạt → +tải T5) |
| 5 | 4×12 • RIR 1–2 (đạt → +tải T7) | 4×12 • RIR 1–2 (đạt → +tải T7) | 4×12 • RIR 1–2 (đạt → +tải T7) | 3×12 (tải mới) • RIR 1–2 | 3×12 (tải mới) • RIR 1–2 |
| **6** | **DELOAD** — 2×8 • RIR 4 | 2×8 • RIR 4 | 2×8 • RIR 4 | 1×12 • RIR 4 | 1×12 • RIR 4 |
| 7 | 4×8 (tải mới) • RIR 2 | 4×8 (tải mới) • RIR 2 | 4×8 (tải mới) • RIR 2 | 3×12 • RIR 2 | 3×12 • RIR 2 |
| 8 | 4×10 • RIR 2 | 4×10 • RIR 2 | 4×10 • RIR 2 | 3×14 • RIR 1–2 | 3×14 • RIR 1–2 |
| 9 | 4×11 • RIR 1–2 | 4×11 • RIR 1–2 | 4×11 • RIR 1–2 | 4×12 • RIR 2 — **THÊM 1 HIỆP** | 4×12 • RIR 2 — **THÊM 1 HIỆP** |
| 10 | 4×12 • RIR 1 (đạt → +tải T11) | 4×12 • RIR 1 (đạt → +tải T11) | 4×12 • RIR 1 (đạt → +tải T11) | 4×14 • RIR 1 | 4×14 • RIR 1 |
| 11 | 4×8 (tải mới) • RIR 1–2 | 4×8 (tải mới) • RIR 1–2 | 4×8 (tải mới) • RIR 1–2 | 4×15 • RIR 1 (đạt → +tải khối sau) | 4×15 • RIR 1 |
| **12** | **DELOAD** — 2×8 nhẹ | 2×8 nhẹ | 2×8 nhẹ | 1×12 nhẹ | 1×12 nhẹ |

### Buổi 5 — Vai / Tay / Abs

Buổi này được phép bỏ khi mệt hoặc ngủ kém. Bỏ thì **không bù**.

| Tuần | Cable Lateral Raise (lần 2) | Rope Facepull | Bar Pressdown | Incline Dumbbell Curl | **ABS B** — Hanging Knee Raise | **Machine Shoulder Press** *(chỉ Meso 2)* |
|---|---|---|---|---|---|---|
| 1 | 2×12 • RIR 2 | 2×12 • RIR 2 | 2×12 • RIR 2 | 2×12 • RIR 2 | 3×10 • RIR 1–2 — *buổi đầu: ghi logbook* | — |
| 2 | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 2×14 (cùng tải) • RIR 2 | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 1–2 | — |
| 3 | 3×14 • RIR 2 | 3×14 • RIR 2 | 2×15 • RIR 1–2 (đạt → +tải T4) | 3×14 • RIR 2 | 3×14 • RIR 1–2 | — |
| 4 | 3×15 • RIR 1–2 (đạt → +tải T5) | 3×15 • RIR 1–2 (đạt → +tải T5) | 2×12 (tải mới) • RIR 2 | 3×15 • RIR 1–2 (đạt → +tải T5) | 3×16 • RIR 1–2 | — |
| 5 | 3×12 (tải mới) • RIR 1–2 | 3×12 (tải mới) • RIR 1–2 | 2×14 • RIR 1–2 | 3×12 (tải mới) • RIR 1–2 | 3×18 • RIR 1–2 | — |
| **6** | 1×12 • RIR 4 | 1×12 • RIR 4 | 1×12 • RIR 4 | 1×12 • RIR 4 | 2×10 • RIR 4 | — |
| 7 | 3×12 • RIR 2 | 3×12 • RIR 2 | 2×12 • RIR 2 | 3×12 • RIR 2 | 3×14 • RIR 1–2 | 3×8 • RIR 3 — *buổi đầu: tự chọn tải, ghi logbook* |
| 8 | 3×14 • RIR 1–2 | 3×14 • RIR 1–2 | 2×14 • RIR 1–2 | 3×14 • RIR 1–2 | 3×16 • RIR 1–2 | 3×10 (cùng tải) • RIR 2 |
| 9 | 4×12 • RIR 2 — **THÊM 1 HIỆP** | 4×12 • RIR 2 — **THÊM 1 HIỆP** | 3×12 • RIR 2 — **THÊM 1 HIỆP** | 4×12 • RIR 2 — **THÊM 1 HIỆP** | 3×18 • RIR 1–2 | 4×8 • RIR 2 — **THÊM 1 HIỆP** |
| 10 | 4×14 • RIR 1 | 4×14 • RIR 1 | 3×14 • RIR 1 | 4×14 • RIR 1 | 3×20 • RIR 1–2 (đạt → bắt đầu thêm tải) | 4×10 • RIR 2 |
| 11 | 4×15 • RIR 1 | 4×15 • RIR 1 | 3×15 • RIR 1 | 4×15 • RIR 1 | 3×12 (có tải) • RIR 1–2 | 4×12 • RIR 1–2 (đạt → +tải khối sau) |
| **12** | 1×12 nhẹ | 1×12 nhẹ | 1×12 nhẹ | 1×12 nhẹ | 2×10 nhẹ | — |

**Cable Pallof Press** chạy 2 × 8–12 mỗi bên • RIR 2 ở mọi tuần không-deload; tuần deload (6 và 12) làm 1 hiệp hoặc bỏ. Đây là bài bracing, không chạy theo ma trận tăng tiến.

> **Đọc cột ABS khác với các cột còn lại.** Bạn vào khối này ở **tuần 5**, nhưng abs là bài **mới thêm** nên chưa có baseline. Buổi abs đầu tiên của bạn đọc ở ô **"Tuần 1"** của cột ABS, buổi thứ hai đọc ô "Tuần 2", và cứ thế đi xuống — trong khi mọi cột khác vẫn đọc theo đúng số tuần của khối. Hai cột ABS (buổi 2 và buổi 5) đi cùng nhịp với nhau. Khi cột ABS chạy hết ô "Tuần 11" thì lặp lại từ "Tuần 7" với tải mới.

### Tóm tắt thay đổi trọng điểm từng tuần

| Tuần | Thay đổi so với tuần trước | Bản chất |
|---|---|---|
| 1 | Thiết lập: Top set RPE 7 theo kg in sẵn; BO Squat/Bench 2 hiệp, BO Deadlift 2 hiệp; bài máy tự chọn tải đúng RIR và ghi logbook. Volume khởi điểm ~63 hiệp/tuần. | Thiết lập |
| 2 | THÊM 1 HIỆP: BO Bench 2→3 (**giữ nguyên tải**); Hip Thrust 2→3; các bài cô lập chính 2→3. Top +2,5 kg, RPE 7,5. **BO Squat giữ 2 hiệp** — sửa 2026-09-16. | Tăng volume đợt 1 |
| 3 | THÊM 1 HIỆP ở máy compound (Hack, RDL, CSR, MCP, Incline, Pulldown, WG Cable Row) 3→4. Top lên RPE 8. | Tăng volume đợt 2 |
| 4 | Top chuyển 5 rep (DL 4 rep), tải nhích, RPE lùi về 7,5 — sóng cường độ. | Sóng cường độ |
| 5 | Đỉnh Meso 1: Top RPE 8–8,5 (140/107,5/167,5). BO Bench 3→4 hiệp; Walking Lunge 3→4. **BO Squat giữ 2 hiệp.** | Đỉnh Meso 1 |
| **6** | **DELOAD**: cắt ~50–60% số hiệp; Top **giữ** nhưng tải nhẹ RPE ≤6 — không bỏ hẳn tải nặng để giữ dung nạp. **Ăn ở mức duy trì.** | Deload |
| 7 | Vào Meso 2: **Machine Shoulder Press xuất hiện ở buổi 5** (Incline ở lại buổi 4). Máy compound tải mới 4×8. Top về RPE 7,5. | Khởi động Meso 2 |
| 8 | Top RPE 8. BO Bench 3→4 hiệp. Máy giữ hiệp, tăng rep. **BO Squat giữ 2 hiệp.** | Tăng cường độ |
| 9 | Volume đỉnh chu kỳ: cô lập chính 3→4; cô lập nhỏ 2→3. **BO Squat và BO Deadlift giữ nguyên số hiệp — có chủ đích.** Top chuyển 4 rep (DL 3). | Volume đỉnh |
| 10 | Top +2,5 kg **có điều kiện¹**: 145/112,5/175 @RPE 8,5. | Đẩy sát trần |
| 11 | Tuần nặng nhất: Top giữ tải @RPE 8,5, đạt → +2,5. BO bớt 1 hiệp để bù mệt. | Đỉnh chu kỳ |
| **12** | **DELOAD + ĐÁNH GIÁ**: Top nhẹ + AMRAP @RPE 8 tùy chọn để ước e1RM mới. Tổng kết eo, cân TB tuần, ảnh, đường e1RM, logbook so tuần 1. **Ăn ở mức duy trì.** | Deload + tổng kết |

### Quy đổi RPE → e1RM (KPI sức mạnh của khối này)

Sau mỗi Top set: `e1RM = tải ÷ hệ số`. Ghi vào logbook và vẽ đường theo tuần.

| Số rep | RPE 7 | RPE 7,5 | RPE 8 | RPE 8,5 |
|---|---|---|---|---|
| 6 rep | 0,769 | 0,779 | 0,790 | — |
| 5 rep | 0,790 | 0,800 | 0,811 | 0,822 |
| 4 rep | — | 0,822 | 0,833 | 0,845 |
| 3 rep | — | — | 0,857 | 0,870 |

*Ví dụ:* Squat tuần 9 — 142,5 kg × 4 rep, cảm nhận RPE 8 → e1RM = 142,5 ÷ 0,833 ≈ 171 kg.

**Cách đọc:** đường e1RM đi ngang hoặc dốc nhẹ lên = khối đang làm đúng việc trong thâm hụt. Dốc xuống 2 tuần liên tiếp = **xem lại deficit và giấc ngủ trước, cắt volume sau**.

Bảng hệ số này là công cụ ước lượng theo thang RIR-based RPE; nó **không phải phép đo**. Người chưa quen đánh giá nỗ lực sẽ có sai số lớn, và knowledge 17.4 lưu rằng RPE/RIR là ước lượng theo một thang cụ thể, không quy đổi được từ mọi thang RPE.

## Dinh dưỡng

**Thứ tự xử lý (knowledge 18.1):** phạm vi sức khỏe → năng lượng → protein → fat/carb → chất lượng khẩu phần → timing → supplement → theo dõi.

**Phạm vi sức khỏe:** user không khai báo bệnh, thuốc, dị ứng hay rối loạn ăn uống. Phần này là **khung dinh dưỡng thể thao cho người trưởng thành khỏe mạnh**, không phải kê đơn và không thay kế hoạch lâm sàng.

### Bước 1 — Năng lượng

```text
REE (Mifflin–St Jeor, nam) = 10 × 76 + 6,25 × 170 − 5 × 25 + 5
                           = 760 + 1.062,5 − 125 + 5
                           = 1.702,5 kcal/ngày
```

```text
TDEE ước tính = REE × 1,5 ≈ 2.554 kcal/ngày
```

**Giả định hệ số 1,5 gồm:** công việc văn phòng ít đi lại + 4 buổi tạ chính + buổi 5 ngắn + mục tiêu 8.000–10.000 bước/ngày. **Đây là giả định, không phải đo.** Khoảng hợp lý: **2.300–2.800 kcal/ngày**. Mifflin–St Jeor dự đoán năng lượng lúc nghỉ ở người khỏe mạnh, không phải công thức riêng cho người tập nặng (knowledge 18.2).

**Không cộng thêm calories do đồng hồ/app báo cho buổi tập** — hệ số 1,5 đã bao gồm phần đó rồi.

### Bước 2 — Mục tiêu năng lượng

| | Giá trị | Ghi chú |
|---|---|---|
| TDEE ước tính | ~2.550 kcal | ±10%, chưa kiểm chứng bằng dữ liệu thực |
| **Mục tiêu hằng ngày** | **~2.200 kcal** | Thâm hụt ~350 kcal ≈ **14%** |
| Tốc độ giảm mục tiêu | **0,35–0,5%/tuần** (~0,27–0,38 kg/tuần) | Theo **trung bình cân 7 ngày**, không theo cân từng ngày |
| Tuần deload (6 và 12) | **~2.550 kcal** (duy trì) | Ăn duy trì trọn tuần |

**Vì sao 14% chứ không sâu hơn:** user chốt giữ cơ/sức thắng tốc độ giảm mỡ. Knowledge 18.3 nêu khoảng 10–15% làm giả định khởi đầu để kiểm thử cho người khỏe mạnh giảm mỡ không thi đấu, và giảm chậm giúp quản lý đánh đổi về khối nạc và thành tích. Mức này nhanh hơn plan cũ của user (~0,25%/tuần) nhưng vẫn nằm trong vùng ít phá hiệu suất.

> **Về mỡ bụng và vòng eo.** Không có cơ chế giảm mỡ khu trú — không bài tập hay cách ăn nào nhắm riêng mỡ bụng. Vòng eo được dùng làm **chỉ số theo dõi chính** của phase này vì trong recomp cân có thể gần đứng yên trong khi eo vẫn giảm. Core work ở buổi 1 phục vụ bracing dưới tải, không phục vụ thẩm mỹ eo.

### Mục tiêu 15% mỡ — số học và thời gian

**Baseline đã chốt:** 76 kg, **20% mỡ**. User đối chiếu bảng so sánh hình ảnh và xác nhận lại ngày 2026-09-16 rằng thể trạng hiện tại khớp đúng mốc 20%. Project dùng con số này làm baseline cho mọi tính toán dưới đây.

**Ghi đúng bản chất của con số:** đây là **tự đánh giá bằng đối chiếu hình ảnh**, không phải DEXA hay kẹp da. Nó đủ tốt để lập kế hoạch — sai số của nó ảnh hưởng đến *thời gian dự kiến*, không ảnh hưởng đến *việc phải làm gì*. Khi có phép đo thật thì cập nhật lại mốc, không cần đổi chương trình.

```text
Ở 76 kg và 20% mỡ:
  khối mỡ  = 76 × 0,20  = 15,2 kg
  khối nạc = 76 − 15,2  = 60,8 kg

Về 15% mỡ mà GIỮ NGUYÊN khối nạc:
  cân đích = 60,8 ÷ 0,85 = 71,5 kg
  cần giảm = 76 − 71,5   = 4,5 kg mỡ

Số TUẦN THÂM HỤT  = 4,5 ÷ (0,27…0,38 kg/tuần) = 12–17 tuần
```

**12–17 tuần đó là số tuần ăn thâm hụt, không phải số tuần trên lịch.** Phải cộng thêm những tuần không thâm hụt đã nằm sẵn trong thiết kế:

| Tuần không thâm hụt | Số tuần | Vì sao có |
|---|---|---|
| Deload tuần 6 và tuần 12 | 2 | Ăn duy trì trọn tuần — đã ghi ở Bước 2 |
| Duy trì giữa hai pha thâm hụt | 2–4 | Quy tắc của roadmap: không nối hai khối deficit liên tiếp |
| Deload trong Phase 2b nếu pha đó kéo dài | 0–1 | Tùy độ dài pha |

```text
Tổng thời gian trên lịch = 12–17 tuần thâm hụt + 4–7 tuần duy trì
                         ≈ 17–24 tuần  (khoảng 4 đến 5,5 tháng)
```

### Mốc dự kiến

Tính ở tốc độ giữa khoảng (~0,32 kg/tuần), giả định giữ nguyên khối nạc 60,8 kg:

| Thời điểm | Cân dự kiến | %mỡ dự kiến |
|---|---|---|
| Bây giờ — vào tuần 5 | 76,0 kg | 20,0% |
| Hết tuần 8 | ~75,0 kg | ~19% |
| **Hết tuần 12 — kết thúc khối này** | **~74,1 kg** | **~17,9%** |
| Sau 2–4 tuần ăn duy trì | ~74,1 kg | ~17,9% |
| Hết Phase 2b (~9 tuần nữa) | **~71,5 kg** | **~15,0%** |

Đọc bảng này đúng cách: **hết khối 12 tuần bạn sẽ ở khoảng 18%, chưa phải 15%.** Đó không phải thất bại — đó là số học. Nếu kỳ vọng 15% vào cuối tuần 12 thì sẽ thất vọng nhầm chỗ và dễ sinh ra quyết định sai là cắt calo sâu hơn.

Nếu tăng được ~1 kg cơ trong quá trình, %mỡ sẽ tới đích **sớm hơn** và ở mức cân **cao hơn** 71,5 kg. Đây là lý do bảng trên là ước lượng định hướng, không phải cam kết.

**Kết luận: chương trình hiện tại đã đưa bạn tới đó rồi.** Không cần cắt calo sâu hơn, không cần thêm cardio, không cần thêm buổi tập. Mục tiêu 15% và kế hoạch đang có là **khớp nhau**, không mâu thuẫn.

Hai kịch bản lệch:

- **Tăng được ~1 kg cơ trong khối:** khối nạc lên 61,8 → cân đích ~72,7 kg. Trên cân chỉ giảm 3,3 kg nhưng thực tế mất ~4,3 kg mỡ. Đây là kịch bản mong muốn và là lý do **không đọc kết quả bằng cân**.
- **Nếu baseline lệch lên 23%:** cần giảm ~7 kg thay vì 4,5 kg, cộng thêm khoảng 8–10 tuần thâm hụt. Vòng eo đo hằng tuần sẽ phát hiện sai lệch này trong 3–4 tuần đầu, sớm hơn nhiều so với chờ một phép đo %mỡ.

**Một điểm đáng nói về khối nạc:** 60,8 kg khối nạc ở chiều cao 170 cm là **nhiều cơ**, và khớp với mức tạ bạn đang kéo (Squat 170 / Bench 130 / Deadlift 200 ở 76 kg). Nghĩa là "to và dày nhưng không nét" đúng là **vấn đề lớp mỡ đơn thuần** — phần cơ đã có sẵn. Khi về 15% bạn sẽ thấy khác biệt lớn mà **không cần xây thêm cơ trước**. Đây là lý do ưu tiên #1 ở khối này là *giữ* khối cơ chứ không phải tăng nó.

### Vì sao "độ nét" không đến từ việc tập

Ở một khối lượng cơ cho trước, độ rõ nét gần như hoàn toàn là hàm của **lượng mỡ dưới da**. Chính bảng đối chiếu là minh họa cho điều đó: cùng một khung cơ, khác nhau ở lớp mỡ phủ lên.

Những thứ **không** làm tăng độ nét:

| Việc hay được làm | Vì sao không có tác dụng |
|---|---|
| Tập rep cao "cho nét" | Dải rep đổi kích thích phì đại, không đổi lớp mỡ. Không có khái niệm "rep để nét" |
| Thêm bài abs | Abs 2 lần/tuần đã đủ cho phì đại. Thêm nữa không làm lộ múi — không giảm mỡ khu trú |
| Cardio lúc đói | Cân bằng năng lượng cả ngày mới quyết định, không phải thời điểm đốt |
| HIIT / circuit | Thêm mệt mỏi và tải khớp — đúng hai thứ bạn muốn tránh |
| Cắt nước, cắt muối | Đổi nước dưới da trong vài ngày, không đổi mỡ. Ảnh hưởng xấu đến hiệu suất buổi tập |

Những thứ dao động **ngày qua ngày và không phải tiến bộ**: nước dưới da (muối, carb, stress, thiếu ngủ), độ đầy glycogen, ánh sáng, pump. Nhìn bụng trong gương sau buổi tập rồi kết luận là đọc nhiễu, không phải đọc kết quả.

> **Cảnh báo về kỳ vọng — đã siết lại 2026-09-16 sau khi đối chiếu [U14](../tai-nguyen/2026-09-16/U14-nippard-get-abs.md).**
>
> | %mỡ (nam) | Nhìn thấy gì |
> |---|---|
> | 30% | Bụng phẳng hơn nhưng **chưa thấy abs** |
> | **20%** ← bạn đang ở đây | **Abs bắt đầu nhìn thấy** |
> | **15%** ← đích của bạn | Giữa hai mốc: abs rõ hơn hiện tại đáng kể, **chưa phải six-pack sắc nét** |
> | **10%** | **Six-pack rõ nét** |
> | 6% | Mức thi đấu |
>
> Muốn mức "sắc nét" thì phải xuống gần **10–12%**, không phải 15%. Nói trước để bạn hiệu chỉnh kỳ vọng **bây giờ**, không phải sau 20 tuần.
>
> Điểm cộng cho lựa chọn 15%: cùng nguồn đó nêu nam duy trì được lâu dài trong khoảng **10–20% mỡ**, và dưới **8–10%** thì năng lượng, cơn đói và libido đều xấu đi. **Đích 15% nằm giữa vùng duy trì được** — đúng với yêu cầu "nét vừa phải, giữ sức khỏe ổn định" của bạn.
>
> Phân bố mỡ vẫn khác nhau theo từng người: có người thấy múi ở 18%, có người phải xuống 12%. Thang trên là điểm tham chiếu, không phải cam kết. Nếu tới 15% mà chưa như hình, đó là giải phẫu cá nhân chứ không phải kế hoạch sai — và câu hỏi lúc đó là có đáng đi tiếp xuống 12–13% không, với chi phí thật về hiệu suất, giấc ngủ và mức độ dễ chịu khi ăn.

### Ba ràng buộc của user — kiểm tra từng cái

User nêu 2026-09-16: muốn nét hơn nhưng **giữ sức khỏe ổn định, không mất sức, không quá tải khớp**, và chỉ cần "nét vừa phải".

| Ràng buộc | Đã xử lý chưa | Bằng cách nào |
|---|---|---|
| Sức khỏe ổn định | **Có** | 15% nằm trong vùng khỏe mạnh cho nam. Vùng bắt đầu có rủi ro về hormone, giấc ngủ, tâm trạng nằm thấp hơn nhiều. Mục tiêu "nét vừa phải" và 15% là khớp nhau |
| Không mất sức | **Có** | Thâm hụt chỉ ~14%; protein 2,17 g/kg; Top set SBD giữ tiếp xúc tải nặng hàng tuần; e1RM là chốt chặn — dốc xuống 2 tuần liên tiếp thì **nâng calo trước**, cắt volume sau |
| Không quá tải khớp | **Có** | BO Squat đã chặn ở 2 hiệp; trần RPE 8,5 và sàn rep; không có HIIT; buổi 5 không có compound nặng; bài máy có tựa lưng gánh phần volume phì đại |

**Rủi ro thật với ba ràng buộc này không phải mỡ hay tạ — là giấc ngủ.** Xem mục *Tập buổi sáng*. Thiếu ngủ trong thâm hụt phá đúng hai thứ bạn xếp ưu tiên số 1: sức mạnh và khối cơ.

### Đo tiến độ tới 15% bằng gì

Cân **không** phải chỉ số chính ở khối này — trong recomp cân có thể gần đứng yên trong lúc mỡ vẫn giảm.

| Chỉ số | Cách đo | Vì sao |
|---|---|---|
| **Vòng eo** (chính) | Ngang rốn, sáng sớm, sau khi đi vệ sinh, trước khi ăn. Cùng một chỗ, cùng cách kéo thước. 1 lần/tuần | Tín hiệu rõ nhất cho mỡ bụng, ít nhiễu hơn cân |
| Trung bình cân 7 ngày | Cân mỗi sáng, lấy trung bình tuần | Chỉ đọc xu hướng, không đọc từng ngày |
| Ảnh | 1 lần/tháng, **cùng ánh sáng, cùng giờ, cùng tư thế, không pump** | Thay đổi diễn ra chậm hơn khả năng nhận ra bằng mắt hằng ngày |
| Đường e1RM | Sau mỗi Top set | Chốt chặn cho "không mất sức" |

Toolkit **chưa có** công thức đã kiểm chứng để quy đổi vòng eo sang %mỡ, nên không đặt một con số eo mục tiêu. Thứ đáng theo dõi là **xu hướng eo của chính bạn theo tuần**.

Cân bioimpedance (cân điện tử đo mỡ) có sai số lớn và dao động theo mức nước trong người — dùng được để xem xu hướng, **không** dùng làm con số chốt. Muốn một con số thì DEXA hoặc kẹp da bởi người có kinh nghiệm, và vẫn phải ghi sai số.

### Bước 3 — Macro

`protein_basis = body_weight` (76 kg). Chưa có ước tính khối nạc nên **không dùng** khoảng g/kg khối nạc.

| Macro | Mục tiêu | g/kg | Năng lượng |
|---|---|---|---|
| Protein | **165 g** | 2,17 g/kg | 660 kcal |
| Fat | **70 g** | 0,92 g/kg | 630 kcal |
| Carbohydrate | **227 g** | 2,99 g/kg | 908 kcal |
| **Tổng** | | | **2.198 kcal** |

```text
Kiểm tra tổng năng lượng:
  165 × 4 = 660
   70 × 9 = 630
  227 × 4 = 908
  ------------------
  Tổng    = 2.198 kcal  ✓ khớp mục tiêu ~2.200
```

**Căn cứ từng macro:**

- **Protein 2,17 g/kg** — ISSN 2017 đặt 1,4–2,0 g/kg cho đa số người tập; Viện Dinh dưỡng nêu 1,6–2,4 g/kg **khi giảm cân**. Ở đầu cao của khoảng vì đang trong thâm hụt và ưu tiên là giữ cơ. Phân bổ đều 4 bữa ~40 g, ưu tiên có một cữ quanh buổi tập. Tổng ngày và phân bố đều quan trọng hơn cửa sổ vài phút.
- **Fat 0,92 g/kg** — nằm trong khoảng 0,5–1,5 g/kg mà review off-season gợi ý. Không hạ dưới ~0,6 g/kg để lấy chỗ cho carb.
- **Carb 2,99 g/kg** — là phần năng lượng còn lại. Thấp hơn khoảng ≥3–5 g/kg thường xét ở giai đoạn nhu cầu cao; **đây là đánh đổi có ý thức của việc ăn thâm hụt**, không phải sai sót. Nếu hiệu suất buổi tạ tụt trước khi cân giảm, carb là biến nên nâng trước (xem bảng dự phòng).

**Ngày tập và ngày nghỉ dùng cùng mức ăn** để dễ tuân thủ. Bỏ một buổi tập **không** dẫn đến nhịn bữa.

### Bước 4 — Chất lượng, nước, supplement

- Ưu tiên thực phẩm nguyên bản, đủ rau và chất xơ. Quy đổi 4/4/9 là tính gần đúng; nhãn thực phẩm chênh vì làm tròn, chất xơ và phương pháp tính.
- **Nước:** nhu cầu khác nhau theo mồ hôi, thời tiết, thời lượng. Không có một số lít đúng cho mọi người. Ước tính thực địa: `mồ hôi mất (L) ≈ cân trước − cân sau (kg) + nước uống (L) − nước tiểu (L)`.
### Supplement — xếp theo mức bằng chứng

**Thứ tự xử lý của toolkit (knowledge 18.1):** năng lượng → protein → macro → chất lượng khẩu phần → timing → **supplement** → theo dõi. Supplement là bước **áp chót**. Không có gì ở đây bù được cho việc ăn thiếu protein hoặc ngủ thiếu.

| Ưu tiên | Chất | Liều | Bằng chứng | Ghi chú cho bạn |
|---|---|---|---|---|
| **1** | **Creatine monohydrate** | **3–5 g/ngày**, bất kỳ lúc nào | **[E]** ISSN position stand | Rẻ nhất, bằng chứng mạnh nhất. Không bắt buộc loading. **Ghi ngày bắt đầu** — tăng nước trong cơ làm cân nhích lên, đừng đọc nhầm thành tăng mỡ. Khoảng 25% người không đáp ứng |
| **2** | **Whey protein** | Theo nhu cầu | **[E]** ISSN protein | **Không bắt buộc**, chỉ là công cụ tiện lợi. Với bạn nó thực dụng: 165 g protein trong 2.200 kcal là chặt, và cữ 8h00 sau tập dễ đạt bằng whey |
| **3** | **Caffeine** | **3–6 mg/kg** = **228–456 mg**. Tối thiểu có thể hiệu quả ~2 mg/kg = 152 mg | **[E]** [ISSN 2021](../tai-nguyen/2026-09-17/U15-supplement-caffeine-bcaa.md) | Xem cảnh báo riêng bên dưới |
| **—** | **BCAA** | **Không dùng** | **[E]** [Wolfe 2017](../tai-nguyen/2026-09-17/U15-supplement-caffeine-bcaa.md) | Xem lý do bên dưới |
| **—** | Beta-alanine, citrulline, HMB, các thành phần pre-workout khác | **Chưa tra** | — | Toolkit chưa có dữ liệu. Không khuyến nghị cũng không bác bỏ |

#### Caffeine và pre-workout — dùng được, nhưng có một bẫy riêng cho bạn

ISSN 2021 xác nhận **pre-workout có chứa caffeine cải thiện cả hiệu suất yếm khí lẫn ưa khí**. Với bài tạ, lợi ích ở sức mạnh và sức bền cơ là **nhỏ đến vừa** — không phải chất thay đổi cuộc chơi.

- **Liều:** bắt đầu ở đầu thấp, **228 mg** (3 mg/kg). Không cần tới 456 mg. **Đừng chạm 684 mg** (9 mg/kg) — liều đó đi kèm tỉ lệ tác dụng phụ cao mà không thêm hiệu quả.
- **Thời điểm:** thường dùng 60 phút trước tập. Buổi của bạn 6h00, dậy 5h00–5h15 → uống ngay khi dậy là hợp lý.
- **Về giấc ngủ:** uống lúc 5h sáng là thời điểm **xa giờ đi ngủ nhất trong ngày** của bạn, nên lo ngại về giấc ngủ mà ISSN nêu ở mức thấp nhất có thể. Nhưng cùng nguồn đó ghi **khác biệt giữa người với người là có thật** — nếu thấy khó ngủ hoặc bồn chồn, giảm liều hoặc bỏ.

> **Bẫy thật sự — và nó gắn thẳng vào blocker D3 của bạn.** ISSN điểm 8: caffeine **có thể cải thiện hiệu suất trong điều kiện thiếu ngủ**. Nghe như lợi ích, nhưng với bạn nó là rủi ro: bạn đang thử khung 6h sáng mà **chưa biết có dời được giờ ngủ hay không**. Caffeine sẽ làm buổi tập thiếu ngủ *cảm thấy* ổn, trong khi nợ hồi phục vẫn tích. Đường e1RM và nhật ký sẽ lộ ra sau vài tuần, lúc đó đã mất thời gian.
>
> **Nên: trong 2 tuần thử giấc ngủ, đừng dùng caffeine để che một đêm ngủ kém.** Ghi giờ ngủ trước, đọc số liệu sau. Dùng caffeine cho buổi nặng khi **đã ngủ đủ** thì không sao.

Caffeine có dung nạp — cân nhắc chỉ dùng ở buổi nặng thay vì mọi buổi.

#### BCAA — khuyến nghị: bỏ

BCAA chỉ gồm 3 trong 9 axit amin thiết yếu. Muốn tổng hợp protein cơ mới thì cần **đủ cả 9** — nạp riêng BCAA thì sáu cái còn lại chỉ có thể lấy từ chính việc **phân giải protein cơ**.

[Wolfe 2017](../tai-nguyen/2026-09-17/U15-supplement-caffeine-bcaa.md) tìm khắp y văn và **không thấy nghiên cứu nào trên người** đo được đáp ứng tổng hợp protein cơ với BCAA uống đơn thuần. Hai nghiên cứu truyền tĩnh mạch đều cho thấy BCAA **giảm cả tổng hợp lẫn phân giải** — tức giảm luân chuyển, và trạng thái dị hóa vẫn tiếp diễn. Kết luận của tác giả: khẳng định BCAA tạo đáp ứng đồng hóa ở người là **không có cơ sở**.

**Với bạn cụ thể:** bạn đã ăn **165 g protein/ngày** từ nguồn đầy đủ. BCAA không thêm được gì mà protein bạn đang ăn chưa cung cấp. Tiền đó để mua creatine hoặc whey thì đúng chỗ hơn.

#### Vẫn giữ nguyên

Ưu tiên thực phẩm. Toolkit **không** tự thêm chất "đốt mỡ", hormone, sắt hay vitamin D liều điều trị, hay thuốc giảm đau để hoàn thành buổi tập.
- **Thực đơn mẫu cố định:** chưa lập. User tự chọn/tính món ăn ngoài. Nếu muốn thực đơn cố định, cần xác nhận trước danh sách món thực sự kiếm được và ngân sách — toolkit không làm bộ chọn món hằng ngày.

### Bước 5 — Nhánh dừng tự động giảm ăn

Dừng việc hạ calo và đề nghị đánh giá phù hợp nếu có: giảm cân ngoài ý muốn, mệt kéo dài, chấn thương do stress lặp lại, hành vi ăn đáng lo, hoặc sa sút chức năng sinh hoạt. Không tự kết luận REDs, và không dùng ngưỡng kcal đơn lẻ làm bộ chẩn đoán.

### Bước 6 — Kế hoạch hậu ăn kiêng và metabolic adaptation

> **Hạng nguồn: [C] — ý kiến chuyên gia**, từ [U13](../tai-nguyen/2026-09-16/U13-nippard-get-lean-stay-lean.md). Chưa có guideline hay nghiên cứu đi kèm. Knowledge của toolkit **chưa có** mục nào về chiến lược hậu ăn kiêng, nên đây là phần lấp khoảng trống chứ không phải ghi đè nguồn mạnh hơn.

**Vì sao 2.200 kcal sẽ không giữ nguyên mức thâm hụt suốt khối.** Khi cân giảm, tổng năng lượng tiêu hao giảm theo trên cả bốn đường: REE giảm vì cơ thể nhỏ đi · năng lượng cho mỗi đơn vị vận động giảm vì cơ thể hiệu quả hơn · NEAT giảm vì ít vận động tự phát hơn · TEF giảm vì ăn ít hơn. Thâm hụt ~350 kcal của tuần 5 sẽ **không còn là 350 kcal** ở tuần 15.

Đây chính là cơ chế đằng sau dòng *"cân đứng yên 3 tuần → giảm 100–200 kcal"* ở bảng dự phòng. Trước đây dòng đó chỉ có quy tắc; giờ có lý do.

**Khi kết thúc một pha thâm hụt — làm gì:**

| Bước | Làm | Không làm |
|---|---|---|
| 1 | Về **maintenance ngay ngày hôm sau**: **+200–600 kcal** so với mức cuối kỳ. Với bạn: 2.200 → **2.400–2.800 kcal**, nghiêng về đầu cao vì bạn không hề crash diet | **Không reverse dieting** — tăng nhỏ giọt vài chục kcal mỗi tuần chỉ kéo dài cảm giác đói mà không có lợi ích tương ứng |
| 2 | Coi maintenance là **một dải động**, không phải một con số. Tiếp tục nhích calo lên **đỉnh của dải mà cân trung bình vẫn giữ** | Không coi con số đầu tiên tìm được là maintenance cố định |
| 3 | **Vẫn cân 2–3 lần/tuần** trong giai đoạn duy trì, lấy trung bình | Không bỏ hẳn việc theo dõi sau khi đạt đích — đó là lúc kết quả hay mất nhất |

Lý do nhích lên đỉnh dải **không phải** "đẩy chuyển hóa" mà là: ăn được nhiều hơn thì đỡ gò bó, dễ duy trì, và hiệu suất buổi tập tốt hơn — quan trọng nếu sau đó vào pha lean gaining.

## Progression và phương án dự phòng

| Nếu | Làm | Giới hạn/đánh đổi | Review/trở lại |
|---|---|---|---|
| **Top set đủ rep, RPE thấp hơn ghi** | Tuần sau +2,5 kg so với số in | Vẫn giữ trần RPE 8,5 và sàn rep | Mỗi buổi |
| **Top set vượt RPE ghi** | Giữ nguyên tải, lặp lại tuần sau; bỏ qua mức tăng của ma trận | Chậm hơn ma trận — chấp nhận được | Buổi kế |
| **BO hiệp cuối ra RIR 4** | Tuần sau +2,5 kg | — | Buổi kế |
| **BO hiệp đầu đã đúng RIR ghi** | **Cắt 1 hiệp, giữ tải.** Không hạ tải để cố đủ hiệp | Mất 1 hiệp volume tuần đó | Buổi kế |
| **Không đủ 4 điều kiện nhận THÊM 1 HIỆP** | Giữ số hiệp cũ; các thông số khác vẫn theo ma trận | Tổng volume tuần thấp hơn thiết kế | Tuần sau |
| **Thiếu giờ (buổi chỉ còn 45–55 phút)** | Theo **Thứ tự cắt** ở mục Lịch hiện hành: cắt phụ trợ thân dưới trước, không đụng Top set/BO, Machine Chest Press, Incline và ABS | Volume nhóm cơ nhỏ giảm tuần đó. **Không bù set vào buổi khác** | Buổi kế theo ma trận bình thường |
| **Lỡ hẳn 1 buổi** | Giữ đúng **thứ tự** buổi, đẩy lùi lịch. Không nhồi 2 buổi liền kề | Tuần đó chỉ 3 buổi | Tuần sau |
| **Lỡ hẳn 1 tuần** | Quay lại ở tuần đã lỡ, **không nhảy cóc**. Nếu nghỉ >2 tuần, lùi 1 tuần trong ma trận | Kéo dài khối quá 12 tuần lịch | Đánh giá ở check-in |
| **Thiếu thiết bị (máy bận/hỏng)** | Dùng bảng Bài thay thế, ưu tiên 1 trước. Áp nguyên hiệp × rep × RIR tuần hiện tại | Đổi bài tạo chuỗi dữ liệu mới → **giữ hết meso**, không đổi qua lại | Cuối meso |
| **Hiệu suất giảm 2 buổi liên tiếp, hoặc RPE tăng bất thường ở cùng tải** | Chọn **một**: nâng calo về duy trì 3–5 ngày **hoặc** kéo deload lên sớm. **Ưu tiên calo trước** vì đang trong thâm hụt | Chậm tiến độ giảm mỡ 3–5 ngày | Đánh giá lại sau 1 tuần |
| **e1RM dốc xuống 2 tuần liên tiếp** | Nâng calo về duy trì (~2.550) trong 3–5 ngày **trước khi** nghĩ đến cắt volume | Tốc độ giảm mỡ dừng lại | Check-in kế |
| **Cân đứng yên 3 tuần liên tiếp với nhật ký đầy đủ** | Giảm **100–200 kcal/ngày**, một bước một lần. Hoặc tăng số bước. **Không đổi calo, cardio và volume cùng lúc** | Nếu cắt sâu hơn, rủi ro cho ưu tiên #1 | Sau 2–3 tuần |
| **Cân giảm nhanh hơn 0,6%/tuần** | Nâng calo lên ~2.400. Giảm nhanh hơn mục tiêu **không** phải điểm cộng ở phase này | — | Check-in kế |
| **Cân đổi mạnh trong 1–3 ngày** | **Giữ kế hoạch.** Kiểm tra muối, carb, tiêu hóa, creatine, điều kiện cân. Chưa coi là thay đổi mỡ | — | — |
| **Ngủ kém hoặc stress công việc cao 1 tuần** | Bỏ buổi 5; cân nhắc hạ 1 hiệp ở BO. Ăn duy trì nếu kéo dài | Mất 1 lần/tuần cho vai bên, vai sau, tay và abs | Check-in |
| **Ngủ dưới 7 giờ từ 3 đêm trở lên trong tuần** (rủi ro chính của khung sáng) | Bỏ buổi 5 **và** ăn ở mức duy trì. Nếu lặp lại 2 tuần → cân nhắc quay về khung chiều | Dừng tiến độ giảm mỡ | Mốc đánh giá 2 tuần |
| **Một bài gây khó chịu nhẹ, không có dấu hiệu cảnh báo** | Đổi sang bài thay thế ưu tiên 1 **trước**, rồi mới giảm tải. **Mỗi lần chỉ đổi một biến số.** Nếu chưa đủ → lộ trình tái tải 3 bước dưới | Các bài khác vẫn chạy bình thường theo ma trận | Quy tắc 24 giờ |
| **Đau tăng dần, tê, yếu cơ tiến triển, sưng lớn, đau ngực/khó thở, chóng mặt kéo dài** | **Dừng bài liên quan và đi khám.** Vượt phạm vi tự điều chỉnh và vượt phạm vi toolkit | — | Sau khi có đánh giá chuyên môn |

### Lộ trình tái tải 3 bước

Áp dụng khi có khó chịu nhẹ **nhưng không có dấu hiệu cảnh báo** ở hàng cuối bảng trên. Nguyên tắc: tìm phiên bản nhẹ nhất mà vẫn thực hiện được với kỹ thuật chấp nhận được, thay vì nghỉ hoàn toàn.

| Bước | Làm gì | Mục đích | Cổng để đi tiếp |
|---|---|---|---|
| 1 — Isometric | 3–5 hiệp × 20–30 giây giữ tĩnh, không đau (split-squat hold, wall sit, dead-hold nửa tầm, giữ tĩnh đáy Bench tải nhẹ) | Tạo tải có kiểm soát không cần chuyển động khớp | 2–5 buổi, khi giữ tĩnh không gây đau tăng |
| 2 — Tempo lift | Cùng bài (hoặc biến thể ưu tiên 1), tải 50–60% bình thường, nhịp 3 giây xuống – 3 giây lên, 3 × 5–6 | Đưa lại chuyển động toàn ROM dưới kiểm soát | 1–2 tuần, khi không có triệu chứng quá 24 giờ |
| 3 — Tăng tải dần | Tăng ~10% mỗi buổi hoặc mỗi tuần, quay dần về ô ma trận. **Chỉ một biến số mỗi lần** | Khôi phục khả năng chịu tải | Khi đạt lại tải ma trận ở đúng RIR mà không có triệu chứng |

**Quy tắc 24 giờ là cổng giữa mọi bước:** khó chịu trong buổi ở mức chịu được là chấp nhận, miễn là về trạng thái nền trong khoảng 24 giờ. Sáng hôm sau đau hơn → **lùi lại một bước**, đừng tiến. Isometric là công cụ thường hữu ích, **không phải phác đồ đúng cho mọi tình trạng**.

## Check-in

- **Nhịp: 7 ngày** (user chọn). Ngày check-in đầu tiên: **7 ngày sau ngày effective_from** — chưa chốt vì chương trình còn ở trạng thái draft.
- **Mốc đánh giá lớn:** cuối tuần 6 và cuối tuần 12 (số đo, ảnh, đường e1RM, quyết định phase kế tiếp).
- Kỳ review khác thời điểm ghi dữ liệu: dữ liệu ghi hằng ngày/hằng buổi, review diễn ra mỗi 7 ngày.

**Dữ liệu cần theo mục tiêu** (cho phép "chưa biết" — không giả định tuân thủ 100%):

| Tần suất | Ghi gì | Vì sao |
|---|---|---|
| Mỗi buổi | Tải – hiệp – rep – RPE/RIR từng bài; e1RM từ Top set; có nhận THÊM 1 HIỆP không | Nguồn dữ liệu chính để chỉnh tải. Thiếu cái này thì mọi điều chỉnh khác là đoán |
| Mỗi sáng | Cân nặng (dùng **trung bình 7 ngày**); mức khó chịu cơ khớp 0–10 | Một ngày cân không đại diện xu hướng mỡ |
| Mỗi tuần | Trung bình cân so tuần trước; **vòng eo** (cùng thời điểm, cùng cách đo); giấc ngủ; số bước | Vòng eo là KPI chính của phase này |
| Tuần 6 và 12 | Số đo, ảnh, e1RM (AMRAP @RPE 8 tùy chọn ở tuần 12) | Mốc quyết định phase |

**Tín hiệu recomp đúng hướng:** eo giảm dần **+** logbook accessory tăng **+** e1RM đi ngang hoặc nhích lên — kể cả khi cân gần đứng yên.

**Chưa xác nhận:** user chưa cho biết thực tế ghi được bao nhiêu trong bảng trên. Hỏi ở check-in đầu; nếu không ghi nổi phần nào thì rút bộ dữ liệu xuống mức làm được thật, vì nhật ký thiếu nhiều thì không đủ cơ sở kết luận và kết quả hợp lệ sẽ là **giữ nguyên, thu thập thêm**.

Log thực tế lưu ở [logs/](../logs/). **Không chép kế hoạch thành completed** — chỉ ghi những gì đã thực sự làm.

## Nguồn và giới hạn

### Mục knowledge đã dùng

| Nội dung | Mục knowledge | Grade |
|---|---|---|
| Volume và hypertrophy; failure không bắt buộc; không có RIR tối ưu cho mọi người | 17.2 (ACSM 2026) | [E] |
| RPE ↔ RIR là ước lượng theo một thang cụ thể; volume theo lift khác volume theo cơ; đổi ROM/tempo/dụng cụ tạo chuỗi dữ liệu mới | 17.4 | [H] |
| Quy trình thiết kế lịch cơ sở; bản đồ ưu tiên khi cắt lịch | 17.5 | [H] |
| Double progression cho bài phụ | 17.6 | [H] |
| Trình tự điều tra khi chững; deload là giảm stress có chủ đích, không bắt buộc theo chu kỳ cố định | 17.7 | [H] |
| Mô hình block/DUP là cách tổ chức, không phải bằng chứng mô hình nào tốt nhất | 17.10 | [H] |
| Mifflin–St Jeor dự đoán REE, không phải TDEE; TDEE cho khoảng thay vì độ chính xác giả | 18.2 | [E]/[H] |
| Thâm hụt 10–15% làm giả định khởi đầu; recomp không hứa chắc cho mọi người | 18.3 | [E]/[H] |
| Protein 1,4–2,0 g/kg (ISSN); 1,6–2,4 g/kg khi giảm cân (Viện Dinh dưỡng); giữ đúng mẫu số | 18.4 | [E] |
| Fat 0,5–1,5 g/kg; carb nhận phần còn lại; kiểm tra tổng năng lượng | 18.5 | [E]/[H] |
| Creatine 3–5 g/ngày, không bắt buộc loading | 18.7 | [E] |
| Nhánh dừng tự động giảm ăn (REDs) | 18.8 | [H] |
| Điều chỉnh 100–200 kcal mỗi lần; không đổi nhiều biến cùng lúc | 18.9 | [H] |
| Cardio phối hợp với tạ; mobility có mục tiêu; ngủ và mệt | 22.2, 22.3, 22.4 | — |
| Quy tắc 24 giờ, entry point và isometric | 19.10 | [H] |

### Tài nguyên người dùng đã đối chiếu

Mục lục đầy đủ kèm thang hạng và mức đã đọc từng nguồn: [tai-nguyen/00-MUC-LUC.md](../tai-nguyen/00-MUC-LUC.md).

**Đợt 1 — sáu video user cung cấp 2026-09-16.** Hạng **transcript — nguồn thấp nhất**, không ghi đè guideline (hợp đồng §5). Bản đối chiếu ở [AUDIT-doi-chieu.md](../tai-nguyen/2026-09-16/AUDIT-doi-chieu.md).

| Mã | Nguồn | Dùng vào đâu |
|---|---|---|
| [U09](../tai-nguyen/2026-09-16/U09-smallgym-5-bi-quyet-giam-mo.md) | SmallGym — 5 bí quyết giảm mỡ | Xác nhận: ưu tiên bước chân hơn cardio; không đổi bài liên tục |
| [U10](../tai-nguyen/2026-09-16/U10-smallgym-bao-nhieu-buoi-tuan.md) | SmallGym — bao nhiêu buổi/tuần | Xác nhận: mục tiêu theo tuần; quá tải không tuyến tính |
| [U11](../tai-nguyen/2026-09-16/U11-smallgym-xep-hang-22-yeu-to.md) | SmallGym — xếp hạng 22 yếu tố | Xác nhận: thâm hụt 10–20%; protein 1,8–2,2 g/kg |
| [U12](../tai-nguyen/2026-09-16/U12-nippard-body-recomposition.md) | Nippard — body recomposition | Xác nhận: volume 10–20 set/nhóm/tuần; **giấc ngủ** (Wing 2018) |
| [U13](../tai-nguyen/2026-09-16/U13-nippard-get-lean-stay-lean.md) | Nippard — get lean & stay lean | **Nguồn của Bước 6**; xác nhận tốc độ giảm chậm |
| [U14](../tai-nguyen/2026-09-16/U14-nippard-get-abs.md) | Nippard — get abs | Thang %mỡ ở cảnh báo kỳ vọng; trần rep ABS B |

**Đợt 2 — nguồn ngoài cho triệu chứng và mobility**, [U16](../tai-nguyen/2026-09-16/U16-nguon-ngoai-trieu-chung-va-mobility.md): NHS (ngưỡng đi khám vì đau gối) · JOSPT CPG đau lưng dưới · directional preference · **2 meta-analysis foam rolling**. Mới đọc tóm tắt, chưa đọc toàn văn.

**Đợt 3 — supplement 2026-09-17**, [U15](../tai-nguyen/2026-09-17/U15-supplement-caffeine-bcaa.md): **[E]** ISSN position stand về caffeine (PMID 33388079) và Wolfe về BCAA (PMID 28852372). Đọc abstract đầy đủ.

**Đã bác bỏ:** công thức calo `cân(lb) × 10–12` của U14 (ra 1.676–2.011 kcal, thâm hụt 21–34% — vượt xa khoảng 10–20% mà chính các nguồn kia khuyến nghị, và ngược ưu tiên giữ cơ). **Chưa nhập:** xếp hạng A–F của U11, phát biểu "hấp thụ 100 g protein một bữa", "GI hạng A", "tạ + cardio cho eo nhỏ hơn" — đều không truy được nghiên cứu gốc.

### Heuristic riêng của chương trình này (không phải kết luận từ nguồn)

- Trần RPE 8,5 + sàn rep (SBD 4/4/3) làm ranh giới giữ khối là hypertrophy. Đây là **lựa chọn vận hành** để khối này không lén thành peaking trong thâm hụt, không phải ngưỡng sinh học.
- BO = Top −10% và "thêm hiệp không thêm tạ": cách quản lý một đường tiến độ duy nhất, chọn để giảm nhiễu dữ liệu.
- Bốn điều kiện nhận THÊM 1 HIỆP: heuristic tự đặt, chưa được kiểm chứng.
- Hệ số 1,5 cho TDEE: giả định, sẽ được cân nặng và phản hồi kiểm tra trong 2–3 tuần đầu.
- Xếp Chest-Supported Row ở vị trí 2 của buổi 2 để ngực/tay sau có 8–10 phút hồi phục trước Machine Chest Press: heuristic sắp xếp, không phải phát hiện từ nghiên cứu.

### Giới hạn phải giữ

- Các kết luận ACSM 2026 đến **phần lớn từ người ít kinh nghiệm**; user ở đây là người tập trên 2 năm. Không tự động áp nguyên.
- Autoregulation (RPE) **không** được chứng minh là luôn tốt hơn %1RM. Chương trình dùng cả hai và để RPE thắng khi mâu thuẫn — đó là lựa chọn vận hành cho hoàn cảnh thâm hụt, không phải tuyên bố RPE ưu việt.
- Bảng RPE → e1RM là ước lượng, **không phải phép đo**. Sai số lớn ở người chưa quen đánh giá nỗ lực.
- Khung joint-by-joint và ba phép thử là **heuristic để đặt câu hỏi**, không phải chẩn đoán. Một khớp cứng không chắc là nguyên nhân duy nhất của đau ở khớp khác.
- Kho nguồn đầy đủ **không** đồng nghĩa đã kiểm chứng mọi phát biểu trong plan kế thừa của user.
- Chương trình này không chứng minh tính đúng y khoa và không thay đánh giá của bác sĩ/chuyên gia vật lý trị liệu.

### Blocker — chưa đủ điều kiện xuất

| Mã | Blocker | Cần gì để gỡ |
|---|---|---|
| ~~**L1**~~ | **Đã gỡ 2026-09-16.** 25/25 bài chính có link đã tra; 26 bài thay thế có link; 26 bài thay thế còn lại chưa tra. | Xong cho bài chính. Phần thay thế còn thiếu: tra tiếp khi cần — danh sách ở cuối [exercise-links.md](../exercise-links.md). |
| **D1** | 1RM 170/130/200 chưa rõ ngày đo và phương pháp. | User xác nhận ở check-in đầu, hoặc dùng e1RM từ Top set tuần 1 để hiệu chỉnh lại toàn bộ kg in trong ma trận. |
| **D2** | Chưa có baseline vòng eo và cân trung bình 7 ngày. | Thu thập trong tuần 1. Chưa diễn giải tốc độ giảm trước khi có. |

**L1 đã gỡ.** Còn D1 và D2 — cả hai thu thập được trong tuần 1 và không chặn việc bắt đầu tập. Program-001 vẫn giữ `draft` vì **user chưa duyệt**, không phải vì thiếu link.

## Phê duyệt

| Ngày | Quyết định | Phạm vi |
|---|---|---|
| 2026-09-16 | **ĐÃ DUYỆT VÀ KÍCH HOẠT.** User chốt trực tiếp. | Toàn bộ program-001 rev 1, gồm bản điều chỉnh tạm thời cho gối/lưng |

**Điểm vào: tuần 5** của ma trận (user đã hoàn thành tuần 1–4 ngoài project). `effective_from` = 2026-09-16.

**Check-in đầu tiên: 2026-09-23** (nhịp 7 ngày).

**Đánh giá bản điều chỉnh tạm thời: 2026-10-07** (3 tuần).

Chương trình đang `active`. Mọi sửa lớn từ đây phải **snapshot bản hiện tại trước**, tạo draft riêng trong `programs/drafts/`, và được duyệt trước khi thay bản active — theo [operating contract](../../../training-toolkit/workflows/operating-contract.md) mục 2.

## Lịch sử thay đổi

| Revision/ngày | Trước → sau | Lý do/dữ liệu | Thời hạn | Trạng thái/phê duyệt | Chi tiết |
|---|---|---|---|---|---|
| rev 1 / 2026-09-16 | (chưa có) → program-001 draft | Intake 2026-09-16. Kế thừa cấu trúc plan 12 tuần user đang chạy; bổ sung số dinh dưỡng, buổi 5 phục hồi, nhịp check-in 7 ngày, bảng dự phòng, mục nguồn/giới hạn. | Khối 12 tuần | draft — chưa duyệt | — |
| rev 1 / 2026-09-16 | link: trống → 25/25 bài chính có link | User cấp quyền tìm ngoài. Không đổi nội dung tập hay dinh dưỡng — chỉ điền cột link. | — | draft — chưa duyệt | [exercise-links.md](../exercise-links.md) |
| rev 1 / 2026-09-16 | BO Squat 3–4 hiệp → **2 hiệp** (T2,3,4,5,7,8,9,10,11) | **Phản hồi thực tế sau 4 tuần chạy:** thêm hiệp BO Squat gây hết sức từ bài đầu. Kiểm tra lại: BO 120 kg = 70,6% 1RM, 3×8 sau Top set → hiệp 3 rơi về RIR 0; tổng 30 rep ở ≥70% trong một bài. Lỗi thiết kế, không phải vấn đề người tập. | Cả khối | draft — chưa duyệt | Tùy chọn 3 hiệp ở Top −15% đã in trong ma trận |
| rev 1 / 2026-09-16 | khung chiều ≤120 phút → **sáng 6h00–7h30, trần cứng 90 phút** | User đổi giờ tập. Kèm: khởi động dài hơn, thêm 1 bước ramp-up, hạ trần RPE 0,5 trong 2 tuần đầu, bố trí lại bữa ăn, cảnh báo giấc ngủ. | Từ khi đổi giờ | draft — chưa duyệt | Mục *Tập buổi sáng* |
| rev 1 / 2026-09-16 | điểm vào tuần 1 → **tuần 5** | User đã hoàn thành tuần 1–4 ngoài project. | — | draft — chưa duyệt | — |
| rev 1 / 2026-09-16 | 4 buổi → **5 buổi** | Trần cứng 90 phút của khung sáng khiến buổi 2 và 4 chỉ còn 6–13 phút đệm; các bài cuối buổi hay bị cắt. Tách vai/tay/abs sang buổi 5: tổng volume gần như không đổi, mọi buổi còn ≥14 phút đệm. | Cả khối | draft — chưa duyệt | Bảng *Kiểm tra tần suất* |
| rev 1 / 2026-09-17 | Mở rộng mục **Supplement** — bảng ưu tiên theo mức bằng chứng; caffeine [E] ISSN 2021 với liều quy theo cân; **BCAA: khuyến nghị bỏ** [E] Wolfe 2017 | User hỏi về pre-workout, BCAA và thực phẩm bổ sung. Kho chỉ có creatine và whey; không có dòng nào về phần còn lại. Đã tra PubMed, lưu [U15](../tai-nguyen/2026-09-17/U15-supplement-caffeine-bcaa.md). Không đổi calo, macro, bài tập. **Bản Word thành stale.** | — | active | [U15](../tai-nguyen/2026-09-17/U15-supplement-caffeine-bcaa.md) |
| rev 1 / 2026-09-16 | **DUYỆT VÀ KÍCH HOẠT** · bỏ mục F (lộ trình tái tải), G (hỏi đáp deload) và toàn bộ mục Prehab khỏi chương trình · rút gọn mục E còn con trỏ sang nhật ký | User chốt. Nội dung bị bỏ là phần giải thích và prehab thêm vào cuối phiên, không phải nội dung tập. **Lộ trình tái tải 3 bước vẫn còn** ở mục *Progression và phương án dự phòng*. F1–F3 chuyển hẳn sang [nhật ký](../logs/nhat-ky-trieu-chung.md). | — | **active** | — |
| rev 1 / 2026-09-16 | **Bỏ buổi prehab riêng. Giữ 5 buổi/tuần như cũ.** Prehab dồn vào **tuần deload 6 và 12**; ba phép thử trả về buổi 5 | User: quá tải. Đúng — tôi chất chồng quá nhiều lớp trong một phiên. Bản gọn: prehab chỉ ở 2 chỗ — warm-up hằng buổi (đã có sẵn) và tuần deload. Ghi rõ đây là **liều thấp**, mang tính rà soát/bảo trì, không tạo thay đổi bền. | Cả khối | draft — chưa duyệt | — |
| ~~rev 1 / 2026-09-16~~ | ~~Prehab thành buổi riêng (buổi P, thứ Tư)~~ — **đã hủy cùng ngày** | Thay bằng dòng trên | — | huỷ | — |
| rev 1 / 2026-09-16 | **Prehab thành buổi riêng (buổi P, thứ Tư, ~32 phút)** thay vì rải vào nghỉ giữa hiệp · chuyển ba phép thử từ buổi 5 sang buổi P · thêm khối prehab tăng liều cho tuần deload | User: **không nhét được vào nghỉ giữa hiệp**, muốn một buổi bổ trợ riêng hoặc một tuần giảm tải. Khuyến nghị "không có buổi phụ" chỉ là ý kiến HLV [C]; knowledge 17.5 yêu cầu chốt lịch theo cái thực sự làm được. Buổi P rơi vào ngày nghỉ giữa tuần nên không lấy gì của buổi tạ. | Cả khối | draft — chưa duyệt | Mức bằng chứng [C]/[H], đã ghi rõ |
| rev 1 / 2026-09-16 | Thêm mục **Prehab — stability và mobility tích hợp** (4 vị trí, knee stability, scapular stability) | User làm rõ: mục đích là **prehab** — tăng stability/mobility để giảm rủi ro chấn thương và tập vững hơn, **không phải điều trị triệu chứng**. Yêu cầu này không cần chẩn đoán. Dựng theo [references/15](../../../training-toolkit/references/15-ket-hop-rehab-mobility-stability-vao-lichtap.md) và [references/05](../../../training-toolkit/references/05-core-stability.md), lọc qua knowledge 22.3. **Thời gian thêm ở phòng tập ≈ 0.** | Cả khối | draft — chưa duyệt | Mức bằng chứng [C]/[H], đã ghi rõ |
| rev 1 / 2026-09-16 | Thêm **lộ trình lấy lại chức năng sinh hoạt** (3 chức năng F1–F3) · làm rõ điều kiện kích hoạt **lộ trình tái tải 3 bước** · trả lời câu hỏi deload/rehab định kỳ | User hỏi vì sao không có bài rehab và có nên xếp tuần nhẹ + rehab định kỳ không. Knowledge 21.1 cho khung tiến theo **chức năng** — hợp lệ khi chưa có chẩn đoán. Knowledge 17.7 cảnh báo không lặp deload để trì hoãn đi khám. | 3 tuần | draft — chưa duyệt | — |
| rev 1 / 2026-09-16 | **Gỡ lệnh dừng tăng Deadlift/Squat/RDL**; thêm mục **Mobility, giãn cơ và foam roller** | User phản hồi: kỹ thuật ổn, không vòng lưng, tải hai bài đó lưng hoàn toàn ổn, và **đi tập đỡ đau hơn ở nhà**. Đúng với knowledge 21.1 (NICE NG59 — duy trì hoạt động; giữ vận động dung nạp được) và 19.7 (không biến nghỉ tương đối thành nghỉ mọi thứ). Thay lệnh cấm bằng **điều kiện qua quy tắc 24 giờ**. | 3 tuần | draft — chưa duyệt | — |
| rev 1 / 2026-09-16 | **Bản điều chỉnh tạm thời cho triệu chứng gối + lưng** (hiệu lực 2026-09-16, đánh giá lại 2026-10-07) | User khai bổ sung 2 cụm triệu chứng vốn bị bỏ sót ở intake. Sàng lọc 19.4 âm tính; user chưa khám được, muốn tập tiếp. Giảm gập thắt lưng có tải, dừng tăng Deadlift, bỏ Leg Extension, giảm tầm Walking Lunge, abs tăng bằng bài chống xoay. **Không phải phác đồ phục hồi.** | 3 tuần, có điều kiện trở lại | draft — chưa duyệt | [nhật ký](../logs/nhat-ky-trieu-chung.md) |
| rev 1 / 2026-09-16 | **bỏ luân phiên meso ở buổi 4** — Incline giữ cả 12 tuần, Machine Shoulder Press chuyển sang buổi 5 ở Meso 2; thêm **Thứ tự cắt** theo ưu tiên; tiêu chí thành công tách riêng nhóm ưu tiên | User siết mục tiêu 2026-09-16: **độ nét thân trên, nhất là mặt trước (ngực, bụng)**; thân dưới chỉ cần to lên; **giữ các bài competition** để không mất kỹ thuật và sức mạnh. Ngực rơi xuống 1 lần/tuần ở Meso 2 trở thành lỗi không chấp nhận được. **Tổng volume không tăng — chỉ đổi chỗ và đổi thứ tự ưu tiên khi cắt.** | Cả khối | draft — chưa duyệt | — |
| rev 1 / 2026-09-16 | siết kỳ vọng tại 15%; ABS B trần rep 15 → **20**; thêm **Bước 6 — kế hoạch hậu ăn kiêng** [C] | Đối chiếu 6 tài nguyên video user cung cấp — xem [AUDIT](../tai-nguyen/2026-09-16/AUDIT-doi-chieu.md). **Không đổi calo, macro, tốc độ giảm, bài compound hay ma trận** — sáu nguồn đều xác nhận các con số hiện tại nằm trong khoảng hợp lý. | — | draft — chưa duyệt | U13, U14 |
| rev 1 / 2026-09-16 | thêm mục **Mục tiêu 15% mỡ**, *Vì sao độ nét không đến từ việc tập*, *Đo tiến độ* | User nêu muốn từ ~20% về ~15%, "nét vừa phải", giữ sức khỏe/sức mạnh, không quá tải khớp. Số học cho thấy kế hoạch hiện tại đã đủ — **không đổi calo, không thêm cardio, không thêm buổi**. Chỉ bổ sung phần giải thích và cách đo. | — | draft — chưa duyệt | — |
| rev 1 / 2026-09-16 | không có abs → **abs 2 lần/tuần, có tải** | User hỏi vì sao không có abs. Lý do cũ (abs chỉ là bracing) đọc hẹp: cơ bụng dày hơn thì lộ rõ hơn ở cùng mức mỡ, và user quan tâm vùng eo. Thêm Cable Crunch (B2, gập cột sống) + Hanging Knee Raise và Pallof Press (B5, gập hông và chống xoay). | Cả khối | draft — chưa duyệt | Mục *Luật riêng cho abs* |

**Phương án đã cân nhắc và không chọn (cấu trúc):** gom toàn bộ lateral raise, curl, tricep và abs vào một buổi 5 duy nhất. Không chọn vì nó hạ vai bên, vai sau, tay trước, tay sau và abs xuống **1 lần/tuần** — mâu thuẫn với nguyên tắc 2 lần/tuần của chính chương trình, và vai là nhóm user xếp ưu tiên. Bản đang dùng giữ một lần ở buổi 2/4 và một lần ở buổi 5.

**Phương án đã cân nhắc và không chọn (dinh dưỡng):** thâm hụt sâu hơn (~20–25%, ~0,7–0,8%/tuần) để giảm mỡ nhanh hơn. Không chọn vì user chốt giữ cơ/sức là ưu tiên khi xung đột, và mức đó làm tăng rủi ro cho cả e1RM lẫn khối nạc trong một khối 12 tuần có volume cao ở tuần 9–11. Ghi lại ở đây để nếu user đổi ưu tiên thì có sẵn điểm so sánh.

## Bản xuất

| File | Ngày | Revision | Trạng thái |
|---|---|---|---|
| [program-001-r1-2026-09-17.docx](../exports/program-001-r1-2026-09-17.docx) | 2026-09-17 | 1 | **stale** — chương trình đã thêm mục Supplement sau khi xuất |

**Markdown này vẫn là nguồn chính.** Bản Word là bản mang đi dùng, không chứa toàn bộ lý giải và nguồn tham chiếu.

Khi chương trình đổi, bản Word thành **stale** và phải xuất lại. Nếu bạn sửa trực tiếp vào file Word, **báo lại để tôi đối chiếu và ghi ngược vào MD** — artifact không được coi là nguồn mới nhất.

**Mức kiểm tra đã thực hiện:** môi trường không có công cụ render `.docx`, nên tôi **chưa xem được trang thật**. Đã kiểm bằng cấu trúc: ZIP toàn vẹn · 6/6 part XML parse được · 30/30 hyperlink resolve, tất cả https · 18/18 bảng có header lặp qua trang · 3 section (dọc → ngang cho ma trận → dọc) · 0 rác markdown · 0 placeholder · các giá trị then chốt (kg Top set SBD, calo, macro) khớp với MD.
