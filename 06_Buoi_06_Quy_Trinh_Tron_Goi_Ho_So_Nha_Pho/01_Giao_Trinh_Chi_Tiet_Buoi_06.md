# GIÁO TRÌNH CHI TIẾT: BUỔI 06
## RÁP TRỌN QUY TRÌNH: TỪ Ý TƯỞNG CỦA CHỦ NHÀ ĐẾN BỘ HỒ SƠ GỬI KHÁCH (ĐỒ ÁN CUỐI KHÓA)

**Thời lượng:** 150 phút (khoảng 20% lý thuyết, 80% thị phạm và đồ án)
**Áp dụng cho:** Claude Code Desktop (tab Code) trên Windows, AutoCAD 2020 trở lên, Blender 4.2 trở lên
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))
**Thông tin công cụ tra ngày 10/10/2026:** tài liệu chính thức Claude Code `code.claude.com/docs/en/sub-agents`, `/skills`, `/goal`, `/permission-modes`, `/desktop`.
**Nối từ các buổi trước:** MCP AutoCAD (Buổi 03); CLAUDE.md an toàn, đường ống AutoCAD sang Blender, script vẽ và dựng nhà (Buổi 04); 3 agent chuyên trách, MCP ChatGPT tạo ảnh, BOQ (Buổi 05).

> File này gồm đủ: giáo trình, kịch bản thị phạm, thư viện prompt cho 7 chặng, đề đồ án Lab 06 và bảng chấm D6. Mọi prompt viết để dán thẳng vào Claude Code Desktop.

---

## 1. MỤC TIÊU BÀI HỌC

Sau buổi học, học viên:
1. **Nhìn thấy cả quy trình hồ sơ nhà phố như một dây chuyền 7 chặng**, mỗi chặng có đầu vào, đầu ra là file và một người chịu trách nhiệm duyệt.
2. **Tự chạy trọn dây chuyền trên căn nhà của mình:** từ ảnh mẫu, yêu cầu chủ nhà đến bản vẽ AutoCAD, mô hình Blender, ảnh phối cảnh nhiều phong cách, BOQ phần thô và một file PDF gửi khách.
3. **Đặt cổng duyệt người** ở những chỗ sai thì tốn kém: chốt thông số, duyệt bản vẽ, duyệt trước khi gửi khách. AI không tự gửi gì ra ngoài.
4. **Xử lý một yêu cầu đổi ý của chủ nhà** bằng cách sửa bản vẽ rồi chạy lại các chặng sau, phát hành hồ sơ lần 2.
5. **Đóng gói quy trình thành skill** dùng lại cho công trình kế tiếp.

---

## 2. TIẾN TRÌNH 150 PHÚT

```
00:00 - 00:10 (10')  Mở đầu: nhìn lại 5 buổi, sơ đồ dây chuyền 7 chặng
00:10 - 00:30 (20')  Lý thuyết: bàn giao bằng file, 3 cổng duyệt, thư mục hồ sơ chuẩn, điều phối đội agent
00:30 - 01:00 (30')  Thị phạm: giảng viên chạy nhanh 7 chặng trên căn nhà mẫu, dừng ở từng cổng duyệt
01:00 - 01:10 (10')  Nghỉ giải lao
01:10 - 02:05 (55')  Đồ án Lab 06: học viên chạy 7 chặng trên căn nhà của mình, phát hành lần 1
02:05 - 02:15 (10')  Tình huống đổi ý: chủ nhà sửa một chi tiết, phát hành lần 2
02:15 - 02:30 (15')  Trình bày chéo, chấm D6, tổng kết khóa
```

**Chuẩn bị của giảng viên trước giờ học**

| Việc | Kiểm tra |
|---|---|
| AutoCAD mở sẵn một bản vẽ trống (không để ở tab Start) | `/mcp` thấy `autocad-mcp` Connected |
| Blender mở, addon vn-blender bật kết nối | `/mcp` thấy `vn-blender` Connected |
| MCP `chatgpt-image` đăng nhập | Prompt C1 Buổi 05 trả về đã đăng nhập |
| 3 agent Buổi 05 có trong `~/.claude/agents/` (để dùng ở mọi thư mục) | Prompt 0.2 bên dưới |
| Chuẩn bị 1 căn nhà mẫu cho thị phạm (ảnh mẫu + 5 dòng yêu cầu chủ nhà) | Nên chạy thử trọn 7 chặng tối hôm trước |
| Học viên mang căn nhà của mình (bài về nhà Buổi 05) | Ai không có thì dùng đề dự phòng ở mục 7.2 |

