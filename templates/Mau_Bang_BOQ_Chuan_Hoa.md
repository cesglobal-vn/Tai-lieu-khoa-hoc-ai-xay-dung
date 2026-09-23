# BẢNG TIÊN LƯỢNG KHỐI LƯỢNG CHUẨN HÓA (STANDARDIZED BOQ TEMPLATE)
*(BẢNG TÍNH MẪU ĐƯỢC THIẾT KẾ CHỐNG LỖI ĐÈ DÒNG, DỄ DÀNG SAO CHÉP VÀO MICROSOFT EXCEL)*

---

**DỰ ÁN:** `[TÊN CÔNG TRÌNH / DỰ ÁN]`  
**GÓI THẦU:** `[TÊN GÓI THẦU XÂY DỰNG / KẾT CẤU / HOÀN THIỆN]`  
**GIAI ĐOẠN:** `[DỰ TOÁN THIẾT KẾ THI CÔNG / MỜI THẦU / THANH TOÁN GIAI ĐOẠN]`  
**ĐƠN VỊ TIỀN TỆ:** Đồng Việt Nam (VNĐ) — **ĐƠN VỊ ĐO LƯỜNG:** Hệ Mét chuẩn Việt Nam  

---

### BẢNG TIÊN LƯỢNG KHỐI LƯỢNG VÀ CHI PHÍ (BILL OF QUANTITIES)

| STT | Mã hiệu ĐM | Mô tả chi tiết công tác kỹ thuật | ĐVT | Khối lượng (Net) | Diễn giải công thức tính toán | Đơn giá vật tư | Đơn giá NC & Máy | Thành tiền (VNĐ) | Ghi chú & Tiêu chuẩn viện dẫn |
| :---: | :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **A** | | **PHẦN KẾT CẤU BÊ TÔNG CỐT THÉP** | | | | | | | |
| **1** | AF.12110 | Bê tông lót móng đá 4x6, mác M100, chiều dày 100mm | m³ | `15.50` | `15.5 * 1.0 * 0.1` | `1,150,000` | `280,000` | `=E3*(G3+H3)` | TCVN 5574:2018 |
| **2** | AF.22110 | Bê tông cột tiết diện <= 0.1m2, mác B35 (M450), đá 1x2, phụ gia chống thấm W10 | m³ | `103.68` | `30 * 0.8 * 0.8 * 5.4` | `1,450,000` | `350,000` | `=E4*(G4+H4)` | Gồm ca bơm cần |
| **3** | AF.82110 | Ván khuôn cột ván ép phủ phim 18mm, hệ xà gồ thép | m² | `441.60` | `30 * (0.8*4) * 4.6` | `185,000` | `120,000` | `=E5*(G5+H5)` | Luân chuyển 4 nước |
| **4** | AF.61210 | Cốt thép cột đường kính D > 18mm, mác thép CB500-V | tấn | `18.25` | `Bảng thống kê thép KT-201` | `16,800,000` | `2,400,000` | `=E6*(G6+H6)` | TCVN 1651:2018 |
| **B** | | **PHẦN HOÀN THIỆN VÀ CỬA CHỐNG CHÁY** | | | | | | | |
| **5** | AK.51110 | Cửa thép chống cháy EI 90 kèm thanh thoát hiểm, tay co thủy lực (D-08) | bộ | `10` | `5 tầng * 2 thang` | `9,500,000` | `850,000` | `=E8*(G8+H8)` | Có tem kiểm định PCCC |
| **6** | AK.11210 | Trát tường dày 15mm, vữa xi măng mác M75 | m² | `1,250.00` | `Chu vi * Chiều cao tường` | `45,000` | `85,000` | `=E9*(G9+H9)` | TCVN 9377:2012 |
| | | **TỔNG CỘNG TRƯỚC THUẾ:** | | | | | | **[TỔNG TIỀN]** | |
| | | **THUẾ GIÁ TRỊ GIA TĂNG (VAT 8% / 10%):** | | | | | | **[TIỀN THUẾ]** | |
| | | **TỔNG CỘNG CHI PHÍ SAU THUẾ:** | | | | | | **[TỔNG SAU THUẾ]** | |

---

### NGUYÊN TẮC QUẢN TRỊ BẢNG TÍNH BOQ BẮT BUỘC
1. **Phân tách rạch ròi cột STT:** Cột A chỉ chứa số thứ tự hoặc mã mục ngắn, tuyệt đối không gộp chung với tên hạng mục dài.
2. **Định dạng số chuẩn:** Khối lượng làm tròn 2 chữ số thập phân (`#,##0.00`), đơn giá và thành tiền hiển thị phân cách hàng nghìn (`#,##0`).
3. **Công thức động:** Cột Thành tiền luôn sử dụng công thức nhân `=Khối lượng * Đơn giá`, không gán cứng số tĩnh.
