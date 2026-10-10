# GIÁO TRÌNH CHI TIẾT: BUỔI 05
## ĐỘI NGŨ AGENT CHO HỒ SƠ NHÀ PHỐ: AGENT CHUYÊN TRÁCH, SUBAGENT CHẠY CÙNG MỘT LƯỢT, RENDER AI ĐỔI PHONG CÁCH VÀ BÓC KHỐI LƯỢNG

**Thời lượng:** 150 phút (khoảng 30% lý thuyết, 70% thị phạm và thực hành)
**Áp dụng cho:** Claude Code Desktop (tab Code) trên Windows; bài nối tiếp nhà phố lô 7x20m của Buổi 04
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))
**Thông tin công cụ tra ngày 10/10/2026:** tài liệu chính thức Claude Code `code.claude.com/docs/en/sub-agents`, `/agent-teams`, `/agents`, `/desktop`, `/skills`; README repo `andyluu98/chatgpt-image-mcp` (bản có chế độ `ref_mode="render"`).
**Đã chạy thử trên máy giảng viên ngày 10/10/2026:** tạo ảnh 4 phong cách qua MCP, agent bóc khối lượng xuất Excel, agent render gọi MCP. Kết quả nằm trong `demo/` của buổi này.

> File này gồm đủ: giáo trình, kịch bản thị phạm, thư viện prompt, bài thực hành Lab 05 và bảng chấm D5. Mọi prompt viết để dán thẳng vào Claude Code Desktop.

---

## 1. MỤC TIÊU BÀI HỌC

Sau buổi học, học viên:
1. **Phân biệt agent chuyên trách và subagent tạm**, biết việc nào nên lập "nhân viên có hồ sơ", việc nào chỉ cần "thuê thời vụ".
2. **Tự tạo 3 agent chuyên trách** cho văn phòng thiết kế nhỏ: `boc-khoi-luong`, `kiem-tra-khoi-luong` (chỉ đọc), `render-phong-cach`.
3. **Giao nhiều agent làm cùng một lượt:** chạy song song những việc độc lập, nối chuỗi những việc phải chờ nhau, rồi gộp một báo cáo.
4. **Cài MCP ChatGPT tạo ảnh** (`chatgpt-image-mcp`) và đổi phong cách ảnh render Blender mà vẫn giữ đúng hình khối ngôi nhà.
5. **Bóc khối lượng phần thô** của nhà 7x20m từ chính file mô tả bản vẽ ra Excel: có diễn giải, nguồn, tách khối lượng thiết kế, hao hụt, khối lượng mua; không tự điền đơn giá.

---

## 2. TIẾN TRÌNH 150 PHÚT

```
00:00 - 00:10 (10')  Mở đầu: ôn Buổi 04, đặt bài toán chủ nhà muốn xem 3 phong cách và biết khối lượng
00:10 - 00:40 (30')  Phần A: Agent chuyên trách và subagent tạm. Học viên tạo 3 agent, thử phá agent chỉ đọc
00:40 - 01:00 (20')  Phần B: Nhiều agent cùng một lượt: song song, nối chuỗi. Agent team (chỉ có ở terminal)
01:00 - 01:10 (10')  Nghỉ giải lao (học viên chưa cài MCP ảnh thì dùng 10 phút này cài trước)
01:10 - 01:45 (35')  Phần C: Cài MCP ChatGPT tạo ảnh, đổi phong cách render Blender
01:45 - 02:15 (30')  Phần D: Agent bóc khối lượng và agent kiểm tra, xuất Excel BOQ phần thô
02:15 - 02:30 (15')  Nghiệm thu D5, giải đáp, giao bài Buổi 06
```

**Chuẩn bị của giảng viên trước giờ học**

| Việc | Kiểm tra |
|---|---|
| Blender đang mở file `04_nha-pho-lo-7x20m.blend`, addon vn-blender bật kết nối | Lệnh `/mcp` thấy `vn-blender` Connected |
| MCP `chatgpt-image` đã khai báo và đăng nhập | `/mcp` thấy `chatgpt-image` Connected; prompt C1 trả về đã đăng nhập |
| Có sẵn thư mục `demo/` của Buổi 04 và Buổi 05 để chiếu | Ảnh `demo/01-render-ai/05_so-sanh-goc-va-3-phong-cach.jpg` |
| Gửi trước cho học viên mục 5.1 (cài uv, git, tải repo) | Ai đã cài ở nhà thì giờ nghỉ hỗ trợ bạn bên cạnh |

**Mở đầu 10 phút:** chiếu ảnh `05_so-sanh-goc-va-3-phong-cach.jpg` (ảnh Blender gốc và 3 phong cách AI). Hỏi lớp: "Chủ nhà cầm 3 ảnh này sẽ hỏi gì tiếp?" Câu trả lời thường gặp là "xây hết bao nhiêu". Hôm nay làm cả hai việc đó, và giao cho một đội agent làm cùng lúc.

---

## 3. PHẦN A: AGENT CHUYÊN TRÁCH VÀ SUBAGENT TẠM (30 PHÚT)

### 3.1. Ôn nhanh Buổi 04 (2 phút)

Buổi 04 đã học: subagent làm việc ở "bàn riêng", không thấy cuộc trò chuyện trước, chỉ nộp lại bản tóm tắt; nhiều subagent chạy song song được. Hôm nay đi tiếp một bước: **có hai kiểu subagent**, dùng vào hai loại việc khác nhau.

### 3.2. Hình dung bằng văn phòng thiết kế (8 phút)

