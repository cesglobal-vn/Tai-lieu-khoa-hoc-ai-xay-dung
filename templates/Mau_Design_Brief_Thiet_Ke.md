# BẢN NHIỆM VỤ THIẾT KẾ KIẾN TRÚC & KỸ THUẬT (DESIGN BRIEF TEMPLATE)
*(CƠ SỞ ĐẦU VÀO ĐỂ AI VÀ ĐỘI NGŨ THIẾT KẾ TRIỂN KHAI PHƯƠNG ÁN Ý TƯỞNG)*

---

**TÊN DỰ ÁN:** `[TÊN CÔNG TRÌNH / DỰ ÁN]`  
**HẠNG MỤC THIẾT KẾ:** `[Ví dụ: Khối đế thương mại & Sảnh đón Tầng 1 / Không gian Văn phòng]`  
**CHỦ ĐẦU TƯ:** `[TÊN CHỦ ĐẦU TƯ]` — **ĐƠN VỊ THIẾT KẾ:** `[TÊN ĐƠN VỊ THIẾT KẾ]`  
**PHIÊN BẢN:** `[V1.0]` — **NGÀY LẬP:** `[Ngày/Tháng/Năm]`  

---

## 1. MỤC TIÊU VÀ ĐỊNH VỊ CÔNG TRÌNH
- **Định vị phân khúc:** `[Hạng A / Tiêu chuẩn quốc tế / Tiết kiệm năng lượng chuẩn LEED]`
- **Ngôn ngữ kiến trúc chủ đạo:** `[Hiện đại, tối giản, thông thoáng, thân thiện với môi trường]`
- **Đối tượng sử dụng chính:** `[Khách thuê văn phòng cao cấp, khách vãng lai mua sắm, chuyên gia quốc tế]`

---

## 2. CHỈ TIÊU QUY HOẠCH & THÔNG SỐ HÌNH HỌC KHỐI CÔNG NĂNG
- **Diện tích sàn khu vực thiết kế:** `[... m²]`
- **Kích thước bao che (dài x rộng):** `[... m x ... m]`
- **Chiều cao thông thủy trần hoàn thiện:** `[Tối thiểu ... m]`
- **Hệ lưới trục kết cấu dự kiến:** `[Ví dụ: 8.4m x 8.4m / 9.0m x 9.0m]`

---

## 3. BẢNG CƠ CẤU PHÂN BỔ DIỆN TÍCH (AREA SCHEDULE)
| STT | Không gian chức năng | Tỷ lệ diện tích (%) | Diện tích sàn (m²) | Yêu cầu kỹ thuật & Vật liệu hoàn thiện |
| :---: | :--- | :---: | :---: | :--- |
| **1** | Sảnh đón chính & Lễ tân | `15%` | `...` | Sàn đá Granite tự nhiên, trần thạch cao giật cấp |
| **2** | Cụm thang máy & Lõi giao thông | `10%` | `...` | Vách ốp đá chống cháy, cửa thang inox gương |
| **3** | Không gian kinh doanh thương mại | `60%` | `...` | Mặt tiền vách kính Low-E tràn viền không khung |
| **4** | Khu vệ sinh & Phòng kỹ thuật | `10%` | `...` | Thiết bị vệ sinh tự động, sàn chống trơn, thoát mùi |
| **5** | Sảnh đệm & Lối thoát hiểm PCCC | `5%` | `...` | Cửa thép chống cháy EI 90, đèn exit sự cố |
| | **TỔNG DIỆN TÍCH:** | **100%** | **... m²** | |

---

## 4. YÊU CẦU DÂY CHUYỀN HOẠT ĐỘNG & LUỒNG GIAO THÔNG
- **Luồng người văn phòng:** Tiếp cận trực tiếp từ sảnh chính qua cổng kiểm soát an ninh (Flap barrier) đến thang máy tốc độ cao.
- **Luồng khách thương mại:** Tiếp cận độc lập từ mặt tiền phố, không ảnh hưởng đến an ninh khu văn phòng.
- **Luồng thoát nạn khẩn cấp:** Đảm bảo khoảng cách từ điểm xa nhất đến cửa buồng thang thoát hiểm $\le 40\text{ m}$ theo QCVN 06:2022/BXD.

---

## 5. ĐẦU RA YÊU CẦU ĐỐI VỚI ĐỘI NGŨ THIẾT KẾ & AI AGENT
1. Xuất tối thiểu 02 phương án mặt bằng phân khu công năng sơ bộ.
2. Sinh mã AutoLISP dựng hệ lưới trục và vị trí cột kết cấu chính xác trên phần mềm AutoCAD.
3. Xuất bảng câu lệnh (Prompts) tạo hình ảnh phối cảnh không gian nội ngoại thất để thuyết minh ý tưởng.
