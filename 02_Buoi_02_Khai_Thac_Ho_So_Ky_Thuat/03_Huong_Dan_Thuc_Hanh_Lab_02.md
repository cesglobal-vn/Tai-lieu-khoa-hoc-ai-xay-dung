# TÀI LIỆU HƯỚNG DẪN BÀI THỰC HÀNH LAB 02
## KHAI THÁC HỒ SƠ KỸ THUẬT, LẬP MA TRẬN YÊU CẦU & SOẠN THẢO RFI
**Thời lượng thực hành:** 55 phút  
**Sản phẩm nghiệm thu (Deliverable D2):** Ma trận yêu cầu kỹ thuật + Phiếu RFI hoàn chỉnh  
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. MỤC TIÊU BÀI LAB 02
- Cấu hình thành công **Agent 02 - Hồ sơ kỹ thuật (Document & Spec Auditor)** trong AI Workspace của dự án.
- Sử dụng Agent 02 để đọc và trích xuất dữ liệu từ trích đoạn hồ sơ kỹ thuật mẫu.
- Tự động lập Bảng Ma trận Yêu cầu Kỹ thuật phục vụ kiểm soát chất lượng vật tư đầu vào.
- Phát hiện mâu thuẫn kỹ thuật tiềm ẩn trong hồ sơ và tự động sinh Phiếu yêu cầu làm rõ thông tin (RFI) đạt chuẩn hành chính.

---

## 2. DỮ LIỆU ĐẦU VÀO MẪU (CASE STUDY ASSETS: DỰ ÁN GREENTECH TOWER)

Học viên sử dụng 02 đoạn văn bản trích dẫn kỹ thuật dưới đây làm dữ liệu đầu vào cho bài thực hành:

### Tài liệu A: Trích đoạn Chỉ dẫn Kỹ thuật PCCC & Vật liệu ngăn cháy (Trang 42)
> *"**Điều 5.3: Yêu cầu đối với hệ thống cửa và vách ngăn buồng thang bộ thoát hiểm**  
> 1. Căn cứ Quy chuẩn kỹ thuật quốc gia QCVN 06:2022/BXD về An toàn cháy cho nhà và công trình, toàn bộ cửa mở vào buồng thang bộ thoát nạn N1 và N2 (từ tầng hầm đến tầng mái) phải là cửa thép chống cháy có giới hạn chịu lửa tối thiểu **EI 90** (chịu lửa và cách nhiệt trong 90 phút).  
> 2. Cửa phải được trang bị cơ cấu tự động đóng (tay co thủy lực) và gioăng ngăn khói chuyên dụng đạt chuẩn BS EN 1634-3.  
> 3. Kính gắn trên cửa chống cháy (nếu có) phải là kính chống cháy đồng bộ đạt giới hạn chịu lửa tối thiểu **EI 90**, chiều dày không nhỏ hơn 25mm.  
> 4. Nhà thầu trước khi đặt hàng sản xuất đại trà bắt buộc phải trình chứng chỉ thử nghiệm mẫu đốt đạt chuẩn do cơ quan có thẩm quyền của Cục Cảnh sát PCCC & CNCH cấp phép."*

### Tài liệu B: Trích đoạn Thuyết minh & Bảng Thống kê Cửa Bản vẽ Kiến trúc (Trang 15, Bản vẽ KT-102)
> *"**Bảng thống kê cửa đi tầng 1 đến tầng 5:**  
> - Ký hiệu cửa: **D-08**  
> - Vị trí: Cửa buồng thang thoát hiểm trục (2-3, C-D) các tầng 1, 2, 3, 4, 5.  
> - Kích thước thông thủy: 1200 x 2200 mm (Cửa đi 1 cánh mở một chiều).  
> - Vật liệu: Thép tấm mạ kẽm dày 1.2mm sơn tĩnh điện hoàn thiện, lõi chèn bông khoáng Rockwool tỷ trọng 100 kg/m³.  
> - Giới hạn chịu lửa yêu cầu: **EI 60** (chống cháy 60 phút).  
> - Phụ kiện đi kèm: Bản lề inox 304 chịu lực, khóa tay gạt inox, thanh thoát hiểm panic bar, tay co thủy lực Hafele hoặc tương đương."*

---

## 3. CÁC BƯỚC THỰC HÀNH TỪNG BƯỚC (STEP-BY-STEP)

### Bước 1: Nạp Dữ Liệu & Cấu Hình Agent 02 (Thời gian: 10 phút)
1. Mở AI Workspace `[CES] - GREENTECH TOWER AI WORKSPACE` đã tạo từ Buổi 01.
2. Thêm file mới hoặc nạp nội dung của **Tài liệu A** và **Tài liệu B** vào phần dữ liệu của Workspace.
3. Kích hoạt **Agent 02** bằng System Prompt từ file [02_Thu_Vien_Prompt_Thuc_Chien_Buoi_02.md](file:///f:/GitHub/Tai-lieu-khoa-hoc-ai-xay-dung/02_Buoi_02_Khai_Thac_Ho_So_Ky_Thuat/02_Thu_Vien_Prompt_Thuc_Chien_Buoi_02.md).

### Bước 2: Lập Ma Trận Yêu Cầu Kỹ Thuật (Thời gian: 15 phút)
1. Sử dụng **Prompt 2.2** trong Thư viện Prompt Buổi 02.
2. Yêu cầu Agent 02 bóc tách toàn bộ các thông số kỹ thuật, quy cách vật liệu và tiêu chuẩn thí nghiệm kiểm định của hệ thống cửa D-08.
3. Kiểm tra kết quả: Đảm bảo bảng có đầy đủ các chỉ số: chiều dày thép, tỷ trọng bông khoáng, phụ kiện, chứng chỉ PCCC.

### Bước 3: Rà Soát & Đối Chiếu Xung Đột (Thời gian: 15 phút)
1. Sử dụng **Prompt 2.3** (Rà soát mâu thuẫn đa tài liệu).
2. Yêu cầu Agent 02 đối chiếu thông số giới hạn chịu lửa giữa Tài liệu A (Chỉ dẫn kỹ thuật) và Tài liệu B (Bản vẽ kiến trúc).
3. Đánh giá phát hiện:
   - Chỉ dẫn kỹ thuật yêu cầu **EI 90**.
   - Bản vẽ kiến trúc yêu cầu **EI 60**.
   - Phân tích rủi ro: Nếu sản xuất theo EI 60 sẽ giảm chi phí ban đầu nhưng công trình chắc chắn sẽ bị đình chỉ nghiệm thu PCCC khi nghiệm thu bàn giao đưa vào sử dụng!

### Bước 4: Soạn Thảo Phiếu RFI Chuẩn Mực (Thời gian: 15 phút)
1. Sử dụng **Prompt 2.4** để sinh Phiếu RFI số `RFI-ARC-001`.
2. Kiểm tra lại văn phong: Đảm bảo ngôn từ lịch thiệp, chặt chẽ, khách quan và thể hiện rõ vị thế của Kỹ sư chuyên nghiệp.
3. Xuất kết quả ra file tài liệu `RFI_01_Lam_Ro_Cua_Chong_Chay.md`.

---

## 4. TỔNG KẾT SẢN PHẨM NỘP BÀI LAB 02
Học viên xuất 02 sản phẩm:
1. File `Ma_Tran_Yeu_Cau_Ky_Thuat_Cua_D08.md`
2. File `Phiếu_RFI_01_Lam_Ro_Cua_Chong_Chay.md`
Hai tài liệu này sẽ được dùng làm căn cứ để tính toán chi phí và BOQ trong Buổi 04.
