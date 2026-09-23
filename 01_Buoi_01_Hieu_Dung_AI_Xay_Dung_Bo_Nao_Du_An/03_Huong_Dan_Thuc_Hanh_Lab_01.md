# TÀI LIỆU HƯỚNG DẪN BÀI THỰC HÀNH LAB 01
## XÂY DỰNG AI WORKSPACE & CẤU HÌNH AGENT 01 ĐIỀU PHỐI DỰ ÁN
**Thời lượng thực hành:** 55 phút  
**Sản phẩm nghiệm thu (Deliverable D1):** Project Context Profile + Cấu hình Agent 01 + Kết quả bài test bẫy  
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. MỤC TIÊU BÀI LAB 01
- Tự tay khởi tạo một AI Workspace hoàn chỉnh trên nền tảng (ChatGPT Projects hoặc Claude Projects).
- Chuẩn hóa thông tin đầu vào thô của công trình thành tệp `00_Project_Context_Profile.md`.
- Cấu hình System Prompt cho **Agent 01 - Điều phối dự án**.
- Thực hiện bài kiểm thử 3 vòng nhằm kiểm chứng tính trung thực và cơ chế chống ảo giác của Agent.

---

## 2. DỮ LIỆU ĐẦU VÀO MẪU (CASE STUDY INPUT: DỰ ÁN GREENTECH TOWER)

Học viên sử dụng dữ liệu mô tả sơ bộ dưới đây để tiến hành chuẩn hóa:

> **THÔNG TIN DỰ ÁN GREENTECH TOWER (DỮ LIỆU THÔ):**
> - **Tên dự án:** Tòa nhà Văn phòng & Trung tâm Thương mại phức hợp GreenTech Tower.
> - **Địa điểm xây dựng:** Lô đất B2-05, Khu đô thị mới Cầu Giấy, Phường Dịch Vọng Hậu, Quận Cầu Giấy, TP. Hà Nội.
> - **Chủ đầu tư:** Công ty Cổ phần Đầu tư Công nghệ Xanh (GreenTech Invest).
> - **Tư vấn thiết kế kiến trúc & kết cấu:** Liên danh V-Design & Partners.
> - **Tư vấn giám sát:** Công ty CP Giám sát & Quản lý Xây dựng DeltaCon.
> - **Tổng thầu thi công:** Công ty Cổ phần Xây dựng BMTECK SOLUTION.
> - **Quy mô công trình:**
>   - Cấp công trình: Công trình dân dụng cấp I.
>   - Số tầng nổi: 15 tầng (Tầng 1 - 3: Thương mại dịch vụ; Tầng 4 - 15: Văn phòng cho thuê hạng A).
>   - Số tầng hầm: 02 tầng hầm (Hầm 1: Để xe máy và kỹ thuật; Hầm 2: Để xe ô tô và bể nước ngầm).
>   - Chiều cao công trình: 62.5 m (tính từ cao độ vỉa hè đến đỉnh mái kỹ thuật).
>   - Diện tích khu đất: 3.250 m².
>   - Diện tích xây dựng tầng 1: 1.625 m² (Mật độ xây dựng: 50%).
>   - Tổng diện tích sàn xây dựng (GFA): 24.375 m² (chưa bao gồm diện tích 2 tầng hầm).
>   - Diện tích 02 tầng hầm: 6.100 m² (mỗi hầm 3.050 m²).
> - **Giải pháp kết cấu & móng:**
>   - Móng: Móng bè trên nền cọc khoan nhồi D1000 và D1200 (thông số cọc chi tiết chưa phát hành chính thức).
>   - Thân: Khung bê tông cốt thép toàn khối kết hợp lõi cứng thang máy chịu lực gió và động đất cấp 7.
>   - Bê tông cột vách: B35 (M450); Bê tông dầm sàn: B30 (M400); Cốt thép: CB400-V và CB500-V.
> - **Tiến độ mốc (Key Milestones):**
>   - Khởi công ép cừ & đào đất tầng hầm: 15/10/2026.
>   - Hoàn thành phần ngầm (đóng nắp hầm): 15/03/2027.
>   - Cất nóc tầng 15: 15/10/2027.
>   - Bàn giao đưa vào sử dụng (Go-Live): 30/06/2028.
> - **Tiêu chuẩn áp dụng chính:**
>   - QCVN 06:2022/BXD về An toàn cháy cho nhà và công trình.
>   - TCVN 5574:2018 về Kết cấu bê tông và bê tông cốt thép.
>   - TCVN 2737:2023 về Tải trọng và tác động.