---

## 3. MỞ ĐẦU VÀ LÝ THUYẾT (30 PHÚT)

### 3.1. Năm buổi vừa qua là năm khúc của một dây chuyền (10 phút)

```
 [1] Đầu vào      [2] Chốt          [3] Bản vẽ       [4] Mô hình     [5] Phối cảnh    [6] Khối lượng   [7] Hồ sơ
 ảnh, yêu cầu --> thông số    -->   AutoCAD     -->  Blender    -->  AI đổi      -->  BOQ phần   -->  gửi khách
 chủ nhà          /plan            (Buổi 03, 04)    (Buổi 04)       phong cách       thô (Buổi 05)    PDF gộp
 (Buổi 01, 02)    CỔNG DUYỆT 1     CỔNG DUYỆT 2                     (Buổi 05)                         CỔNG DUYỆT 3
```

| Chặng | Đầu vào | Đầu ra (file) | Công cụ | Ai duyệt |
|---|---|---|---|---|
| 1. Đầu vào | Ảnh mẫu, file yêu cầu (PDF, Word, Zalo chép ra) | `01-ho-so-dau-vao/*.md`, `00-thong-tin-cong-trinh.md` | MarkItDown, đọc ảnh | |
| 2. Chốt thông số | Phiếu thông tin | `02-thong-so/01_phieu-thong-so.md` | `/plan` | **Cổng 1: kỹ sư chủ trì** |
| 3. Bản vẽ | Phiếu thông số | DWG, DXF, PDF A3 các tờ KT | MCP AutoCAD, script vẽ Buổi 04 | **Cổng 2: kỹ sư chủ trì** |
| 4. Mô hình | DXF | File mô tả JSON, `.blend`, ảnh phối cảnh, ảnh tách tầng | vn-blender, script dựng nhà Buổi 04 | Tự kiểm: số cửa khớp bảng |
| 5. Phối cảnh AI | Ảnh render Blender | 2 đến 3 ảnh phong cách + bảng so sánh | Agent `render-phong-cach` | Tự kiểm: giữ kiến trúc |
| 6. Khối lượng | File mô tả JSON | BOQ Excel + tóm tắt | Agent `boc-khoi-luong`, `kiem-tra-khoi-luong` | Tự kiểm: agent kiểm tra |
| 7. Hồ sơ gửi khách | Đầu ra chặng 3 đến 6 | PDF gộp + thư gửi khách (nháp) trong `04-phat-hanh/yymmdd_lan-N/` | Python ghép PDF, Excel xuất PDF | **Cổng 3: kỹ sư chủ trì gửi** |

### 3.2. Ba nguyên tắc ráp dây chuyền (10 phút)

1. **Bàn giao bằng file, không bằng trí nhớ.** Mỗi chặng ghi kết quả ra file trong thư mục hồ sơ; chặng sau đọc file đó. Nhờ vậy subagent (không thấy cuộc trò chuyện) vẫn làm đúng, và hôm sau mở phiên mới vẫn làm tiếp được.
2. **Cổng duyệt đặt ở chỗ sai thì đắt.** Sai thông số thì vẽ lại cả bộ; sai bản vẽ thì mô hình, ảnh, khối lượng đều sai theo; gửi nhầm cho khách thì không lấy lại được. Ba chỗ đó **người duyệt**, AI dừng chờ. Các chặng còn lại để agent tự kiểm chéo.
3. **Bản vẽ là nguồn.** Chủ nhà đổi ý thì sửa bản vẽ (chặng 3) rồi chạy lại chặng 4 đến 7, không sửa tay mô hình, ảnh hay Excel. Mỗi lần gửi khách là một thư mục phát hành mới `yymmdd_lan-N`, thư mục cũ giữ nguyên.

**Ai điều phối:** agent chính (phiên Claude anh/chị đang chat) làm "chủ trì hồ sơ": đọc CLAUDE.md của dự án, giao việc cho 3 agent chuyên trách của Buổi 05, gộp kết quả, dừng ở cổng duyệt. Lệnh `/goal` dùng để kiểm hồ sơ phát hành đã đủ thành phần chưa (Prompt 7.2). Tài liệu chính thức ghi `/goal` chạy được trong Desktop; agent team thì không (Buổi 05, mục 4.3).

### 3.3. Thư mục hồ sơ chuẩn cho một căn nhà (thống nhất cả lớp)

