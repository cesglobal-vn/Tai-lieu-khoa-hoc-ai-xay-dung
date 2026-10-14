# HƯỚNG DẪN BỔ SUNG BUỔI 06: ĐỘI AI AGENT VÀ BỘ ĐỒ NGHỀ CÀI BẰNG PROMPT

> Đi kèm slide `05_slide-buoi-06-bo-sung-swiss.html` (24 slide). Học viên dùng Claude Code, không cần biết lệnh terminal: mỗi việc là **một prompt**.
> Nguồn: tài liệu Claude Code `code.claude.com/docs/en/sub-agents`; README `microsoft/markitdown`, `pascalorg/editor`, `andyluu98/MotionFly` (tra 14/10/2026).

| Phần | Nội dung | Slide | Phút |
|---|---|---|---|
| 1 | Đội AI Agent: vì sao, cách tổ chức, 5 bước lập đội | 3 đến 15 | 45 |
| 2 | Cài markitdown, Pascal Editor, MotionFly bằng prompt; làm video | 16 đến 23 | 30 |

---

## PHẦN 1. ĐỘI AI AGENT

### 1.1. Vì sao cần đội

Một agent ôm hết việc thì đầy trí nhớ và tự chấm bài mình. Chia nhiều agent: mỗi người đọc ít hơn, làm kỹ hơn, có người thứ ba soát chéo.

### 1.2. Đội agent giống tổ chức công trường

| Công trường | Trong Claude Code | Việc |
|---|---|---|
| Chỉ huy trưởng | Agent chính (cuộc trò chuyện anh chị đang gõ) | Nhận việc, chia việc, gộp kết quả |
| Tổ chuyên môn | Subagent | Mỗi tổ một việc: kiến trúc, bóc khối lượng |
| Giám sát | Agent kiểm tra | Chỉ đọc, kết luận ĐẠT hay CẦN SỬA |
| Biên bản bàn giao | File handoff | Ai làm xong ghi lại để người sau đọc |

### 1.2b. Một dự án nhà phố thật cần bao nhiêu agent

| # | Agent | Việc | Model |
|---|---|---|---|
| 1 | Tiếp nhận yêu cầu | Phiếu yêu cầu, câu hỏi khách | sonnet |
| 2 | Kiến trúc | Vẽ AutoCAD qua MCP | opus |
| 3 | Kết cấu | Móng, dầm, sàn, thép | opus |
| 4 | Điện nước | Mặt bằng ME | sonnet |
| 5 | Dựng 3D | Blender, Pascal từ file mô tả | sonnet |
| 6 | Render | Đổi phong cách qua ChatGPT MCP | sonnet |
| 7 | Bóc khối lượng | Từ bản vẽ, có diễn giải | sonnet |
| 8 | Dự toán, báo giá | Giá theo công bố giá Sở XD | sonnet |
| 9 | Kiểm soát hồ sơ | Chỉ đọc, soát chéo cả bộ | sonnet, high |
| 10 | Hồ sơ gửi khách | PDF, video MotionFly, thư nháp | sonnet |

Không bật cả 10 cùng lúc: chạy theo từng chặng. Người duyệt ở 3 chỗ: khách chốt phương án, kỹ sư ký bản vẽ, người bấm gửi.

### 1.2c. CLAUDE.md gọn nhẹ: tách luật ra `.claude/rules/`

- CLAUDE.md và các file trong `.claude/rules/` **không** ghi `paths`: nạp ngay khi mở phiên.
- Rule có `paths` (ví dụ `paths: handoff/**`): chỉ nạp khi Claude đọc, sửa file khớp. Đây là cách giảm tải thật.
- `@import` chỉ cho gọn mắt, file được import vẫn nạp từ đầu.
- `~/.claude/rules/`: luật chung cho mọi dự án. Nên giữ mỗi CLAUDE.md dưới 200 dòng.
- Nguồn: `code.claude.com/docs/en/memory`, tra 14/10/2026.

### 1.2d. MCP cài ở dự án hay Global

| Phạm vi | Lưu ở đâu | Dùng được ở | Hợp với |
|---|---|---|---|
| local (mặc định) | `~/.claude.json`, theo dự án | Chỉ dự án này, chỉ mình | Thử MCP mới |
| project | `.mcp.json` ở thư mục dự án | Dự án này, chia sẻ cả nhóm | MCP riêng một công trình |
| user (Global) | `~/.claude.json` | Mọi dự án trên máy | AutoCAD, Blender, ChatGPT ảnh |

