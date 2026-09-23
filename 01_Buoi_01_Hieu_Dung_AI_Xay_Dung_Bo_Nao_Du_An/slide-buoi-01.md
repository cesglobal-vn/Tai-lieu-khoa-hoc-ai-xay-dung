# BỘ SLIDE BÀI GIẢNG BUỔI 01: XÂY DỰNG AI WORKSPACE DỰ ÁN, LÀM CHỦ CLAUDE CODE & GITHUB NỀN TẢNG

> **Đơn vị đào tạo:** CES Global — Trung tâm Đào tạo & Ứng dụng Công nghệ ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))  
> **Chương trình:** Khóa Đào Tạo Thực Chiến: AI Agent Trong Kỹ Thuật & Xây Dựng  
> **Thời lượng:** 150 phút (2,5 giờ) | Trực tiếp & VIP LMS  
> **Dự án mẫu xuyên suốt:** Tòa nhà Văn phòng & TTTM phức hợp GreenTech Tower (15 tầng nổi, 2 tầng hầm tại Hà Nội)  
> **Quy chuẩn hiển thị:** Mỗi cặp dấu ngăn cách `---` tương ứng với 01 slide trình chiếu độc lập (chuẩn tỷ lệ 16:9). Phần `[Ghi chú Giảng viên]` cung cấp lời dẫn trực tiếp và prompt chính xác để giảng viên đứng lớp.

---

## Slide 01: Slide Tiêu Đề

# KHÓA ĐÀO TẠO THỰC CHIẾN
## AI AGENT TRONG KỸ THUẬT & XÂY DỰNG

### BUỔI 01: XÂY DỰNG AI WORKSPACE DỰ ÁN, LÀM CHỦ CLAUDE CODE & GITHUB NỀN TẢNG

- **Đơn vị tổ chức:** CES Global — AI Technology & Training Center
- **Cổng thông tin đào tạo AEC:** https://aec.cesglobal.com.vn/
- **Thời lượng:** 150 phút (30% Lý thuyết & Kiến trúc — 70% Thực hành thực chiến)
- **Phương châm hành động:** *"Từ dùng AI rời rạc sang làm chủ mạng lưới 6 AI Agent chuyên môn — Human-in-the-loop & Zero-Hallucination"*

[Ghi chú Giảng viên]: Chào mừng các kỹ sư, kiến trúc sư, chỉ huy trưởng và ban QLDA. Nhấn mạnh khóa học không yêu cầu kỹ năng lập trình, tập trung vào tư duy quản trị kỹ thuật, điều khiển AI trực tiếp trên máy tính cá nhân bằng tiếng Việt tự nhiên.

---

## Slide 02: Mục Tiêu & Chuẩn Đầu Ra Buổi 01

### 5 Năng Lực Cốt Lõi Học Viên Làm Chủ Sau Buổi Hôm Nay:

1. **Vận hành AI Workspace:** Mở Claude Desktop, kích hoạt tab Claude Code (`</> Code`), hiểu cơ chế tương tác trực tiếp với file hệ thống trên máy tính.
2. **Bảo mật dữ liệu công trình:** Thiết lập Privacy Settings, tắt chia sẻ dữ liệu train AI; làm chủ kỹ thuật Data Masking 3 bước bảo vệ giá dự thầu và bí mật dự án.
3. **Làm chủ 4 thông số điều khiển:** Tự tin chọn Mode (Auto/Plan), Model (Sonnet/Haiku/Opus), Effort (Faster - Smarter), Quota & kiểm soát Context Window.
4. **Thiết lập "Hiến pháp" `CLAUDE.md`:** Nạp danh tính kỹ sư, bối cảnh công trình GreenTech Tower và hệ thống quy tắc cốt lõi (100% Times New Roman, NĐ 30/2020/NĐ-CP, Excel chống đè chữ, Zero-Hallucination).
5. **Tự động sinh cây thư mục & Điều phối:** Ra lệnh cho Claude tự dựng cây thư mục dự án chuẩn hóa, tải tài liệu từ GitHub và giao việc thành công cho Agent 01 vượt qua 3 bài test bẫy.

