# HƯỚNG DẪN THỰC HÀNH LAB 04
## SUBAGENT, CLAUDE.MD AN TOÀN VÀ DỰNG NHÀ 3D TỪ BẢN VẼ AUTOCAD

**Thời lượng:** 35 phút thực hành (sau 15 phút cài đặt chung)
**Sản phẩm nộp (D4):** 1 file subagent + CLAUDE.md đã gài nguyên tắc + ảnh mô hình + cặp ảnh trước, sau khi sửa bản vẽ
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

Điều kiện: đã làm xong `06_Checklist_Cai_Dat_Truoc_Buoi_Hoc.md`.
Trước khi làm: **chép thư mục `demo\07-nha-pho-lo-7x20m\` sang một thư mục riêng của mình**, ví dụ `C:\lab04\`, rồi làm trên bản chép (gọi là `<DEMO>` trong các prompt). Không làm trên bản gốc của khóa học.

---

## BƯỚC 1: TẠO SUBAGENT (5 PHÚT)

1. Mở Claude Code tại thư mục làm việc của mình.
2. Dùng **Prompt 1.1** để tạo file `.claude/agents/soat-ho-so.md`.
3. Chạy **Prompt 1.2**: giao 3 subagent soát 3 cặp hồ sơ Buổi 02 song song.
4. Quan sát: 3 subagent chạy cùng lúc; agent chính chỉ nhận về 3 bảng tóm tắt.

**Đạt khi:** có bảng tổng gom kết quả của cả 3 cặp, mỗi dòng có nguồn (file, mục hoặc trang).

## BƯỚC 2: GÀI CLAUDE.MD GLOBAL (5 PHÚT)

1. Chạy **Prompt 2.1**. Kiểm tra Claude đã sao lưu bản cũ vào `~/.claude/_backup/` trước khi sửa.
2. Mở một phiên Claude mới (CLAUDE.md nạp khi bắt đầu phiên).
3. Chạy 3 phép thử ở **Prompt 2.2**. Ghi lại Claude phản ứng ra sao ở mỗi phép thử.

**Đạt khi:** cả 3 phép thử đều ra đúng kết quả mong đợi. Phép nào chưa đạt thì sửa câu chữ nguyên tắc cho rõ hơn rồi thử lại.

## BƯỚC 3: DỰNG NHÀ 3D TỪ BẢN VẼ (15 PHÚT)

Thứ tự khởi động: **mở Blender, bấm "Bật kết nối", rồi mới làm việc với Claude.**

| # | Việc | Prompt | Kiểm |
|---|---|---|---|
| 1 | Kiểm tra kết nối | 3.1 | Thấy phiên bản Blender |
| 2 | Xem layer bản vẽ | 5.1 | Có layer TUONG, COT, CUA, MAI, NOI-THAT và 4 layer bảng |
| 3 | Đọc bản vẽ thành file mô tả | 5.2 | 71 tường, 30 cửa, 32 cột, 57 nội thất, không cảnh báo |
| 4 | Dựng trong Blender | 5.3 | Gọi `nhin` thấy đủ 3 tầng và tum, không có khối bay |
| 5 | Tách tầng, render | 5.4 | Kéo `tach_m` thấy các tầng bung ra; có ít nhất 1 ảnh PNG |

Nếu số liệu khác bảng trên: không sửa tay trong Blender. Hỏi Claude "số cửa em đếm được khác 30, vì sao?" để tìm nguyên nhân.

## BƯỚC 4: SỬA BẢN VẼ RỒI DỰNG LẠI (10 PHÚT)

1. Chụp ảnh mặt hông mô hình hiện tại (ảnh **trước**).
2. Chạy **Prompt 5.5**: đổi chiều cao cửa S1 trong bảng thống kê cửa từ 2200 thành 2400, xuất lại DXF, đọc lại, dựng lại.
3. Chụp ảnh mặt hông lần nữa (ảnh **sau**). Các cửa S1 phải cao lên, mọi thứ khác giữ nguyên.

**Không có AutoCAD:** nhờ Claude sửa đúng ô chữ đó thẳng trong file DXF bằng thư viện ezdxf (sao lưu file DXF trước), rồi làm tiếp từ Prompt 5.2.

**Đạt khi:** cặp ảnh trước, sau cho thấy S1 thay đổi; số cửa đọc lại vẫn khớp bảng thống kê.

---

## NỘP BÀI

Nộp vào thư mục bài nộp của lớp:
1. File `soat-ho-so.md` (subagent) và bảng tổng 3 cặp hồ sơ.
2. Ảnh chụp đoạn CLAUDE.md đã thêm 6 nguyên tắc, kèm kết quả 3 phép thử.
3. Ảnh mô hình: 1 ảnh phối cảnh và 1 ảnh bung tầng.
4. Cặp ảnh trước, sau khi sửa bản vẽ, kèm 2 dòng: đã sửa ô nào, số cửa đọc lại là bao nhiêu.

## LỖI HAY GẶP

| Hiện tượng | Cách xử lý |
|---|---|
| Claude báo không nối được Blender | Blender chưa mở, hoặc chưa bấm "Bật kết nối" ở tab MCP Xây Dựng (phím N) |
| Không thấy công cụ Blender trong Claude | Khởi động lại Claude sau khi khai báo MCP |
| `chay_python` báo "Code bị chặn" | Đọc lý do; không tự tắt bộ soát. Hỏi trợ giảng |
| Dựng xong cảnh trống | Script xóa cảnh cũ trước khi dựng: gọi `nhin` lại; xem `Window > Toggle System Console` |
| AutoCAD không trả lời | AutoCAD đang ở tab Start hoặc có hộp thoại đang chờ: mở bản vẽ, đóng hộp thoại |
| Sau khi xuất DXF, AutoCAD đang mở file DXF | Bình thường: mở lại file DWG trước khi sửa tiếp |
| Ảnh render tối | Đã có sẵn đèn trong script; nếu tự dựng thêm thì gọi cả `tao_den` và `anh_sang_moi_truong` |
