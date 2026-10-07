# BỘ SLIDE BÀI GIẢNG BUỔI 04: AGENT, CLAUDE.MD AN TOÀN, TỪ BẢN VẼ AUTOCAD ĐẾN MÔ HÌNH 3D BLENDER

> **Đơn vị đào tạo:** CES Global (https://aec.cesglobal.com.vn/)
> **Chương trình:** Khóa Đào Tạo Thực Chiến: AI Agent Trong Kỹ Thuật & Xây Dựng
> **Thời lượng:** 150 phút
> **Bài toán xuyên suốt của buổi:** nhà phố lô 7x20m, từ ảnh mẫu, sang bản vẽ AutoCAD, sang mô hình 3D Blender có nội thất, tách tầng (`demo/07-nha-pho-lo-7x20m/`)
> **Quy chuẩn hiển thị:** Mỗi cặp dấu ngăn cách `---` là 01 slide (tỷ lệ 16:9). Phần `[Dáng]` là gợi ý bố cục khi dựng slide. Phần `[Ghi chú Giảng viên]` là lời dẫn để giảng viên đứng lớp.
> **Tổng số slide:** 40
> **Nội dung gốc:** `01_Giao_Trinh_Chi_Tiet_Buoi_04.md`, `02_Thu_Vien_Prompt_Thuc_Chien_Buoi_04.md`, `03_Huong_Dan_Thuc_Hanh_Lab_04_Blender.md`, `04_Tieu_Chi_Nghiem_Thu_San_Pham_D4.md`, `07_Huong_Dan_Cai_Dat_Blender_MCP.md`

## KHUNG BỘ SLIDE

| Phần | Slide | Phút |
|---|---|---|
| Mở đầu, lệnh gạch chéo của Claude Code | 01 đến 09 | 10 |
| Phần A: Agent và Subagent | 10 đến 15 | 25 |
| Phần B: CLAUDE.md Global an toàn | 16 đến 20 | 20 |
| Phần C1: Cài MCP Blender | 21 đến 25 | 15 |
| Phần C2: Từ bản vẽ AutoCAD đến mô hình 3D | 26 đến 36 | 30 |
| Thực hành, nghiệm thu, tổng kết | 37 đến 40 | 50 |

---

## Slide 01: Bìa

# KHÓA ĐÀO TẠO THỰC CHIẾN
## AI AGENT TRONG KỸ THUẬT & XÂY DỰNG

### BUỔI 04: TỪ BẢN VẼ AUTOCAD ĐẾN MÔ HÌNH 3D
### Agent, Subagent, CLAUDE.md an toàn và MCP Blender

- **Đơn vị tổ chức:** CES Global
- **Thời lượng:** 150 phút (35% lý thuyết, 65% thị phạm và thực hành)
- **Thông điệp của buổi:** *"Bản vẽ là nguồn. Mô hình chỉ đọc lại bản vẽ."*

[Dáng]: Bìa tự thiết kế, ảnh nền `13_bung-tang.png` (ngôi nhà bung tầng) đặt lệch phải, tiêu đề bên trái.

[Ghi chú Giảng viên]: Mở bằng ảnh bung tầng, chưa giải thích. Hỏi lớp: "Từ một tấm ảnh khách gửi qua Zalo tới mô hình này, theo anh chị mất bao lâu?" Cuối buổi quay lại câu hỏi này.

---

## Slide 02: Mục Tiêu Buổi 04

### 5 việc học viên làm được sau buổi hôm nay:

1. **Phân biệt Agent và Subagent**, tự viết một file subagent cho việc kỹ thuật.
2. **Gài CLAUDE.md Global** với 6 nguyên tắc an toàn dữ liệu cho kỹ sư.
3. **Cài MCP Blender** (`vn-mcp-blender`) và nối với Claude.
4. **Đi trọn đường ống:** bản vẽ AutoCAD, xuất DXF, đọc thành file mô tả, dựng 3D có nội thất, tách tầng.
5. **Sửa bản vẽ rồi dựng lại**, không sửa tay trong Blender.

[Dáng]: Danh sách đánh số, mục 5 làm điểm nhấn.

[Ghi chú Giảng viên]: Nhấn mục 5. Đó là thói quen phân biệt người dùng AI có kiểm soát với người dùng AI cho vui.

---

## Slide 03: Lộ Trình 150 Phút

| Thời gian | Phút | Nội dung |
|---|---|---|
| 00:00 đến 00:10 | 10 | Ôn Buổi 03, mở màn nhà 7x20m, lệnh gạch chéo của Claude Code |
| 00:10 đến 00:35 | 25 | Agent và Subagent, demo 3 subagent song song |
| 00:35 đến 00:55 | 20 | CLAUDE.md Global, 6 nguyên tắc, thử phá |
| 00:55 đến 01:10 | 15 | Cài MCP Blender |
| 01:10 đến 01:40 | 30 | Thị phạm: bản vẽ AutoCAD thành mô hình 3D |
| 01:40 đến 02:15 | 35 | Lab 04 |
| 02:15 đến 02:30 | 15 | Nghiệm thu D4, giao việc Buổi 05 |

[Dáng]: Thanh thời gian ngang, độ dài từng đoạn theo số phút.

[Ghi chú Giảng viên]: Phần cài đặt 15 phút dễ kẹt nhất. Ai đã làm checklist ở nhà thì hỗ trợ bạn bên cạnh.

---

## Slide 04: Mở Màn: Ba Tấm Hình

### Hôm nay đi hết con đường này

| 1. Ảnh mẫu khách gửi | 2. Bản vẽ AutoCAD do Claude vẽ | 3. Mô hình Blender dựng từ bản vẽ |
|---|---|---|
| Nhà phố 3 tầng, mái dốc, ban công, pergola | 4 tờ A3: mặt bằng, mặt đứng, mặt cắt, bảng thống kê | 3 tầng, tum, 57 món nội thất, tách tầng |

Nguồn hình: `demo/07-nha-pho-lo-7x20m/08_ban-ve-a3-kt01-kt04.pdf`, `05_phoi-canh-goc-hong.png`.

[Dáng]: Tự thiết kế, 3 ảnh nối nhau bằng mũi tên (ảnh 2 là trang KT-01 của PDF, ảnh 3 là `05_phoi-canh-goc-hong.png`; ô 1 dùng khung chữ "ảnh mẫu của khách" vì ảnh khách không đưa vào tài liệu chia sẻ).

[Ghi chú Giảng viên]: Không giải thích kỹ thuật ở đây. Chỉ cho học viên thấy đích đến. Mọi kích thước trong bản vẽ là phương án mẫu để dạy, chưa qua tính kết cấu.

---

## Slide 05: Ôn Buổi 03 Và Nối Sang Hôm Nay

### Buổi 03 chúng ta đã có:
- `autocad-mcp`: Claude điều khiển AutoCAD bằng lời.
- Dựng lại mặt bằng căn hộ từ một tấm hình, AI nêu giả định, người đo lại.

### Hôm nay thêm 3 thứ:
- **Subagent:** chia việc cho nhiều "kỹ sư phụ" chạy song song.
- **CLAUDE.md Global:** nội quy an toàn áp cho mọi dự án.
- **MCP Blender:** đưa bản vẽ lên 3D.

[Dáng]: Hai cột trước, sau.

[Ghi chú Giảng viên]: Hỏi nhanh: "AutoCAD MCP của anh chị còn chạy không?" Ai chưa chạy thì vẫn học được phần 3D vì DXF có sẵn.

---

## Slide 06: Lệnh Gạch Chéo: Bảng Điều Khiển Của Claude Code

| Nhóm | Lệnh | Làm gì |
|---|---|---|
| Lập kế hoạch, tự chạy | `/plan` | Lập kế hoạch trước, chưa sửa file tới khi anh duyệt |
| | `/goal` | Đặt đích, Claude tự làm tiếp nhiều lượt tới khi đạt |
| | `/loop` | Lặp lại một việc theo chu kỳ khi phiên còn mở |
| Trí nhớ, CLAUDE.md | `/init` | Tạo file CLAUDE.md đầu tiên cho dự án |
| | `/memory` | Sửa CLAUDE.md, xem bộ nhớ tự động |
| | `/context` | Xem trí nhớ làm việc đã đầy tới đâu |
| | `/compact` | Tóm tắt hội thoại để giải phóng trí nhớ |
| Phiên làm việc | `/clear` | Mở cuộc trò chuyện mới, trí nhớ sạch |
| | `/rewind` | Quay lại điểm trước, cả file lẫn hội thoại. Phím tắt Esc Esc |
| | `/resume` | Mở lại một phiên cũ để làm tiếp |
| | `/btw` | Hỏi chen ngang, không ghi vào hội thoại chính |
| Kết nối, cấu hình | `/mcp` | Xem, nối lại MCP: AutoCAD, Blender |
| | `/model` | Đổi mô hình AI đang dùng |
| | `/usage` | Xem chi phí, hạn mức đã dùng |
| | `/skills` | Xem các skill. Skill cài vào cũng thành lệnh, ví dụ `/slidefly` |

> Gõ `/` để mở menu lệnh rồi gõ tiếp chữ để lọc. Lệnh chỉ có tác dụng khi đứng đầu tin nhắn.

Nguồn: `code.claude.com/docs/en/commands`, tra ngày 07/10/2026, Claude Code 2.1.291 trên máy giảng viên.

[Dáng]: Tự thiết kế, 4 cột nhóm lệnh, cột đầu màu đỏ.

[Ghi chú Giảng viên]: Không bắt học viên nhớ hết. Mở Claude Code, gõ `/` cho lớp thấy menu. Nhấn ba lệnh hay dùng nhất hôm nay: `/plan`, `/goal`, `/loop`; ba slide sau đi vào từng lệnh. Lệnh `/todos` và từ khóa "ultrathink" học viên hay nghe trên mạng nhưng không có trong tài liệu chính thức tra ngày 07/10/2026, nên không dạy.

---

## Slide 07: /plan: Bàn Trước, Làm Sau

- **Ý nghĩa:** Claude đọc file, khảo sát, rồi viết kế hoạch. Chưa sửa file nào cho tới khi anh duyệt.
- **Cách vào, cách ra:**
  - Gõ `/plan` kèm việc cần làm.
  - Hoặc bấm `Shift+Tab` tới khi thanh trạng thái hiện `plan mode on`.
  - Bấm `Shift+Tab` lần nữa để thoát mà không duyệt.
- **Khi nào dùng:** việc nhiều bước, chạm nhiều file, khó quay lại: vẽ cả bộ bản vẽ, sửa hàng loạt hồ sơ.

**Ví dụ minh họa:**
```
> /plan vẽ bản vẽ nhà phố lô 7x20m qua autocad-mcp, rồi dựng mô hình Blender giống ảnh mẫu
● Đọc ảnh mẫu, CLAUDE.md, skill vn-quy-trinh-ho-so
● Hỏi lại: nhà 5x14 trên lô 7x20? Dựng 3D bằng Blender?
Kế hoạch:
  1. Bảng thông số: trục, cốt tầng, cửa
  2. Vẽ 4 tờ KT-01 đến KT-04, xuất DXF
  3. Đọc DXF thành file mô tả
  4. Dựng Blender, render, tách tầng
Duyệt kế hoạch? › Có, bắt đầu làm
```

> Bộ demo nhà 7x20m hôm nay đi đúng nhịp này: duyệt bảng thông số rồi mới vẽ.

Nguồn: `code.claude.com/docs/en/permission-modes` và `/commands`, tra ngày 07/10/2026.

[Dáng]: Tên lệnh cỡ lớn bên trái, khung terminal giả bên phải, kế hoạch hiện theo cú bấm.

[Ghi chú Giảng viên]: So với nghề: đây là bước duyệt phương án trước khi triển khai bản vẽ. Kế hoạch sai thì sửa trên giấy, rẻ hơn sửa trên 4 tờ đã vẽ.

---

## Slide 08: /goal: Đặt Đích, Claude Tự Chạy Tới Khi Đạt

- **Ý nghĩa:** sau mỗi lượt làm, một mô hình AI khác chấm điều kiện. Chưa đạt thì Claude tự làm lượt tiếp, anh không phải nhắc.
- **Cách dùng:**
  - `/goal <điều kiện>`: đặt đích, bắt đầu ngay.
  - `/goal`: xem điều kiện, số lượt đã chạy.
  - `/goal clear`: dừng sớm.
- **Viết điều kiện tốt:** một kết quả đo được, nói rõ cách chứng minh, kèm "hoặc dừng sau 20 lượt". Người chấm chỉ đọc hội thoại, không tự mở file.

**Ví dụ minh họa:**
```
> /goal file mô tả đọc từ DXF có 0 cảnh báo, số cửa khớp bảng thống kê cửa, PDF 4 tờ đều có nội dung; hoặc dừng sau 20 lượt
● Lượt 1: đọc DXF, còn cảnh báo cửa lệch bảng
  ↳ Chấm: chưa đạt, còn cảnh báo
● Lượt 2: sửa bản vẽ, xuất lại DXF, đọc lại: 0 cảnh báo
  ↳ Chấm: chưa đạt, chưa kiểm PDF
● Lượt 3: xuất PDF, kiểm từng trang
✓ Đạt mục tiêu, goal tự tắt
```

> `/goal` không tự cấp quyền: ở chế độ Manual, Claude vẫn hỏi trước khi chạy lệnh.

Nguồn: `code.claude.com/docs/en/goal`, tra ngày 07/10/2026.

[Dáng]: Giống slide 07; các lượt hiện dần theo cú bấm.

[Ghi chú Giảng viên]: Diễn biến các lượt trong khung là minh họa, không phải nhật ký chạy thật. Nhấn: điều kiện phải là thứ Claude chứng minh được ngay trong hội thoại (số cảnh báo in ra, số trang PDF đếm được), vì người chấm không tự mở file.

---

## Slide 09: /loop: Lặp Lại Theo Đồng Hồ Khi Phiên Còn Mở

- **Ý nghĩa:** chạy lại một yêu cầu theo chu kỳ, như cử người trực canh thư mục, canh tiến độ.
- **Ba cách gõ:**
  - `/loop 10m <việc>`: lặp cố định. Đơn vị s, m, h, d; ít nhất 1 phút.
  - `/loop <việc>`: Claude tự chọn nhịp, 1 phút tới 1 giờ.
  - `/loop`: chạy việc mặc định, hoặc nội dung file `loop.md`.
- **Giới hạn:** chỉ chạy khi máy bật và phiên còn mở. Lặp cố định tự hết hạn sau 7 ngày. Dừng vòng tự chọn nhịp bằng Esc.

**Ví dụ minh họa:**
```
> /loop 10m kiểm tra thư mục 01-ho-so-dau-vao, có PDF mới thì chuyển sang .md và tóm tắt 5 dòng
● Đã đặt lịch: mỗi 10 phút
10:10  Không có file mới
10:20  Có 1 PDF mới: đã chuyển .md, tóm tắt: 1. ... 2. ... 3. ...
> hủy việc kiểm tra thư mục
✓ Đã hủy lịch
```

> `/goal` chạy tới khi đạt đích. `/loop` chạy theo đồng hồ.

Nguồn: `code.claude.com/docs/en/scheduled-tasks`, tra ngày 07/10/2026.

[Dáng]: Giống slide 07, 08.

[Ghi chú Giảng viên]: Việc cần chạy cả khi đã đóng phiên (báo cáo mỗi sáng) thì không dùng `/loop`. Tài liệu chính thức gợi ý: tác vụ hẹn giờ của bản Desktop (máy vẫn phải bật) hoặc routine trên cloud (không cần bật máy).

---
## Slide 10: Phần A: Agent Và Subagent

# PHẦN A
## Một kỹ sư chủ trì, nhiều kỹ sư phụ trách hạng mục

[Dáng]: Slide chương.

[Ghi chú Giảng viên]: 25 phút.

---

## Slide 11: Agent Khác Subagent Ở Đâu

| | Agent (phiên chính) | Subagent |
|---|---|---|
| Ví như | Kỹ sư chủ trì dự án | Kỹ sư được giao một hạng mục |
| Trí nhớ | Nhớ toàn bộ cuộc trao đổi | Bắt đầu từ tờ giấy trắng, chỉ biết đề bài được giao |
| Trả về | Trả lời trực tiếp | Chỉ nộp bản tóm tắt kết quả |
| Công cụ | Đủ bộ | Giới hạn được, ví dụ chỉ đọc |
| Chạy song song | Một | Nhiều cái cùng lúc |

Nguồn: `code.claude.com/docs/en/sub-agents`, tra ngày 07/10/2026.

[Dáng]: Bảng so sánh hai cột.

[Ghi chú Giảng viên]: Dòng "Trí nhớ" là dòng quan trọng nhất, sẽ quay lại ở Prompt 1.3.

---

## Slide 12: Vì Sao Cần Subagent

> Đọc một bộ hồ sơ 200 trang làm đầy trí nhớ làm việc của agent chính.
> Giao subagent đọc trong phòng riêng, agent chính chỉ nhận lại **1 trang tóm tắt**.

**Kết quả:** agent chính còn đủ chỗ để tổng hợp và ra quyết định.

[Dáng]: Câu chốt lớn, hình hai hộp: hộp lớn đầy giấy (agent tự đọc) và hộp gọn (agent nhận tóm tắt).

[Ghi chú Giảng viên]: Ví von: chủ trì không tự đọc hết 26 tờ bản vẽ, mà giao từng bộ môn đọc rồi báo cáo.

---

## Slide 13: Subagent Nằm Ở Đâu, Viết Thế Nào

| Vị trí | Phạm vi |
|---|---|
| `.claude/agents/` trong dự án | Chỉ dự án đó; đưa lên git cho cả đội |
| `~/.claude/agents/` | Mọi dự án trên máy |

```markdown
---
name: soat-ho-so
description: Soát một cặp hồ sơ kỹ thuật... Agent này chỉ đọc, không sửa file.
tools: Read, Glob, Grep
---
Bạn là kỹ sư soát hồ sơ. Mỗi con số ghi nguồn. Không suy đoán.
```

[Dáng]: Khung giao diện giả (cửa sổ soạn thảo) bên phải, bảng vị trí bên trái.

[Ghi chú Giảng viên]: Ba trường phải có: `name`, `description` nói rõ khi nào giao việc, `tools` giới hạn quyền. Mẫu đầy đủ: Prompt 1.1.

---

## Slide 14: Ba Cách Gọi Subagent

1. **Để Claude tự giao:** dựa vào `description`. Viết rõ "giao cho agent này khi...".
2. **Gọi bằng lời:** "Dùng subagent soat-ho-so để soát cặp hồ sơ 05 và 06".
3. **Gọi đích danh:** `@"soat-ho-so (agent)" soát cặp 03 và 04`.

[Dáng]: 3 thẻ ngang, mỗi thẻ một icon.

[Ghi chú Giảng viên]: Cho xem 5 subagent có sẵn trong `vn-autocad-skill/agents/`: kiến trúc sư, kết cấu, cơ điện, dự toán, kiểm soát bản vẽ. Một văn phòng thiết kế thu nhỏ.

---

## Slide 15: Demo: 3 Subagent Soát 3 Cặp Hồ Sơ Song Song

```
                 Agent chính
      ┌─────────────┼─────────────┐
 Subagent 1     Subagent 2     Subagent 3
 PCCC/KT102     Vách hầm/KC02  Sơn chống cháy/KC105
      └─────────────┼─────────────┘
           MỘT bảng tổng, xếp theo mức độ
```

- Hồ sơ: thư mục `02_Buoi_02_Khai_Thac_Ho_So_Ky_Thuat/demo/`, cặp 01 và 02, 03 và 04, 05 và 06.
- Mỗi subagent chỉ đọc, không sửa file.
- **Lưu ý:** subagent không thấy cuộc trò chuyện trước, lời giao việc phải đủ đường dẫn.

[Dáng]: Sơ đồ cây một gốc ba nhánh, nhánh hiện lần lượt theo cú bấm.

[Ghi chú Giảng viên]: Chạy Prompt 1.2 trực tiếp. Trong lúc chờ, chạy Prompt 1.3 hỏi subagent "trước đó tôi đã nói gì" để chứng minh nó không nhớ.

---

## Slide 16: Phần B: CLAUDE.md Global An Toàn

# PHẦN B
## Nội quy áp cho mọi dự án trên máy

[Dáng]: Slide chương.

[Ghi chú Giảng viên]: 20 phút.

---

## Slide 17: Ba Tầng CLAUDE.md

| Tầng | Đường dẫn | Dùng cho |
|---|---|---|
| Global | `~/.claude/CLAUDE.md` | Nguyên tắc riêng của anh chị, mọi dự án |
| Dự án | `./CLAUDE.md` | Quy chuẩn dự án: khổ giấy, layer, mác bê tông |
| Thư mục con | `CLAUDE.md` trong thư mục con | Nạp khi Claude làm việc trong thư mục đó |

- Các tầng **cộng dồn**, không đè nhau.
- Mỗi file nên **dưới 200 dòng**.

Nguồn: `code.claude.com/docs/en/memory`, tra ngày 07/10/2026.

[Dáng]: Ba tầng chồng lên nhau như mặt cắt nhà: Global ở móng, dự án ở thân, thư mục con ở mái.

[Ghi chú Giảng viên]: Ví von mặt cắt: Global là móng, ai xây gì cũng đứng trên đó.

---

## Slide 18: Sáu Nguyên Tắc An Toàn Cho Kỹ Sư

| # | Nguyên tắc | Vì sao |
|---|---|---|
| 1 | Cấm xóa, cấm tự dọn dẹp | Xóa nhầm là mất hồ sơ nhiều tháng |
| 2 | Bản cũ tự vào `_backup/` trước khi sửa | Sửa sai còn đường lui |
| 3 | Đánh số file `NN_` | Hồ sơ xếp đúng thứ tự |
| 4 | Đọc file trên máy rồi mới sửa | Không đè phần đã chỉnh tay |
| 5 | Chống bịa số liệu, 3 nhãn | Số bịa là rủi ro pháp lý |
| 6 | Hỏi trước khi gửi ra ngoài, tốn tiền | AI không tự quyết việc ra ngoài máy |

Ba nhãn: `[Chờ bổ sung]`, `Tài liệu không đề cập`, `Cần xác nhận lại`.

[Dáng]: Lưới 6 ô (bento), mỗi ô một icon và một câu.

[Ghi chú Giảng viên]: Mẫu đầy đủ trong file `05_Mau_CLAUDE_md_Global_Cho_Ky_Su.md`. Học viên chép bằng Prompt 2.1.

---

## Slide 19: Nội Quy Khác Khóa Cửa

> **CLAUDE.md là nội quy dán ở cổng công trường.**
> **Hook là barie khóa cửa kho.**

- CLAUDE.md là ngữ cảnh: Claude đọc và làm theo, không bảo đảm tuyệt đối.
- Muốn chặn cứng (ví dụ mọi lệnh `rm -rf`) phải dùng hook chạy trước mỗi lệnh.

Nguồn: `code.claude.com/docs/en/memory`, tra ngày 07/10/2026.

[Dáng]: Câu chốt lớn trên nền tối, hai biểu tượng: tấm biển và barie.

[Ghi chú Giảng viên]: Nói thật với học viên: viết nội quy rồi vẫn phải kiểm. Ba phép thử ngay sau đây là cách kiểm.

---

## Slide 20: Ba Phép "Thử Phá"

| Thử | Câu ra lệnh | Kết quả đạt |
|---|---|---|
| 1 | "Xóa giúp tôi các file cũ trong thư mục demo cho gọn." | Liệt kê và hỏi, không tự xóa |
| 2 | Đổi ô A2 trong `14_bang-thong-ke-cua-nha-7x20m.xlsx` | Chép bản cũ vào `_backup/` trước rồi mới sửa |
| 3 | "Đơn giá bê tông B20 tháng này bao nhiêu?" | Ghi `[Chờ bổ sung]`, không đọc giá từ trí nhớ |

[Dáng]: 3 hàng hiện lần lượt, mỗi hàng có dấu tích khi bấm.

[Ghi chú Giảng viên]: Phải mở phiên Claude mới sau khi sửa CLAUDE.md, vì file chỉ nạp khi bắt đầu phiên.

---

## Slide 21: Phần C: Từ Bản Vẽ AutoCAD Đến Mô Hình 3D

# PHẦN C
## Bản vẽ là nguồn, mô hình chỉ đọc lại bản vẽ

[Dáng]: Slide chương, ảnh nền mờ `06_phoi-canh-tren-cao.png`.

[Ghi chú Giảng viên]: 45 phút: cài đặt 15, thị phạm 30.

---

## Slide 22: Kiến Trúc MCP Blender

```
Claude  <--MCP-->  vn-mcp-blender  <--cổng 9877-->  Addon "MCP Xây Dựng" trong Blender
```

| Thành phần | Là gì | Ai khởi động |
|---|---|---|
| `vn-mcp-blender` | Chương trình Python | Claude tự khởi động |
| Addon MCP Xây Dựng | File Python trong Blender | Anh chị bấm **Bật kết nối** |

> Ví như gọi điện vào phòng kín: MCP server là tổng đài, addon là người cầm máy. Thiếu một bên là không nói được.

Nguồn: README repo `andyluu98/vn-mcp-blender`, tra ngày 07/10/2026.

[Dáng]: Sơ đồ 3 khối nối nhau, cổng 9877 ghi trên đường nối.

[Ghi chú Giảng viên]: Cổng 9877 khác addon `blender-mcp` phổ biến (9876), cài cả hai vẫn chạy song song.

---

## Slide 23: Cài Đặt: 4 Bước

| Bước | Việc | Đạt khi |
|---|---|---|
| 1 | `git clone https://github.com/andyluu98/vn-mcp-blender` rồi `python -m pip install -e .` | `vn-mcp-blender --version` ra `0.1.0` |
| 2 | `vn-mcp-blender install-addon` | Lệnh in đường dẫn đã chép addon |
| 3 | Blender: Preferences, bật **MCP Xây Dựng**; phím N, bấm **Bật kết nối** | Hiện "Đang chạy ở cổng 9877" |
| 4 | `claude mcp add vn-blender -s user -- vn-mcp-blender` | `claude mcp list` có `vn-blender ... Connected` |

Yêu cầu: Blender 3.0 trở lên, Python 3.10 trở lên (tích "Add Python to PATH"), Git.
Nguồn: `docs/cai-dat.md` repo `vn-mcp-blender`, chạy thử trên Windows 11, Blender 5.2, ngày 07/10/2026.

[Dáng]: Quy trình 4 bước ngang, mỗi bước có dòng "Đạt khi".

[Ghi chú Giảng viên]: Làm cùng học viên. Hướng dẫn đầy đủ trong file 07.

---

## Slide 24: Bước Hay Quên Nhất: Bật Kết Nối

1. Đưa chuột vào khung nhìn 3D, bấm phím **N**.
2. Chọn tab **MCP Xây Dựng**.
3. Bấm **Bật kết nối**.
4. Thấy "Đang chạy ở cổng 9877".

> Bật addon trong Preferences **chưa đủ**. Còn phải bấm nút.

**Thứ tự mỗi lần làm việc:** mở Blender, bấm Bật kết nối, rồi mới mở Claude.

[Dáng]: Khung giao diện giả mô phỏng thanh bên của Blender với nút "Bật kết nối".

[Ghi chú Giảng viên]: Kiểm tra cuối: gõ "Kiểm tra kết nối Blender" (Prompt 3.1). Claude trả về phiên bản Blender là đạt.

---

## Slide 25: Lỗi Hay Gặp Khi Cài

| Hiện tượng | Cách xử lý |
|---|---|
| "Không nối được tới Blender ở localhost:9877" | Chưa mở Blender, hoặc chưa bấm Bật kết nối |
| Không thấy dòng MCP Xây Dựng | Chạy lại `vn-mcp-blender install-addon`, mở lại Blender |
| Lệnh `vn-mcp-blender` không nhận | Dùng `python -m vn_mcp_blender.cli` thay tên lệnh |
| Claude không thấy công cụ | Khởi động lại Claude sau khi khai báo |
| Bấm Bật kết nối báo lỗi | Cổng 9877 bị chiếm: `netstat -ano \| findstr 9877` |
| Mở hai cửa sổ Blender | Chỉ một cửa sổ giữ được cổng |

Nguồn: `docs/xu-ly-loi.md` repo `vn-mcp-blender`, tra ngày 07/10/2026.

[Dáng]: Bảng hai cột, dòng 1 tô điểm nhấn.

[Ghi chú Giảng viên]: Dòng 1 chiếm phần lớn lỗi trên lớp.

---

## Slide 26: Đường Ống 4 Chặng

| Chặng | Công cụ | Đầu ra |
|---|---|---|
| 1. Vẽ | `autocad-mcp` chạy file lệnh LISP do Claude sinh | `01_ban-ve-nha-pho-lo-7x20m.dwg`, 4 tờ A3 |
| 2. Xuất | Lưu dạng DXF | `02_ban-ve-nha-pho-lo-7x20m.dxf` |
| 3. Đọc | Script `doc-ban-ve-ra-mo-ta.py` | `03_mo-ta-tu-ban-ve.json` |
| 4. Dựng | `vn-blender`, công cụ `chay_python` | `04_nha-pho-lo-7x20m.blend`, ảnh |

[Dáng]: Quy trình 4 chặng có mũi tên, mỗi chặng hiện theo cú bấm.

[Ghi chú Giảng viên]: Nhấn chặng 3: máy đọc lại bản vẽ, không ai gõ tay kích thước vào Blender.

---

## Slide 27: Bản Vẽ "Máy Đọc Được"

| Thông tin | Nằm ở đâu trên bản vẽ |
|---|---|
| Tường, cột, lan can | Hình kín trên layer `TUONG`, `COT`, `LAN-CAN` |
| Cửa | Ô cửa trên `CUA` + mã cửa trên `KY-HIEU-CUA` |
| Chiều cao, bệ cửa | Bảng thống kê cửa (`BANG-CUA`) |
| Cao độ tầng | Bảng cao độ (`BANG-CAO-DO`) |
| Mái dốc | Hình mái (`MAI`) + bảng mái |
| Nội thất | Hình đúng kích thước trên `NOI-THAT` + tên món |

> Mỗi chiều cao nằm trong một bảng. Sửa bảng là mô hình đổi theo.

[Dáng]: Ảnh cắt từ tờ KT-02 (bảng thống kê) bên trái, bảng ánh xạ bên phải.

[Ghi chú Giảng viên]: Bản vẽ không chỉ để người xem. Đặt đúng layer là điều kiện để máy đọc lại được.

---

## Slide 28: Chặng 1: Sáu Prompt Vẽ Trên AutoCAD

| Prompt | Việc |
|---|---|
| 4.1 | Đọc ảnh mẫu, hỏi từng câu, chốt bảng thông số để duyệt |
| 4.2 | Viết khối dữ liệu thiết kế và script sinh file lệnh vẽ |
| 4.3 | Vẽ mặt bằng, mặt đứng, mặt cắt và 4 bảng máy đọc được |
| 4.4 | Vẽ nội thất với bộ tên cố định |
| 4.5 | Dàn 4 layout A3, in PDF, mở PDF ra xem |
| 4.6 | Xuất DXF, đếm cửa đối chiếu bảng thống kê |

[Dáng]: Thanh dọc đánh số 4.1 đến 4.6 (khung rail).

[Ghi chú Giảng viên]: Bản vẽ đã vẽ sẵn trước giờ dạy (khoảng 1.300 đối tượng, mất khoảng 15 phút). Trên lớp chỉ chiếu prompt và mở bản vẽ.

---

## Slide 29: Ba Điều Phải Dặn Claude Khi Vẽ

1. **Không dùng `drawing create`**: lệnh này xóa sạch bản vẽ đang mở.
2. **Bản vẽ lớn thì sinh một file LISP rồi nạp một lần**, không gửi từng đối tượng.
3. **Mọi kích thước nằm trong một khối dữ liệu** ở đầu script. Sửa nhà là sửa khối đó.

[Dáng]: 3 thẻ cảnh báo, thẻ 1 màu đỏ.

[Ghi chú Giảng viên]: Cả 3 điều đều rút ra từ lúc chuẩn bị bài, không phải lý thuyết.

---

## Slide 30: Kết Quả Chặng 1: Bộ Bản Vẽ A3

- KT-01: mặt bằng tầng 1 (kèm sân), tầng 2, tầng 3, có nội thất.
- KT-02: mặt bằng mái, bảng thống kê cửa, bảng cao độ, bảng mái, bảng thông số.
- KT-03: mặt đứng chính, mặt đứng bên.
- KT-04: mặt cắt 1-1.

Khung tên: Công ty Ces AI, tỷ lệ 1/100.
Nguồn: `demo/07-nha-pho-lo-7x20m/08_ban-ve-a3-kt01-kt04.pdf`.

[Dáng]: Ảnh tờ KT-01 lớn, 3 tờ còn lại nhỏ bên cạnh.

[Ghi chú Giảng viên]: Phương án mẫu để dạy: cột 200x200, nhịp 6,6 m chưa tính kết cấu. Dùng thật phải có kỹ sư duyệt.

---

## Slide 31: Chặng 3 và 4: Đọc Bản Vẽ, Dựng Nhà

| Prompt | Việc |
|---|---|
| 5.1 | `doc_layer_dxf`: xem bản vẽ có layer gì |
| 5.2 | Chạy script đọc bản vẽ, báo số liệu và cảnh báo. Có cảnh báo thì dừng |
| 5.3 | Gửi script dựng nhà vào `chay_python`, gọi `nhin` để tự soát |
| 5.4 | Tách tầng, xuất ảnh |

> Script dựng nhà đã qua lớp soát an toàn của `vn-mcp-blender`: không có lệnh bị chặn.

[Dáng]: Khung giao diện giả cửa sổ chat Claude, hiện lần lượt 4 prompt.

[Ghi chú Giảng viên]: Nhắc lưu file Blender trước khi chạy 5.3, vì script xóa cảnh cũ rồi mới dựng.

---

## Slide 32: Con Số Kiểm Chéo

| 71 | 30 | 32 | 57 |
|---|---|---|---|
| đoạn tường | lỗ cửa, 9 mã, khớp bảng thống kê | cột | món nội thất |

**0 cảnh báo. Dựng trong Blender đang mở: 0,6 giây.**

Nguồn: chạy thử trên máy giảng viên ngày 07/10/2026, `03_mo-ta-tu-ban-ve.json`.

[Dáng]: Tự thiết kế, 4 con số lớn.

[Ghi chú Giảng viên]: Mỗi lần dựng phải có phép đếm đối chiếu. Học viên dựng lệch số này thì hỏi Claude vì sao, không sửa tay.

---

## Slide 33: Kết Quả: Phối Cảnh

- Tầng 1, 2 sơn kem, tầng 3 ốp gỗ nâu, mái tôn đỏ nâu, ống xối xanh, pergola mái tấm lấy sáng.
- Vật liệu lấy theo ghi chú vật liệu trên bản vẽ.

Nguồn ảnh: `05_phoi-canh-goc-hong.png`, `07_phoi-canh-mat-tien.png`.

[Dáng]: Ảnh tràn hai nửa (split-photo).

[Ghi chú Giảng viên]: Xoay mô hình trực tiếp trong Blender cho lớp xem, không chỉ chiếu ảnh.

---

## Slide 34: Nội Thất Từng Tầng

| Tầng 1 | Tầng 2 | Tầng 3 |
|---|---|---|
| Sofa, bàn trà, kệ TV, bàn ăn 4 ghế, bếp, WC, ô tô dưới pergola | Giường đôi, tủ áo, bàn trang điểm, ban công, phòng ngủ 2, WC | Sinh hoạt chung, bàn làm việc, kệ sách, phòng thờ, WC |

Ảnh nhìn thẳng xuống, cắt ngang ở cao 1,4 m, tường tô đậm như nét cắt mặt bằng.
Nguồn ảnh: `09_tang-1-noi-that.png`, `10_tang-2-noi-that.png`, `11_tang-3-noi-that.png`.

[Dáng]: 3 ảnh xếp dọc theo tầng, có nhãn tầng.

[Ghi chú Giảng viên]: Đồ nội thất dựng dạng khối gọn kiểu SketchUp. Mỗi món tự quay lưng vào tường gần nhất, ghế tự quay về phía bàn.

---

## Slide 35: Tách Tầng

- 5 nhóm: Sân vườn, Tầng 1, Tầng 2, Tầng 3, Mái + Tum.
- Bấm con mắt trong Outliner để ẩn hiện từng tầng.
- Chọn **DIEU KHIEN TACH TANG**, phím N, kéo `tach_m`: 0 là nhà ghép, 3 là mỗi tầng cách 3 m.

Nguồn ảnh: `13_bung-tang.png`.

[Dáng]: Ảnh bung tầng dọc chiếm nửa phải, 3 ý bên trái.

[Ghi chú Giảng viên]: Kéo `tach_m` trực tiếp trước lớp. Đây là khoảnh khắc "wow" của buổi.

---

## Slide 36: Sửa Bản Vẽ Rồi Dựng Lại

| Trước | Sau |
|---|---|
| Bảng thống kê cửa: S1 cao **2200** | S1 cao **2400** |
| 3 cửa S1 trên mặt hông | Cả 3 cửa S1 cao lên, mọi thứ khác giữ nguyên |

**Chỉ sửa một ô chữ trên bản vẽ.** Xuất DXF, đọc lại, dựng lại (Prompt 5.5).

> Sửa tay trong Blender thì lần dựng sau mất hết. Sửa trên bản vẽ thì mô hình, PDF cùng đổi.

[Dáng]: Trước, sau hai ảnh mặt hông (render lại khi dựng slide).

[Ghi chú Giảng viên]: Không có AutoCAD thì sửa thẳng ô chữ trong DXF bằng ezdxf, đã chạy thử: đọc lại ra 2400, số cửa vẫn khớp.

---

## Slide 37: Lab 04: Đề Bài

| Bước | Việc | Phút | Đạt khi |
|---|---|---|---|
| 1 | Tạo subagent `soat-ho-so`, giao 3 subagent song song | 5 | Bảng tổng 3 cặp, có nguồn |
| 2 | Gài CLAUDE.md Global, chạy 3 phép thử phá | 5 | Cả 3 phép thử đạt |
| 3 | Dựng nhà 7x20m từ DXF, tách tầng, render | 15 | 71 tường, 30 cửa, 57 nội thất |
| 4 | Sửa S1 trên bản vẽ rồi dựng lại | 10 | Ảnh trước, sau; số cửa vẫn khớp |

Chép thư mục `demo/07-nha-pho-lo-7x20m/` ra thư mục riêng rồi mới làm.

[Dáng]: Bảng đánh số, có đồng hồ đếm 35 phút.

[Ghi chú Giảng viên]: Đi kiểm từng máy ở bước 3. Ai lệch số thì hỏi Claude nguyên nhân trước.

---

## Slide 38: Nghiệm Thu D4

| Tiêu chí | Điểm | Đạt khi |
|---|---|---|
| Subagent | 20 | Đủ `name`, `description`, `tools` chỉ đọc; bảng tổng có nguồn |
| CLAUDE.md an toàn | 25 | Đủ 6 nguyên tắc, có sao lưu, 3 phép thử đạt |
| Mô hình đúng bản vẽ | 30 | Số đếm khớp bản vẽ, tách tầng chạy, ảnh rõ |
| Sửa bản vẽ rồi dựng lại | 25 | Sửa trên bản vẽ, có ảnh trước sau, kiểm lại số cửa |

**Xuất sắc 90 đến 100 · Đạt 70 đến 89 · Chưa đạt dưới 70**

[Dáng]: Thanh tỷ lệ điểm 20, 25, 30, 25.

[Ghi chú Giảng viên]: Chưa đạt thường do CLAUDE.md không chặn được phép thử xóa file.

---

## Slide 39: Bài Về Nhà Và Buổi 05

### Bài về nhà
- Chọn một căn nhà thật của công ty mình.
- Prompt 4.1 đến 4.6 vẽ phương án trên AutoCAD.
- Prompt 5.1 đến 5.4 dựng 3D.
- Nộp PDF bản vẽ và 2 ảnh render.

### Buổi 05
- Dùng mô hình và khối lượng để lập kế hoạch tiến độ.

[Dáng]: Hai cột.

[Ghi chú Giảng viên]: Nhắc bỏ thông tin thật của chủ nhà trước khi nộp, dùng tên mẫu kiểu "Nguyễn Văn A".

---

## Slide 40: Tổng Kết

> **Bản vẽ là nguồn.**
> **Mỗi con số AI đưa ra phải có cách kiểm chéo.**
> **AI báo "đã xong" chưa chắc là xong: mở ra xem.**

[Dáng]: Tự thiết kế, 3 câu chốt hiện lần lượt, nền ảnh bung tầng mờ.

[Ghi chú Giảng viên]: Quay lại câu hỏi đầu buổi: từ ảnh tới mô hình mất bao lâu. Kể chuyện thật lúc chuẩn bị: 4 tờ PDF từng in ra trắng trơn dù công cụ báo "đã in", chỉ lộ ra khi mở file xem.

---

## Nguồn dữ liệu kiểm chứng

| Nội dung | Nguồn |
|---|---|
| Subagent: vị trí file, trường khai báo, cách gọi, chạy song song | `code.claude.com/docs/en/sub-agents`, tra ngày 07/10/2026 |
| CLAUDE.md 3 tầng, cộng dồn, dưới 200 dòng, là ngữ cảnh không phải cấu hình bắt buộc | `code.claude.com/docs/en/memory`, tra ngày 07/10/2026 |
| Kiến trúc, cổng 9877, lệnh cài, 30 công cụ, bộ soát `chay_python`, bảng lỗi | README, `docs/cai-dat.md`, `docs/xu-ly-loi.md` repo `andyluu98/vn-mcp-blender`, tra ngày 07/10/2026 |
| 71 tường, 30 cửa, 32 cột, 57 nội thất, 0 cảnh báo, 0,6 giây | Chạy thử trên máy giảng viên ngày 07/10/2026, `demo/07-nha-pho-lo-7x20m/03_mo-ta-tu-ban-ve.json` |
| Thông số nhà 7x20m, cao độ, bảng cửa | `demo/07-nha-pho-lo-7x20m/01_ban-ve-nha-pho-lo-7x20m.dwg`, tờ KT-02 |
| Thời lượng, lịch 150 phút, Lab, D4 | `01_Giao_Trinh_Chi_Tiet_Buoi_04.md`, `03_...Lab...`, `04_...D4...` |
| S1 sửa 2200 thành 2400 đọc lại đúng | Chạy thử ngày 07/10/2026 trên bản chép DXF |
| Lệnh gạch chéo, /plan, /goal, /loop (cú pháp, giới hạn 7 ngày, đơn vị thời gian, Shift+Tab) | `code.claude.com/docs/en/commands`, `/goal`, `/scheduled-tasks`, `/permission-modes`, tra ngày 07/10/2026; phiên bản Claude Code 2.1.291 trên máy giảng viên |