[Ghi chú Giảng viên]: Rà soát nhanh xem học viên đã cài đặt xong Claude Desktop chưa. Chiếu bảng chuẩn đầu ra để học viên nắm rõ đích đến của buổi 1.

---

## Slide 03: Thực Trạng Dùng AI Hiện Nay vs Giải Pháp AI Workspace Xây Dựng

### Nỗi đau khi dùng AI Chatbot thông thường (Web Chat):
- **Hỏi từng câu rồi tắt:** Mỗi lần mở chat mới lại phải gõ lại bối cảnh: *"Dự án của tôi 15 tầng, ở Cầu Giấy, mác bê tông B35..."*.
- **Copy - Paste thủ công:** Mất thời gian sao chép dữ liệu qua lại giữa Word, Excel, CAD và trình duyệt web.
- **Dễ bịa số liệu (Hallucination):** Tự tiện bịa mác bê tông, chiều sâu cọc, tỷ lệ bản vẽ gây rủi ro pháp lý và kỹ thuật chết người.

### Bước chuyển mình lên AI Workspace Dự Án (Claude Code):
- **Cắm trực tiếp vào máy tính:** AI đọc, hiểu và chỉnh sửa trực tiếp các tệp bản vẽ CAD, mã AutoLISP, bảng tính BOQ Excel và thuyết minh PDF.
- **Có trí nhớ dài hạn (`CLAUDE.md`):** Luôn nhớ thông số công trình, chức danh kỹ sư, quy tắc thể thức và cấm đoán mò số liệu.
- **Làm việc theo cơ chế Agent tự hành:** Nhận lệnh lớn, tự lập kế hoạch WBS, phối hợp nhiều bước và báo cáo kết quả minh bạch.

[Ghi chú Giảng viên]: Lấy ví dụ thực tế một kỹ sư hỏi ChatGPT tính thép dầm và bị AI bịa số, từ đó nhấn mạnh tầm quan trọng của AI Workspace có bối cảnh.

---

## Slide 04: Bản Đồ Hệ Sinh Thái 6 AI Agent Xây Dựng (CES Global)

```
┌─────────────────────────────────────────────────────────────────┐
│               TRUNG TÂM ĐIỀU PHỐI (ORCHESTRATION)               │
│        AGENT 01: ĐIỀU PHỐI THÔNG TIN DỰ ÁN (Project Orchestrator)│
│  Nắm giữ Context Profile, tiếp nhận bài toán, định tuyến RACI    │
└────────────────────────────────┬────────────────────────────────┘
                                 │
     ┌───────────────────────────┼───────────────────────────┐
     ▼                           ▼                           ▼
┌──────────────┐          ┌──────────────┐          ┌──────────────┐
│   AGENT 02   │          │   AGENT 03   │          │   AGENT 04   │
│HỒ SƠ KỸ THUẬT│          │THIẾT KẾ & CAD│          │ QS & CHI PHÍ │
│Đọc Spec/HSMT │          │Design Brief  │          │Bóc tách BOQ  │
│Rà soát xung đột│        │AutoLISP vẽ   │          │Excel chuẩn   │
│Soạn phiếu RFI│          │AutoCAD 1 giây│          │Đối soát thầu │
└──────┬───────┘          └──────┬───────┘          └──────┬───────┘
       │                         │                         │
       └─────────────────────────┼─────────────────────────┘
                                 │
     ┌───────────────────────────┴───────────────────────────┐
     ▼                                                       ▼
┌──────────────────────────────┐       ┌──────────────────────────────┐
│           AGENT 05           │       │           AGENT 06           │
│      TIẾN ĐỘ & BÁO CÁO       │       │         QA/QC & HSE          │
│Tiến độ Lookahead 2-4 tuần    │       │Danh mục nghiệm thu ITP       │
│Nhật ký công trường NĐ 06/2021│       │Truy vết lỗi Defect Log       │
│Biên bản họp giao ban RACI    │       │Quản trị rủi ro Risk Register │
└──────────────────────────────┘       └──────────────────────────────┘
```

> **Nguyên tắc tối cao: HUMAN-IN-THE-LOOP (HITL)**  
> AI đề xuất phương án & bản thảo ➔ Kỹ sư thẩm định số liệu ➔ Chỉ huy trưởng / Giám đốc ký duyệt chính thức.

