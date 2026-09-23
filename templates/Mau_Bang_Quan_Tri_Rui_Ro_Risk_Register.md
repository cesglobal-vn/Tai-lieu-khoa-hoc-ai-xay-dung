# BẢNG QUẢN TRỊ RỦI RO DỰ ÁN XÂY DỰNG (PROJECT RISK REGISTER TEMPLATE)
*(CÔNG CỤ QUẢN LÝ RỦI RO HIỆN TRƯỜNG THEO CHUẨN QUỐC TẾ PMBOK & QUY CHUẨN AN TOÀN QCVN 18:2021/BXD)*

---

**DỰ ÁN:** `[TÊN CÔNG TRÌNH / DỰ ÁN]`  
**GIAI ĐOẠN:** `[THI CÔNG PHẦN NGẦM / PHẦN THÂN / HOÀN THIỆN & CƠ ĐIỆN]`  
**NGƯỜI QUẢN TRỊ (RISK MANAGER):** `[Họ và tên Kỹ sư QA/QC / Chỉ huy phó Kỹ thuật]`  
**NGÀY CẬP NHẬT:** `[Ngày/Tháng/Năm]` — **CHU KỲ CẬP NHẬT:** Hàng tuần  

---

## 1. THANG ĐO MA TRẬN RỦI RO ($P \times I$)

- **Xác suất xảy ra ($P$ - Probability):**
  - `1`: Rất hiếm khi xảy ra ($< 10\%$).
  - `2`: Ít khi xảy ra ($10\% - 30\%$).
  - `3`: Có thể xảy ra ($30\% - 50\%$).
  - `4`: Khả năng xảy ra cao ($50\% - 70\%$).
  - `5`: Rất dễ xảy ra / Thường xuyên ($> 70\%$).
- **Mức độ tác động ($I$ - Impact về Tiến độ / Chi phí / An toàn):**
  - `1`: Không đáng kể (Thiệt hại $< 10$ triệu VNĐ, chậm $< 1$ ngày, không tai nạn).
  - `2`: Nhẹ (Thiệt hại $10 - 50$ triệu VNĐ, chậm $1 - 3$ ngày, sơ cứu tại chỗ).
  - `3`: Trung bình (Thiệt hại $50 - 200$ triệu VNĐ, chậm $3 - 7$ ngày, nghỉ việc ngắn ngày).
  - `4`: Lớn (Thiệt hại $200 - 500$ triệu VNĐ, chậm $1 - 2$ tuần, tai nạn nặng).
  - `5`: Thảm họa (Thiệt hại $> 500$ triệu VNĐ, chậm $> 1$ tháng, chết người hoặc đình chỉ dự án).
- **Điểm rủi ro ($Risk Score = P \times I$):**
  - `1 - 4`: **RỦI RO THẤP (LOW)** ➔ Chấp nhận và theo dõi định kỳ.
  - `5 - 9`: **RỦI RO TRUNG BÌNH (MEDIUM)** ➔ Áp dụng biện pháp phòng ngừa và kiểm soát.
  - `10 - 15`: **RỦI RO CAO (HIGH)** ➔ Lập phương án xử lý khẩn cấp và giám sát hàng ngày.
  - `16 - 25`: **RỦI RO NGHIÊM TRỌNG (EXTREME)** ➔ Báo cáo Giám đốc dự án, dừng thi công nếu cần thiết.

---

## 2. BẢNG THEO DÕI VÀ QUẢN TRỊ RỦI RO CHI TIẾT (RISK REGISTER LOG)

| Mã RR | Danh mục rủi ro & Mô tả tình huống | Nguyên nhân gốc rễ (Root Cause) | Xác suất (P) | Mức tác động (I) | Điểm ($P \times I$) | Phân cấp rủi ro | Biện pháp phòng ngừa & Kế hoạch ứng phó | Người phụ trách (Risk Owner) | Trạng thái hiện tại |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **R01** | **Nước mưa tràn gây sạt lở bờ ta luy hố móng** | Mưa dông bất chợt; rãnh thoát nước tạm thời bị đất cát bồi lấp | `4` | `4` | **16** | **Nghiêm trọng** | Đắp gờ bê tông bao quanh mép hố đào; lắp đặt 4 bơm chìm dự phòng; phủ bạt bảo vệ ta luy | Chỉ huy phó Công trường | Đang kiểm soát |
| **R02** | **Chuyển vị cừ larsen làm lún nứt nhà dân lân cận** | Đào đất quá sâu khi hệ shoring chưa kích đủ tải; địa chất bùn yếu | `2` | `5` | **10** | **Cao** | Lắp đặt hệ thống quan trắc tự động inclinometer; kích tải shoring đúng quy trình; mua bảo hiểm công trình | Kỹ sư Trắc đạc | Theo dõi liên tục |
| **R03** | **Tai nạn ngã cao khi lắp dựng ván khuôn & giàn giáo** | Công nhân không móc dây an toàn; sàn thao tác thiếu lan can chắn | `3` | `4` | **12** | **Cao** | Tổ chức huấn luyện an toàn đầu giờ (Toolbox talk); phạt đình chỉ thợ vi phạm; gắn lưới đỡ an toàn | Cán bộ an toàn HSE | Giám sát chặt |
| **R04** | **Chậm tiến độ cấp bê tông do kẹt xe hoặc tắc trạm** | Trạm trộn ở xa công trường; cấm đường giờ cao điểm tại Hà Nội | `3` | `3` | **9** | **Trung bình** | Ký hợp đồng với 2 trạm trộn độc lập; chỉ đổ bê tông cấu kiện lớn từ 21h đêm đến 05h sáng | Kỹ sư Điều độ Tiến độ | Đã áp dụng |
| **R05** | **Rò rỉ khí chữa cháy FM200 gây ngạt tại phòng Server** | Cảm biến báo cháy giả kích hoạt xả khí khi đang có người vận hành | `1` | `5` | **5** | **Trung bình** | Cài đặt độ trễ xả khí 30 giây kèm còi hú lớn; trang bị mặt nạ dưỡng khí cách ly tại cửa phòng | Kỹ sư Cơ điện MEP | Đang hoàn thiện |

---

## 3. QUY TRÌNH HÀNH ĐỘNG KHI RỦI RO BIẾN THÀNH SỰ CỐ THỰC TẾ
1. **Bước 1 (Cô lập):** Ngừng ngay lập tức hoạt động tại khu vực có nguy cơ; sơ tán toàn bộ nhân sự đến điểm tập kết an toàn.
2. **Bước 2 (Kích hoạt kế hoạch ứng phó):** Triển khai ngay các biện pháp đã chuẩn bị trước trong cột *Biện pháp phòng ngừa*.
3. **Bước 3 (Báo cáo):** Risk Owner thông báo khẩn cấp cho Chỉ huy trưởng trong vòng 15 phút.
4. **Bước 4 (Đánh giá lại):** Họp rút kinh nghiệm, điều chỉnh điểm rủi ro và cập nhật lại Risk Register.