```
<CT>\                                  (ví dụ D:\AI-XayDung\ct-01-nha-pho-anh-a)
├── CLAUDE.md                          quy trình 7 chặng, 3 cổng duyệt (Prompt 0.1 tạo)
├── 00-thong-tin-cong-trinh.md
├── 01-ho-so-dau-vao\                  ảnh mẫu, yêu cầu chủ nhà và bản .md
├── 02-thong-so\                       phiếu thông số đã duyệt
├── 03-ban-ve\                         DWG, DXF, PDF, script vẽ
├── 04-mo-hinh-3d\                     file mô tả JSON, .blend, ảnh Blender, ảnh AI
├── 05-khoi-luong\                     BOQ Excel, tóm tắt, script
├── 06-phat-hanh\yymmdd_lan-N\         hồ sơ đã gửi khách: không sửa, không xóa
└── _backup\
```

---

## 4. KỊCH BẢN THỊ PHẠM 30 PHÚT

| Phút | Việc | Prompt | Điểm nhấn cho lớp |
|---|---|---|---|
| 0 đến 3 | Tạo thư mục, CLAUDE.md dự án | 0.1 | Một lần cho mỗi công trình |
| 3 đến 6 | Chặng 1: đọc ảnh mẫu, yêu cầu | 1.1 | Thông tin thiếu thì ghi `[Chờ bổ sung]`, không đoán |
| 6 đến 10 | Chặng 2: `/plan` chốt thông số | 2.1 | **Cổng 1**: dừng hỏi, giảng viên sửa 1 thông số rồi duyệt |
| 10 đến 18 | Chặng 3: vẽ 4 tờ, xuất PDF, DXF | 3.1 | **Cổng 2**: mở PDF xem tận mắt (bài học "PDF trắng" Buổi 04) |
| 18 đến 22 | Chặng 4: dựng Blender, tách tầng | 4.1 | Số cửa trên mô hình khớp bảng cửa |
| 22 đến 26 | Chặng 5 và 6 chạy song song | 5.1 | Mở bảng Tasks: 2 agent cùng chạy |
| 26 đến 30 | Chặng 7: ghép PDF, soạn thư, `/goal` kiểm đủ | 7.1, 7.2 | **Cổng 3**: AI dừng, không gửi |

Nếu một chặng chạy lâu (AutoCAD, render), giảng viên mở sẵn kết quả của lần chạy thử tối hôm trước để không mất nhịp.

---

## 5. ĐỒ ÁN LAB 06 (55 PHÚT) VÀ TÌNH HUỐNG ĐỔI Ý (10 PHÚT)

### 5.1. Đề bài