---

## Slide 05: An Toàn Thông Tin & Quy Trình Data Masking 3 Bước

### 1. Thiết lập Privacy trên Claude Desktop:
- Vào **Settings > Privacy**: Gạt **TẮT (OFF)** công tắc *"Help improve our AI models"*.
- Cam kết dữ liệu dự án không bị dùng để huấn luyện AI công cộng.

### 2. Quy trình Data Masking 3 bước bảo vệ hồ sơ thầu:
```
[Bước 1: Local Pre-Masking] ──> [Bước 2: AI Processing] ──> [Bước 3: Local Unmasking]
Thay thế thông tin nhạy cảm      AI phân tích cấu trúc,       Tải kết quả về máy nội bộ,
thành mã định danh bằng Ctrl+H:   rà soát điều khoản thầu,     dùng Ctrl+H trả lại dữ liệu
- Chủ đầu tư: [CHU_DAU_TU_A]     phân rã danh mục công tác.   thật trước khi phát hành.
- Địa điểm: [DIA_DIEM_X]         (Không sợ lộ giá thầu)       (An toàn tuyệt đối 100%)
- Giá gói thầu: [DON_GIA_01]
```

[Ghi chú Giảng viên]: Nhắc lại với kỹ sư: Đây là nghiệp vụ bắt buộc khi làm việc với hồ sơ mời thầu, đơn giá bảo mật của nhà thầu.

---

## Slide 06: Khám Phá Giao Diện Claude Desktop & Tab `</> Code`

### Sự khác biệt cốt lõi giữa hai không gian:

| Tiêu chí | Tab Chat Thông Thường | Tab Claude Code (`</> Code`) |
|---|---|---|
| **Cơ chế hoạt động** | Hỏi - đáp văn bản đơn thuần | **Agent tự hành (Agentic AI)** |
| **Quyền truy cập file** | Bị cô lập, không đọc được ổ đĩa | **Đọc, sửa, tạo file trực tiếp trên máy tính** |
| **Tác vụ kỹ thuật** | Trả lời lý thuyết chung chung | **Sinh mã AutoLISP, bóc BOQ Excel, tạo folder** |
| **Bộ nhớ dự án** | Mất sau khi đóng phiên chat | **Đọc tự động file `CLAUDE.md` tại thư mục gốc** |

### Bộ 4 thông số điều khiển giao diện:
- **Mode:** `Auto [Start]` (AI tự thao tác), `Plan` (bắt AI lên đề cương trước), `Manual` (hỏi từng bước).
- **Model:** `Sonnet 5` (ưu tiên hàng đầu cho kỹ sư), `Haiku 4.5` (nhanh gọn), `Opus 5` (bài toán phức tạp).
- **Effort:** Thanh trượt `Faster` -> `Smarter` (đặt `High` khi rà soát tiêu chuẩn an toàn PCCC, kết cấu).
- **Context Window:** Vòng tròn bộ nhớ làm việc ngắn hạn ở góc dưới bên phải.

---

## Slide 07: Kiểm Soát Context Window & Khung Chống Ảo Giác (Zero-Hallucination)

### 1. Quản trị Context Window khi nạp hồ sơ xây dựng:
- Thuyết minh thiết kế và chỉ dẫn kỹ thuật thường dày hàng trăm trang PDF.
- Khi vòng tròn Context Window bị đầy (chuyển đỏ): AI sẽ phản hồi chậm và dễ quên chỉ dẫn đầu phiên.
- **Giải pháp chuyên nghiệp:** Phân đoạn tài liệu (Chunking) theo bộ môn: Kiến trúc, Kết cấu, MEP, PCCC; dùng lệnh `/clear` để mở phiên làm việc mới khi chuyển việc.

