# CHECKLIST CÀI ĐẶT TRƯỚC BUỔI 04

**Gửi học viên trước giờ học ít nhất 1 ngày.** Làm từng dòng; dòng nào chưa đạt thì nhắn trợ giảng trước giờ học.
Hướng dẫn chi tiết từng bước và cách xử lý lỗi: `07_Huong_Dan_Cai_Dat_Blender_MCP.md`.

---

## A. BẮT BUỘC (PHẦN BLENDER)

| # | Việc | Đạt khi |
|---|---|---|
| 1 | Cài Blender 3.0 trở lên | `Help > About Blender` hiện số phiên bản |
| 2 | Cài Python 3.10 trở lên, tích "Add Python to PATH" | `python --version` ra từ 3.10 |
| 3 | Cài Git | `git --version` ra số phiên bản |
| 4 | Tải và cài `vn-mcp-blender` (hướng dẫn mục 2) | `vn-mcp-blender --version` ra `0.1.0` |
| 5 | Cài addon, bật **MCP Xây Dựng** trong Blender (mục 3) | Tab MCP Xây Dựng hiện khi bấm phím N |
| 6 | Bấm **Bật kết nối** | Hiện "Đang chạy ở cổng 9877"; `vn-mcp-blender check` in ra thông tin Blender |
| 7 | Khai báo với Claude (mục 4) | `claude mcp list` có `vn-blender ... Connected` |
| 8 | Hỏi Claude "Kiểm tra kết nối Blender" | Claude trả về phiên bản Blender |

## B. NÊN CÓ (PHẦN AUTOCAD)

| # | Việc | Đạt khi |
|---|---|---|
| 9 | AutoCAD có `autocad-mcp` từ Buổi 03 | Hỏi Claude "kiểm tra kết nối AutoCAD" ra trạng thái |

Không có AutoCAD vẫn học được phần dựng 3D: bản vẽ DXF có sẵn trong thư mục demo.

## C. TÀI LIỆU KHÓA HỌC

| # | Việc | Đạt khi |
|---|---|---|
| 10 | Lấy thư mục `04_Buoi_04_Agent_ClaudeMD_Blender_3D` | Có thư mục `demo\07-nha-pho-lo-7x20m\` với file `02_ban-ve-nha-pho-lo-7x20m.dxf` và thư mục `scripts\` |
| 11 | Lấy thư mục `02_Buoi_02_Khai_Thac_Ho_So_Ky_Thuat` | Có các file 01 đến 06 trong `demo\` (dùng cho bài subagent) |

---

## THỨ TỰ MỞ MỖI LẦN LÀM VIỆC

1. Mở Blender, bấm **Bật kết nối** ở tab MCP Xây Dựng.
2. Mở AutoCAD và **mở một bản vẽ** (không để ở tab Start) nếu dùng phần AutoCAD.
3. Mở Claude.