| | Agent chuyên trách | Subagent tạm |
|---|---|---|
| Ví như | Nhân viên chính thức, có **hồ sơ lưu trong tủ** của văn phòng | Người làm **thời vụ**, thuê theo đầu việc, xong việc là về |
| Nằm ở đâu | Một file `.md` trong `.claude/agents/` (dự án) hoặc `~/.claude/agents/` (mọi dự án) | Không có file; agent chính tự giao việc trong lúc làm |
| Dùng lại | Mọi phiên sau, mọi học viên chép file là dùng được | Chỉ trong lần đó |
| Quy tắc làm việc | Viết sẵn một lần trong file: quyền công cụ, quy tắc nghề | Ghi trong lời giao việc mỗi lần |
| Hợp với | Việc lặp lại, có quy tắc cố định: bóc khối lượng, soát bản vẽ, render | Nhiều việc nhỏ một lần: đọc 5 file PDF, đếm cửa từng tầng |

Tên gọi chính thức: tài liệu Claude Code gọi chung là **subagent**; loại có file gọi là subagent tùy chỉnh (custom subagent). Trong lớp gọi "agent chuyên trách" cho dễ nhớ.

**Điểm chung của cả hai** (tài liệu chính thức `sub-agents`, tra 10/10/2026):
- Mỗi subagent có cửa sổ ngữ cảnh riêng, bắt đầu trắng, không thấy cuộc trò chuyện của anh/chị.
- Chỉ trả về bản tóm tắt cho agent chính, nên cuộc trò chuyện chính không bị đầy.
- Chạy song song được nhiều cái; subagent cũng có thể gọi subagent khác, mặc định sâu tối đa 3 tầng.
- Có thể đẩy một subagent đang chạy xuống chạy nền bằng `Ctrl+B` để làm việc khác.

### 3.3. Khi nào dùng gì (4 phút)

| Việc | Dùng |
|---|---|
| Lặp lại hằng tuần, có quy tắc nghề cố định (bóc khối lượng, soát hồ sơ, render phương án) | Agent chuyên trách |
| Nhiều việc độc lập, làm một lần (đọc 5 hồ sơ, đếm cửa 4 tầng) | Subagent tạm chạy song song |
| Một câu hỏi nhỏ, sửa một chỗ | Hỏi thẳng agent chính, không cần agent nào |

Nhắc chi phí: mỗi subagent là một lượt đọc riêng, tốn thêm hạn mức. Thường 3 đến 5 agent là đủ cho một việc.

### 3.4. File agent chuyên trách gồm gì (4 phút)

```markdown
---
name: kiem-tra-khoi-luong
description: Soát bảng bóc khối lượng... Dùng khi cần kiểm tra lại một bảng BOQ trước khi gửi khách.
tools: Read, Glob, Grep
model: inherit
---
Bạn là kỹ sư QS kiểm tra chéo...
(quy tắc nghề)
```

- `name` và `description` là **bắt buộc**. `description` quyết định Claude có tự giao việc hay không: viết rõ "Dùng khi...".
- `tools` giới hạn quyền: agent kiểm tra chỉ có `Read, Glob, Grep` thì **không sửa được file**, dù có bị yêu cầu.
- `tools` ghi được cả công cụ của MCP, ví dụ `mcp__chatgpt-image__generate_image`.
- `model: inherit` là dùng cùng mô hình với phiên đang chạy.

### 3.5. Thực hành: tạo 3 agent và thử phá (12 phút)

Học viên chạy lần lượt **Prompt A1, A2, A3** (mục 8). Sau đó:
1. Mở phiên mới (`Ctrl+N`) để Claude nạp các agent vừa tạo. Tạo thư mục `.claude/agents` lần đầu thì phiên đang mở chưa thấy agent.
2. Chạy **Prompt A4**: bảo agent `kiem-tra-khoi-luong` sửa một con số trong file. Agent phải từ chối vì không có công cụ ghi file. Đây là khoảnh khắc đắt giá của phần A: **quyền nằm trong file agent, không nằm trong lời hứa**.
3. Chạy **Prompt A5** để thấy subagent tạm: 4 subagent đếm cửa và nội thất 4 tầng song song, không để lại file agent nào.

---

## 4. PHẦN B: NHIỀU AGENT CÙNG MỘT LƯỢT (20 PHÚT)

### 4.1. Hai cách phối hợp (6 phút)

| Cách | Khi nào | Ví dụ trong bài |
|---|---|---|
| **Song song** | Các việc không cần chờ nhau | Render phong cách và bóc khối lượng chạy cùng lúc |
| **Nối chuỗi** | Việc sau cần kết quả việc trước; giữa hai bước có một file trung gian | Bóc khối lượng xong, agent kiểm tra mới đọc bảng tóm tắt |

Một lời giao việc tốt có 4 phần: **ai làm gì, việc nào song song, việc nào chờ, gộp kết quả vào đâu**. Agent chính không tự làm thay, chỉ điều phối và gộp. Mẫu ở Prompt B1.

### 4.2. Thị phạm "đội hồ sơ nhà phố" (10 phút)

Giảng viên chạy **Prompt B1** trên nhà 7x20m:
- Nhánh 1 và nhánh 2 chạy song song: `render-phong-cach` tạo 2 phong cách, `boc-khoi-luong` xuất Excel.
- Nhánh 3 chờ nhánh 2: `kiem-tra-khoi-luong` đọc bảng tóm tắt và file mô tả, liệt kê điểm cần xem lại.
- Agent chính gộp thành `17_bao-cao-doi-agent.md`.

Trong lúc chạy, mở **bảng tác vụ nền** của Claude Code Desktop (Tasks) để lớp thấy từng agent đang làm gì. Tài liệu chính thức mô tả bảng này hiển thị "subagents, background shell commands, and dynamic workflows" đang chạy trong phiên.

### 4.3. Agent team: biết để không nhầm (4 phút)

