# GIÁO TRÌNH CHI TIẾT: BUỔI 04
## AGENT VÀ SUBAGENT, CLAUDE.MD GLOBAL AN TOÀN CHO KỸ SƯ, TỪ BẢN VẼ AUTOCAD ĐẾN MÔ HÌNH 3D BLENDER

**Thời lượng:** 150 phút (khoảng 35% lý thuyết, 65% thị phạm và thực hành)
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))
**Thông tin công cụ tra ngày 07/10/2026:** tài liệu chính thức Claude Code `code.claude.com/docs/en/sub-agents`, `code.claude.com/docs/en/memory`; README và `docs/` của repo `andyluu98/vn-mcp-blender`; README của repo `andyluu98/vn-autocad-claude` (đã dùng ở Buổi 03).

---

## 1. MỤC TIÊU BÀI HỌC

Sau buổi học, học viên:
1. **Phân biệt được Agent và Subagent**, biết khi nào giao việc cho subagent và tự viết được một file subagent cho công việc kỹ thuật.
2. **Thiết lập CLAUDE.md Global** có 6 nguyên tắc an toàn dữ liệu cho kỹ sư: cấm xóa, tự sao lưu, đánh số file, đọc trước sửa sau, chống bịa số liệu, hỏi trước khi gửi ra ngoài.
3. **Cài đặt MCP Blender** (`vn-mcp-blender`) và nối với Claude.
4. **Đi trọn đường ống bản vẽ thành mô hình:** bản vẽ AutoCAD vẽ bằng MCP, xuất DXF, đọc lại thành file mô tả, dựng 3D trong Blender có nội thất, tách tầng, render.
5. **Hiểu nguyên tắc "bản vẽ là nguồn":** muốn sửa mô hình thì sửa bản vẽ rồi dựng lại, không sửa tay trong Blender.

---

## 2. TIẾN TRÌNH 150 PHÚT

```
00:00 - 00:10 (10')  Ôn Buổi 03 AutoCAD MCP. Mở màn: ảnh mẫu, bản vẽ, mô hình nhà 7x20m
00:10 - 00:35 (25')  Agent và Subagent: khái niệm, demo 3 subagent soát 3 hồ sơ song song
00:35 - 00:55 (20')  CLAUDE.md Global: 3 tầng, 6 nguyên tắc an toàn, demo "thử phá"
00:55 - 01:10 (15')  Cài MCP Blender (học viên làm theo, trợ giảng đi kiểm từng máy)
01:10 - 01:40 (30')  Thị phạm: bản vẽ AutoCAD nhà 7x20m thành mô hình 3D có nội thất, tách tầng
01:40 - 02:15 (35')  Học viên thực hành Lab 04
02:15 - 02:30 (15')  Nghiệm thu D4, giải đáp, giao bài Buổi 05
```

**Mở màn 10 phút đầu:** chiếu lần lượt 3 thứ để học viên thấy đích đến của buổi học:
1. Ảnh mẫu một căn nhà phố (khách hàng gửi, kiểu SketchUp).
2. Bộ bản vẽ A3 do Claude vẽ trong AutoCAD qua MCP: `demo/07-nha-pho-lo-7x20m/08_ban-ve-a3-kt01-kt04.pdf`.
3. Ảnh mô hình Blender dựng từ chính bản vẽ đó: `05_phoi-canh-goc-hong.png`, `13_bung-tang.png`.

---

## 3. PHẦN A: AGENT VÀ SUBAGENT (25 PHÚT)

### 3.1. Hình dung đơn giản

| | Agent (phiên làm việc chính) | Subagent |
|---|---|---|
| Ví như | Kỹ sư chủ trì dự án | Kỹ sư được giao một hạng mục |
| Trí nhớ | Nhớ toàn bộ cuộc trao đổi với anh/chị | Bắt đầu từ tờ giấy trắng, chỉ biết đề bài được giao |
| Kết quả trả về | Trả lời trực tiếp | Chỉ nộp **bản tóm tắt kết quả** cho agent chính |
| Công cụ | Đủ bộ | Có thể giới hạn: ví dụ chỉ được đọc, không được sửa |
| Chạy song song | Một | Nhiều subagent cùng lúc |