Mỗi học viên (hoặc nhóm 2 người) chạy 7 chặng trên **căn nhà của mình**, phát hành hồ sơ lần 1 trong thư mục `06-phat-hanh\yymmdd_lan-1\`.

Giới hạn để kịp 55 phút:
- Nhà phố hoặc nhà ống, **tối đa 3 tầng**, mặt bằng chữ nhật.
- Bản vẽ: 4 tờ như Buổi 04 (mặt bằng các tầng, mặt đứng, mặt cắt, bảng thống kê cửa). Chưa làm kết cấu, điện nước.
- Phối cảnh AI: 2 phong cách.
- BOQ: phần thô 4 nhóm như Buổi 05.

**Học viên chưa chạy được AutoCAD:** bỏ chặng 3, dùng DXF mẫu của nhà 7x20m (`04_Buoi_04.../demo/07-nha-pho-lo-7x20m/02_ban-ve-nha-pho-lo-7x20m.dxf`) và làm tiếp từ chặng 4. Vẫn chấm đủ các tiêu chí còn lại.

### 5.2. Mốc thời gian gợi ý

| Phút (trong 55') | Chặng |
|---|---|
| 0 đến 8 | 0.1, chặng 1, chặng 2 (đến cổng 1) |
| 8 đến 28 | Chặng 3 (đến cổng 2) |
| 28 đến 38 | Chặng 4 |
| 38 đến 48 | Chặng 5 và 6 song song |
| 48 đến 55 | Chặng 7, `/goal` kiểm đủ |

### 5.3. Tình huống đổi ý (10 phút)

Giảng viên phát cho mỗi bàn **một yêu cầu đổi ý** (chọn 1):
- Chủ nhà muốn cửa sổ phòng ngủ tầng 2 cao thêm 200 mm.
- Chủ nhà muốn thêm 1 cửa sổ ở mặt hông tầng 3.
- Chủ nhà ưng phong cách nhiệt đới và muốn biết thêm lam gỗ mặt tiền thì khối lượng thay đổi thế nào.

Học viên chạy **Prompt 8.1**: sửa bản vẽ, chạy lại chặng 4 đến 7, phát hành `lan-2`, kèm bảng so sánh khối lượng lần 1 và lần 2. Tình huống thứ ba là bẫy: lam gỗ chỉ có trên ảnh AI, chưa có trên bản vẽ, nên **không bóc được**; câu trả lời đúng là đề xuất bổ sung bản vẽ chi tiết lam trước.

---

## 6. NGHIỆM THU D6 VÀ TỔNG KẾT KHÓA (15 PHÚT)

### 6.1. Thành phần hồ sơ D6 (đồ án cuối khóa)

1. Thư mục công trình đúng cấu trúc mục 3.3, có `CLAUDE.md` dự án.
2. Thư mục phát hành `lan-1`: PDF gộp gửi khách (bìa, bản vẽ, phối cảnh, BOQ) và thư gửi khách dạng nháp.
3. Thư mục phát hành `lan-2` sau tình huống đổi ý, kèm bảng so sánh khối lượng.
4. Nhật ký quy trình `nhat-ky-quy-trinh.md`: mỗi chặng ghi giờ bắt đầu, kết thúc, ai duyệt, sửa gì ở cổng duyệt.
5. Skill `ho-so-nha-pho` (Prompt 9.1) hoặc sổ prompt cá nhân dùng lại cho công trình sau.

### 6.2. Bảng chấm (thang 100)

| STT | Tiêu chí | Điểm | ĐẠT | CHƯA ĐẠT |
|---|---|---|---|---|
| 1 | Hồ sơ phát hành lần 1 đủ thành phần; PDF mở ra có nội dung ở mọi trang; ảnh AI có ghi chú "ảnh minh họa phong cách, không phải hồ sơ kỹ thuật"; BOQ không tự điền đơn giá | 35 | | |
| 2 | Ba cổng duyệt có thật: nhật ký ghi rõ AI dừng chờ ở cổng 1, 2, 3 và người duyệt đã sửa hoặc xác nhận gì; không có gì tự gửi ra ngoài | 20 | | |
| 3 | Số liệu xuyên suốt khớp nhau: số cửa trên bản vẽ, trong file mô tả, trong BOQ bằng nhau; kích thước khối nhà trên bản vẽ và mô hình bằng nhau | 20 | | |
| 4 | Tình huống đổi ý: sửa từ bản vẽ, phát hành lần 2 thư mục mới, lần 1 giữ nguyên; có bảng so sánh khối lượng; xử lý đúng bẫy "chỉ có trên ảnh AI" nếu gặp | 15 | | |
| 5 | Có skill hoặc sổ prompt dùng lại được cho công trình sau | 10 | | |

**Xếp loại:** Xuất sắc 90 đến 100 · Đạt 70 đến 89 · Chưa đạt dưới 70.

### 6.3. Tổng kết khóa (5 phút)

Ba câu chốt của khóa học:
1. **Bản vẽ là nguồn.** Mô hình, ảnh, khối lượng đều đọc lại từ bản vẽ.
2. **Người duyệt ở chỗ đắt tiền.** AI làm nhanh, người chịu trách nhiệm ký.
3. **Không bịa số.** Thiếu thì ghi `[Chờ bổ sung]`, mâu thuẫn thì báo, đơn giá lấy từ công bố giá có nguồn.

Hồ sơ trong khóa là bản triển khai theo cấu tạo để học. Trước khi xin phép hay thi công phải có kỹ sư, kiến trúc sư có chứng chỉ hành nghề phù hợp kiểm tra và ký.

---

## 7. THƯ VIỆN PROMPT

Quy ước đường dẫn trong prompt:
- `<CT>`: thư mục công trình của học viên (mục 3.3). Mở Claude Code Desktop tại thư mục này.
- `<B04>`: thư mục `04_Buoi_04_Agent_ClaudeMD_Blender_3D` trong tài liệu khóa học (có `demo\07-nha-pho-lo-7x20m\scripts\`).
- `yymmdd`: ngày phát hành, ví dụ `261011`.

### Prompt 0.1: Tạo thư mục công trình và CLAUDE.md dự án

```
Tạo khung thư mục công trình trong thư mục hiện tại theo cấu trúc:
00-thong-tin-cong-trinh.md, 01-ho-so-dau-vao, 02-thong-so, 03-ban-ve, 04-mo-hinh-3d, 05-khoi-luong, 06-phat-hanh, _backup.
Rồi tạo file CLAUDE.md của dự án với nội dung:

