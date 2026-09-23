# TÀI LIỆU HƯỚNG DẪN BÀI THỰC HÀNH LAB 04
## BÓC TÁCH KHỐI LƯỢNG BOQ & ĐỐI SOÁT BÁO GIÁ ĐA NHÀ THẦU BẰNG AI
**Thời lượng thực hành:** 55 phút  
**Sản phẩm nghiệm thu (Deliverable D4):** Bảng tính BOQ Excel + Bảng phân tích so sánh 3 báo giá + Tờ trình phân tích ngân sách  
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. MỤC TIÊU BÀI LAB 04
- Cấu hình thành thạo **Agent 04 - Kỹ sư QS & Chi phí (Cost & QS Specialist)** trong AI Workspace.
- Vận hành Agent 04 để tính toán chính xác khối lượng bê tông và ván khuôn cho hệ kết cấu 30 cột Tầng 1 dự án GreenTech Tower.
- Chuẩn hóa Bảng tiên lượng khối lượng (BOQ) với công thức minh bạch, xuất sang Microsoft Excel mà không bị lỗi đè dòng.
- Thực hành phân tích, chuẩn hóa mặt bằng so sánh cho 03 bảng chào thầu bê tông, phát hiện chi phí ẩn và lập Báo cáo đề xuất lựa chọn nhà thầu.

---

## 2. DỮ LIỆU ĐẦU VÀO MẪU (CASE STUDY INPUTS)

### Phần A: Dữ liệu hình học hệ cột Tầng 1 GreenTech Tower
- Số lượng cột bê tông: 30 cột.
- Tiết diện ngang cột: $b \times h = 800\text{ mm} \times 800\text{ mm} = 0.8\text{ m} \times 0.8\text{ m}$.
- Chiều cao tầng 1: $H_{\text{tầng}} = 5.40\text{ m}$.
- Chiều cao dầm chính sàn tầng 2 giao đỉnh cột: $h_{\text{dầm}} = 800\text{ mm} = 0.8\text{ m}$.
- **Chiều cao tịnh của cột (đổ bê tông đến đáy dầm):** $H_{\text{tịnh}} = 5.40\text{ m} - 0.80\text{ m} = 4.60\text{ m}$.
- Yêu cầu vật liệu: Bê tông thương phẩm B35 (M450), phụ gia chống thấm W10, ván khuôn phủ phim 18mm.

### Phần B: Dữ liệu chào giá của 3 Trạm trộn Bê tông
*(Đã cung cấp chi tiết trong Thư viện Prompt 4.3: Trạm Việt Đức, Trạm Chèm, Trạm Vĩnh Tuy cho khối lượng 110 m³ chia làm 2 ca bơm).*

---

## 3. CÁC BƯỚC THỰC HÀNH TỪNG BƯỚC (STEP-BY-STEP)

### Bước 1: Kích Hoạt Agent 04 Trong AI Workspace (Thời gian: 10 phút)
1. Trong Workspace dự án, thiết lập System Prompt cho **Agent 04** từ file [02_Thu_Vien_Prompt_Thuc_Chien_Buoi_04.md](file:///f:/GitHub/Tai-lieu-khoa-hoc-ai-xay-dung/04_Buoi_04_Boc_Tach_Khoi_Luong_BOQ_Du_Toan/02_Thu_Vien_Prompt_Thuc_Chien_Buoi_04.md).
2. Kiểm tra tính năng Anti-Guesswork: Thử hỏi *"Diện tích sơn tường tầng hầm là bao nhiêu?"* ➔ Agent phải trả lời *"Hồ sơ hiện tại chưa có bản vẽ chi tiết tường hầm, cần kỹ sư xác minh"*.

### Bước 2: Bóc Tách Khối Lượng Bê Tông & Ván Khuôn (Thời gian: 15 phút)
1. Sử dụng **Prompt 4.1** để yêu cầu Agent 04 tính toán khối lượng theo công thức hình học chuẩn:
   - **Khối lượng bê tông thân cột:**
     $$V_{\text{thân}} = 30 \times (0.8 \times 0.8 \times 4.6) = 88.32\text{ m³}$$
   - **Khối lượng bê tông nút khung (phần giao với dầm sàn):**
     $$V_{\text{nút}} = 30 \times (0.8 \times 0.8 \times 0.8) = 15.36\text{ m³}$$
   - **Tổng khối lượng bê tông hình học:**
     $$V_{\text{tổng}} = 88.32 + 15.36 = 103.68\text{ m³}$$
   - **Diện tích ván khuôn thân cột (4 mặt):**
     $$S_{\text{vk}} = 30 \times (4 \times 0.8) \times 4.6 = 30 \times 3.2 \times 4.6 = 441.60\text{ m²}$$
2. Yêu cầu Agent 04 lập bảng phân rã chi tiết.

### Bước 3: Xuất Bảng BOQ Chuẩn Hóa Sang Excel (Thời gian: 15 phút)
1. Sử dụng **Prompt 4.2** để sinh bảng BOQ hoàn chỉnh gồm 8 cột.
2. Sao chép nội dung bảng Markdown được tạo ra.
3. Mở Microsoft Excel, dán vào Sheet mới.
4. Kiểm tra định dạng: Bảng có cột STT riêng, căn lề số liệu thẳng hàng bên phải, có công thức tính Thành tiền tự động (`= Khối lượng * Đơn giá`).

### Bước 4: Chạy Bài Toán So Sánh Báo Giá & Phát Hiện Bẫy Chi Phí (Thời gian: 15 phút)
1. Sử dụng **Prompt 4.3** nạp dữ liệu chào giá của 3 Trạm trộn vào.
2. Yêu cầu Agent 04 tính tổng chi phí thanh toán thực tế cho 110 m³ (gồm tiền vật tư, phụ gia W10 và 2 ca bơm):
   - **Trạm A (Việt Đức):**
     $$\text{Tổng} = (110 \times 1.450.000) + (2 \times 4.500.000) = 159.500.000 + 9.000.000 = 168.500.000\text{ VNĐ}$$
   - **Trạm B (Chèm):**
     $$\text{Tổng} = 110 \times (1.420.000 + 60.000 + 110.000) = 110 \times 1.590.000 = 174.900.000\text{ VNĐ}$$
   - **Trạm C (Vĩnh Tuy):**
     $$\text{Tổng} = 110 \times (1.390.000 + 80.000 + 130.000) = 110 \times 1.600.000 = 176.000.000\text{ VNĐ}$$
3. **Phát hiện thú vị:** Trạm Vĩnh Tuy có giá vật tư niêm yết rẻ nhất (1.390.000 VNĐ) nhưng khi cộng đầy đủ phụ gia và phí bơm theo mét khối thì tổng chi phí lại **đắt nhất** (176.000.000 VNĐ)! Trạm Việt Đức có giá vật tư cao nhất lại là đơn vị có **tổng chi phí thấp nhất và điều kiện thanh toán an toàn nhất**.
4. Xuất Báo cáo đề xuất lựa chọn nhà thầu bằng **Prompt 4.4**.

---

## 4. TỔNG KẾT SẢN PHẨM NỘP BÀI LAB 04
Học viên nộp:
1. File Excel `BOQ_Cot_Tang_1_GreenTech.xlsx` (hoặc bản xuất Markdown).
2. File `Bao_Cao_So_Sanh_Chao_Gia_Be_Tong.md`.