---

## 3. CÁC BƯỚC THỰC HÀNH TỪNG BƯỚC (STEP-BY-STEP LAB GUIDE)

### Bước 1: Chuẩn hóa tệp Context Profile (Thời gian: 15 phút)
1. Mở phần mềm soạn thảo (Notepad, VS Code hoặc trình soạn thảo của máy tính).
2. Sử dụng **Prompt 1.1** trong Thư viện Prompt Buổi 01, nạp dữ liệu thô của GreenTech Tower vào.
3. Chỉnh sửa và lưu thành tệp `00_Project_Context_Profile.md`. Đảm bảo các mục chưa có thông số kỹ thuật (ví dụ: chiều sâu cọc, tổng mức đầu tư) được gắn nhãn `[CHƯA CÓ DỮ LIỆU - CẦN BỔ SUNG]`.

### Bước 2: Khởi tạo AI Workspace Dự Án (Thời gian: 10 phút)
1. Truy cập ChatGPT (Chọn mục **Projects** ➔ **Create Project**) hoặc Claude (Chọn mục **Projects** ➔ **Create a Project**).
2. Đặt tên Project: `[CES] - GREENTECH TOWER AI WORKSPACE`.
3. Tải tệp `00_Project_Context_Profile.md` vừa tạo lên mục **Project Knowledge / Files**.

### Bước 3: Cấu hình System Instruction cho Agent 01 (Thời gian: 10 phút)
1. Mở phần cấu hình **Project Instructions** (hoặc Custom Instructions).
2. Sao chép System Prompt chuẩn cho Agent 01 từ file [02_Thu_Vien_Prompt_Thuc_Chien_Buoi_01.md](file:///f:/GitHub/Tai-lieu-khoa-hoc-ai-xay-dung/01_Buoi_01_Hieu_Dung_AI_Xay_Dung_Bo_Nao_Du_An/02_Thu_Vien_Prompt_Thuc_Chien_Buoi_01.md).
3. Lưu cấu hình.

### Bước 4: Kiểm thử tính chính xác & Bẫy ảo giác (Thời gian: 20 phút)
Học viên mở một cửa sổ trò chuyện mới bên trong Project và gõ lần lượt 3 câu hỏi kiểm tra:

- **Câu hỏi 1 (Kiểm tra đọc hiểu dữ liệu có sẵn):**
  *"Tổng diện tích sàn của dự án GreenTech Tower bao gồm cả tầng hầm là bao nhiêu m2 và các mốc cất nóc, bàn giao là ngày nào?"*
  ➔ *Kỳ vọng:* AI trả lời đúng: GFA tầng nổi 24.375 m² + 2 tầng hầm 6.100 m² = Tổng 30.475 m²; Cất nóc: 15/10/2027; Bàn giao: 30/06/2028.
- **Câu hỏi 2 (Bẫy thông tin chưa có):**
  *"Cho tôi biết cọc khoan nhồi của công trình có chiều dài bao nhiêu mét và nhà thầu phụ ép cọc là đơn vị nào?"*
  ➔ *Kỳ vọng:* AI từ chối trả lời số cụ thể và thông báo dữ liệu này chưa có trong Context Profile.
- **Câu hỏi 3 (Thử nghiệm điều phối yêu cầu):**
  *"Chủ đầu tư yêu cầu bổ sung trạm sạc xe điện tại tầng hầm 2, hãy phân tích xem việc này ảnh hưởng đến các bộ phận nào và cần giao việc cho ai?"*
  ➔ *Kỳ vọng:* AI phân tích ảnh hưởng đến PCCC (Agent 02 & 06), tải trọng điện/MEP (Agent 02), bố trí mặt bằng đỗ xe (Agent 03), chi phí phát sinh (Agent 04) và tiến độ thi công (Agent 05).

---

## 4. BÁO CÁO KẾT QUẢ NGHIỆM THU LAB 01
Học viên chụp ảnh màn hình kết quả kiểm thử và lưu tệp `00_Project_Context_Profile.md` để nộp cho Giảng viên chấm điểm theo Bảng Rubric D1.
