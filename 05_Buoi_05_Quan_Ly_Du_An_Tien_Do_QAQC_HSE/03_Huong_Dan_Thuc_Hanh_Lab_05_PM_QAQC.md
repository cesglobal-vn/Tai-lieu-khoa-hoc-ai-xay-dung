# TÀI LIỆU HƯỚNG DẪN BÀI THỰC HÀNH LAB 05
## TỰ ĐỘNG HÓA NHẬT KÝ THI CÔNG & THIẾT LẬP BẢNG QUẢN TRỊ RỦI RO (RISK REGISTER)
**Thời lượng thực hành:** 55 phút  
**Sản phẩm nghiệm thu (Deliverable D5):** Nhật ký thi công ngày hoàn chỉnh + Bảng tiến độ Lookahead 2 tuần + Bảng Risk Register  
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. MỤC TIÊU BÀI LAB 05
- Cấu hình đồng thời hai trợ lý: **Agent 05 (Tiến độ - Báo cáo)** và **Agent 06 (QA/QC - HSE)** trong AI Workspace.
- Xử lý tình huống thực tế: Biến chuỗi tin nhắn Zalo phản ánh sự cố hiện trường thành Nhật ký thi công ngày chuẩn Nghị định 06/2021/NĐ-CP.
- Lập Kế hoạch tiến độ cuốn chiếu 2 tuần (Lookahead Schedule) nhận diện chính xác các công việc trên đường găng (Critical Path).
- Xây dựng Bảng quản trị rủi ro công trường (Risk Register) đánh giá mức độ nguy hiểm và đề xuất biện pháp xử lý sự cố sạt trượt hố đào.

---

## 2. DỮ LIỆU ĐẦU VÀO TÌNH HUỐNG HIỆN TRƯỜNG (CASE STUDY INPUT)

Học viên nhận được chuỗi tin nhắn từ Nhóm Zalo Điều hành Công trường GreenTech Tower ngày 25/11/2026:

> **[07:15 - Kỹ sư hiện trường Nam]:**  
> *"Chào Chỉ huy trưởng và anh em, hôm nay thời tiết sáng nắng ráo 24 độ, độ ẩm 75%. Quân số có mặt: Tổ cốt thép 18 thợ, tổ ván khuôn 12 thợ, tổ phụ trách bơm nước 4 thợ, lái máy 3 người. Dự kiến sáng nay hoàn thành lắp dựng cốt thép đài móng ĐM-01 đến ĐM-04 trục 1-2. Chiều mời TVGS DeltaCon nghiệm thu lúc 15h00."*
> 
> **[11:30 - Kỹ sư trắc đạc Hưng]:**  
> *"Đã quan trắc xong mốc chuyển vị cừ larsen trục A giáp nhà dân số 18 ngõ 2. Hiện tại độ nghiêng cừ là 4mm, vẫn trong giới hạn cho phép (< 15mm). Mực nước ngầm hố móng dâng nhẹ sau trận mưa hôm qua, đang chạy 2 bơm chìm 5.5kW liên tục."*
> 
> **[14:45 - Kỹ sư an toàn HSE Long]:**  
> *"KHẨN CẤP! Lúc 14h20 xuất hiện mưa dông cục bộ rất to kèm gió giật cấp 6. Nước mưa tràn vào góc hố móng trục F gây sạt lở khoảng 15m3 đất đắp bờ ta luy tạm, vùi lấp một đoạn rãnh thoát nước. Đã yêu cầu toàn bộ công nhân rút khỏi hố móng lên mặt bằng an toàn. Một công nhân tổ ván khuôn bị trượt ngã nhẹ ở bậc tam cấp, đã sơ cứu tại lán y tế, không có thương tích nặng."*
> 
> **[16:30 - Chỉ huy trưởng Thành]:**  
> *"Mưa đã tạnh. Yêu cầu: (1) Đội cơ giới điều máy đào 0.8m3 khơi thông ngay rãnh thoát nước và đắp bờ bao ngăn nước mặt tràn; (2) Huy động thêm 2 máy bơm công suất lớn 7.5kW hút cạn nước hố móng trước 21h đêm nay; (3) Hoãn nghiệm thu cốt thép với TVGS sang 08h30 sáng mai; (4) Anh Nam và Long tổng hợp nhật ký và làm biên bản sự cố để báo cáo Ban QLDA."*

