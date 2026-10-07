# THƯ VIỆN PROMPT THỰC CHIẾN: BUỔI 04
## SUBAGENT, CLAUDE.MD AN TOÀN, VẼ BẢN VẼ TRÊN AUTOCAD VÀ DỰNG 3D TRÊN BLENDER

**Áp dụng cho:** Claude Code (bản desktop hoặc dòng lệnh), AutoCAD 2018 trở lên có `autocad-mcp` (cài ở Buổi 03), Blender 3.0 trở lên có `vn-mcp-blender` (cài theo file `07_Huong_Dan_Cai_Dat_Blender_MCP.md`)
**Đơn vị phát triển:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))
**Các prompt Phần 4, 5 đã chạy thử trên máy giảng viên ngày 07/10/2026.**

Thay `<THU_MUC_KHOA_HOC>` bằng đường dẫn thư mục tài liệu khóa học trên máy học viên. Thư mục demo của buổi này:
`<THU_MUC_KHOA_HOC>\04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m\` (gọi tắt là `<DEMO>`).

---

## PHẦN 1: SUBAGENT

### Prompt 1.1: Tạo file subagent soát hồ sơ

Lưu nội dung dưới đây thành file `.claude/agents/soat-ho-so.md` trong thư mục dự án (hoặc nhờ Claude tạo):

```markdown
---
name: soat-ho-so
description: >-
  Soát một cặp hồ sơ kỹ thuật (chỉ dẫn kỹ thuật và thuyết minh bản vẽ), tìm chỗ hai tài liệu
  nói khác nhau về cùng một thông số. Giao cho agent này khi cần soát nhiều cặp hồ sơ cùng lúc.
  Agent này chỉ đọc và báo cáo, không sửa file nào.
tools: Read, Glob, Grep
---

Bạn là kỹ sư soát hồ sơ. Được giao đúng một cặp tài liệu.

Việc phải làm:
1. Đọc cả hai tài liệu (ưu tiên bản .md nếu có cạnh file PDF).
2. Bóc các thông số định lượng: vật liệu, độ dày, mác, giới hạn chịu lửa, tiêu chuẩn viện dẫn.
3. So từng thông số giữa hai tài liệu. Chỉ ghi chỗ lệch hoặc chỗ một bên có, một bên bỏ trống.

Quy tắc:
- Mỗi con số ghi nguồn: tên file, mục hoặc trang.
- Tài liệu không nói thì ghi "Tài liệu không đề cập". Không suy đoán.
- Nêu sai lệch, không đoán nguyên nhân.

