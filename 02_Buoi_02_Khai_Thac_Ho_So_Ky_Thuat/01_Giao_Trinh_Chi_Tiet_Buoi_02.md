# GIÁO TRÌNH CHI TIẾT — BUỔI 02
## TỪ RÀ SOÁT HỒ SƠ KỸ THUẬT ĐẾN ĐÓNG GÓI SKILL TỰ ĐỘNG HÓA CHUẨN TCVN
**Khóa học:** Ứng Dụng AI Agent Trong Kỹ Thuật & Xây Dựng (CES Global AEC)  
**Thời lượng chuẩn:** 150 phút (30% Lý thuyết & Kiến trúc — 70% Thực hành thực chiến)  
**Phương pháp:** Khung sư phạm 4 thành phần: *(1) Lời dẫn GV — (2) Prompt thực chiến — (3) File Demo PDF — (4) Kết quả mong đợi*  
**Bộ dữ liệu mẫu thực tế:** Thư mục `demo/` gồm các file PDF chuẩn thể thức hành chính & kỹ thuật xây dựng:
- `demo/01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf` (Tài liệu A: Yêu cầu cửa chống cháy buồng thang N1/N2 đạt EI 90 theo QCVN 06:2022/BXD, trang 42).
- `demo/02_Thuyet_Minh_Ban_Ve_KT102.pdf` (Tài liệu B: Bản vẽ KT-102 & Bảng thống kê cửa ghi chú D-08 là EI 60, trang 15).
- `demo/03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf` (Tài liệu C: Kiểm chứng tính tái sử dụng của Skill với bê tông B35, chống thấm W10, trang 48).
- `demo/skill-mau/SKILL.md` (Mẫu cấu hình Skill chuẩn để học viên đối chiếu).

---

## 1. MỤC TIÊU BÀI HỌC (LEARNING OBJECTIVES)