# Quy trình hồ sơ nhà phố 7 chặng
1. Đầu vào: chuyển mọi file yêu cầu sang .md bằng markitdown, lưu 01-ho-so-dau-vao.
2. Chốt thông số: lập 02-thong-so/01_phieu-thong-so.md. DỪNG, chờ tôi duyệt (cổng 1).
3. Bản vẽ: vẽ trên AutoCAD qua autocad-mcp, xuất DWG, DXF, PDF A3 vào 03-ban-ve. DỪNG, chờ tôi mở PDF duyệt (cổng 2).
4. Mô hình: đọc DXF thành file mô tả, dựng Blender, render, tách tầng, lưu 04-mo-hinh-3d.
5. Phối cảnh AI: giao agent render-phong-cach, lưu 04-mo-hinh-3d/ai.
6. Khối lượng: giao agent boc-khoi-luong, sau đó agent kiem-tra-khoi-luong, lưu 05-khoi-luong.
7. Hồ sơ gửi khách: ghép PDF và soạn thư nháp vào 06-phat-hanh/yymmdd_lan-N. DỪNG, chờ tôi gửi (cổng 3). Không tự gửi email, Zalo hay bất kỳ thứ gì ra ngoài.
Quy tắc chung:
- Bản vẽ là nguồn. Đổi thiết kế thì sửa bản vẽ rồi chạy lại các chặng sau.
- Thư mục 06-phat-hanh là hồ sơ đã gửi: không sửa, không xóa; lần sau tạo thư mục lan-N mới.
- Mỗi chặng xong thì ghi một dòng vào nhat-ky-quy-trinh.md: chặng, giờ, kết quả, ai duyệt.
- Không bịa số liệu. Thiếu thì ghi [Chờ bổ sung].
- Khung tên bản vẽ ghi tên công ty của tôi: <TÊN CÔNG TY>.
```

### Prompt 0.2: Kiểm tra đội agent (chạy một lần đầu buổi)

```
Liệt kê các agent chuyên trách tôi đang có ở ~/.claude/agents và .claude/agents của thư mục hiện tại. Cần có: boc-khoi-luong, kiem-tra-khoi-luong, render-phong-cach.
Agent nào đang chỉ nằm trong thư mục Buổi 05 thì chép sang ~/.claude/agents để dùng ở mọi công trình (không xóa bản gốc). Kiểm tra thêm các MCP autocad-mcp, vn-blender, chatgpt-image đang kết nối.
```
Chép xong thì mở phiên mới (`Ctrl+N`) để Claude nạp agent.

### CHẶNG 1: ĐẦU VÀO

### Prompt 1.1: Đọc ảnh mẫu và yêu cầu chủ nhà

```
Trong 01-ho-so-dau-vao có ảnh mẫu và file yêu cầu của chủ nhà.
1. Chuyển mọi file PDF, Word sang .md bằng markitdown, lưu cùng thư mục.
2. Mô tả ảnh mẫu: số tầng, kiểu mái, ban công, nhà xe, vật liệu mặt tiền. Chỉ ghi điều nhìn thấy.
3. Điền 00-thong-tin-cong-trinh.md: tên công trình, chủ nhà (dùng tên mẫu nếu là hồ sơ học tập), địa điểm, kích thước lô đất, số tầng, công năng từng tầng, số phòng ngủ, WC, gara, hướng nhà, ngân sách nếu có. Thiếu thông tin nào ghi [Chờ bổ sung], không tự đoán.
4. Liệt kê các câu cần hỏi lại chủ nhà.
```

### CHẶNG 2: CHỐT THÔNG SỐ (CỔNG 1)

### Prompt 2.1: Lập phiếu thông số bằng /plan

```
/plan Từ 00-thong-tin-cong-trinh.md và ảnh mẫu, lập phiếu thông số thiết kế cho căn nhà, lưu 02-thong-so/01_phieu-thong-so.md:
- Lô đất, khối nhà, khoảng lùi trước, sau.
- Lưới trục (mm), cốt các tầng (mm, ±0.000 tại nền tầng 1), chiều dày tường, sàn.
- Công năng và kích thước từng phòng theo tầng.
- Bảng cửa: mã, rộng, cao, bậu, số lượng, vị trí.
- Mái: kiểu, độ dốc, cao độ đỉnh và mép.
Mọi thông số tự đề xuất đánh dấu (đề xuất) để tôi duyệt. Bám theo cách lập bảng thông số nhà 7x20m ở Buổi 04.
```
Cổng 1: đọc phiếu, sửa ít nhất 1 thông số (ví dụ chiều cao tầng 1), rồi duyệt kế hoạch.

### CHẶNG 3: BẢN VẼ AUTOCAD (CỔNG 2)

### Prompt 3.1: Vẽ 4 tờ từ phiếu thông số

```
Vẽ bộ bản vẽ kiến trúc cho căn nhà theo 02-thong-so/01_phieu-thong-so.md, dùng autocad-mcp, làm theo cách của Buổi 04:
1. Chép script <B04>\demo\07-nha-pho-lo-7x20m\scripts\ve-ban-ve-autocad.py vào 03-ban-ve, chỉ sửa khối dữ liệu đầu file (trục, cốt tầng, tường, cửa, mái, phòng, nội thất) theo phiếu thông số. Không sửa phần hàm vẽ.
2. Sinh file .lsp và nạp vào AutoCAD bằng một lệnh (load ...). Không dùng lệnh tạo bản vẽ mới (sẽ xóa bản vẽ đang mở).
3. Giữ đúng layer "máy đọc được" và 4 bảng: BANG-CUA, BANG-CAO-DO, BANG-MAI, BANG-THONG-SO.
4. Dàn 4 layout KT-01 đến KT-04 khổ A3 tỷ lệ 1/100, khung tên ghi tên công ty theo CLAUDE.md.
5. Lưu DWG, xuất DXF, in PDF gộp 4 tờ vào 03-ban-ve.
6. Mở PDF, chuyển từng trang sang ảnh, xem từng trang có nội dung không. Trang nào trắng thì báo, không nói là xong.
Xong thì DỪNG để tôi duyệt (cổng 2).
```
Nếu vẽ lỗi: dùng lại các prompt chi tiết 4.2 đến 4.6 trong `02_Thu_Vien_Prompt_Thuc_Chien_Buoi_04.md`.

### CHẶNG 4: MÔ HÌNH BLENDER

### Prompt 4.1: Đọc bản vẽ, dựng nhà, tách tầng

```
Dựng mô hình từ bản vẽ đã duyệt, làm theo cách của Buổi 04, lưu mọi kết quả vào 04-mo-hinh-3d:
1. Chạy script <B04>\demo\07-nha-pho-lo-7x20m\scripts\doc-ban-ve-ra-mo-ta.py đọc DXF trong 03-ban-ve thành 03_mo-ta-tu-ban-ve.json. Báo số tường, cột, cửa, nội thất và các cảnh báo.
2. Nếu số cửa trong file mô tả lệch bảng cửa: DỪNG báo tôi, không tự sửa.
3. Dựng nhà trong Blender đang mở bằng dung-nha-blender.py qua vn-blender, render phối cảnh góc hông, góc cao, mặt tiền.
4. Chạy tach-tang-mat-bang.py để có ảnh từng tầng nhìn từ trên xuống.
5. Lưu file .blend. Xem lại từng ảnh render trước khi báo xong.
```

### CHẶNG 5 VÀ 6: PHỐI CẢNH AI VÀ KHỐI LƯỢNG (CHẠY SONG SONG)

### Prompt 5.1: Giao song song hai agent, sau đó kiểm tra

```
Giao việc cho đội agent, không tự làm thay:
Nhánh 1 (song song): agent render-phong-cach đổi phong cách ảnh phối cảnh góc hông trong 04-mo-hinh-3d thành 2 phong cách chủ nhà thích (đọc trong 00-thong-tin-cong-trinh.md; chưa có thì dùng Đông Dương và hiện đại tối giản). Lưu vào 04-mo-hinh-3d\ai, kèm bảng so sánh với ảnh gốc.
Nhánh 2 (song song): agent boc-khoi-luong bóc khối lượng phần thô 4 nhóm (tường xây, bê tông sàn, cột, cửa) từ 04-mo-hinh-3d\03_mo-ta-tu-ban-ve.json, quy ước như Prompt D1 Buổi 05. Xuất 05-khoi-luong\01_boq-phan-tho.xlsx, file tóm tắt .md và script.
Bước 3 (chờ nhánh 2): agent kiem-tra-khoi-luong soát bảng, nêu tối thiểu 3 điểm cần xem lại.
Gộp kết quả, ghi nhật ký quy trình.
```

### CHẶNG 7: HỒ SƠ GỬI KHÁCH (CỔNG 3)

### Prompt 7.1: Ghép PDF gửi khách và soạn thư nháp

```
Lập hồ sơ gửi chủ nhà lần 1 trong thư mục 06-phat-hanh\yymmdd_lan-1:
1. Một file PDF gộp, khổ A3 ngang, theo thứ tự:
   (a) Trang bìa: tên công trình, chủ nhà, địa điểm, ngày, tên công ty, danh mục hồ sơ.
   (b) Các tờ bản vẽ PDF trong 03-ban-ve.
   (c) Ảnh phối cảnh Blender và ảnh tách tầng trong 04-mo-hinh-3d.
   (d) Ảnh phối cảnh AI, mỗi trang ghi rõ: "Ảnh minh họa phong cách tạo bằng AI, không phải hồ sơ kỹ thuật".
   (e) Bảng khối lượng phần thô: xuất từ Excel sang PDF; đơn giá còn trống thì để nguyên [Chờ bổ sung].
   Dùng Python để ghép; xuất Excel sang PDF thì mở Excel ở chế độ chỉ đọc. Đặt tên file 01_ho-so-phuong-an-<ten-cong-trinh>.pdf.