Trùng tên: local thắng project, project thắng user. MCP kết nối khi mở phiên; công cụ của nó được tìm khi cần (tool search, mặc định bật). MCP ở project: Claude hỏi duyệt trước khi dùng lần đầu. Nguồn: `code.claude.com/docs/en/mcp`, tra 14/10/2026.

### 1.2e. Bộ demo chạy trong lớp

Thư mục `demo/02-doi-agent-ho-so-nha-pho/`: 4 agent (tiếp nhận, kiến trúc, khối lượng, kiểm tra) lập hồ sơ trình khách cho nhà 7x20m. Prompt trong `01_prompt-chay-doi.md`. Điểm cần chỉ: khách muốn 3 phòng ngủ, bản vẽ có 2.

### 1.3. Điều quan trọng nhất: ngữ cảnh

Mỗi agent ngồi một phòng riêng (cửa sổ ngữ cảnh riêng), **không nghe** cuộc trò chuyện của anh chị. Nó chỉ biết CLAUDE.md, skill, MCP và lời giao việc. Muốn nó biết gì thì ghi vào lời giao việc hoặc vào file.

### 1.4. Mỗi thành viên phải định bốn thứ

| Thứ | Ý nghĩa | Ghi trong file agent |
|---|---|---|
| Nhiệm vụ | Một vai, một đầu ra rõ | `description:` và phần thân |
| Model | Chọn theo độ khó của việc | `model:` (sonnet, opus, haiku, inherit) |
| Mức suy luận | Nghĩ nhiều hay nghĩ nhanh | `effort:` (low, medium, high, xhigh, max) |
| Quyền | Được dùng công cụ nào | `tools:` (người soát: `Read, Glob, Grep`) |

### 1.5. Việc nào dùng model nào

| Vai | Việc | Model | Mức suy luận |
|---|---|---|---|
| Kiến trúc sư | Đọc bản vẽ, lập bảng thông số | opus | high |
| Kỹ sư bóc khối lượng | Tính theo kích thước, ra Excel | sonnet | high |
| Kỹ sư kiểm tra | Soát chéo, chỉ đọc | sonnet | high |
| Thư ký | Đổi tên file, gom danh sách | haiku | low |

### 1.6. Lập đội trong 5 bước

**Bước 1. Vẽ sơ đồ đội trước khi gõ prompt.** Agent chính chia việc; `kien-truc` và `boc-kl` chạy song song; `kiem-tra` chờ `boc-kl` xong mới chạy; agent chính gộp báo cáo.

**Bước 2. Tạo file cho từng agent.**

```
Trong dự án hiện tại, tạo 3 file agent trong .claude/agents/ theo chuẩn subagent của
Claude Code (name, description, tools, model, effort):
kien-truc-su (opus, high), ky-su-boc-khoi-luong (sonnet, high),
ky-su-kiem-tra (sonnet, high, chỉ đọc: tools Read, Glob, Grep).
Mỗi agent ghi kết quả vào handoff/NN_ten.md theo mẫu chung. Không bịa số liệu.
Tạo xong đọc lại cho tôi kiểm.
```

Tạo xong mở cuộc trò chuyện mới để Claude nhận agent.

**Bước 3. Quy định file bàn giao.**

```
du-an-nha-pho\
├── 00_phieu-giao-viec.md      agent chính
├── handoff\
│   ├── 01_kien-truc.md
│   ├── 02_boc-khoi-luong.md
│   └── 03_kiem-tra.md         dòng đầu: Kết luận ĐẠT / CẦN SỬA
└── 99_bao-cao-tong-hop.md     agent chính gộp
```

Mẫu chung mỗi file bàn giao: việc được giao, đầu vào đã đọc, đầu ra, giả định, chỗ chưa chắc, việc người sau cần làm. Mỗi agent chỉ sửa file của mình.

**Bước 4. Giao việc cho cả đội.**

```
Lập đội 3 agent cho hồ sơ nhà phố trong thư mục này. Viết 00_phieu-giao-viec.md trước.
Đặt tên "kien-truc" (agent kien-truc-su) và "boc-kl" (agent ky-su-boc-khoi-luong),
cho chạy song song, mỗi người chỉ sửa file của mình. Hai người xong mới chạy
"kiem-tra" (agent ky-su-kiem-tra). Mỗi agent ghi handoff/NN_ten.md.
Cuối cùng gộp vào 99_bao-cao-tong-hop.md.
```