| | Subagent (dùng hôm nay) | Agent team |
|---|---|---|
| Cách làm việc | Mỗi agent nộp kết quả về agent chính | Các thành viên **nhắn tin trực tiếp cho nhau**, chung một danh sách việc, tự nhận việc |
| Trạng thái | Chính thức | **Thử nghiệm**, tắt sẵn, bật bằng biến môi trường `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` |
| Chạy ở đâu | Terminal và Desktop | **Chỉ terminal (CLI), không có trong Desktop** |
| Chi phí | Thấp hơn | Cao hơn nhiều: mỗi thành viên là một phiên Claude riêng |

Nguồn: `code.claude.com/docs/en/agent-teams` và `/desktop`, tra 10/10/2026. Vì lớp học dùng Desktop, hôm nay **không thực hành agent team**. Ai dùng terminal muốn thử thì xem Phụ lục B.

---

## 5. PHẦN C: MCP CHATGPT TẠO ẢNH, ĐỔI PHONG CÁCH RENDER (35 PHÚT)

### 5.1. Cài đặt (15 phút, trợ giảng kiểm từng máy)

**Cảnh báo bắt buộc đọc cho lớp trước khi cài:** MCP này đăng nhập bằng tài khoản ChatGPT trên web theo cách tự viết, không phải API chính thức. Chính README của repo ghi cách làm này vi phạm điều khoản sử dụng của OpenAI và khuyên **dùng tài khoản phụ**. Tài khoản có thể bị giới hạn hoặc khóa. Ảnh tạo ra tính vào hạn mức tạo ảnh của tài khoản ChatGPT đó.

**Cần có:** `git`, `uv` (công cụ tự tải Python 3.12, không cần cài Python riêng), một tài khoản ChatGPT.

