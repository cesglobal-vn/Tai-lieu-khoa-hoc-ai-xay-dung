# Báo cáo tổng hợp: hồ sơ trình phương án nhà phố lô 7x20m

- **Ngày:** 14/10/2026
- **Khách hàng:** Nguyễn Văn A (tình huống giả định)
- **Đội:** kien-truc (opus), boc-kl (sonnet) chạy song song; kiem-tra (sonnet, chỉ đọc) chạy sau.
- **Kết luận kiểm tra:** CẦN SỬA. Không có lỗi số liệu mức cao; còn 1 điểm mức trung bình và 6 điểm mức thấp (xem `handoff/04_kiem-tra.md`). Chưa sửa vòng nào.

## 1. Phương án kiến trúc (nguồn: `handoff/02_kien-truc.md`, đã kiểm khớp)

| Hạng mục | Nội dung | Nguồn |
|---|---|---|
| Lô đất | 7 x 20 m | JSON `ranh_dat` |
| Khối nhà | 5000 x 14000 mm, áp sát ranh phải; lối đi hông 2000, sân trước 5000, sân sau 1000 | JSON `san`, `san_vuon`; KT-01 |
| Cao độ | Sân -0.450; T1 ±0.000; T2 +3.600; T3 +7.000; sân thượng +10.400; mái tum +13.400 | JSON `cao_do`; KT-02 |
| Tầng 1 | Phòng khách, sảnh, WC, bếp ăn | KT-01 |
| Tầng 2 | Ban công +3.550, phòng ngủ 1, phòng ngủ 2, WC | KT-01 |
| Tầng 3 | Phòng sinh hoạt, WC, phòng thờ | KT-01 |
| Tum, sân thượng | Máy giặt, bồn nước; giàn phơi | KT-02 |
| Cửa | 30 bộ (D1 1, D2 6, D3 1, D4 3, S1 3, S2 8, S3 4, S4 3, S5 1) | Bảng thống kê cửa; JSON `cua` |

## 2. Yêu cầu khách so với phương án

| Mong muốn | Phương án | Đánh giá |
|---|---|---|
| 3 phòng ngủ | 2 phòng ngủ (tầng 2) | **Chưa khớp** |
| Chỗ để 1 ô tô | Sân trước có pergola, ô tô vẽ trên mặt bằng T1 | Khớp |
| Phòng thờ | Có, tầng 3 | Khớp |
| Sân thượng phơi đồ | Có, giàn phơi | Khớp |
| Phong cách Indochine | 4 tờ KT chưa thể hiện; có ảnh phối cảnh `05_phoi-canh-indochine.png` nhưng đội chưa đọc | Cần xác nhận lại |
| Khối lượng phần thô sơ bộ | Có (mục 3) | Khớp |

## 3. Khối lượng phần thô sơ bộ (nguồn: `handoff/03_boc-khoi-luong.md`, giữ nguyên số BOQ, đã kiểm khớp)

| Nhóm | KL thiết kế | ĐVT |
|---|---:|---|
| Bê tông nền tầng 1 | 8.40 | m3 |
| Bê tông cột | 4.16 | m3 |
| Ván khuôn cột | 83.25 | m2 |
| Bê tông sàn, mái BTCT | 19.38 | m3 |
| Ván khuôn sàn, mái BTCT | 160.41 | m2 |
| Cầu thang | 16.60 | m2 |
| Cầu thang | 1.96 | m3 |
| Xây tường dày 200 | 68.59 | m3 |
| Xây tường dày 100 | 10.16 | m3 |
| Xây lan can, chắn mái | 5.52 | m3 |
| Trát tường trong | 561.56 | m2 |
| Trát tường ngoài | 254.48 | m2 |
| Trát trần | 159.27 | m2 |
| Mái tôn | 52.36 | m2 |
| Ngoài nhà | 1.70 | m |
| Ngoài nhà | 70.00 | m2 |

- Hao hụt, đơn giá, thành tiền: [Chờ bổ sung].
- Tài liệu không đề cập: móng, giằng móng, cọc, dầm, lanh tô, thép, bể nước. Đây là khối lượng sơ bộ phần kiến trúc, **chưa đủ để ký hợp đồng**.

## 4. Vấn đề cần xử lý trước khi trình khách

| # | Vấn đề | Mức độ | Ai xử lý |
|---|---|---|---|
| 1 | Thiếu 1 phòng ngủ so với yêu cầu khách | Cao (nội dung phương án) | Kiến trúc sư chủ trì quyết, hỏi khách |
| 2 | Mái M1, M2 vượt ranh phải 150 mm; M4, xà pergola vượt 100 mm. Mái tôn 52.36 m2 đang gồm phần vượt ranh | Trung bình | kien-truc sửa phương án, boc-kl ghi Cần xác nhận lại |
| 3 | Cửa S3 ở tum: cao bệ 1200 + cao 1800 = 3000 mm, lớn hơn tường 2880 mm | Trung bình | kien-truc |
| 4 | Cửa D2 ghi "cửa gỗ" nhưng ghi chú vật liệu nói mọi cửa khung nhôm | Thấp | kien-truc |
| 5 | Số 9 bậc mỗi vế cầu thang: số bậc hay số vạch | Thấp | Cần xác nhận lại |
| 6 | Lỗi trích dẫn nhỏ trong 02, 03 (dòng 2 đến 6 bảng kiểm tra) | Thấp | kien-truc, boc-kl |

## 5. Câu cần hỏi khách

1. Anh chị cần 3 phòng ngủ; phương án hiện có 2. Anh chị muốn đổi phòng sinh hoạt tầng 3 thành phòng ngủ, hay thêm tầng, hay giữ 2 phòng?
2. Phong cách Indochine: anh chị muốn thể hiện ở mặt tiền, nội thất, hay cả hai?
3. Ngân sách dự kiến và thời gian muốn khởi công?

## 6. Thư nháp gửi khách (CHƯA GỬI, chờ kỹ sư duyệt)

> Kính gửi anh Nguyễn Văn A,
>
> Công ty Ces AI gửi anh phương án sơ bộ nhà phố lô 7x20m: nhà 3 tầng và tum, có sân để ô tô, phòng thờ và sân thượng phơi đồ. Hiện phương án có 2 phòng ngủ, chưa đủ 3 phòng như anh mong muốn; chúng tôi xin trao đổi thêm với anh cách bố trí phòng ngủ thứ 3. Kèm theo là khối lượng phần thô sơ bộ để anh tham khảo; đơn giá và phần móng sẽ bổ sung sau khi chốt phương án.
>
> Anh vui lòng cho chúng tôi biết ngân sách dự kiến và thời gian muốn khởi công.
>
> Trân trọng,
> Công ty Ces AI

## Nguồn dữ liệu kiểm chứng

| Nội dung | Nguồn |
|---|---|
| Phương án, cao độ, công năng | `handoff/02_kien-truc.md`; `dau-vao/01_mo-ta-tu-ban-ve.json`; KT-01, KT-02 |
| Khối lượng, số cửa | `handoff/03_boc-khoi-luong.md`; `dau-vao/04_tom-tat-boq-phan-tho.md` mục 1; `dau-vao/03_bang-thong-ke-cua.md` |
| Kết luận kiểm tra | `handoff/04_kiem-tra.md` |
| Yêu cầu khách | `00_yeu-cau-khach-hang.md` |