**Bước 5. Soát và gộp trước khi dùng.** Mở từng file bàn giao; đọc kết luận kiểm tra, CẦN SỬA thì giao lại đúng agent; đối chiếu số với bản vẽ; ghi kinh nghiệm vào file agent cho lần sau. Người ký vẫn là kỹ sư.

### 1.7. Bốn lỗi hay gặp

| Lỗi | Cách sửa |
|---|---|
| Không thấy agent vừa tạo | Mở cuộc trò chuyện mới |
| Hai agent ghi đè file nhau | Mỗi người một file riêng |
| Agent bịa số | Ghi luật "không có trong tài liệu thì ghi Tài liệu không đề cập" |
| Tốn token | Việc nhẹ dùng sonnet hoặc haiku; đội 3 người là đủ |

---

## PHẦN 2. BỘ ĐỒ NGHỀ CÀI BẰNG PROMPT

Một prompt cài đặt tốt có 4 phần: **nguồn** (link repo, tên gói), **trình độ** ("tôi không rành terminal"), **giới hạn** ("không cài thêm gì ngoài README"), **bằng chứng** ("cài xong chạy thử, báo kết quả").

### 2.1. markitdown: hợp đồng, hồ sơ thành chữ cho AI

```
Cài công cụ markitdown của Microsoft cho tôi (gói 'markitdown[all]', đọc được PDF, Word,
Excel, PowerPoint). Máy chưa có Python thì hướng dẫn tôi từng bước, tôi không rành terminal.
Cài xong chuyển thử một file PDF trong thư mục này sang .md và báo kết quả.
```

```
Mở CLAUDE.md Global của tôi, sao lưu bản cũ trước, thêm mục: khi tôi đưa .pdf, .docx, .xlsx
thì tự chuyển sang .md bằng markitdown, lưu cùng thư mục, mở ra kiểm. File .md gần như
trống thì báo tôi đó là PDF scan.
```

### 2.2. Pascal Editor: dựng 3D nhanh trên trình duyệt

```
Cài Pascal Editor từ repo https://github.com/pascalorg/editor cho tôi. Đọc README trước,
chọn cách cài không cần tải mã nguồn (gói npm @pascal-app/cli). Máy chưa có Node.js thì
hướng dẫn tôi từng bước. Cài xong mở Pascal lên, rồi nối Pascal với Claude Code qua MCP
theo README và kiểm tra kết nối.
```

```
Dùng Pascal dựng lại ngôi nhà theo file mô tả bản vẽ trong thư mục này (đơn vị mét):
từng tầng, cửa, cầu thang, mái, sân. Chụp góc 3/4 và góc bung tầng.
Bản vẽ không có thì ghi "Tài liệu không đề cập".
```

### 2.3. MotionFly: video giới thiệu công trình

Quy trình như một đoàn làm phim: kịch bản (anh chị duyệt), giọng đọc, phân cảnh, dựng hình (anh chị duyệt tờ ảnh khung hình), xuất MP4 kèm phụ đề.

```
Cài plugin MotionFly cho Claude Code của tôi từ repo https://github.com/andyluu98/MotionFly
theo đúng hướng dẫn trong README. Cài xong kiểm tra máy còn thiếu gì (Node.js, ffmpeg,
giọng đọc) và cài giúp tôi, tôi không rành terminal. Xong báo tôi khi máy đã sẵn sàng.
```

```
Dùng MotionFly làm video khoảng 1 phút giới thiệu công trình nhà phố của tôi để thuyết trình
cho chủ nhà, khung 16:9, style dark-keynote. Tư liệu: bản vẽ PDF và ảnh render trong thư mục
này. Số liệu chỉ lấy từ bản vẽ. Cho tôi duyệt kịch bản trước, rồi duyệt tờ ảnh khung hình,
rồi mới xuất MP4.
```

Sửa bằng lời: "đổi giọng nam", "nhạc nhỏ lại", "sửa cảnh 3". Ví dụ thật: video nhà phố 7x20m, 54 giây.

---

## Nguồn dữ liệu kiểm chứng

| Nội dung | Nguồn |
|---|---|
| Trường `name`, `description`, `tools`, `model`, `effort` của file agent | `code.claude.com/docs/en/sub-agents`, tra 14/10/2026 |
| Gói `markitdown[all]` | README `microsoft/markitdown`, tra 14/10/2026 |
| Gói `@pascal-app/cli`, nối MCP | README `pascalorg/editor`, tra 14/10/2026 |
| Cài plugin MotionFly | README `andyluu98/MotionFly`, tra 14/10/2026 |