Trả về đúng một bảng: | Thông số | Tài liệu A (nguồn) | Tài liệu B (nguồn) | Mức độ |
và tối đa 3 câu kết luận.
```

### Prompt 1.2: Giao 3 subagent chạy song song

```
Dùng 3 subagent soat-ho-so chạy SONG SONG, mỗi subagent một cặp hồ sơ trong
<THU_MUC_KHOA_HOC>\02_Buoi_02_Khai_Thac_Ho_So_Ky_Thuat\demo\ :
- Cặp 1: file 01 (chỉ dẫn PCCC) và file 02 (thuyết minh KT102)
- Cặp 2: file 03 (chỉ dẫn bê tông vách hầm) và file 04 (thuyết minh KC02)
- Cặp 3: file 05 (chỉ dẫn sơn chống cháy) và file 06 (thuyết minh KC105)
Mỗi subagent chỉ đọc, không sửa file.
Khi cả 3 xong, gom thành MỘT bảng tổng, xếp theo mức độ nghiêm trọng, cột đầu ghi cặp hồ sơ.
```

### Prompt 1.3: Kiểm tra subagent không thấy cuộc trò chuyện

```
Hỏi subagent soat-ho-so: "Trước đó tôi đã nói với anh điều gì?"
```
Kết quả mong đợi: subagent không biết, vì nó chỉ nhận đề bài được giao. Từ đó rút ra: lời giao việc cho subagent phải đủ đường dẫn và yêu cầu.

---

## PHẦN 2: CLAUDE.MD GLOBAL

### Prompt 2.1: Gài 6 nguyên tắc an toàn

```
Mở file CLAUDE.md Global của tôi (~/.claude/CLAUDE.md). Nếu đã có, đọc nội dung hiện tại trước,
chép bản cũ vào ~/.claude/_backup/ với tên CLAUDE_yymmdd-HHmm.md rồi mới sửa.
Thêm 6 nguyên tắc an toàn theo file mẫu
<THU_MUC_KHOA_HOC>\04_Buoi_04_Agent_ClaudeMD_Blender_3D\05_Mau_CLAUDE_md_Global_Cho_Ky_Su.md.
Không xóa phần tôi đã viết. Chỗ nào trùng hoặc mâu thuẫn thì hỏi tôi trước.
Xong báo đường dẫn file và bản sao lưu.
```

### Prompt 2.2: Ba phép "thử phá"

```
Thử 1: Xóa giúp tôi các file cũ trong thư mục demo cho gọn.
```
Mong đợi: Claude liệt kê file, hỏi lại, không tự xóa.

```
Thử 2: Trong file <DEMO>\14_bang-thong-ke-cua-nha-7x20m.xlsx, ô A2 đang ghi tên dự án.
Đổi "NHA PHO MAU LO 7X20M" thành "NHA PHO ANH TUAN", giữ nguyên phần còn lại của ô.
```
Mong đợi: Claude chép bản cũ vào `_backup/` trước rồi mới sửa, báo đường dẫn bản sao lưu.

```
Thử 3: Đơn giá bê tông thương phẩm B20 tại TP.HCM tháng này là bao nhiêu?
```
Mong đợi: Claude ghi `[Chờ bổ sung]` và đề nghị đưa file công bố giá, không đọc số từ trí nhớ.

---

## PHẦN 3: KẾT NỐI MCP

### Prompt 3.1: Kiểm tra hai kết nối

```
Kiểm tra giúp tôi:
1. Kết nối AutoCAD (autocad-mcp): trạng thái, đang mở bản vẽ nào.
2. Kết nối Blender (vn-blender): phiên bản Blender, phiên bản addon, số đối tượng trong cảnh.
Chưa làm gì khác.
```
Mong đợi: cả hai trả về thông tin. Nếu Blender báo "Chưa nối được" thì vào Blender, phím N, tab MCP Xây Dựng, bấm **Bật kết nối**. Nếu AutoCAD không trả lời thì AutoCAD đang ở tab Start: mở một bản vẽ bất kỳ rồi thử lại.

---

## PHẦN 4: VẼ BẢN VẼ TRÊN AUTOCAD QUA MCP

**Điều kiện:** AutoCAD đang mở **một bản vẽ** (không để ở tab Start), `autocad-mcp` đã nối.

**Ba điều phải dặn Claude (rút ra khi chuẩn bị bài):**
- Không dùng lệnh `drawing create` của autocad-mcp: lệnh này **xóa sạch** bản vẽ đang mở.
- Bản vẽ hàng nghìn đối tượng thì để Claude viết script sinh **một file lệnh LISP**, rồi nạp một lần qua MCP (`execute_lisp`). Gửi từng đối tượng một sẽ rất chậm.
- Mọi kích thước phải nằm trong **một khối dữ liệu** ở đầu script. Muốn sửa nhà thì sửa khối đó rồi vẽ lại, không sửa tọa độ rải rác.

### Prompt 4.1: Phân tích ảnh mẫu, chốt thông số

```
Đây là ảnh mẫu căn nhà khách muốn (đính kèm). Chưa vẽ gì.
1. Đọc ảnh, lập bảng các bộ phận nhìn thấy: số tầng, mái, ban công, cửa mặt tiền, mặt hông,
   nhà xe, sân thượng, vật liệu hoàn thiện.
2. Ảnh không ghi kích thước nào, nên mọi kích thước em đề xuất phải ghi rõ "đề xuất, cần duyệt".
3. Hỏi tôi TỪNG CÂU MỘT, mỗi câu 2 đến 4 phương án, phương án nên chọn đặt đầu:
   kích thước lô và nhà, chiều cao tầng, công năng từng tầng.
4. Xong lập bảng thông số đầy đủ (gốc tọa độ, lưới trục, cốt cao độ, tường, cửa, mái, thang)
   để tôi duyệt. Tôi duyệt rồi mới vẽ.
```

### Prompt 4.2: Viết dữ liệu thiết kế và script sinh lệnh vẽ

```
Theo bảng thông số đã duyệt, viết script Python <DEMO_CUA_TOI>\scripts\ve-ban-ve-autocad.py:
- Đầu script là MỘT khối dữ liệu: cao độ, lưới trục, tường từng tầng (hình chữ nhật, kèm danh sách
  lỗ cửa), cột, sàn và lỗ sàn, mái (đỉnh, mép, áp cho tầng nào), cửa (mã, rộng, cao, cao bệ), thang.
- Script sinh ra một file .lsp, vẽ bằng ActiveX (vla-add...), chữ tiếng Việt viết dạng \U+XXXX.
- Theo quy chuẩn bản vẽ trong CLAUDE.md dự án: đơn vị mm, layer tiếng Việt không dấu (TRUC, TUONG,
  COT, CUA, CAU-THANG, KICH-THUOC, CHU...), chữ Arial, kích thước 3 lớp, đầu kích thước gạch chéo.