**Vì sao cần subagent?** Đọc một bộ hồ sơ 200 trang làm đầy "trí nhớ làm việc" của agent chính. Giao cho subagent đọc trong "phòng riêng", agent chính chỉ nhận lại 1 trang tóm tắt, nên vẫn đủ chỗ để tổng hợp và ra quyết định.

### 3.2. Subagent nằm ở đâu

| Vị trí | Phạm vi |
|---|---|
| `.claude/agents/` trong thư mục dự án | Chỉ dự án đó; đưa lên git để cả đội dùng chung |
| `~/.claude/agents/` | Mọi dự án trên máy anh/chị |

Mỗi subagent là **một file Markdown**: phần đầu khai báo tên, mô tả khi nào giao việc, công cụ được dùng; phần dưới là lời dặn công việc. Mẫu ở Thư viện Prompt mục 1.

### 3.3. Ba cách gọi subagent

1. **Để Claude tự giao:** dựa vào trường `description`. Viết mô tả rõ "giao cho agent này khi...".
2. **Gọi bằng lời:** "Dùng subagent soat-ho-so để soát cặp hồ sơ 05 và 06".
3. **Gọi đích danh bằng @:** `@"soat-ho-so (agent)" soát cặp 03 và 04`.

### 3.4. Thị phạm

- Mở thư mục `vn-autocad-skill/agents/` cho học viên xem 5 subagent có sẵn: kiến trúc sư, kỹ sư kết cấu, kỹ sư cơ điện, kỹ sư dự toán, người kiểm soát bản vẽ. Đây là "một văn phòng thiết kế thu nhỏ".
- Tạo subagent `soat-ho-so` (Prompt 1.1), rồi ra lệnh Prompt 1.2: agent chính giao **3 subagent chạy song song**, mỗi subagent soát một cặp hồ sơ của Buổi 02. Agent chính gom 3 kết quả thành một bảng.
- Nhấn mạnh: subagent **không thấy** cuộc trao đổi trước đó, nên lời giao việc phải ghi đủ đường dẫn file và yêu cầu.

---

## 4. PHẦN B: CLAUDE.MD GLOBAL VÀ NGUYÊN TẮC AN TOÀN (20 PHÚT)

### 4.1. Ba tầng CLAUDE.md

| Tầng | Đường dẫn | Dùng cho |
|---|---|---|
| Global | `~/.claude/CLAUDE.md` (Windows: `C:\Users\<tên>\.claude\CLAUDE.md`) | Nguyên tắc của **riêng anh/chị** áp dụng mọi dự án |
| Dự án | `./CLAUDE.md` hoặc `./.claude/CLAUDE.md` | Quy chuẩn của dự án: khổ giấy, layer, mác bê tông |
| Thư mục con | `CLAUDE.md` đặt trong thư mục con | Nạp khi Claude làm việc trong thư mục đó |

Các file **cộng dồn**, không đè nhau. Tài liệu chính thức khuyên mỗi file **dưới 200 dòng**: file càng dài Claude càng dễ bỏ sót.

### 4.2. Sáu nguyên tắc an toàn cho kỹ sư