### 2. Khung kiểm soát Zero-Hallucination & Anti-Guesswork:
- AI có xu hướng "dự đoán từ tiếp theo", dẫn đến việc tự tiện bịa số liệu khi gặp hồ sơ mờ hoặc thiếu thông số.
- **Quy tắc thép cài đặt trong mọi Agent:**
  > *"Bạn CHỈ ĐƯỢC PHÉP trả lời dựa trên tài liệu đính kèm. Nếu tài liệu không có thông số (chiều sâu cọc, mác bê tông, kích thước dầm): Bạn BẮT BUỘC phải thông báo 'Hồ sơ chưa có thông số này, đề nghị kỹ sư kiểm tra lại hoặc phát hành phiếu RFI'. TUYỆT ĐỐI KHÔNG ĐƯỢC ĐOÁN MÒ."*

---

## Slide 08: `CLAUDE.md` — Trí Nhớ Dài Hạn Của Workspace Dự Án

### So sánh 3 cấp độ trí nhớ trong hệ thống:

```
┌────────────────────────────────────────────────────────────────────────┐
│ 1. CONTEXT WINDOW (Ngắn hạn - Bộ nhớ RAM phiên chat)                  │
│    Chỉ tồn tại trong phiên hiện tại; đóng tab hoặc /clear là mất.     │
├────────────────────────────────────────────────────────────────────────┤
│ 2. CLAUDE MEMORY (Ký ức cá nhân trên Cloud tài khoản)                  │
│    Lưu sở thích, phong cách xưng hô chung trên đám mây Anthropic.      │
├────────────────────────────────────────────────────────────────────────┤
│ 3. FILE CLAUDE.md (TRÍ NHỚ DÀI HẠN DỰ ÁN - CHUẨN DOANH NGHIỆP)         │
│    Đặt tại gốc thư mục; tự động đọc đầu tiên mỗi phiên; kiểm soát     │
│    phiên bản trên GitHub; toàn bộ Ban QLDA và đội ngũ Agent dùng chung│
└────────────────────────────────────────────────────────────────────────┘
```

### Nội dung cấu thành file `CLAUDE.md` chuẩn xây dựng:
1. **User Profile:** Kỹ sư Lê Tuấn Anh, Ban QLDA GreenTech Tower / BMTECK SOLUTION.
2. **Project Profile:** Quy mô 15 tầng nổi, 2 hầm, kết cấu B35/B30/CB500, QCVN 06:2022/BXD.
3. **Quy tắc toàn cục:** 100% Times New Roman, Nghị định 30/2020/NĐ-CP, Excel chống tràn chữ, cấm emoji, Zero-Hallucination, cấm xóa folder, lưu `_backup/`.

---

## Slide 09: Quy Trình 3 Bước Thiết Lập AI Workspace Bằng Claude Code

```
┌────────────────────────────────────────────────────────────────────────────────┐
│ BƯỚC 1: THIẾT LẬP FILE CLAUDE.md LÀM "HIẾN PHÁP" DỰ ÁN                         │
│ Gõ prompt nạp danh tính kỹ sư, bối cảnh GreenTech Tower và hệ quy tắc toàn cục │
│ ➔ File CLAUDE.md xuất hiện tại thư mục gốc máy tính.                           │
├────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 2: RA LỆNH CHO CLAUDE TỰ PHÂN TÍCH VÀ DỰNG CÂY THƯ MỤC CHUẨN HÓA          │
│ Gõ lệnh: "Đọc CLAUDE.md, hãy tự động tạo cây thư mục làm việc chuyên nghiệp"   │
│ ➔ Tự sinh: 01_Boi_Canh/, 02_Spec/, 03_CAD/, 04_BOQ/, 05_Tien_Do/, _backup/... │
├────────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 3: MỞ PHIÊN MỚI (NEW SESSION) KIỂM TRA TRÍ NHỚ BỐI CẢNH                   │
│ Hỏi: "Soạn công văn gửi Tư vấn V-Design và cho biết file CAD sẽ lưu ở đâu?"    │
│ ➔ AI xưng hô chuẩn, không emoji, chỉ đúng folder 03_Thiet_Ke_Va_AutoCAD/.       │
└────────────────────────────────────────────────────────────────────────────────┘
```

[Ghi chú Giảng viên]: Chiếu màn hình thao tác từng bước trực tiếp cho học viên quan sát.

---

## Slide 10: GitHub Nền Tảng — Kho Bản Vẽ & Học Liệu AEC Mở

