# Prompt chạy đội agent (demo trong lớp, khoảng 10 phút)

Mở thư mục `02-doi-agent-ho-so-nha-pho` trong Claude Code, mở **cuộc trò chuyện mới** (để Claude nhận 4 agent), rồi dán:

```
Lập đội agent cho hồ sơ trình khách nhà phố trong thư mục này.

0. Khách gửi yêu cầu bằng file Word 00_yeu-cau-khach-hang.docx: chuyển sang .md bằng
   markitdown trước (đã có .md trùng tên thì sao lưu bản cũ vào _backup).
1. Viết 00_phieu-giao-viec.md trước: mục tiêu, đầu vào, ai làm gì, ai chờ ai.
2. Chạy song song 3 agent, đặt tên để chúng nhắn được cho nhau, mỗi agent chỉ ghi file của mình:
   - "tiep-nhan" dùng agent tiep-nhan-yeu-cau -> handoff/01_tiep-nhan.md
   - "kien-truc" dùng agent kien-truc-su -> handoff/02_kien-truc.md
   - "khoi-luong" dùng agent ky-su-boc-khoi-luong -> handoff/03_boc-khoi-luong.md
3. Ba agent xong mới chạy "kiem-tra" dùng agent ky-su-kiem-tra. Ghi kết luận của kiem-tra
   vào handoff/04_kiem-tra.md.
4. Kiểm tra kết luận CẦN SỬA thì giao lại đúng agent đã làm, tối đa 1 vòng.
5. Gộp vào 99_bao-cao-tong-hop.md: tóm tắt phương án, bảng yêu cầu khách khớp/chưa khớp,
   khối lượng sơ bộ, câu hỏi cần hỏi khách, và một thư nháp gửi khách (chưa gửi).
```

## Điều giảng viên chỉ cho lớp xem trong lúc đội chạy

- 3 agent chạy cùng lúc, agent kiểm tra đứng chờ.
- Thư mục `handoff/` có file mới lần lượt.
- Agent tiếp nhận phát hiện: khách muốn **3 phòng ngủ**, bản vẽ có **2 phòng ngủ** (tầng 2). Đây là lý do cần bước tiếp nhận trước khi trình khách.
- Agent kiểm tra chỉ đọc: thử bảo nó sửa file, nó sẽ từ chối.

## Cấu trúc thư mục

```
02-doi-agent-ho-so-nha-pho\
├── CLAUDE.md                      ngắn, chỉ nói dự án là gì, file ở đâu
├── .claude\
│   ├── rules\so-lieu.md           luật số liệu, luôn nạp
│   ├── rules\ban-giao.md          mẫu bàn giao, chỉ nạp khi làm với handoff/
│   └── agents\                    4 agent: tiep-nhan-yeu-cau, kien-truc-su, ky-su-boc-khoi-luong, ky-su-kiem-tra
├── 00_yeu-cau-khach-hang.docx     khách gửi bằng Word (tình huống mẫu)
├── 00_yeu-cau-khach-hang.md       bản chuyển bằng markitdown
├── 01_prompt-chay-doi.md          file này
├── dau-vao\                       bản vẽ (PDF, MD), file mô tả JSON, bảng cửa, BOQ tóm tắt, ảnh phối cảnh
└── ket-qua-mau\                   kết quả một lần chạy thật (14/10/2026) để đối chiếu; đội không đọc thư mục này
```

Kết quả mẫu: `ket-qua-mau\` có phiếu giao việc, 3 file bàn giao và báo cáo tổng hợp của lần chạy với 3 agent kien-truc, boc-kl, kiem-tra. Chạy xong, so kết quả của mình với thư mục này.

```
```