---

## 3. CÁC BƯỚC THỰC HÀNH TỪNG BƯỚC (STEP-BY-STEP)

### Bước 1: Kích Hoạt Cặp Trợ Lý Agent 05 & 06 (Thời gian: 10 phút)
1. Trong Workspace GreenTech Tower, nạp System Instruction cho **Agent 05** và **Agent 06** từ file [02_Thu_Vien_Prompt_Thuc_Chien_Buoi_05.md](file:///f:/GitHub/Tai-lieu-khoa-hoc-ai-xay-dung/05_Buoi_05_Quan_Ly_Du_An_Tien_Do_QAQC_HSE/02_Thu_Vien_Prompt_Thuc_Chien_Buoi_05.md).

### Bước 2: Tự Động Hóa Soạn Thảo Nhật Ký Thi Công Ngày (Thời gian: 15 phút)
1. Sử dụng **Prompt 5.1**, dán toàn bộ chuỗi tin nhắn Zalo ở Mục 2 vào.
2. Kiểm tra bản Nhật ký thi công được Agent 05 sinh ra:
   - Mục 1: Mô tả thời tiết có sự biến động (sáng nắng ráo, chiều mưa dông to gió giật cấp 6).
   - Mục 2: Tổng hợp đủ 37 nhân lực (18 thép + 12 cốp pha + 4 bơm + 3 máy) và danh mục thiết bị (máy đào, bơm chìm).
   - Mục 3: Ghi nhận công việc sáng hoàn thành thép đài móng ĐM-01 đến ĐM-04; chiều dừng thi công lúc 14h20 do mưa bão.
   - Mục 4: Ghi chú hoãn nghiệm thu sang sáng hôm sau; kết quả quan trắc chuyển vị cừ đạt 4mm.
   - Mục 5: Ghi nhận sự cố sạt lở 15m³ ta luy tạm, biện pháp khơi thông và sơ cứu công nhân kịp thời.
3. Xuất kết quả ra file `Nhat_Ky_Thi_Cong_25_11_2026.md`.

### Bước 3: Lập Bảng Quản Trị Rủi Ro Risk Register (Thời gian: 15 phút)
1. Sử dụng **Prompt 5.3** kích hoạt Agent 06 để bóc tách các rủi ro hố móng trong mùa mưa bão:
   - Rủi ro R01: Nước mặt tràn gây sạt lở bờ ta luy hố đào ($P=4, I=4 \rightarrow \text{Score } 16$ — Rất cao).
   - Rủi ro R02: Chuyển vị cừ larsen vượt ngưỡng làm nứt nhà dân lân cận ($P=2, I=5 \rightarrow \text{Score } 10$ — Cao).
   - Rủi ro R03: Ngập úng làm ngâm nước cốt thép và hư hỏng bê tông lót ($P=3, I=3 \rightarrow \text{Score } 9$ — Trung bình).
   - Rủi ro R04: Trượt ngã, tai nạn lao động do đường dốc trơn trượt mùa mưa ($P=4, I=3 \rightarrow \text{Score } 12$ — Cao).
2. Hoàn thiện các giải pháp ứng phó và chỉ định Risk Owner.
3. Xuất file `Risk_Register_Phan_Ngam_GreenTech.md`.

### Bước 4: Lập Kế Hoạch Lookahead 2 Tuần Khắc Phục Chậm Tiến Độ (Thời gian: 15 phút)
1. Sử dụng **Prompt 5.2** yêu cầu Agent 05 lập tiến độ bù đắp thời gian đã mất do trận mưa bão ngày 25/11.
2. Xác định các công việc làm thêm ca đêm (tăng ca đổ bê tông đài móng) để không ảnh hưởng mốc hoàn thành tầng hầm ngày 15/03/2027.

---

## 4. TỔNG KẾT SẢN PHẨM NỘP BÀI LAB 05
Học viên nộp:
1. File `Nhat_Ky_Thi_Cong_25_11_2026.md`
2. File `Risk_Register_Phan_Ngam_GreenTech.md`
3. File `Ke_Hoach_Lookahead_2_Tuan.md`.