2. Thư gửi chủ nhà dạng nháp 02_thu-gui-chu-nha.md: lời chào, tóm tắt phương án (số tầng, diện tích sàn tính từ bản vẽ, các phòng), các câu cần chủ nhà trả lời, bước tiếp theo. Không ghi giá tiền nếu chưa có đơn giá.
3. Mở PDF, chuyển từng trang sang ảnh, kiểm tra không có trang trắng, đếm số trang.
Xong thì DỪNG. Không gửi email, Zalo hay bất kỳ thứ gì ra ngoài.
```

### Prompt 7.2: Dùng /goal kiểm hồ sơ đủ thành phần

```
/goal Thư mục 06-phat-hanh\yymmdd_lan-1 có đủ: file PDF gộp mà mọi trang đều có nội dung (đã chuyển từng trang sang ảnh và báo số trang), có trang bìa, có bản vẽ, có phối cảnh, có ghi chú ảnh AI, có bảng khối lượng; có thư gửi chủ nhà dạng nháp; nhật ký quy trình có đủ 7 chặng; số cửa trong bản vẽ, file mô tả và BOQ bằng nhau. Thiếu thì bổ sung, không gửi gì ra ngoài. Hoặc dừng sau 15 lượt.
```
Theo tài liệu chính thức: sau mỗi lượt, một mô hình khác chấm điều kiện; `/goal` không tự cấp quyền, ở chế độ Manual Claude vẫn hỏi trước khi chạy lệnh; `/goal clear` để dừng sớm.

### TÌNH HUỐNG ĐỔI Ý

### Prompt 8.1: Chủ nhà đổi ý, phát hành lần 2

```
Chủ nhà yêu cầu: <dán yêu cầu đổi ý>.
1. Lưu yêu cầu vào 01-ho-so-dau-vao\yeu-cau-sua-lan-1.md kèm ngày.
2. Nếu yêu cầu chỉ có trên ảnh AI mà chưa có trên bản vẽ (ví dụ lam gỗ), DỪNG: báo tôi cần bổ sung bản vẽ chi tiết gì trước, không tự bóc khối lượng.
3. Ngược lại: sao lưu bản vẽ cũ vào _backup, sửa đúng dữ liệu liên quan trong script vẽ, vẽ lại, xuất DXF, PDF. DỪNG chờ tôi duyệt.
4. Sau khi tôi duyệt: chạy lại chặng 4 đến 7, phát hành vào 06-phat-hanh\yymmdd_lan-2. Thư mục lan-1 giữ nguyên.
5. Lập bảng so sánh khối lượng lần 1 và lần 2: hạng mục, lần 1, lần 2, chênh lệch, lý do. Chênh lệch do Python tính.
```

### ĐÓNG GÓI

### Prompt 9.1: Đóng gói quy trình thành skill

```
Đóng gói quy trình 7 chặng vừa chạy thành một skill để dùng cho công trình sau:
- Vị trí: ~/.claude/skills/ho-so-nha-pho/SKILL.md
- Phần đầu: name: ho-so-nha-pho; description: "Lập hồ sơ phương án nhà phố từ ảnh mẫu và yêu cầu chủ nhà đến PDF gửi khách, 7 chặng, 3 cổng duyệt. Dùng khi bắt đầu một công trình nhà phố mới."
- Nội dung: 7 chặng, đầu vào, đầu ra từng chặng, 3 cổng duyệt bắt buộc dừng, các prompt đã dùng tốt hôm nay (lấy từ cuộc trò chuyện này), các lỗi đã gặp và cách xử lý.
- Không ghi thông tin thật của chủ nhà vào skill.
Tạo xong đọc lại file, rồi cho tôi biết cách gọi: gõ /ho-so-nha-pho trong phiên mới.
```

---

## 8. ĐỀ DỰ PHÒNG CHO HỌC VIÊN KHÔNG MANG CĂN NHÀ

```
Nhà phố anh Nguyễn Văn A (tên mẫu), lô 5x20m, hướng Đông Nam.
- 3 tầng, mái bằng có sân thượng phía sau, tum thang.
- Tầng 1: gara 1 ô tô phía trước, phòng khách, bếp và ăn phía sau, 1 WC.
- Tầng 2: 2 phòng ngủ, 1 WC chung, ban công phía trước.
- Tầng 3: 1 phòng ngủ master có WC riêng, phòng thờ phía trước.
- Thích phong cách hiện đại, nhiều cây xanh.
```
Các thông số chưa có (chiều cao tầng, bảng cửa) học viên để Claude đề xuất ở chặng 2 và tự duyệt.

---

## 9. XỬ LÝ LỖI HAY GẶP

| Hiện tượng | Cách xử lý |
|---|---|
| Claude chạy một mạch qua cổng duyệt | Kiểm tra CLAUDE.md dự án có chữ "DỪNG, chờ tôi duyệt"; nhắc lại trong prompt chặng đó |
| AutoCAD không nhận lệnh, MCP báo timeout | AutoCAD phải mở sẵn một bản vẽ (không ở tab Start); nhờ Claude chạy `system init` của autocad-mcp |
| PDF in ra trang trắng | Viewport chưa phóng về đúng vùng; dùng cách sửa ở Prompt 4.5 Buổi 04 |
| Số cửa file mô tả lệch bảng cửa | Sửa bản vẽ (lớp KY-HIEU-CUA hoặc bảng BANG-CUA), không sửa file JSON |
| Agent không nhận tên | Agent chưa có trong `~/.claude/agents/` hoặc chưa mở phiên mới sau khi chép |
| Ảnh AI đổi cả kiến trúc | Kiểm `ref_mode="render"`; xem Buổi 05 mục 5.2 |
| `/goal` chạy mãi không dừng | Điều kiện phải đo được và có câu "hoặc dừng sau N lượt"; `/goal clear` để dừng |
| Thư mục `06-phat-hanh` bị sửa | Không sửa thư mục đã phát hành; tạo `lan-N` mới |

---

## PHỤ LỤC: NGUỒN KIỂM CHỨNG VÀ GIỚI HẠN

| Nội dung | Nguồn |
|---|---|
| Subagent: ngữ cảnh riêng, chạy song song, file `~/.claude/agents/` dùng mọi dự án | `code.claude.com/docs/en/sub-agents`, tra 10/10/2026 |
| Skill: vị trí `~/.claude/skills/<ten>/SKILL.md`, gọi bằng `/ten` | `code.claude.com/docs/en/skills`, tra 10/10/2026 |
| `/goal`: chấm sau mỗi lượt, không tự cấp quyền, chạy trong Desktop | `code.claude.com/docs/en/goal`, tra 10/10/2026 |
| `/plan`, chế độ lập kế hoạch | `code.claude.com/docs/en/permission-modes`, tra 10/10/2026 |
| Script vẽ, đọc bản vẽ, dựng Blender, tách tầng | `04_Buoi_04.../demo/07-nha-pho-lo-7x20m/scripts/`, chạy trên nhà 7x20m ngày 07/10 và 10/10/2026 |
| Agent render, agent bóc khối lượng, MCP tạo ảnh | Buổi 05, chạy thử 10/10/2026 |

**Giới hạn cần nói rõ với lớp:**
- Các chặng 3 và 4 đã chạy trọn trên nhà 7x20m. Với căn nhà khác, script vẽ chỉ cần sửa khối dữ liệu, nhưng **giảng viên nên chạy thử trọn 7 chặng trên căn nhà thị phạm tối hôm trước**.
- Chặng 7 (ghép PDF gửi khách) và Prompt 8.1, 9.1 là prompt mới, **chưa chạy thử** trước ngày soạn bài.
- Mặt đứng, mặt cắt sinh từ dữ liệu mặt bằng nên chỉ đúng với nhà hình hộp; nhà có hình khối phức tạp cần kỹ sư chỉnh tay.
