# TIÊU CHÍ NGHIỆM THU SẢN PHẨM ĐẦU RA — DELIVERABLE D3
## CHỦ ĐỀ: THIẾT KẾ Ý TƯỞNG & ĐIỀU KHIỂN AUTOCAD BẰNG AI
**Mã sản phẩm nghiệm thu:** D3  
**Học phần:** Buổi 03 — Từ yêu cầu công năng đến ý tưởng thiết kế & điều khiển AutoCAD  
**Đơn vị ban hành:** Hội đồng chuyên môn CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. THÀNH PHẦN HỒ SƠ NGHIỆM THU D3
Học viên nộp bộ hồ sơ gồm 4 sản phẩm:
1. **Design Brief:** Tài liệu Nhiệm vụ thiết kế tầng 1 công trình GreenTech Tower có cơ cấu diện tích chuẩn xác.
2. **Tệp mã nguồn AutoLISP (`.lsp`):** Tệp lệnh AutoLISP có chú thích rõ ràng, xử lý lưu và khôi phục biến hệ thống.
3. **Bản vẽ AutoCAD nghiệm thu:** Tệp `.dwg` hoặc ảnh chụp màn hình AutoCAD hiển thị hệ thống 5x6 lưới trục và 30 cột bê tông 800x800mm được vẽ hoàn toàn tự động bằng script.
4. **Checklist kiểm soát bản vẽ:** Bảng kiểm tra 10 điểm kỹ thuật trước khi bàn giao sang bộ phận bóc tách khối lượng QS.

---

## 2. BẢNG TIÊU CHÍ CHẤM ĐIỂM CHI TIẾT (RUBRIC D3 — THANG ĐIỂM 100)

| STT | Tiêu chí đánh giá | Trọng số | Tiêu chuẩn ĐẠT CHUẨN (PASS) | Lỗi không đạt (FAIL / Cần sửa) | Điểm tối đa |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **1** | **Chất lượng Nhiệm vụ thiết kế (Design Brief)** | **20%** | Đầy đủ cơ cấu diện tích, phân tích luồng giao thông sảnh/thương mại; tuân thủ quy chuẩn thoát nạn QCVN 06:2022/BXD. | Viết sơ sài, thiếu phân bổ diện tích hoặc bỏ qua tiêu chuẩn an toàn PCCC. | **20** |
| **2** | **Cấu trúc & An toàn của mã AutoLISP** | **35%** | Mã có hàm `c:`, tắt bắt điểm đầu hàm và khôi phục biến hệ thống cuối hàm; phân tách rõ ràng Layer nét trục (`L_TRUC`), Layer cột (`L_COT`) và Chữ (`L_TEXT`). | Mã lỗi cú pháp không load được vào AutoCAD; không tắt bắt điểm dẫn đến tọa độ cột bị méo lệch; không khôi phục biến hệ thống. | **35** |
| **3** | **Độ chính xác hình học trên AutoCAD** | **25%** | Lưới trục đúng khoảng cách 8400mm; đủ 30 cột tiết diện 800x800mm đúng tâm giao điểm; ký hiệu trục tròn và tên trục (1-5, A-F) hiển thị sắc nét. | Cột bị lệch khỏi tâm lưới trục; sai kích thước tiết diện; thiếu hoặc sai tên ký hiệu trục. | **25** |
| **4** | **Checklist rà soát kỹ thuật bản vẽ** | **20%** | Bảng checklist 10 điểm rà soát tỉ mỉ các yếu tố: độ đồng quy trục, cao độ, lỗ mở kỹ thuật, tỷ lệ nét in, dimstyle. | Checklist qua loa, hình thức; không chỉ ra được các điểm xung đột tiềm ẩn trước khi đo bóc. | **20** |

---

## 3. PHÂN LOẠI KẾT QUẢ NGHIỆM THU

- **Xuất sắc (90 – 100 điểm):** Bản vẽ CAD hoàn mỹ, mã LISP chạy trơn tru không phát sinh lỗi dòng lệnh, Design Brief có tính khả thi thương mại cao.
- **Đạt yêu cầu (70 – 89 điểm):** Mã LISP chạy thành công, dựng đúng hình học trên AutoCAD; cần hoàn thiện thêm về layer hoặc cỡ chữ dimstyle.
- **Chưa đạt (< 70 điểm):** Mã LISP bị lỗi cú pháp không thể thực thi trong AutoCAD hoặc bản vẽ sai lệch tọa độ nghiêm trọng. Học viên phải sửa lỗi mã nguồn cùng Giảng viên.