| # | Nguyên tắc | Vì sao kỹ sư cần |
|---|---|---|
| 1 | **Cấm xóa, cấm tự dọn dẹp.** Chỉ xóa một file khi được gọi đích danh | Một lệnh xóa nhầm thư mục dự án là mất hồ sơ nhiều tháng |
| 2 | **Bản cũ tự vào `_backup/`** trước khi sửa, tên kèm ngày giờ `ten-goc_yymmdd-HHmm` | Sửa sai còn đường lui; bên ngoài chỉ một bản mới nhất |
| 3 | **Đánh số file `NN_`**, quét thư mục lấy số tiếp theo | Hồ sơ xếp đúng thứ tự, không còn "ban-cuoi-that-su-v3" |
| 4 | **Đọc file trên máy rồi mới sửa**, sửa đúng phần được yêu cầu | Không ghi đè phần anh/chị đã chỉnh tay |
| 5 | **Chống bịa số liệu**: mọi con số có nguồn; dùng 3 nhãn `[Chờ bổ sung]`, `Tài liệu không đề cập`, `Cần xác nhận lại` | Khối lượng, đơn giá bịa ra là rủi ro pháp lý |
| 6 | **Hỏi trước** khi gửi email, đăng bài, đổi cấu hình, tốn tiền | AI không được tự quyết việc đi ra ngoài máy |

Mẫu đầy đủ để học viên chép: file `05_Mau_CLAUDE_md_Global_Cho_Ky_Su.md`.

### 4.3. Điều phải nói rõ: nội quy khác khóa cửa

Theo tài liệu chính thức, CLAUDE.md là **ngữ cảnh**, không phải cấu hình bắt buộc. Claude đọc và làm theo, nhưng không có gì bảo đảm tuyệt đối. Muốn **chặn cứng** một thao tác bất kể Claude nghĩ gì, phải dùng **hook** (chạy trước mỗi lệnh, ví dụ chặn mọi lệnh có `rm -rf`).

> Ví von: CLAUDE.md là nội quy công trường dán ở cổng; hook là barie khóa cửa kho.

### 4.4. Thị phạm "thử phá"

1. Bảo Claude: "Xóa giúp tôi các file cũ trong thư mục demo cho gọn." Claude phải liệt kê và hỏi, không tự xóa.
2. Bảo Claude sửa ô A2 trong file Excel `demo/07-nha-pho-lo-7x20m/14_bang-thong-ke-cua-nha-7x20m.xlsx`. Claude phải chép bản cũ vào `_backup/` trước rồi mới sửa.
3. Hỏi "đơn giá bê tông B20 tháng này bao nhiêu?" khi chưa đưa công bố giá. Claude phải trả lời `[Chờ bổ sung]`, không đọc giá từ trí nhớ.

---

## 5. PHẦN C: TỪ BẢN VẼ AUTOCAD ĐẾN MÔ HÌNH 3D BLENDER (45 PHÚT: CÀI 15 + THỊ PHẠM 30)

### 5.1. Đường ống 4 chặng

```
Ảnh mẫu, yêu cầu  ->  [1] AutoCAD (MCP autocad-mcp)  ->  [2] Xuất DXF
                  ->  [3] Đọc bản vẽ thành file mô tả JSON  ->  [4] Blender (MCP vn-blender)
```

| Chặng | Công cụ | Đầu ra trong `demo/07-nha-pho-lo-7x20m/` |
|---|---|---|
| 1. Vẽ | `autocad-mcp` (Buổi 03) chạy file lệnh LISP do Claude sinh | `01_ban-ve-nha-pho-lo-7x20m.dwg`, 4 tờ A3 KT-01 đến KT-04 |
| 2. Xuất | Lưu dạng DXF | `02_ban-ve-nha-pho-lo-7x20m.dxf` |
| 3. Đọc | Script `scripts/doc-ban-ve-ra-mo-ta.py` (thư viện ezdxf) | `03_mo-ta-tu-ban-ve.json` |
| 4. Dựng | `vn-blender`, công cụ `chay_python` chạy `scripts/dung-nha-blender.py` ngay trong Blender đang mở | `04_nha-pho-lo-7x20m.blend`, ảnh `05` đến `13` |

Kiến trúc của MCP Blender:

```
Claude  <--MCP-->  vn-mcp-blender (chương trình Python)  <--cổng 9877-->  Addon "MCP Xây Dựng" trong Blender
```

Ví như gọi điện vào phòng kín: MCP server là tổng đài, addon là người cầm máy trong Blender. Thiếu một bên là không nói chuyện được. Cổng 9877 khác với addon `blender-mcp` phổ biến (9876), chạy song song được.

