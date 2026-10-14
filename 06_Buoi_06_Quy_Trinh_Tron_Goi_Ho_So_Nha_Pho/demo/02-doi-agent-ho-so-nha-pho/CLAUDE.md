# CLAUDE.md: Demo đội agent hồ sơ nhà phố

Dự án mẫu: nhà phố lô 7x20m của khách Nguyễn Văn A (tình huống giả định).

- Đầu vào nằm trong `dau-vao/`. Không sửa file trong `dau-vao/`.
- Đội agent nằm trong `.claude/agents/`. Mỗi agent ghi kết quả vào `handoff/NN_ten.md`.
- Agent chính viết `00_phieu-giao-viec.md` trước khi giao, gộp vào `99_bao-cao-tong-hop.md` sau cùng.
- Quy tắc chi tiết tách ra `.claude/rules/` (số liệu, bàn giao) để file này ngắn.