Sau khi hoàn thành Buổi 02, học viên đạt được các năng lực chuyên môn sau:
1. **Hiểu bản chất Skill trong AI Workspace:** Giải thích được Skill là gì (SOP dạng số cho AI), khác gì với việc gõ prompt ngẫu hứng mỗi lần; nắm vững vị trí đặt file (`.claude/skills/<tên-skill>/SKILL.md`) và vai trò then chốt của trường `description` trong cơ chế tự nạp (auto-load).
2. **Khai thác kho tri thức bằng Grounded Search (Chống bịa số):** Nạp và tra cứu hàng trăm trang hồ sơ PDF kỹ thuật có dẫn nguồn số trang, điều khoản cụ thể. Áp dụng triệt để nguyên tắc: *"Chỗ nào tài liệu không có thì ghi không đề cập, tuyệt đối không suy đoán"*.
3. **Phát hiện mâu thuẫn đa hồ sơ (Cross-Document Conflict Detection):** Sử dụng AI đối chiếu tự động giữa Chỉ dẫn kỹ thuật (Specs) và Bản vẽ thiết kế, phát hiện ngay các lỗi vênh tiêu chuẩn chết người (như ca mâu thuẫn EI 90 vs EI 60).
4. **Tự tay đóng gói một Skill kỹ thuật đầu tay:** Đúc kết quy trình 5 lượt chat làm tay thành 1 Skill hoàn chỉnh `soat-ho-so-ky-thuat`, có thể tái sử dụng cho mọi dự án tiếp theo chỉ với 1 câu lệnh ngắn.
5. **Hiểu kiến trúc Hệ sinh thái Skill Xây dựng đỉnh cao (North Star):** Khám phá cấu trúc của repo thực chiến [vn-autocad-skill](https://github.com/andyluu98/vn-autocad-skill) (Bộ 8 Skill + 5 Agent + 3 Slash Command) để hiểu cách AI tự động hóa dựng 26 tờ bản vẽ A3 chuẩn TCVN và dự toán Excel.

---

## 2. TIẾN TRÌNH GIẢNG DẠY 150 PHÚT (PEDAGOGICAL TIMELINE)

```
00:00 ─── 00:15 (15') : [Khởi động] Ôn tập Buổi 01 & Đặt bài toán: "Nỗi đau lặp lại quy trình soát hồ sơ"
00:15 ─── 00:40 (25') : [Lý thuyết cốt lõi] Khái niệm Skill là gì? Cấu trúc SKILL.md & Quy tắc chống bịa số
00:40 ─── 01:15 (35') : [Live Demo 1] Từ 5 lượt chat rà soát mâu thuẫn PCCC ➔ Đóng gói thành Skill đầu tay
01:15 ─── 01:45 (30') : [Live Demo 2 - North Star] Giải mã Repo vn-autocad-skill: Bộ 8 Skill + 5 Agent TCVN
01:45 ─── 02:20 (35') : [Lab 02] Học viên tự tay đóng gói Skill & chạy trên tài liệu dự án thật
02:20 ─── 02:30 (10') : [Nghiệm thu & Bàn giao] Đánh giá Skill học viên, chuẩn bị bước vào vẽ AutoCAD Buổi 03
```

---

## 3. NỘI DUNG CHI TIẾT TỪNG PHÂN ĐOÀN

### [00:00 - 00:15] Khởi động & Ôn tập Buổi 01

- **Lời dẫn GV:** *"Chào các anh chị. Buổi trước chúng ta đã khởi tạo AI Workspace dự án và cấu hình Agent 01 - Điều phối (Project Orchestrator). Nhưng có một vấn đề: Nếu mỗi lần cần rà soát một tập chỉ dẫn kỹ thuật hay bản vẽ dày cộp, chúng ta lại phải ngồi gõ lại hàng loạt câu lệnh dài dòng thì rất mất thời gian và dễ sót việc. Hôm nay, chúng ta sẽ học cách dạy cho AI một quy trình chuẩn để nó tự động làm chuẩn từng bước mỗi lần: Đó chính là SKILL."*
- **Câu hỏi tương tác nhanh (3 phút):**
  1. *Hồ sơ dự án của bạn thường có bao nhiêu trang spec và bản vẽ? Có ai từng đọc sót một điều khoản quan trọng khiến công trình bị đình chỉ hoặc đội chi phí chưa?*
  2. *Sự khác nhau giữa việc chat ngẫu hứng và việc đóng gói quy trình thành Skill là gì?*

---

### [00:15 - 00:40] Lý thuyết cốt lõi: Skill là gì trong AI Workspace?

- **Lời dẫn GV:** *"Hãy hình dung Skill giống như một tờ Quy trình thao tác chuẩn (SOP) dán trên tường của Ban Chỉ huy công trường. Ai vào làm việc đó cũng cứ nhìn tờ quy trình mà làm theo, kết quả ra giống hệt nhau. Skill là tờ quy trình đó, nhưng được đóng gói cho AI đọc và thực thi."*
- **3 Trọng tâm lý thuyết:**
  1. **Skill nằm ở đâu:**
     - Là một thư mục nằm trong dự án tại: `.claude/skills/<tên-skill>/`
     - Bên trong chỉ cần 01 file duy nhất: `SKILL.md`.
  2. **Cấu trúc 2 phần của `SKILL.md`:**
     - **Phần đầu (YAML Frontmatter):**
       ```yaml
       ---
       name: soat-ho-so-ky-thuat
       description: Dùng khi cần rà soát chỉ dẫn kỹ thuật, đối chiếu mâu thuẫn giữa bản vẽ và thuyết minh, lập ma trận nghiệm thu vật tư và sinh phiếu RFI.
       ---
       ```
       *Nhấn mạnh:* Dòng `description` là quan trọng nhất! Claude dựa vào dòng này để **tự động nạp Skill** khi câu hỏi của người dùng khớp với mô tả, không cần phải gọi tên skill.
     - **Phần thân (Body):** Các bước chỉ dẫn chi tiết, định dạng bảng mong muốn và quy tắc kiểm soát.
  3. **Quy tắc quan trọng nhất: Chống bịa số liệu kỹ thuật (Anti-Hallucination):**
     - Mọi thông số (mác bê tông, chiều dày thép, giới hạn EI, kích thước) BẮT BUỘC phải kèm theo số trang trích dẫn.
     - Chỗ nào hồ sơ không đề cập, BẮT BUỘC ghi rõ: *"Tài liệu không đề cập / Cần xác nhận của Kỹ sư trưởng"*, tuyệt đối không đoán mò!

---

### [00:40 - 01:15] Demo Giảng viên 1: Từ 5 lượt chat rà soát hồ sơ ➔ Đóng gói thành Skill đầu tay

> **Ý đồ sư phạm:** Giảng viên KHÔNG đưa sẵn file mẫu cho học viên chép. Giảng viên thị phạm trên màn hình chia sẻ bằng 5 lượt chat liên hoàn trên 02 file PDF thật (`demo/01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf` và `demo/02_Thuyet_Minh_Ban_Ve_KT102.pdf`). Mỗi lượt chat sẽ trở thành một mục trong Skill!

#### Lượt 1: Tóm tắt thông thường để thấy điểm hạn chế
- **Lời dẫn GV:** *"Tôi có tập Chỉ dẫn PCCC dày cộp. Tôi hỏi AI theo cách bình thường nhất mà người dùng hay hỏi."*
- **Prompt:**
  ```
  Tóm tắt giúp tôi yêu cầu cửa chống cháy trong file demo/01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf
  ```
- **Kết quả mong đợi:** AI trả lời chung chung: Cửa thép chống cháy, tự động đóng, đạt chuẩn an toàn... Giảng viên chỉ ra: *"Nghe rất xuôi tai, nhưng mang bản này đi nghiệm thu hay đặt hàng sản xuất là chết ngay, vì thiếu mác vật liệu, thiếu giới hạn chịu lửa và không có số trang dẫn chứng!"*

#### Lượt 2: Ép bóc tách phạm vi và quy cách kỹ thuật
- **Lời dẫn GV:** *"Tôi ép nó bóc đúng chi tiết cấu tạo vật liệu."*
- **Prompt:**
  ```
  Chưa đủ. Bóc tách chi tiết: độ dày thép khung, thép cánh, tỷ trọng bông cách nhiệt và phụ kiện đi kèm.
  ```
- **Kết quả mong đợi:** AI bóc ra: Thép khung 1.5mm, cánh 1.2mm, bông Rockwool tỷ trọng >= 120 kg/m³, tấm MgO 5mm, tay co thủy lực EN 1154.

#### Lượt 3: Lập Ma trận yêu cầu kỹ thuật & nghiệm thu 6 cột
- **Lời dẫn GV:** *"Kỹ sư hiện trường và QA/QC cần một bảng ma trận để kiểm soát vật tư đầu vào."*
- **Prompt:**
  ```
  Lập Ma trận yêu cầu kỹ thuật và nghiệm thu gồm 6 cột: STT, Hạng mục, Quy cách kỹ thuật, Tiêu chuẩn áp dụng (TCVN/QCVN), Hồ sơ nghiệm thu đầu vào bắt buộc, và Vị trí trích dẫn số trang.
  ```
- **Kết quả mong đợi:** Bảng xuất hiện rõ ràng: QCVN 06:2022/BXD, TCVN 9383:2012, Giấy kiểm định phương tiện PCCC của Cục Cảnh sát PCCC & CNCH, Trích dẫn Điều 5.3 Trang 42.

#### Lượt 4: Rà soát mâu thuẫn đa hồ sơ (Khoảnh khắc "Cú nổ")
- **Lời dẫn GV:** *"Bây giờ là điểm đáng tiền nhất của AI. Tôi nạp thêm file PDF Bản vẽ KT-102 và bảo nó đối chiếu chéo."*
- **Prompt:**
  ```
  Đối chiếu giữa Chỉ dẫn PCCC (file 01) và Bản vẽ KT-102 (file 02): Có mâu thuẫn nào về giới hạn chịu lửa và quy cách của cửa thang bộ D-08 không?
  ```
- **Kết quả mong đợi:** AI phát hiện ra điểm vênh nghiêm trọng:
  - *Chỉ dẫn kỹ thuật PCCC (Trang 42):* Bắt buộc cửa buồng thang thoát hiểm N1/N2 phải là **EI 90** (Rockwool 120 kg/m³ + tấm MgO).
  - *Bản vẽ kiến trúc KT-102 (Trang 15):* Lại chỉ ghi chú cửa D-08 là **EI 60** (Rockwool 100 kg/m³).
  - *Đánh giá rủi ro:* Nếu sản xuất theo EI 60 sẽ giảm chi phí ban đầu nhưng chắc chắn công trình sẽ **BỊ ĐÌNH CHỈ NGHIỆM THU PCCC KHI BÀN GIAO**, thiệt hại hàng tỷ đồng!

#### Lượt 5: Quy tắc chống bịa & Tự động sinh Phiếu RFI
- **Lời dẫn GV:** *"Tôi thử hỏi một câu mà hồ sơ không hề nói tới: Phạt tiến độ giao chậm cửa là bao nhiêu tiền?"*
- **Prompt:**
  ```
  Trong hai tài liệu trên, mức phạt tiền nếu nhà thầu giao chậm cửa chống cháy là bao nhiêu?
  ```
- **Kết quả mong đợi:** AI trả lời: *"Tài liệu không đề cập thông tin về mức phạt chậm tiến độ. Cần tham chiếu Hợp đồng thi công chính."* (Không hề bịa ra con số).
- **Lời dẫn GV:** *"Chuẩn rồi. Bây giờ xuất luôn cho tôi một Phiếu yêu cầu làm rõ (RFI-ARC-001) gửi TVTK và Chủ đầu tư!"*

#### Bước 6: Đóng gói 5 lượt chat thành một Skill hoàn chỉnh
- **Lời dẫn GV:** *"Nhìn lại xem: Chúng ta mất 5 lượt hỏi đáp mới ra được kết quả ưng ý. Tuần sau gặp gói thầu cơ điện hay kết cấu, chẳng lẽ lại gõ lại 5 lượt? Giờ tôi bảo AI đóng gói lại thành một Skill."*
- **Prompt:**
  ```
  Tôi thấy kết quả rất chuẩn rồi. Bây giờ hãy đóng gói toàn bộ quy trình rà soát hồ sơ, đối chiếu mâu thuẫn và lập phiếu RFI này thành một Skill cho tôi.
  Lưu vào đường dẫn: .claude/skills/soat-ho-so-ky-thuat/SKILL.md
  Dòng description ghi rõ: "Dùng khi cần rà soát chỉ dẫn kỹ thuật, đối chiếu mâu thuẫn giữa bản vẽ và thuyết minh, lập ma trận nghiệm thu vật tư và sinh phiếu RFI."
  Cấu trúc xuất ra phải luôn đủ 5 phần:
  1. TÓM TẮT QUY CÁCH KỸ THUẬT
  2. MA TRẬN YÊU CẦU NGHIỆM THU (kèm tiêu chuẩn TCVN và chứng chỉ PCCC)
  3. BẢNG ĐỐI CHIẾU MÂU THUẪN (nêu rõ số trang sai khác)
  4. PHIẾU RFI ĐỀ XUẤT LÀM RÕ
  5. QUY TẮC: Chỉ dùng thông tin có thật, không có ghi 'không đề cập', trích dẫn số trang chính xác.
  ```
- **Kết quả mong đợi:** AI tạo file `.claude/skills/soat-ho-so-ky-thuat/SKILL.md`. Giảng viên mở file cho lớp xem và chỉ rõ: Mỗi mục trong file chính là biên bản đúc kết từ các câu hỏi mà mình vừa trải qua.

#### Bước 7: Kiểm chứng tính tái sử dụng thần tốc
- **Lời dẫn GV:** *"Bây giờ đưa một tài liệu hoàn toàn khác: file PDF Chỉ dẫn Bê tông vách hầm (`demo/03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf`). Xem tôi chỉ gõ đúng 1 câu duy nhất!"*
- **Prompt:**
  ```
  Rà soát yêu cầu kỹ thuật và nghiệm thu trong demo/03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf
  ```
- **Kết quả mong đợi:** Claude tự động kích hoạt `soat-ho-so-ky-thuat` và xuất ra ngay Ma trận kỹ thuật: B35, W10, độ sụt 16±2cm, phụ gia giảm nước bù co ngót, lớp bảo vệ 40mm, thí nghiệm nén R7 và R28... chỉ trong vòng 10 giây!

---

### [01:15 - 01:45] Demo Giảng viên 2: North Star — Giải mã Repo `vn-autocad-skill`

- **Lời dẫn GV:** *"Skill các anh chị vừa tạo là một skill đơn lẻ. Bây giờ, tôi cho các anh chị xem một Hệ sinh thái Skill thực chiến quy mô doanh nghiệp mà tôi đã xây dựng và phát hành mã nguồn mở trên GitHub: repo `andyluu98/vn-autocad-skill`."*
- **Trình chiếu và phân tích kiến trúc:**
  1. **8 Skills chuyên ngành phối hợp nhịp nhàng:**
     - `vn-quy-trinh-ho-so`: Điều phối 11 bước, kiểm soát cổng bàn giao.
     - `vn-kien-truc`: Mặt bằng, mặt đứng, mặt cắt, khai triển thang, WC, lát gạch.
     - `vn-ket-cau`: Móng, dầm, sàn, thống kê thép tự động sinh từ kích thước.
     - `vn-co-dien`: Bản vẽ điện nước từng tầng, sơ đồ tủ điện nguyên lý.
     - `vn-bo-cuc-to-giay`: Chia lưới model space, bố trí Layout A3, viewport đa tỷ lệ.
     - `vn-soat-ban-ve`: 4 phép soát tự động chống nét cắt qua chữ, đo ô bao, soát kỹ thuật.
     - `vn-du-toan`: Xuất file Excel dự toán tự động liên kết khối lượng từ bản vẽ.
     - `vn-xuat-autocad`: Xuất DXF sang DWG qua AutoCAD MCP và PDF.
  2. **5 Sub-Agents chuyên trách:** `kien-truc-su`, `ky-su-ket-cau`, `ky-su-co-dien`, `kiem-soat-ban-ve`, `ky-su-du-toan`.
  3. **Lệnh tắt (Slash Commands):**
     - `/ho-so-moi nhà phố 4x16m, 3 tầng, có gara`
     - `/soat-ban-ve`
     - `/xuat-dwg`
  4. **Thành quả đầu ra:** 01 file DXF/DWG chứa trọn vẹn **26 tờ A3** chuẩn TCVN kèm dự toán Excel 100% Times New Roman.
- **Ranh giới an toàn cần nhớ:** AI hỗ trợ triển khai hồ sơ và thống kê theo cấu tạo, KHÔNG thay thế việc tính toán nội lực và KHÔNG thay thế chữ ký của kỹ sư có chứng chỉ hành nghề.

---

### [01:45 - 02:20] Học viên thực hành Lab 02 (35 phút)

- **Đề bài thực hành:**
  1. Mở thư mục dự án đã tạo từ Buổi 01.
  2. Tạo thư mục `.claude/skills/soat-ho-so-ky-thuat/`.
  3. Tự tay đóng gói file `SKILL.md` (hoặc tham khảo file mẫu tại `demo/skill-mau/SKILL.md`).
  4. Chạy thử nghiệm trên 02 file PDF demo (`01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf` và `02_Thuyet_Minh_Ban_Ve_KT102.pdf`) hoặc dùng hồ sơ dự án thật của mình.
  5. Xuất ra 02 file nộp bài:
     - `Ma_Tran_Yeu_Cau_Ky_Thuat.md`
     - `Phieu_RFI_01_Lam_Ro_Thong_Tin.md`
- **Trợ giảng & Giảng viên hỗ trợ 1-1 tại chỗ.**

---

### [02:20 - 02:30] Nghiệm thu & Giới thiệu Buổi 03

- **Nghiệm thu đồng đẳng (Peer Review):** Kiểm tra xem Skill của học viên có tự động nạp không, có bóc tách đủ điều khoản và trích dẫn số trang chính xác không.
- **Giới thiệu Buổi 03:**
  > *"Hôm nay chúng ta đã biến hồ sơ kỹ thuật thành dữ liệu chuẩn và làm chủ tư duy Skill. Buổi 03 tới đây, chúng ta sẽ bước sang khâu Thiết kế & Triển khai CAD: Dùng AI và mã AutoLISP tự động vẽ lưới trục, cột, tường và xuất bản vẽ ngay trên phần mềm AutoCAD trước mắt các anh chị!"*
- **Bài tập về nhà:** Chuẩn bị 01 đề bài mặt bằng khu đất (chiều dài, chiều rộng, hướng, số tầng) để chuẩn bị thực hành vẽ AutoCAD ở Buổi 03.