### 5.2. Ý tưởng cốt lõi: bản vẽ phải "máy đọc được"

Bản vẽ không chỉ để người xem. Mỗi đối tượng nằm đúng layer, mỗi chiều cao nằm trong một bảng:

| Thông tin | Nằm ở đâu trên bản vẽ |
|---|---|
| Tường, cột, lan can | Hình kín trên layer `TUONG`, `COT`, `LAN-CAN` của từng mặt bằng |
| Cửa | Ô cửa trên layer `CUA` + mã cửa (D1, S2...) trên layer `KY-HIEU-CUA` |
| Chiều cao, bệ cửa | **Bảng thống kê cửa** (layer `BANG-CUA`) |
| Cao độ tầng | **Bảng cao độ** (layer `BANG-CAO-DO`) |
| Mái dốc | Hình mái trên layer `MAI` + **bảng mái** (đỉnh, mép, áp cho tầng nào) |
| Thông số dựng hình | **Bảng thông số** (sàn dày, lan can cao, tường rào cao...) |
| Nội thất | Hình chữ nhật đúng kích thước trên layer `NOI-THAT` + tên món đồ |

Script đọc bản vẽ đối chiếu luôn: đếm cửa trên mặt bằng so với cột số lượng của bảng thống kê. Lệch là báo.

### 5.3. Kết quả đã chạy thử trên máy giảng viên ngày 07/10/2026

| Hạng mục | Số liệu |
|---|---|
| Nhà | Lô 7x20m, nhà 5x14m, 3 tầng + tum, sân trước có pergola, lối đi hông 2 m |
| Cao độ | Sân -0.450, tầng 1 ±0.000, tầng 2 +3.600, tầng 3 +7.000, sân thượng +10.400, mái tum +13.400 |
| Đọc lại từ DXF | 71 đoạn tường, 30 lỗ cửa (9 mã, đếm khớp bảng thống kê), 32 cột, 57 món nội thất, không cảnh báo |
| Dựng trong Blender qua MCP | 0,6 giây, 1.149 đối tượng |
| Tách tầng | 5 nhóm: Sân vườn, Tầng 1, Tầng 2, Tầng 3, Mái + Tum; kéo thuộc tính `tach_m` để bung tầng |

Bộ thông số trên là **phương án mẫu để dạy**, không phải hồ sơ xin phép. Tiết diện cột 200x200, nhịp 6,6 m chưa qua tính toán kết cấu.

### 5.4. Kịch bản thị phạm 30 phút

| Phút | Việc | Prompt |
|---|---|---|
| 0 đến 5 | Mở `01_...dwg` trong AutoCAD, cho xem layer, 4 bảng, nội thất. Giải thích vì sao vẽ sẵn: vẽ 1.300 đối tượng mất khoảng 15 phút | 4.1 đến 4.6 (chiếu prompt, không chạy lại) |
| 5 đến 10 | Đọc bản vẽ: xem layer, chạy script đọc, đọc kết quả đối chiếu cửa | 5.1, 5.2 |
| 10 đến 18 | Dựng trong Blender đang mở, gọi `nhin` xem ảnh, xoay mô hình | 5.3 |
| 18 đến 23 | Tách tầng: ẩn từng tầng, kéo `tach_m` bung tầng; mặt bằng nội thất từng tầng | 5.4 |
| 23 đến 30 | **Sửa bản vẽ rồi dựng lại:** đổi chiều cao cửa S1 trong bảng thống kê từ 2200 thành 2400, xuất DXF, đọc lại, dựng lại; mọi cửa S1 trong nhà cao lên | 5.5 |

### 5.5. Bài học cần chốt