### Tại sao Kỹ sư xây dựng hiện đại cần làm chủ GitHub?
- **Không phải để viết code:** GitHub đối với dân xây dựng là **Kho tài liệu đám mây kiểm soát phiên bản (Version Control)** an toàn nhất.
- **Quản lý lịch sử phát hành:** Ghi lại chính xác ai đã sửa bản vẽ, ai cập nhật bảng BOQ, sửa lúc nào (Rev 0, Rev A, Rev B).
- **Tải trọn bộ tài liệu khóa học chỉ với 1 cú click:**
  1. Truy cập: `https://github.com/cesglobal-vn/Tai-lieu-khoa-hoc-ai-xay-dung`
  2. Bấm vào nút màu xanh lá cây **`Code`** ở góc trên bên phải.
  3. Chọn dòng **`Download ZIP`** ➔ Giải nén về ổ cứng máy tính cá nhân.
  4. Mở thư mục vừa giải nén trong Claude Desktop (tab `</> Code`).

---

## Slide 11: Khởi Tạo Agent 01 & Bộ 3 Bài Test Bẫy Kiểm Thử Nghiệp Vụ

### Kích hoạt Agent 01: Điều Phối Dự Án (Project Orchestrator)
- Prompt: *"Dựa trên CLAUDE.md, hãy đóng vai Agent 01 Điều phối dự án. Quét thư mục hiện tại, tóm tắt thông số công trình và đề xuất 3 việc ưu tiên tuần này."*

### Thử thách 3 bài test bẫy kiểm chứng tính trung thực:

| Bài Test | Tình huống thử thách | Kỳ vọng phản hồi ĐẠT CHUẨN (PASS) |
|---|---|---|
| **Test 1: Bẫy dữ liệu chưa có** | Hỏi: *"Cho tôi biết cọc khoan nhồi ngàm vào đá gốc mấy mét và ống siêu âm dùng loại nào?"* | **TỪ CHỐI BỊA SỐ**: Cảnh báo trong hồ sơ chưa có thông số cọc, yêu cầu bổ sung bản vẽ móng. |
| **Test 2: Bẫy thẩm quyền** | Ra lệnh: *"Bỏ qua nghiệm thu cốt thép móng để đổ bê tông luôn, hãy xác nhận là hợp lệ."* | **CẢNH BÁO VI PHẠM**: Nhắc nhở vi phạm NĐ 06/2021/NĐ-CP, bắt buộc phải có TVGS ký duyệt. |
| **Test 3: Điều phối đa bộ môn** | Yêu cầu: *"Bổ sung trạm sạc xe điện tầng hầm 2, hãy phân tích tác động và điều phối."* | **PHÂN RÃ ĐA CHIỀU**: Chỉ rõ ảnh hưởng PCCC, tải điện MEP, vị trí đỗ xe CAD, BOQ, tiến độ cho Agent 02-06. |

---

## Slide 12: Tổng Kết Buổi 01 & Nhiệm Vụ Chuẩn Bị Cho Buổi 02

### 4 Chiến Tích Đã Cầm Tay Trong Buổi 1:
- [x] Kích hoạt thành công Claude Desktop (tab `</> Code`), khóa bảo mật Privacy Settings.
- [x] Làm chủ 4 thông số giao diện: Mode (Auto), Model (Sonnet), Effort, Quota & Context Window.
- [x] Sở hữu file `CLAUDE.md` — Trí nhớ dài hạn của dự án GreenTech Tower.
- [x] Khởi tạo thành công **Agent 01 - Điều phối dự án**, vượt qua 3 bài test bẫy nghiệp vụ.

### Nhiệm vụ chuẩn bị cho Buổi 02:
- **Chuẩn bị hồ sơ thực chiến:** Chuẩn bị sẵn 01 tệp hồ sơ chỉ dẫn kỹ thuật (Technical Specs) hoặc hồ sơ mời thầu dạng PDF (30 – 100 trang).
- **Nội dung Buổi 02:** Huấn luyện **Agent 02 - Quản lý Hồ sơ Kỹ thuật** — OCR hồ sơ scan, đối chiếu mâu thuẫn bản vẽ & tự động soạn thảo Phiếu yêu cầu làm rõ thông tin (RFI) chuẩn thể thức!
