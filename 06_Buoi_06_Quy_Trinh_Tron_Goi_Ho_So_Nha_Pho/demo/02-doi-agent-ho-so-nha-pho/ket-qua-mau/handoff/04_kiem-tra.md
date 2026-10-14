# Bàn giao: kiem-tra (agent ky-su-kiem-tra, chỉ đọc)

> Agent kiem-tra không được ghi file. Agent chính chép nguyên văn câu trả lời của kiem-tra vào đây, ngày 14/10/2026.

Kết luận: CẦN SỬA

Mức độ: không có lỗi số liệu nào ở mức cao. Mọi số đã kiểm đều khớp file gốc. Cần sửa vì còn 1 chỗ hở giữa hai file (mức trung bình) và vài chỗ trích dẫn, hiểu ngầm (mức thấp). Cả hai file đều đủ 6 mục theo `.claude/rules/ban-giao.md`. Không có file 01_tiep-nhan.md nên không đòi file này.

## Bảng lỗi

| STT | File | Vị trí | Vấn đề | Mức độ | Giao lại cho agent nào | Đề xuất sửa |
|---:|---|---|---|---|---|---|
| 1 | 03_boc-khoi-luong.md | mục 3.1 dòng 14 (mái tôn 52.36 m2), mục 5 | 02 mục 3.3.A và mục 6.2 báo mái M1, M2 lấn ranh phải 150 mm và nhờ boc-kl lưu ý khi bóc mái. 03 không nhắc. Mái tôn 52.36 m2 lấy theo hình chữ nhật mái M1, M2 trong JSON (mat_bang.MAI.mai, x từ -150 tới 5150), trong khi ranh phải x = 5000. | Trung bình | boc-kl | Thêm vào mục 5 của 03 một dòng "Cần xác nhận lại": 52.36 m2 gồm phần mái vượt ranh phải 150 mm. Nếu thu mái về ranh thì khối lượng đổi. Tương tự, ghi cả M4 và xà pergola vượt ranh 100 mm, nhưng chúng đã loại khỏi phạm vi phần thô. Sửa xong, đề nghị boc-kl tự kiểm lại diện tích mái. |
| 2 | 02_kien-truc.md | mục 2, mục 3.3 dòng 9 | Thư mục dau-vao có `05_phoi-canh-indochine.png`, không nằm trong danh sách đầu vào của phiếu và 02 không đọc. 02 kết luận "Tài liệu không đề cập chi tiết Indochine trên 4 tờ KT" nhưng ảnh phối cảnh phong cách Indochine có sẵn trong đầu vào. | Thấp | kien-truc | Ghi rõ trong mục 2 là chưa đọc file ảnh này, hoặc đọc và đối chiếu với ghi chú vật liệu. Câu "Tài liệu không đề cập" chỉ đúng với 4 tờ KT. |
| 3 | 02_kien-truc.md | mục 3.1 (sân sau 1000 mm; khối nhà 14000) | 02 trích "[KT-01 kích thước 1000]" và "KT-01 kích thước 14000". Bản `.md` của KT-01 không có hai số này làm đường kích thước. Không mở được PDF để xác nhận. Các số vẫn khớp JSON. | Thấp | kien-truc | Chỉ ghi nguồn JSON cho hai số này, hoặc ghi rõ "đọc từ hình PDF" nếu thật sự thấy trên tờ. |
| 4 | 02_kien-truc.md | mục 3.2 dòng 1 | Mô tả "vách có cửa D2 vào phòng thờ" gộp chung với vách WC. Theo JSON T3, WC chiếm x 200 tới 2500; cửa D2 ở x 3700 tới 4600, ngoài đoạn vách WC. Bồn cầu T3 (lưng "S", y 10950 tới 11650) áp sát vách này phía WC nhưng 02 không nhắc. Kết luận "Đạt" vẫn đúng với bàn thờ. | Thấp | kien-truc | Tách rõ vách chung WC (x 200 tới 2500) và cửa D2 (x 3700 tới 4600). Ghi thêm "lưng bồn cầu chung vách phía phòng thờ" để chủ trì quyết. |
| 5 | 03_boc-khoi-luong.md | mục 5 dòng 3 | Ghi ngày bảng cửa ở "dòng 4" của `03_bang-thong-ke-cua.md`; thực tế là dòng 5. | Thấp | boc-kl | Sửa thành dòng 5. |
| 6 | 03_boc-khoi-luong.md | mục 3.2 "Đối chiếu với BOQ" | Viết "tổng bề rộng lỗ 36.000 m" rồi "36 000 mm", dễ đọc nhầm thành 36 nghìn mét. | Thấp | boc-kl | Viết "36.000 m (tức 36 m)" hoặc dùng mm. |
| 7 | 02 mục 3.3.H và 03 mục 5 | cầu thang | Hai file hiểu "9 bậc mỗi vế" khác nhau mà không nêu: 02 coi 9 là số bậc; BOQ giả thiết 17 tính số bậc = số vạch + 1. | Thấp | Agent chính, kèm kien-truc và boc-kl | Ghi "Cần xác nhận lại": số 9 trong JSON (so_bac_moi_ve) là số bậc hay số vạch. |

## Đã kiểm khớp (tóm tắt)

- Cao độ SAN -450, T1 0, T2 3600, T3 7000, ST 10400, TUM 13400 khớp KT-02.
- Lô đất 7000 x 20000 mm, khối nhà 5000 x 14000 mm, mép phải trùng ranh phải.
- Nhận định mái lấn ranh: ĐÚNG. M1, M2 tới x = 5150; M4, xà pergola tới x = 5100; ranh phải x = 5000.
- Phòng ngủ: bản vẽ có 2, khách cần 3.
- Cửa: 30 bộ (D1 1, D2 6, D3 1, D4 3, S1 3, S2 8, S3 4, S4 3, S5 1), khớp bảng cửa, JSON và BOQ. 7 ô cửa trên tường 100 khớp BOQ.
- 16 dòng khối lượng của 03 khớp từng chữ số với BOQ mục 1. Không có đơn giá, hao hụt tự điền.
- Cảnh báo cửa S3 tum (1200 + 1800 = 3000 mm > tường 2880 mm) đúng.

## File đã đọc

`handoff/02_kien-truc.md`, `handoff/03_boc-khoi-luong.md`, `dau-vao/01_mo-ta-tu-ban-ve.json`, `dau-vao/02_ban-ve-a3-kt01-kt04.md`, `dau-vao/03_bang-thong-ke-cua.md`, `dau-vao/04_tom-tat-boq-phan-tho.md`, `00_yeu-cau-khach-hang.md`, `00_phieu-giao-viec.md`, `.claude/agents/ky-su-kiem-tra.md`, `.claude/rules/so-lieu.md`, `.claude/rules/ban-giao.md`.

Chưa đọc: `dau-vao/02_ban-ve-a3-kt01-kt04.pdf` (máy thiếu pdftoppm), `dau-vao/03_bang-thong-ke-cua.xlsx` (dùng bản .md), `dau-vao/05_phoi-canh-indochine.png`.