1. **Bản vẽ là nguồn.** Sửa trong Blender thì lần dựng sau mất hết; sửa trên bản vẽ thì mô hình, PDF, khối lượng cùng đổi.
2. **Mỗi lần dựng phải có phép đếm đối chiếu:** số cửa, số tường, số món nội thất so với bản vẽ. Con số AI đưa ra phải có cách kiểm chéo.
3. **Giới hạn phải nói thật:** nội thất dựng dạng khối gọn kiểu SketchUp, không phải mô hình chi tiết; công cụ `boc_khoi_luong` của `vn-mcp-blender` chỉ đo cấu kiện do chính các lệnh `dung_tuong`, `dung_san`... tạo ra, không đo mô hình dựng bằng script này.
4. **Bài học khi chuẩn bị:** layout A3 từng in ra trang trắng vì viewport nằm ngoài màn hình giấy, AutoCAD không cho vào MSPACE để đặt tâm. Cách chữa: làm từng tờ, ZOOM toàn tờ và REGEN trước khi vào MSPACE (Prompt 4.5). Luôn đóng mở lại file và mở PDF ra xem trước khi gửi: AI báo "đã in" chưa chắc tờ giấy có hình.

---

## 6. PHẦN THỰC HÀNH LAB 04 (35 PHÚT)

Học viên làm theo `03_Huong_Dan_Thuc_Hanh_Lab_04_Blender.md`:
- Tạo một subagent của riêng mình.
- Thêm 6 nguyên tắc an toàn vào CLAUDE.md Global và chạy thử "thử phá".
- Dựng nhà 7x20m từ DXF vào Blender, tách tầng, render 1 ảnh.
- Sửa một thông số trên bản vẽ rồi dựng lại, chụp ảnh trước và sau.

---

## 7. NGHIỆM THU VÀ BÀI VỀ NHÀ (15 PHÚT)

- Chấm D4 theo `04_Tieu_Chi_Nghiem_Thu_San_Pham_D4.md`.
- Bài về nhà: chọn một căn nhà thật của công ty mình, dùng Prompt 4.1 đến 4.6 vẽ phương án trên AutoCAD, rồi Prompt 5.1 đến 5.4 dựng 3D. Nộp PDF bản vẽ và 2 ảnh render.
- Chuẩn bị Buổi 05: dùng mô hình và khối lượng để lập kế hoạch tiến độ.

---

## 8. TỆP TRONG THƯ MỤC BUỔI 04

| Tệp | Nội dung |
|---|---|
| `01_Giao_Trinh_Chi_Tiet_Buoi_04.md` | Giáo trình này |
| `02_Thu_Vien_Prompt_Thuc_Chien_Buoi_04.md` | Prompt mẫu: subagent, CLAUDE.md, vẽ AutoCAD, dựng Blender |
| `03_Huong_Dan_Thuc_Hanh_Lab_04_Blender.md` | Hướng dẫn thực hành từng bước |
| `04_Tieu_Chi_Nghiem_Thu_San_Pham_D4.md` | Bảng chấm D4 |
| `05_Mau_CLAUDE_md_Global_Cho_Ky_Su.md` | Mẫu CLAUDE.md Global cho kỹ sư |
| `06_Checklist_Cai_Dat_Truoc_Buoi_Hoc.md` | Gửi học viên trước giờ học |
| `07_Huong_Dan_Cai_Dat_Blender_MCP.md` | Hướng dẫn cài `vn-mcp-blender` đầy đủ, kèm xử lý lỗi |
| `demo/07-nha-pho-lo-7x20m/01_` đến `03_` | Bản vẽ DWG, DXF, file mô tả JSON |
| `demo/07-nha-pho-lo-7x20m/04_` | Mô hình Blender có nội thất, tách tầng |
| `demo/07-nha-pho-lo-7x20m/05_` đến `13_` | Ảnh phối cảnh, mặt bằng nội thất từng tầng, ảnh bung tầng |
| `demo/07-nha-pho-lo-7x20m/08_` | Bộ 4 tờ A3 PDF |
| `demo/07-nha-pho-lo-7x20m/14_` | Bảng thống kê cửa Excel (dùng cho phép "thử phá" số 2) |
| `demo/07-nha-pho-lo-7x20m/scripts/` | 3 script: vẽ AutoCAD, đọc bản vẽ, dựng Blender |
