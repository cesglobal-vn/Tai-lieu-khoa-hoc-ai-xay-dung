# TIÊU CHÍ NGHIỆM THU SẢN PHẨM: DELIVERABLE D4
## SUBAGENT, CLAUDE.MD AN TOÀN, MÔ HÌNH 3D TỪ BẢN VẼ AUTOCAD

**Mã sản phẩm:** D4
**Học phần:** Buổi 04
**Đơn vị ban hành:** Hội đồng chuyên môn CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. THÀNH PHẦN HỒ SƠ D4

1. File subagent `soat-ho-so.md` và bảng tổng kết quả soát 3 cặp hồ sơ.
2. Đoạn CLAUDE.md Global đã gài 6 nguyên tắc, kèm kết quả 3 phép "thử phá".
3. Ảnh mô hình nhà 7x20m: 1 ảnh phối cảnh, 1 ảnh bung tầng.
4. Cặp ảnh trước, sau khi sửa một thông số trên bản vẽ, kèm ghi chú ô đã sửa và kết quả đếm cửa đọc lại.

## 2. BẢNG CHẤM (THANG 100)

| STT | Tiêu chí | Điểm | ĐẠT | CHƯA ĐẠT |
| :---: | :--- | :---: | :--- | :--- |
| 1 | **Subagent** | 20 | File có đủ `name`, `description` nói rõ khi nào giao việc, `tools` chỉ cho đọc; bảng tổng gom đủ 3 cặp, mỗi dòng có nguồn | Mô tả mơ hồ; subagent có quyền sửa file; bảng thiếu nguồn |
| 2 | **CLAUDE.md an toàn** | 25 | Đủ 6 nguyên tắc, viết ngắn rõ; bản cũ đã sao lưu trước khi sửa; cả 3 phép thử ra đúng kết quả | Thiếu nguyên tắc; ghi đè CLAUDE.md cũ không sao lưu; Claude tự xóa file hoặc tự điền đơn giá |
| 3 | **Mô hình 3D đúng bản vẽ** | 30 | Đủ 3 tầng và tum; số đọc lại khớp bản vẽ (71 tường, 30 cửa, 32 cột, 57 món nội thất); tách tầng hoạt động; ảnh render rõ hình khối | Thiếu tầng; số đếm lệch mà không giải thích; sửa tay trong Blender; ảnh tối hoặc không thấy cửa |
| 4 | **Sửa bản vẽ rồi dựng lại, kiểm chéo** | 25 | Sửa đúng một thông số **trên bản vẽ** (ví dụ chiều cao S1), có sao lưu; dựng lại cho thấy thay đổi đúng chỗ; số cửa đọc lại vẫn khớp bảng thống kê, ghi rõ nguồn | Sửa trực tiếp trong Blender; không có ảnh trước, sau; không kiểm lại số cửa |

## 3. XẾP LOẠI

- **Xuất sắc (90 đến 100):** đạt cả 4 tiêu chí, thêm được một lần sửa thứ hai (ví dụ dời vị trí một món nội thất trên bản vẽ) và mô hình đổi đúng theo.
- **Đạt (70 đến 89):** đủ 4 thành phần, mô hình khớp số đếm, có cặp ảnh trước, sau.
- **Chưa đạt (dưới 70):** thiếu thành phần, hoặc CLAUDE.md không chặn được phép thử xóa file. Làm lại cùng trợ giảng.