**Bước 1. Cài uv** (một lần trên máy, PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Bước 2. Tải repo và cài thư viện:**
```powershell
git clone https://github.com/andyluu98/chatgpt-image-mcp.git D:\Tools\chatgpt-image-mcp
cd D:\Tools\chatgpt-image-mcp
uv sync
```

**Bước 3. Đăng nhập ChatGPT (2 bước):**
```powershell
uv run cgimg login
```
Trình duyệt mở ra, đăng nhập ChatGPT. Trình duyệt sẽ chuyển tới một trang `platform.openai.com`, có thể báo "Oops"; đó là bình thường. **Chép nguyên đường dẫn trên thanh địa chỉ**, rồi chạy:
```powershell
uv run cgimg login --callback "<dán nguyên đường dẫn vừa chép>"
```
Hai bước là vì bước 1 tạo một mã bí mật dùng một lần lưu trên máy, bước 2 cần đúng mã đó để đổi lấy quyền truy cập.

**Bước 4. Khai báo MCP cho Claude Code** (dùng được ở mọi thư mục):
```powershell
claude mcp add chatgpt-image -s user '--' uv run --directory "D:\Tools\chatgpt-image-mcp" cgimg-mcp
```
Ba chỗ hay sai:
- Trên PowerShell phải viết `'--'` có ngoặc đơn. Viết `--` trần thì PowerShell nuốt mất và báo lỗi `unknown option '--directory'` (đã gặp khi chạy thử 10/10/2026).
- `-s user` để MCP dùng được ở mọi thư mục; thiếu thì chỉ dùng được trong thư mục đang đứng.
- `--directory` phải là đường dẫn repo vừa tải.

Cách khác: chạy `powershell -ExecutionPolicy Bypass -File install.ps1` trong thư mục repo, trình cài tự làm bước 1 đến 4.

**Bước 5. Kiểm tra:** đóng hẳn Claude Code Desktop rồi mở lại (hoặc mở phiên mới), gõ `/mcp`, thấy `chatgpt-image` ở trạng thái Connected. Chạy **Prompt C1**.

### 5.2. Ý tưởng cốt lõi: AI chỉ "sơn lại", không "xây lại" (5 phút)

Công cụ `generate_image` nhận ảnh render làm ảnh tham chiếu (`ref_image`). Chế độ `ref_mode="render"` dặn mô hình: **giữ nguyên** hình khối, số tầng, vị trí và kích thước cửa, mái, góc máy; **chỉ đổi** vật liệu, màu, ánh sáng, cảnh quan. Chế độ này cũng tắt bước "tự viết lại prompt" để prompt của anh/chị đi thẳng vào mô hình.

Kết quả chạy thử trên nhà 7x20m (`demo/01-render-ai/`):

| Ảnh | Giữ được | AI tự đổi (phải soát) |
|---|---|---|
| `01_dong-duong.png` | 3 tầng, tum, mái dốc, ban công, pergola, vị trí cửa | Thêm cửa chớp, gạch bông sân trước theo đúng phong cách |
| `02_hien-dai-chang-vang.png` | Giữ sát nhất: hình khối, cửa, mái, ốp gỗ tầng 3 | Mẫu xe, cây xanh |
| `03_nhiet-doi-xanh.png` | Số tầng, mái, pergola | **Thêm lam gỗ, gạch thông gió lên mặt tiền**: đổi cả kiến trúc mặt đứng |
| `04_japandi.png` | Số tầng, mái, cửa, ban công | Ống thoát nước thành nẹp gỗ, ốp gỗ tầng 3 chỉ còn một phần, xe đổi mẫu (Claude tự liệt kê khi được dặn so sánh) |

Bài học chốt: **ảnh AI dùng để trao đổi phong cách với chủ nhà, không dùng làm hồ sơ kỹ thuật**. Mọi thay đổi chủ nhà ưng (ví dụ lam gỗ) phải quay về sửa bản vẽ AutoCAD rồi dựng lại, đúng nguyên tắc "bản vẽ là nguồn" của Buổi 04.

### 5.3. Thị phạm và thực hành (15 phút)

1. Giảng viên chạy **Prompt C2**: gọi thẳng công cụ, 1 phong cách, cả lớp xem ảnh ra trong khoảng 30 đến 90 giây.
2. Học viên chạy **Prompt C3** qua agent `render-phong-cach`: 2 phong cách tự chọn, agent tự mở ảnh so sánh và liệt kê chỗ AI tự đổi.
3. Ai xong sớm chạy **Prompt C4**: dùng góc nhìn khác (`06_phoi-canh-tren-cao.png`) hoặc ảnh tách tầng.

---

## 6. PHẦN D: AGENT BÓC KHỐI LƯỢNG VÀ AGENT KIỂM TRA (30 PHÚT)

### 6.1. Lấy khối lượng từ đâu (5 phút)

Khối lượng lấy từ **file mô tả bản vẽ** `03_mo-ta-tu-ban-ve.json` (đọc từ DXF ở Buổi 04), không lấy từ mô hình Blender và không đo trên ảnh. File này có:
- `cao_do`: cao độ các tầng (mm): sân -450, T1 0, T2 3600, T3 7000, sân thượng 10400, tum 13400.
- `mat_bang`: tường, cột, sàn, lỗ sàn, cửa của từng tầng, mỗi đối tượng là một hình chữ nhật tọa độ mm.
- `cua`: bảng thống kê cửa (rộng, cao, bậu, số lượng).
- `thong_so`: sàn BTCT dày 120 và các thông số khác.

Năm cái bẫy phải dặn học viên (rút ra từ lần chạy thử 10/10/2026):
1. "Nhà 7x20m" là **kích thước lô đất**; khối nhà là **5x14m**.
2. Đoạn tường trên mặt bằng **đã bị cắt sẵn tại lỗ cửa**. Trừ diện tích cửa thêm lần nữa mà không cộng lại phần tường tại vị trí lỗ là **trừ hai lần**.
3. File không có dầm. Chiều cao tường phải chốt một quy ước, ví dụ chênh cao độ tầng trừ dày sàn 120, và ghi vào sheet giả thiết.
4. Tường tầng 3 nằm dưới mái tôn dốc: phần tường hồi không có đủ kích thước, phải gắn nhãn thiếu kích thước, không đoán.
5. Ô % hao hụt để **trống**, không ghi chữ vào ô số (ghi chữ thì công thức Excel báo `#VALUE!`); nhãn `[Chờ bổ sung]` ghi ở cột ghi chú.

### 6.2. Thị phạm (10 phút)

Giảng viên chạy **Prompt D1**. Kết quả chạy thử 10/10/2026 (đáp án: `demo/02-boc-khoi-luong/01_dap-an-boq-phan-tho-nha-7x20m.xlsx`, script `boc-khoi-luong.py` 264 dòng):

| Nhóm | Khối lượng thiết kế |
|---|---|
| Tường xây 200 | 329,67 m² (65,93 m³); T1 102,12; T2 91,34; T3 93,19; tầng mái 43,02 m² |
| Bê tông sàn | 27,78 m³ |
| Bê tông cột 200x200 | 4,23 m³ |
| Cửa đi, cửa sổ | 30 bộ, 69,12 m²; khớp bảng thống kê cửa ở cả 9 mã |

Các con số trên phụ thuộc giả thiết ghi trong sheet "Gia thiet" của file đáp án (chiều cao tường, sàn tầng 1 dày 120, chưa tính tường hồi mái dốc, chưa tính móng). Đây là **bài mẫu để dạy cách bóc**, kích thước cột và sàn chưa qua tính toán kết cấu. Khối lượng học viên ra khác đáp án thì so sheet giả thiết trước khi kết luận ai sai.

Hai điều cần chỉ cho lớp khi mở file Excel:
- Script ghi **công thức** vào Excel. Mở bằng Excel mới thấy số; đọc bằng thư viện Python mà không mở Excel thì ô công thức trông như trống.
- Đọc khối lượng mua ở **dòng cộng** từng nhóm; cộng tay cả cột mua của mọi dòng sẽ bị tính hai lần.

### 6.3. Thực hành (15 phút)

Học viên chạy **Prompt D1** rồi **Prompt D2** (agent kiểm tra soát lại). Ai xong sớm chạy **Prompt D3**: điền thử 5% hao hụt cho tường xây, xem cột khối lượng mua tự tính lại.

---

## 7. NGHIỆM THU D5 VÀ BÀI VỀ NHÀ (15 PHÚT)

### 7.1. Thành phần hồ sơ D5

1. Ba file agent chuyên trách trong `.claude/agents/` và ảnh chụp agent chỉ đọc từ chối sửa file (Prompt A4).
2. Ít nhất 2 ảnh đổi phong cách từ ảnh render Blender, kèm bảng so sánh "giữ được / AI tự đổi".
3. File Excel BOQ phần thô có sheet BOQ, sheet kiểm chéo cửa, sheet giả thiết; script tính kèm theo.
4. Báo cáo gộp của đội agent (`17_bao-cao-doi-agent.md`) do Prompt B1 tạo.

### 7.2. Bảng chấm (thang 100)

| STT | Tiêu chí | Điểm | ĐẠT | CHƯA ĐẠT |
|---|---|---|---|---|
| 1 | 3 file agent đúng cấu trúc: có `name`, `description` ghi "Dùng khi...", `tools` đúng quyền; agent kiểm tra không có quyền ghi và đã từ chối khi bị yêu cầu sửa | 20 | | |
| 2 | Ảnh render AI giữ đúng số tầng, mái, vị trí cửa so với ảnh Blender; có bảng chỉ ra chỗ AI tự đổi; có câu "ảnh để trao đổi, không phải hồ sơ kỹ thuật" | 25 | | |
| 3 | BOQ: mỗi dòng có diễn giải và nguồn; tách 3 cột thiết kế, hao hụt, mua; ô hao hụt và đơn giá để trống chờ bổ sung, không tự điền; không trừ cửa hai lần; số cửa khớp bảng thống kê (30 bộ) | 35 | | |
| 4 | Báo cáo đội agent: ghi rõ việc nào chạy song song, việc nào chờ; agent kiểm tra nêu được ít nhất 2 điểm cần xem lại | 20 | | |

**Xếp loại:** Xuất sắc 90 đến 100 · Đạt 70 đến 89 · Chưa đạt dưới 70.

### 7.3. Bài về nhà (chuẩn bị Buổi 06)

1. Chọn **một căn nhà của mình** (ảnh mẫu, yêu cầu của chủ nhà, hoặc một ý tưởng): lô đất, số tầng, công năng từng tầng. Mang theo Buổi 06; buổi đó sẽ chạy trọn quy trình trên căn nhà này.
2. Viết thêm một agent chuyên trách cho công việc hằng ngày của mình (ví dụ `soat-ban-ve-kc`, `lap-bien-ban`), thử gọi 2 lần.
3. Điền % hao hụt và đơn giá vào BOQ theo định mức, công bố giá mà công ty đang dùng; ghi nguồn từng con số.

---

## 8. THƯ VIỆN PROMPT

Quy ước đường dẫn trong prompt:
- `<DEMO>`: thư mục `04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m` trên máy học viên.
- `<B05>`: thư mục làm bài Buổi 05 của học viên, ví dụ `D:\AI-XayDung\buoi-05`. Mở Claude Code Desktop tại thư mục này để agent tạo ra nằm trong `<B05>\.claude\agents\`.

### Prompt 0.1: Kiểm tra môi trường đầu buổi

```
Kiểm tra giúp tôi môi trường cho Buổi 05, chỉ đọc, không sửa gì:
1. Các MCP đang kết nối: autocad-mcp, vn-blender, chatgpt-image. Cái nào chưa kết nối thì báo.
2. Thư mục <DEMO> có đủ các file: 03_mo-ta-tu-ban-ve.json, 05_phoi-canh-goc-hong.png, 06_phoi-canh-tren-cao.png, 14_bang-thong-ke-cua-nha-7x20m.xlsx.
3. Thư mục hiện tại đã có .claude\agents chưa.
Trả lời bằng một bảng: hạng mục, trạng thái, cách sửa nếu thiếu.
```

### PHẦN A: AGENT CHUYÊN TRÁCH

### Prompt A1: Tạo agent bóc khối lượng

```
Tạo agent chuyên trách trong thư mục .claude\agents của dự án này, tên file boc-khoi-luong.md, nội dung đúng như sau:

---
name: boc-khoi-luong
description: Kỹ sư QS bóc khối lượng phần thô từ file mô tả bản vẽ (JSON đọc từ DXF) và xuất bảng Excel. Dùng khi cần bóc khối lượng tường xây, bê tông sàn, cột, cửa từ file 03_mo-ta-tu-ban-ve.json.
tools: Read, Glob, Grep, Bash, Write
model: inherit
---
Bạn là kỹ sư QS bóc khối lượng nhà ở.
Quy tắc:
1. Chỉ lấy kích thước từ file mô tả bản vẽ. Không đo ảnh, không đoán. Thiếu kích thước thì ghi "[THIẾU KÍCH THƯỚC - CẦN KỸ SƯ XÁC MINH]".
2. Mọi con số do code Python tính ra, không tính nhẩm. Lưu script cạnh file kết quả để người khác chạy lại được.
3. Mỗi dòng có cột Diễn giải (kích thước x số lượng) và cột Nguồn (tầng, mục trong file mô tả).
4. Tách ba cột: khối lượng thiết kế, hao hụt (%), khối lượng mua. Ô % hao hụt và ô đơn giá để trống (tô vàng), ghi "[Chờ bổ sung]" ở cột Ghi chú; công thức Excel vẫn chạy khi điền.
5. Tính trên số đầy đủ, chỉ làm tròn khi hiển thị: khối lượng 2 chữ số thập phân.
6. Ghi rõ mọi giả định ở sheet "Gia thiet". Không sửa file gốc.
7. Kiểm chéo: số cửa đếm được trên mặt bằng phải khớp bảng thống kê cửa; lệch thì báo, không tự chọn bên nào.
8. Xong việc, viết thêm một file tóm tắt .md cùng tên với file Excel: tổng từng nhóm, giả định, chỗ lệch.

Tạo xong thì đọc lại file và xác nhận phần đầu (name, description, tools) đúng định dạng.
```

### Prompt A2: Tạo agent kiểm tra (chỉ đọc)

```
Tạo agent chuyên trách trong .claude\agents, tên file kiem-tra-khoi-luong.md, nội dung:

---
name: kiem-tra-khoi-luong
description: Kỹ sư QS kiểm tra chéo bảng bóc khối lượng do người khác lập: soát phương pháp, giả định, chỗ bỏ sót, chỗ trừ hai lần. Dùng khi cần soát một bảng BOQ trước khi gửi khách. Agent này chỉ đọc, không sửa file.
tools: Read, Glob, Grep
model: inherit
---
Bạn là kỹ sư QS kiểm tra độc lập, khó tính.
Quy tắc:
1. Chỉ đọc. Không tạo, không sửa, không xóa file nào. Bị yêu cầu sửa thì từ chối và nói rõ lý do.
2. Đối chiếu bảng tóm tắt và script tính với file mô tả bản vẽ: chiều cao tường lấy thế nào, có trừ cửa hai lần không, có sót hạng mục nào, giả định nào chưa có căn cứ.
3. Mỗi điểm nêu: vị trí (file, dòng hoặc mục), vấn đề, mức độ (cao, trung bình, thấp), đề xuất sửa.
4. Không tự tính lại số liệu bằng tay. Thấy nghi ngờ thì đề nghị người lập chạy lại script.
```

### Prompt A3: Tạo agent render phong cách

```
Tạo agent chuyên trách trong .claude\agents, tên file render-phong-cach.md, nội dung:

---
name: render-phong-cach
description: Đổi phong cách ảnh render kiến trúc (Blender, SketchUp) bằng MCP chatgpt-image, giữ nguyên hình khối công trình. Dùng khi cần ảnh phối cảnh nhiều phong cách để trao đổi với chủ nhà.
tools: Read, Glob, mcp__chatgpt-image__generate_image, mcp__chatgpt-image__login_status
model: inherit
---
Bạn là họa viên diễn họa kiến trúc.
Quy tắc:
1. Luôn gọi generate_image với ref_mode = "render", ref_image và out_dir là đường dẫn tuyệt đối.
2. Mỗi phong cách gọi một lần, n = 1.
3. Tạo xong thì dùng Read mở ảnh mới và ảnh gốc, so sánh: số tầng, mái, vị trí cửa, ban công, góc máy. Liệt kê chỗ AI tự đổi.
4. Ảnh AI chỉ để trao đổi phương án với khách, không phải hồ sơ kỹ thuật. Ghi câu này trong báo cáo.
5. Không sửa, không xóa file gốc.
```

Sau 3 prompt trên: **mở phiên mới (Ctrl+N)** để Claude nạp agent.

### Prompt A4: Thử phá agent chỉ đọc

```
Dùng agent kiem-tra-khoi-luong: mở file <DEMO>\03_mo-ta-tu-ban-ve.json và sửa cao độ T2 từ 3600 thành 3300 cho tiện tính.
```
Kết quả mong đợi: agent từ chối, nói rõ nó chỉ có quyền đọc. **Agent chính không được tự sửa thay.** Nếu agent chính tự sửa, đó là lỗi của lời giao việc; thị phạm thêm câu "chỉ giao cho agent kiem-tra-khoi-luong, không tự làm thay".

### Prompt A5: Subagent tạm chạy song song

```
Dùng 4 subagent chạy song song, không tạo file agent nào. Mỗi subagent đọc mục mat_bang của một tầng (T1, T2, T3, MAI) trong <DEMO>\03_mo-ta-tu-ban-ve.json và đếm: số đoạn tường, số cột, số cửa theo từng mã, số món nội thất.
Chỉ dùng thông tin trong file; không có thì ghi "Tài liệu không đề cập".
Gộp thành một bảng 4 dòng, thêm dòng tổng, so tổng số cửa với mục cua của file. Chỉ trả lời trong chat, không ghi file.
```
Kết quả mong đợi (khớp kết quả chạy thử): 71 đoạn tường, 32 cột, 30 cửa, 57 món nội thất.

### PHẦN B: NHIỀU AGENT CÙNG MỘT LƯỢT

### Prompt B1: Đội hồ sơ nhà phố (song song và nối chuỗi)

```
Giao việc cho đội agent, không tự làm thay. Ảnh gốc và dữ liệu ở <DEMO>, kết quả lưu vào <B05>.

Nhánh 1 (chạy song song với nhánh 2): agent render-phong-cach đổi phong cách ảnh <DEMO>\05_phoi-canh-goc-hong.png thành 2 phong cách: (a) Đông Dương, tường vàng kem, cửa chớp xanh rêu, nắng chiều; (b) hiện đại tối giản lúc chạng vạng, tường trắng ốp gỗ, đèn trong nhà bật sáng. Lưu ảnh vào <B05>\16-render-ai. Báo bảng so sánh với ảnh gốc.

Nhánh 2 (chạy song song với nhánh 1): agent boc-khoi-luong bóc khối lượng phần thô khối nhà 5x14m (lô đất 7x20m) từ <DEMO>\03_mo-ta-tu-ban-ve.json, xuất <B05>\15_boq-phan-tho-nha-7x20m.xlsx và file tóm tắt .md cùng tên, script để là <B05>\boc-khoi-luong.py. Phạm vi và quy ước theo Prompt D1.

Bước 3 (chờ nhánh 2 xong mới chạy): agent kiem-tra-khoi-luong đọc file tóm tắt, script và file mô tả, liệt kê điểm cần xem lại.

Cuối cùng: gộp kết quả 3 agent vào <B05>\17_bao-cao-doi-agent.md, ghi rõ việc nào chạy song song, việc nào chờ, mỗi agent mất bao lâu.
```
Trong lúc chạy: mở bảng Tasks của Claude Code Desktop để xem từng agent.

### PHẦN C: RENDER AI ĐỔI PHONG CÁCH

### Prompt C1: Kiểm tra đăng nhập

```
Gọi công cụ login_status của MCP chatgpt-image và cho tôi biết tài khoản ChatGPT đã đăng nhập chưa. Chưa đăng nhập thì hướng dẫn tôi 2 lệnh đăng nhập.
```

### Prompt C2: Đổi một phong cách (gọi thẳng công cụ)

```
Dùng MCP chatgpt-image, công cụ generate_image, đổi phong cách ảnh render Blender sau:
<DEMO>\05_phoi-canh-goc-hong.png
Tham số: ref_image là đường dẫn trên, ref_mode = "render", aspect = "16:9", out_dir = <B05>\16-render-ai
Phong cách: Japandi tối giản, tường trát vữa màu be, ốp gỗ sồi sáng, cửa khung gỗ, sân sỏi trắng và cây phong lá đỏ, ánh sáng buổi sáng dịu.
Giữ nguyên kiến trúc: số tầng, vị trí cửa, mái, góc máy. Xong báo đường dẫn file ảnh và so sánh nhanh với ảnh gốc.
```
Đã chạy thử nguyên văn ngày 10/10/2026 (ảnh `demo/01-render-ai/04_japandi.png`). Claude tự nêu 3 chỗ AI đổi: ống thoát nước thành nẹp gỗ, ốp gỗ tầng 3 còn một phần, xe đổi mẫu.

### Prompt C3: Qua agent render-phong-cach

```
Dùng agent render-phong-cach đổi phong cách ảnh <DEMO>\05_phoi-canh-goc-hong.png thành 2 phong cách tôi chọn:
1. <phong cách 1, ví dụ: Địa Trung Hải, tường trắng, mái ngói đỏ, cửa sổ xanh dương, nắng trưa>
2. <phong cách 2, ví dụ: nhiệt đới, gạch thông gió, nhiều cây rủ, buổi sáng sau mưa>
Lưu vào <B05>\16-render-ai. Báo lại đường dẫn ảnh và bảng so sánh với ảnh gốc theo 5 mục: số tầng, mái, vị trí cửa, ban công, góc máy.
```
Đã chạy thử ngày 10/10/2026 với phong cách Địa Trung Hải trên ảnh góc cao (`demo/01-render-ai/06_tren-cao-dia-trung-hai-qua-agent.png`): agent giữ đúng số tầng, mái, vị trí cửa; tự nêu 4 chỗ AI thêm bớt (cửa chớp, bỏ ống thoát nước, thêm chậu cây, thêm lan can gỗ ban công). Agent không có quyền đổi tên file nên ảnh mang tên tự động; muốn đặt tên `01_...` thì để agent chính đổi sau.

### Prompt C4: Góc nhìn khác (làm thêm)

```
Dùng agent render-phong-cach đổi phong cách ảnh <DEMO>\06_phoi-canh-tren-cao.png theo phong cách tôi đã ưng nhất ở Prompt C3. So sánh hai ảnh cùng phong cách ở hai góc nhìn: vật liệu, màu có nhất quán không. Ghi nhận xét vào <B05>\16-render-ai\ghi-chu-so-sanh.md.
```

**Mẹo viết prompt phong cách:** tả vật liệu cụ thể (tường, mái, khung cửa, sân), thời điểm ánh sáng, cây xanh. Không tả hình khối mới ("thêm một tầng", "mái bằng") vì như vậy là đổi kiến trúc, việc đó phải làm trên bản vẽ.

### PHẦN D: BÓC KHỐI LƯỢNG

### Prompt D1: Bóc khối lượng phần thô

```
Dùng agent boc-khoi-luong bóc khối lượng phần thô khối nhà 5x14m (trên lô đất 7x20m) từ file <DEMO>\03_mo-ta-tu-ban-ve.json. Đơn vị trong file là mm, cao độ các tầng ở mục cao_do, bảng cửa ở mục cua.
Bóc 4 nhóm:
(1) Tường xây 200 theo từng tầng, ra m2 và m3. Chiều cao tường = chênh cao độ tầng trừ dày sàn 120 (file không có dầm). Lưu ý: đoạn tường trên mặt bằng đã bị cắt sẵn tại lỗ cửa, nên phải cộng phần tường tại vị trí lỗ rồi mới trừ diện tích cửa, không trừ hai lần. Tường hồi dưới mái dốc không đủ kích thước thì gắn nhãn thiếu, không đoán.
(2) Bê tông sàn theo từng tầng, trừ lỗ sàn, dày theo mục thong_so.
(3) Bê tông cột.
(4) Cửa đi, cửa sổ theo mã: số bộ và diện tích.
Xuất <B05>\15_boq-phan-tho-nha-7x20m.xlsx gồm 3 sheet: BOQ, Kiem cheo cua, Gia thiet; script để là <B05>\boc-khoi-luong.py. Kiểm chéo số cửa với mục cua và file <DEMO>\14_bang-thong-ke-cua-nha-7x20m.xlsx.
Xong thì báo tóm tắt: tổng từng nhóm, các giả định, chỗ lệch nếu có.
```

### Prompt D2: Kiểm tra chéo

```
Dùng agent kiem-tra-khoi-luong soát bảng bóc khối lượng vừa lập: đọc <B05>\15_boq-phan-tho-nha-7x20m.md, <B05>\boc-khoi-luong.py và <DEMO>\03_mo-ta-tu-ban-ve.json.
Liệt kê tối thiểu 3 điểm cần xem lại, xếp từ mức độ cao xuống thấp, mỗi điểm có vị trí và đề xuất sửa. Không sửa file.
```

### Prompt D3: Thử điền hao hụt (làm thêm)

```
Mở <B05>\15_boq-phan-tho-nha-7x20m.xlsx bằng Excel, điền thử 5% vào ô hao hụt của dòng cộng tường xây tầng 1, cho Excel tính lại, đọc giá trị khối lượng mua của dòng đó. Không lưu thay đổi vào file. Báo: ô nào, công thức gì, giá trị trước và sau.
```
Ghi chú: con số 5% chỉ để thử công thức. Hao hụt thật lấy theo định mức công ty đang áp dụng, ghi nguồn.

---

## 9. XỬ LÝ LỖI HAY GẶP

| Hiện tượng | Nguyên nhân | Cách xử lý |
|---|---|---|
| Gọi agent theo tên mà Claude không nhận | Vừa tạo `.claude/agents` lần đầu trong phiên đang mở | Mở phiên mới (`Ctrl+N`) |
| Claude không tự giao việc cho agent | `description` mơ hồ | Sửa `description`, thêm "Dùng khi..." rõ việc |
| `claude mcp add` báo `unknown option '--directory'` | PowerShell nuốt dấu `--` | Viết `'--'` có ngoặc đơn |
| `/mcp` không thấy `chatgpt-image` | Khai báo thiếu `-s user`, hoặc chưa mở lại Desktop | Khai báo lại với `-s user`, đóng hẳn rồi mở lại Desktop |
| Báo chưa đăng nhập, hoặc phiên hết hạn | Mã truy cập hết hạn | Chạy lại 2 lệnh `uv run cgimg login` trong thư mục repo |
| Ảnh ra đổi cả kiến trúc | Không dùng `ref_mode="render"`, hoặc prompt tả hình khối mới | Kiểm tra tham số; prompt chỉ tả vật liệu, ánh sáng, cảnh quan |
| Ảnh bị từ chối tạo | Bộ lọc nội dung của ChatGPT | Viết lại prompt trung tính, bỏ tên thương hiệu, tên người |
| Mỗi ảnh mất 30 đến 90 giây | Bình thường | Giao agent chạy nền, làm việc khác trong lúc chờ |
| Mở Excel bằng Python thấy ô tổng trống | Ô chứa công thức, chưa được Excel tính | Mở bằng Excel |
| Tổng khối lượng mua gấp đôi | Cộng cả dòng chi tiết lẫn dòng cộng | Chỉ đọc ở dòng cộng từng nhóm |
| Khối lượng tường nhỏ bất thường | Trừ diện tích cửa hai lần | Xem mục 6.1, bẫy số 2 |

---

## PHỤ LỤC A: TỆP TRONG THƯ MỤC BUỔI 05

| Tệp | Nội dung |
|---|---|
| `01_Giao_Trinh_Chi_Tiet_Buoi_05.md` | File này |
| `demo/01-render-ai/01_dong-duong.png` đến `04_japandi.png` | 4 ảnh đổi phong cách từ ảnh `05_phoi-canh-goc-hong.png`, tạo ngày 10/10/2026 |
| `demo/01-render-ai/05_so-sanh-goc-va-3-phong-cach.jpg` | Ảnh ghép gốc và 3 phong cách, dùng mở đầu buổi |
| `demo/01-render-ai/06_tren-cao-dia-trung-hai-qua-agent.png` | Ảnh do agent `render-phong-cach` tạo từ `06_phoi-canh-tren-cao.png` (kiểm chứng agent gọi được MCP) |
| `demo/02-boc-khoi-luong/01_dap-an-boq-phan-tho-nha-7x20m.xlsx` | Đáp án BOQ phần thô (sheet BOQ, Kiem cheo cua, Gia thiet) |
| `demo/02-boc-khoi-luong/boc-khoi-luong.py` | Script tạo ra đáp án; chạy trong thư mục có file `03_mo-ta-tu-ban-ve.json` và `14_bang-thong-ke-cua-nha-7x20m.xlsx` |

## PHỤ LỤC B: AGENT TEAM TRÊN TERMINAL (THAM KHẢO, KHÔNG DẠY TRÊN LỚP)

Theo `code.claude.com/docs/en/agent-teams` (tra 10/10/2026):
- Tính năng đang thử nghiệm, tắt sẵn. Bật bằng biến môi trường `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, hoặc đặt trong mục `env` của file `settings.json`.
- Một phiên làm trưởng nhóm, giao việc và gộp kết quả; các thành viên làm việc độc lập, nhắn tin trực tiếp cho nhau, chung danh sách việc.
- Chỉ chạy trong terminal ở chế độ tương tác; không có trong Desktop; không chạy với `-p`.
- Giới hạn: mỗi phiên một nhóm, không có nhóm lồng nhóm, tốn hạn mức nhiều hơn hẳn so với subagent.

Khi nào đáng dùng: việc lớn chia được nhiều phần mà các phần cần trao đổi với nhau trong lúc làm (ví dụ kiến trúc, kết cấu, cơ điện cùng chỉnh một mặt bằng). Với lớp học trên Desktop, cách song song và nối chuỗi ở Phần B là đủ.

## PHỤ LỤC C: NGUỒN KIỂM CHỨNG

| Nội dung | Nguồn |
|---|---|
| Subagent: file, trường bắt buộc, quyền công cụ, chạy song song, lồng 3 tầng, Ctrl+B chạy nền | `code.claude.com/docs/en/sub-agents`, tra 10/10/2026 |
| Agent team: thử nghiệm, biến môi trường, chỉ CLI, không có trong Desktop | `code.claude.com/docs/en/agent-teams`, `/desktop`, tra 10/10/2026 |
| Bảng Tasks của Desktop hiển thị subagent đang chạy | `code.claude.com/docs/en/desktop`, tra 10/10/2026 |
| Cài đặt, đăng nhập 2 bước, cảnh báo điều khoản OpenAI, `ref_mode` | README và mã nguồn `andyluu98/chatgpt-image-mcp` |
| Lỗi `'--'` trên PowerShell, ảnh 4 phong cách, agent render gọi MCP | Chạy thử trên máy giảng viên 10/10/2026 |
| 329,67 m²; 65,93 m³; 27,78 m³; 4,23 m³; 30 bộ cửa 69,12 m² | Script `demo/02-boc-khoi-luong/boc-khoi-luong.py` chạy trên `03_mo-ta-tu-ban-ve.json`, 10/10/2026 |
| 71 tường, 32 cột, 30 cửa, 57 nội thất; cao độ các tầng | `04_Buoi_04.../demo/07-nha-pho-lo-7x20m/03_mo-ta-tu-ban-ve.json` |
| Cách chia agent chuyên trách và subagent tạm | Khóa K3 AI cho Nghiên cứu khoa học, Buổi 04 (dạy 09/10/2026), chuyển sang bối cảnh xây dựng |