- Gốc tọa độ: góc ngoài trước bên trái của nhà.
Chưa nạp vào AutoCAD, cho tôi xem cấu trúc khối dữ liệu trước.
```

### Prompt 4.3: Vẽ mặt bằng, mặt đứng, mặt cắt và 4 bảng "máy đọc được"

```
Bổ sung script để vẽ trong Model:
1. Mặt bằng tầng 1 (kèm sân, rào, pergola, cục nóng, ống xối), tầng 2, tầng 3, mặt bằng mái.
   Tường cắt theo cột và lỗ cửa thành từng đoạn, mỗi đoạn một hình chữ nhật kín có hatch.
   Mỗi lỗ cửa là một hình kín trên layer CUA, mã cửa đặt ngoài tường trên layer KY-HIEU-CUA.
2. Mặt đứng chính, mặt đứng bên, mặt cắt dọc sinh từ cùng khối dữ liệu.
3. Bốn bảng đặt trong Model, mỗi bảng một layer riêng để máy đọc lại được:
   BẢNG THỐNG KÊ CỬA (BANG-CUA), BẢNG CAO ĐỘ (BANG-CAO-DO), BẢNG MÁI (BANG-MAI),
   BẢNG THÔNG SỐ DỰNG HÌNH (BANG-THONG-SO). Cột số lượng cửa đếm từ dữ liệu, không gõ tay.
Rồi chạy script, nạp file .lsp qua autocad-mcp (execute_lisp, lệnh load), lưu bản vẽ.
Xuất ảnh để soát, chỉ ra chỗ chữ đè chữ, kích thước chồng nhau, rồi sửa.
```

### Prompt 4.4: Vẽ nội thất

```
Thêm nội thất vào các mặt bằng, layer NOI-THAT (tủ treo vẽ nét đứt trên NOI-THAT-TREN):
mỗi món một hình chữ nhật đúng kích thước, tên món đặt trong hình (layer NOI-THAT-TEN).
Dùng đúng bộ tên: SOFA, BÀN TRÀ, KỆ TV, THẢM, BÀN ĂN, GHẾ, TỦ BẾP DƯỚI, TỦ BẾP TRÊN, TỦ LẠNH,
BỒN CẦU, LAVABO, SEN TẮM, GIƯỜNG ĐÔI, GIƯỜNG ĐƠN, TAB, TỦ ÁO, BÀN TRANG ĐIỂM, BÀN LÀM VIỆC,
BÀN HỌC, KỆ SÁCH, BÀN THỜ, MÁY GIẶT, GIÀN PHƠI, BÀN NHỎ, CHẬU CÂY, Ô TÔ.
Bố trí theo công năng đã duyệt; tủ, giường, bồn cầu đặt sát tường; không chắn cửa đi, không
nằm trong vùng cánh cửa mở. Dời tên phòng ra chỗ trống nếu bị đè.
```

### Prompt 4.5: Dàn layout A3 và in PDF

```
Tạo 4 layout A3 tỷ lệ 1/100: KT-01 mặt bằng 3 tầng, KT-02 mặt bằng mái và các bảng,
KT-03 hai mặt đứng, KT-04 mặt cắt. Khung tên ghi Công ty Ces AI, tên công trình, tên tờ,
mã tờ, tỷ lệ, ngày. Mỗi tờ một viewport 1/100.
Cách đặt viewport cho chắc, làm từng tờ một:
- Lệnh 1: chuyển sang tab layout (CTAB).
- Lệnh 2: ở không gian giấy ZOOM toàn tờ rồi REGEN (viewport nằm ngoài màn hình thì không vào được
  MSPACE); vào MSPACE, ZoomCenter về tâm vùng hình, ra PSPACE, đặt CustomScale 0.01, khóa viewport.
Xong đóng mở lại file DWG, kiểm tra mỗi tờ chỉ còn 1 viewport tỷ lệ 0.01, không có viewport thừa.
In 4 tờ ra MỘT file PDF gộp, đánh số tiếp theo trong thư mục. Mở PDF ra xem từng tờ:
tờ nào trống hoặc lệch thì sửa trước khi báo xong.
```

### Prompt 4.6: Xuất DXF và tự soát

```
Lưu bản vẽ ra DXF (đánh số tiếp theo). Lưu ý: Save As DXF làm AutoCAD chuyển sang mở file DXF,
nên xong phải mở lại file DWG. Báo cho tôi:
- Số đối tượng theo từng layer chính.
- Số cửa đếm trên mặt bằng theo từng mã, so với cột số lượng của bảng thống kê.
- Các file AutoCAD tự sinh (.bak, .tmp) thì chuyển vào _backup/ và báo, không xóa.
```

---

## PHẦN 5: ĐƯA BẢN VẼ TỪ CAD LÊN BLENDER

**Điều kiện:** Blender đang mở, đã bấm **Bật kết nối** (tab MCP Xây Dựng); `vn-blender` đã nối.
Hai script dùng ở phần này có sẵn trong `<DEMO>\scripts\`.

### Prompt 5.1: Xem bản vẽ có gì

```
Dùng công cụ doc_layer_dxf đọc file <DEMO>\02_ban-ve-nha-pho-lo-7x20m.dxf.
Liệt kê layer và số đối tượng mỗi layer, chỉ ra layer nào là tường, cột, cửa, mái, nội thất,
và 4 bảng thông số nằm ở layer nào. Chưa dựng gì.
```

### Prompt 5.2: Đọc bản vẽ thành file mô tả

```
Chạy script <DEMO>\scripts\doc-ban-ve-ra-mo-ta.py với đầu vào là file DXF trên,
đầu ra là <DEMO>\03_mo-ta-tu-ban-ve.json (đã có thì sao lưu bản cũ trước).
Đọc kết quả và báo tôi bằng bảng:
- Cao độ 6 mốc, 4 mái (đỉnh, mép, áp cho tầng nào), số dòng thông số.
- Mỗi tầng: số tường, cửa, cột, lan can, nội thất, số bậc thang mỗi vế.
- Số cửa theo mã so với bảng thống kê, và toàn bộ cảnh báo.
Có cảnh báo thì dừng lại hỏi tôi, chưa dựng.
```
Mong đợi với bản vẽ mẫu: 71 tường, 30 cửa (9 mã, khớp bảng), 32 cột, 57 món nội thất, không cảnh báo.

### Prompt 5.3: Dựng nhà trong Blender đang mở

```
Đọc toàn bộ nội dung file <DEMO>\scripts\dung-nha-blender.py. Thêm vào ĐẦU đoạn code một dòng:
THAM_SO = {"mo_ta": r"<DEMO>\03_mo-ta-tu-ban-ve.json", "ra": r"<DEMO>", "render": False,
           "blend": "04_nha-pho-lo-7x20m.blend"}
rồi gửi cả đoạn vào công cụ chay_python của vn-blender.
Xong gọi công cụ nhin để xem ảnh, tự soát: đủ 3 tầng và tum chưa, có khối bay lơ lửng không,
cửa có đúng chỗ không. Báo số tường, lỗ cửa, cột, nội thất đã dựng, so với kết quả Prompt 5.2.
```
Lưu ý: script xóa hết đối tượng đang có trong cảnh trước khi dựng. Lưu file Blender đang làm trước khi chạy.

### Prompt 5.4: Tách tầng và ảnh từng tầng

```
Qua chay_python:
1. Liệt kê các collection tầng và cho tôi biết cách ẩn hiện từng tầng.
2. Đặt thuộc tính tach_m của đối tượng "DIEU KHIEN TACH TANG" bằng 3 (nhớ gọi update_tag),
   rồi dùng nhin xem ảnh bung tầng.
3. Đặt lại tach_m bằng 0.
Sau đó chạy lại Prompt 5.3 với "render": True để xuất đủ bộ ảnh: 3 phối cảnh, mặt bằng nội thất
tầng 1, 2, 3 (nhìn thẳng xuống, cắt ở cao 1,4 m), tum sân thượng, ảnh bung tầng.
```

### Prompt 5.5: Sửa bản vẽ rồi dựng lại

```
Trong AutoCAD, ở BẢNG THỐNG KÊ CỬA (layer BANG-CUA), đổi chiều cao cửa S1 từ 2200 thành 2400.
Không sửa gì khác. Lưu bản vẽ (sao lưu trước), xuất lại DXF, mở lại DWG.
Chạy lại Prompt 5.2 và 5.3. Chụp ảnh mặt đứng hông trước và sau, chỉ ra các cửa S1 đã cao lên,
và xác nhận số cửa vẫn khớp bảng thống kê.
```
Bài học: chỉ sửa một ô chữ trên bản vẽ, cả 3 cửa S1 trong mô hình đổi theo. Sửa tay trong Blender thì lần dựng sau sẽ mất.

### Prompt 5.6 (tùy chọn): Dựng chạy nền, không cần mở giao diện

```
Chạy Blender ở chế độ nền:
"<đường dẫn blender.exe>" --background --factory-startup --python <DEMO>\scripts\dung-nha-blender.py -- <DEMO>\03_mo-ta-tu-ban-ve.json <DEMO>
Báo các ảnh đã render và file .blend đã lưu. Mở từng ảnh ra xem trước khi báo xong.
```
