# Tóm tắt BOQ phần thô: nhà phố mẫu lô 7x20m

- **Lập:** 11/10/2026 21:57 bằng `boc-khoi-luong.py` (cùng thư mục).
- **Phạm vi:** phần thô (chủ dự án chốt ngày 11/10/2026). Danh mục trong phạm vi: xem mục Giả thiết, dòng 1.
- **Căn cứ:** `01_ban-ve-nha-pho-lo-7x20m.dwg` đang mở trong AutoCAD (DBMOD = 29, có thay đổi chưa lưu), tờ KT-01..KT-04, phương án mẫu ngày 07/10/2026, chưa có lần phát hành. Model space đọc qua COM (chỉ đọc), trùng 100% với `02_ban-ve-nha-pho-lo-7x20m.dxf` theo handle.
- **Khối nhà:** 5.000 x 14.000 m; lô đất 7.000 x 20.000 m (layer RANH-DAT). Diện tích sàn tính theo khối nhà.
- Khối lượng tính trên số đầy đủ, hiển thị 2 chữ số thập phân. Hao hụt, mã hiệu, đơn giá: [Chờ bổ sung].

## 1. Tổng theo nhóm công tác

| Nhóm | KL thiết kế | ĐVT | Nguồn (tờ, layer) |
|---|---:|---|---|
| Bê tông nền tầng 1 | 8.40 | m3 | KT-01 SAN; KT-04 MAT-CAT |
| Bê tông cột | 4.16 | m3 | KT-01, KT-02 COT; bảng cao độ KT-02 |
| Ván khuôn cột | 83.25 | m2 | KT-01, KT-02 COT |
| Bê tông sàn, mái BTCT | 19.38 | m3 | KT-01, KT-02 SAN, SAN-LO, MAI (M3); KT-04 |
| Ván khuôn sàn, mái BTCT | 160.41 | m2 | KT-01, KT-02 SAN, SAN-LO, COT, MAI |
| Cầu thang (m2) | 16.60 | m2 | KT-01 CAU-THANG; KT-04 |
| Cầu thang (m3) | 1.96 | m3 | KT-01 CAU-THANG; KT-04 |
| Xây tường dày 200 | 68.59 | m3 | KT-01, KT-02 TUONG, CUA, KY-HIEU-CUA; BANG-CUA |
| Xây tường dày 100 | 10.16 | m3 | KT-01 TUONG, CUA, KY-HIEU-CUA; BANG-CUA |
| Xây lan can, chắn mái | 5.52 | m3 | KT-01, KT-02 LAN-CAN, BAC-THEM; KT-03, KT-04 |
| Trát tường trong | 561.56 | m2 | KT-01, KT-02 TUONG, COT, CUA |
| Trát tường ngoài | 254.48 | m2 | KT-01, KT-02 TUONG, COT, LAN-CAN; ghi chú vật liệu |
| Thông tin (không cộng) | 155.16 | m2 | KT-01 RANH-DAT, TUONG |
| Trát trần | 159.27 | m2 | KT-01, KT-02 SAN, SAN-LO, MAI, CAU-THANG |
| Mái tôn | 52.36 | m2 | KT-02 MAI; bảng mái |
| Ngoài nhà (m) | 1.70 | m | KT-01 SAN-VUON, RAO |
| Ngoài nhà (m2) | 70.00 | m2 | KT-01 SAN-VUON, RAO |

## 2. Chi tiết các dòng có số

| STT | Công tác | ĐVT | KL thiết kế | Nhãn |
|---:|---|---|---:|---|
| | **PHẦN I: PHẦN NGẦM VÀ MÓNG** | | | |
| 1 | Cọc (ép/khoan), đài cọc | m / m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 2 | Đào đất hố móng, rãnh giằng | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 3 | Bê tông lót móng | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 4 | Bê tông móng, giằng móng | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 5 | Ván khuôn móng, giằng móng | m2 | Tài liệu không đề cập | Tài liệu không đề cập |
| 6 | Cốt thép móng, giằng móng (D ≤ 10 và D > 10) | kg | Tài liệu không đề cập | Tài liệu không đề cập |
| 7 | Cổ cột, tường móng dưới cốt ±0.000 | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 8 | Đắp đất, cát tôn nền tầng 1 | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 9 | Bê tông nền tầng 1 dày 120 (sàn nền trên đất, tách khỏi sàn BTCT các tầng) | m3 | 8.40 | Cần xác nhận lại |
| 10 | Bể phốt, bể nước ngầm | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| | **PHẦN II: KHUNG BÊ TÔNG CỐT THÉP THÂN NHÀ** | | | |
| 11 | Bê tông cột Tầng 1 (10 cột) | m3 | 1.39 |  |
| 12 | Bê tông cột Tầng 2 (10 cột) | m3 | 1.27 |  |
| 13 | Bê tông cột Tầng 3 (8 cột) | m3 | 1.04 |  |
| 14 | Bê tông cột Tum, sân thượng (4 cột) | m3 | 0.46 |  |
| 15 | Ván khuôn cột Tầng 1 (4 mặt) | m2 | 27.84 |  |
| 16 | Ván khuôn cột Tầng 2 (4 mặt) | m2 | 25.41 |  |
| 17 | Ván khuôn cột Tầng 3 (4 mặt) | m2 | 20.79 |  |
| 18 | Ván khuôn cột Tum, sân thượng (4 mặt) | m2 | 9.22 |  |
| 19 | Bê tông sàn tầng 2 (cốt +3.600) | m3 | 7.58 |  |
| 20 | Bê tông sàn tầng 3 (cốt +7.000) | m3 | 6.74 |  |
| 21 | Bê tông sàn sân thượng và sàn tum (cốt +10.400) | m3 | 2.78 |  |
| 22 | Bê tông mái bằng tum M3 (cốt +13.400) | m3 | 2.28 |  |
| 23 | Ván khuôn đáy sàn Tầng 2 | m2 | 62.77 |  |
| 24 | Ván khuôn đáy sàn Tầng 3 | m2 | 55.85 |  |
| 25 | Ván khuôn đáy sàn sân thượng, tum | m2 | 22.94 |  |
| 26 | Ván khuôn đáy mái bằng tum M3 | m2 | 18.84 |  |
| 27 | Bê tông dầm các tầng (dầm khung, dầm phụ, dầm môi) | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 28 | Ván khuôn dầm (đáy + 2 hông) | m2 | Tài liệu không đề cập | Tài liệu không đề cập |
| 29 | Bê tông lanh tô trên lỗ cửa | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 30 | Bê tông chiếu nghỉ cầu thang Tầng 1 lên Tầng 2 | m3 | 0.22 | Cần xác nhận lại |
| 31 | Bê tông chiếu nghỉ cầu thang Tầng 2 lên Tầng 3 | m3 | 0.22 | Cần xác nhận lại |
| 32 | Bê tông chiếu nghỉ cầu thang Tầng 3 lên Tum, sân thượng | m3 | 0.22 | Cần xác nhận lại |
| 33 | Bản thang Tầng 1: diện tích bản xiên (căn cứ ván khuôn đáy, chưa có chiều dày) | m2 | 5.61 | Cần xác nhận lại |
| 34 | Bản thang Tầng 2: diện tích bản xiên (căn cứ ván khuôn đáy, chưa có chiều dày) | m2 | 5.50 | Cần xác nhận lại |
| 35 | Bản thang Tầng 3: diện tích bản xiên (căn cứ ván khuôn đáy, chưa có chiều dày) | m2 | 5.50 | Cần xác nhận lại |
| 36 | Khối bậc thang Tầng 1 (tam giác trên bản xiên) | m3 | 0.44 | Cần xác nhận lại |
| 37 | Khối bậc thang Tầng 2 (tam giác trên bản xiên) | m3 | 0.42 | Cần xác nhận lại |
| 38 | Khối bậc thang Tầng 3 (tam giác trên bản xiên) | m3 | 0.42 | Cần xác nhận lại |
| 39 | Bê tông bản thang | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 40 | Cốt thép khung, sàn, thang: D ≤ 10 | kg | Tài liệu không đề cập | Tài liệu không đề cập |
| 41 | Cốt thép khung, sàn, thang: D > 10 | kg | Tài liệu không đề cập | Tài liệu không đề cập |
| | **PHẦN III: XÂY, TÔ** | | | |
| 42 | Xây tường dày 200 Tầng 1 | m3 | 20.50 |  |
| 43 | Xây tường dày 100 Tầng 1 | m3 | 2.23 |  |
| 44 | Xây tường dày 200 Tầng 2 | m3 | 18.34 |  |
| 45 | Xây tường dày 100 Tầng 2 | m3 | 3.96 |  |
| 46 | Xây tường dày 200 Tầng 3 | m3 | 21.13 |  |
| 47 | Xây tường dày 100 Tầng 3 | m3 | 3.96 |  |
| 48 | Xây tường dày 200 Tum, sân thượng | m3 | 8.62 |  |
| 49 | Xây tường lan can dày 200, cao 1000 (ban công tầng 2, sân thượng) | m3 | 3.20 | Cần xác nhận lại |
| 50 | Xây tường chắn mái tum dày 200, cao 400 | m3 | 1.34 | Cần xác nhận lại |
| 51 | Xây bậc tam cấp (khối đặc từ cốt sân -0.450) | m3 | 0.97 | Cần xác nhận lại |
| 52 | Trát tường, cột trong nhà Tầng 1 | m2 | 150.62 |  |
| 53 | Trát tường, cột trong nhà Tầng 2 | m2 | 171.61 |  |
| 54 | Trát tường, cột trong nhà Tầng 3 | m2 | 185.75 |  |
| 55 | Trát tường, cột trong nhà Tum, sân thượng | m2 | 53.58 |  |
| 56 | Trát tường, cột ngoài nhà tầng 1, tầng 2 (mặt sơn nước) | m2 | 124.41 |  |
| 57 | Trát tường, cột ngoài nhà tầng 3, tum, lan can, tường chắn mái (mặt ốp tấm gỗ nhựa) | m2 | 130.07 | Cần xác nhận lại |
| 58 | Thông tin: mặt tường giáp ranh đất bên phải (không trát, không tính vào tổng) | m2 | 155.16 | Cần xác nhận lại |
| 59 | Trát trần dưới sàn Tầng 2 (trần Tầng 1) | m2 | 55.04 |  |
| 60 | Trát trần dưới sàn Tầng 3 (trần Tầng 2) | m2 | 47.91 |  |
| 61 | Trát trần dưới sàn sân thượng, tum (trần Tầng 3) | m2 | 18.48 |  |
| 62 | Trát trần dưới mái bằng tum M3 | m2 | 15.64 |  |
| 63 | Trát trần cầu thang Tầng 1 (đáy bản thang + đáy chiếu nghỉ) | m2 | 7.47 |  |
| 64 | Trát trần cầu thang Tầng 2 (đáy bản thang + đáy chiếu nghỉ) | m2 | 7.36 |  |
| 65 | Trát trần cầu thang Tầng 3 (đáy bản thang + đáy chiếu nghỉ) | m2 | 7.36 |  |
| 66 | Lợp mái tôn M1 (mái tôn dốc 1 phía), diện tích xiên | m2 | 40.94 | Cần xác nhận lại |
| 67 | Lợp mái tôn M2 (mái tôn che ban công), diện tích xiên | m2 | 11.42 | Cần xác nhận lại |
| 68 | Xà gồ mái tôn M1, M2 | kg | Tài liệu không đề cập | Tài liệu không đề cập |
| 69 | Sênô, máng xối BTCT | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| 70 | Chân bồn nước trên mái tum | m3 | Tài liệu không đề cập | Tài liệu không đề cập |
| | **PHẦN IV: CƠ ĐIỆN (PHẦN ỐNG, HỘP ÂM THÔ)** | | | |
| 71 | Ống luồn dây điện, hộp âm tường | gói | Tài liệu không đề cập | Tài liệu không đề cập |
| 72 | Ống cấp, thoát nước âm sàn, âm tường; ống xối | gói | Tài liệu không đề cập | Tài liệu không đề cập |
| 73 | Tiếp địa chống sét (kim thu sét 6 cái trên mái) | gói | Tài liệu không đề cập | Tài liệu không đề cập |
| | **PHẦN V: NGOÀI NHÀ (TRONG RANH ĐẤT)** | | | |
| 74 | Sân, lối đi bê tông (cốt -0.450): diện tích | m2 | 70.00 | Cần xác nhận lại |
| 75 | Tường rào mặt tiền (đoạn đặc), chiều dài | m | 1.70 | Cần xác nhận lại |
| 76 | Móng tường rào, móng trụ pergola | m3 | Tài liệu không đề cập | Tài liệu không đề cập |

## 3. Tài liệu không đề cập

- Cọc (ép/khoan), đài cọc: Hồ sơ chỉ có KT-01..KT-04, không có tờ móng (KC)
- Đào đất hố móng, rãnh giằng: Không có mặt bằng móng, cốt đáy móng, cốt đất tự nhiên
- Bê tông lót móng: Không có tờ móng
- Bê tông móng, giằng móng: Không có tờ móng
- Ván khuôn móng, giằng móng: Không có tờ móng
- Cốt thép móng, giằng móng (D ≤ 10 và D > 10): Không có bảng thống kê thép
- Cổ cột, tường móng dưới cốt ±0.000: Mặt cắt 1-1 chỉ vẽ từ cốt ±0.000 trở lên
- Đắp đất, cát tôn nền tầng 1: Không có cốt đất tự nhiên; chỉ biết nền ±0.000, sân -0.450
- Bể phốt, bể nước ngầm: Không thể hiện trên mặt bằng tầng 1
- Bê tông dầm các tầng (dầm khung, dầm phụ, dầm môi): Không có layer DAM; mặt cắt 1-1 không vẽ dầm (sàn tựa thẳng lên tường, cột). Tiết diện dầm: [Chờ bổ sung] từ hồ sơ KC
- Ván khuôn dầm (đáy + 2 hông): Không có dầm trên bản vẽ
- Bê tông lanh tô trên lỗ cửa: Không có chi tiết lanh tô. Tham khảo: 30 lỗ cửa, tổng bề rộng lỗ 36.000 m (chưa kể gối)
- Bê tông bản thang: Không có chiều dày bản thang, chi tiết thang
- Cốt thép khung, sàn, thang: D ≤ 10: Không có tờ KC, bảng thống kê cốt thép
- Cốt thép khung, sàn, thang: D > 10: Không có tờ KC, bảng thống kê cốt thép
- Xà gồ mái tôn M1, M2: Bảng thông số chỉ ghi 'mái tôn dày 120 kể xà gồ', không có quy cách xà gồ
- Sênô, máng xối BTCT: Không thể hiện; ống xối PVC thuộc phần cơ điện
- Chân bồn nước trên mái tum: Bảng thông số ghi chân bồn cao 300, không có kích thước, vật liệu
- Ống luồn dây điện, hộp âm tường: Không có tờ DN (điện nước)
- Ống cấp, thoát nước âm sàn, âm tường; ống xối: Không có tờ DN; KT chỉ vẽ vị trí 5 ống xối
- Tiếp địa chống sét (kim thu sét 6 cái trên mái): Chỉ có vị trí kim trên KT-02, không có hệ tiếp địa
- Móng tường rào, móng trụ pergola: Không có chi tiết

## 4. Giả thiết (nhãn SỐ ƯỚC / Cần xác nhận lại)

| # | Hạng mục | Giả thiết | Nhãn | Căn cứ |
|---:|---|---|---|---|
| 1 | Phạm vi phần thô | Gồm: phần ngầm, khung BTCT, xây, trát tường và trần, lợp mái tôn, ống âm cơ điện, sân và rào. Không gồm: cán nền, chống thấm, ốp lát, sơn bả, cửa, cổng, pergola, thiết bị | Cần xác nhận lại | Chủ dự án chốt phạm vi 'phần thô' ngày 11/10/2026; danh mục chi tiết trong phạm vi chưa được liệt kê |
| 2 | Nguồn số liệu | Tọa độ đọc từ DWG đang mở (DBMOD = 29) qua COM, chỉ đọc; Model space trùng DXF 02_ theo handle |  | doc-dwg-dang-mo.py, sheet Nguon |
| 3 | Đơn vị | Bản vẽ mm (INSUNITS = 4); khối lượng m, m2, m3; diễn giải ghi m, dấu chấm thập phân |  | biến hệ thống |
| 4 | Chiều cao tường, cột | Từ mặt sàn tầng tới đáy sàn BTCT tầng trên (cao độ tầng trên - 120) hoặc tới mặt dưới mái |  | Bảng cao độ, bảng thông số KT-02; mặt cắt 1-1 KT-04 |
| 5 | Dầm | Bản vẽ không có dầm; không trừ chiều cao dầm khỏi tường. Khi có hồ sơ KC: tường giảm theo chiều cao dầm, thêm BT dầm | Cần xác nhận lại | Không có layer DAM; mặt cắt 1-1 không vẽ dầm |
| 6 | Mái tôn M1, M2 | Dốc về phía mặt tiền (tiêu đề bảng mái); mặt trên đi qua (mép, đỉnh) ở hai đầu hình chữ nhật mái; mặt dưới thấp hơn 120 (mái tôn dày kể xà gồ) |  | Bảng mái, bảng thông số KT-02; khớp mặt cắt 1-1 |
| 7 | Tường dưới mái dốc M1 (tầng 3) | Tường hồi hai bên tính hình thang theo mặt dưới mái; tường mặt tiền và cột lấy tại tim |  | Khớp mặt đứng bên KT-03 (đỉnh +12.680 tại trục sau mái) |
| 8 | Cột tầng 2 đầu nhà | Cao tới mặt dưới mái M2 tại tim cột (+6.360) |  | Khớp mặt đứng chính KT-03 |
| 9 | Ngưỡng trừ lỗ mở | Chỉ trừ lỗ > 0.5 m2 cho cả xây và trát; S4 600x600 (0.36 m2) không trừ |  | Thông lệ |
| 10 | Lỗ cửa | Tường trên mặt bằng đã cắt tại lỗ cửa; phần tường tại lỗ = dài lỗ x cao tường - diện tích cửa (bảng cửa KT-02). Mỗi lỗ trừ một lần trên đúng đoạn tường chứa nó, cùng chiều dày |  | layer CUA, KY-HIEU-CUA, BANG-CUA |
| 11 | Giao cột | Tường, lan can giao cột: cắt bỏ đoạn trùng cột; cột tính riêng |  | layer TUONG, LAN-CAN, COT |
| 12 | Sàn | Dày 120; diện tích theo khối nhà 5000 x 14000 (không theo ranh đất 7000 x 20000), trừ lỗ thang; cột dừng ở đáy sàn |  | Bảng thông số; mặt cắt 1-1 |
| 13 | Nền tầng 1 | Dải 120 tại ±0.000 trên mặt cắt; tách riêng khỏi sàn BTCT; vật liệu, lớp lót, đầm nền không ghi | Cần xác nhận lại | KT-04 |
| 14 | Mái tum M3 | BTCT dày 120 như sàn | Cần xác nhận lại | Bảng mái ghi 'Mái bằng tum BTCT'; mặt cắt vẽ dày 120 |
| 15 | Lan can ban công, sân thượng | Tường đặc dày 200 cao 1000 | Cần xác nhận lại | Mặt cắt 1-1 tô đặc; vật liệu không ghi |
| 16 | Tường chắn mái tum | Cao 400, dày 200, chạy theo chu vi mái M3 (4 cạnh) | Cần xác nhận lại | Mặt cắt 1-1 và hai mặt đứng; không vẽ trên mặt bằng |
| 17 | Cầu thang | Số bậc mỗi vế = số vạch bậc + 1; cao bậc = nửa chiều cao tầng / số bậc; chiếu nghỉ dày 120 | Cần xác nhận lại | layer CAU-THANG; mặt cắt 1-1 |
| 18 | Trát | Mặt trong/ngoài xác định theo vùng trong nhà từng tầng; mặt giáp tường, cột khác không trát; mặt trên ranh đất phải không trát; chưa tính má cửa, gờ chỉ, mặt trên lan can | Cần xác nhận lại | Tính bằng lấy mẫu 10 mm dọc mặt |
| 19 | Bậc tam cấp | 3 bậc, khối đặc từ cốt sân -0.450 | Cần xác nhận lại | layer BAC-THEM; bảng thông số |
| 20 | Hao hụt | Thư viện 01-thu-vien-chung\04-dinh-muc-tieu-chuan đang trống: hao hụt để [Chờ bổ sung] |  |  |
| 21 | Đơn giá | Không điền; dùng công bố giá Sở Xây dựng TP.HCM đúng tháng/quý anh đưa |  |  |
| 22 | Mã hiệu | Chưa có căn cứ định mức trong thư viện: [Chờ bổ sung] |  |  |

## 5. Cảnh báo

- Bộ hồ sơ chỉ có kiến trúc: không có móng, dầm, thép, bản thang, lanh tô. Tổng bê tông và tường chưa phải số đủ để ký hợp đồng.
- Bản vẽ ghi: 'Phương án kiến trúc mẫu để dựng 3D; kết cấu chưa tính toán, cần kỹ sư duyệt' (layer CHU, KT-02).
- Tường đang tính tới đáy sàn vì không có dầm; khi có hồ sơ KC thì thể tích tường giảm theo chiều cao dầm.
- DWG đang có thay đổi chưa lưu; Model space hiện trùng DXF. Lưu DWG rồi chạy lại `doc-dwg-dang-mo.py` và script nếu có sửa thêm.
- Cửa: S3 Tum, sân thượng: cao bệ 1200 + cao 1800 = 3000 mm > chiều cao tường 2880 mm (đỉnh lỗ +13.400 vượt đáy kết cấu trên +13.280); chỉ trừ phần lỗ nằm trong tường; Cần xác nhận lại

## 6. Kiểm tra

| Hạng mục | Kết quả | Chi tiết |
|---|---|---|
| Đối chiếu DWG đang mở với DXF theo handle | Khớp | DWG 1337 đối tượng Model, DXF 1337; lệch: [] |
| Chồng lấn tường, cột trên mặt bằng | Không có | Đoạn tường, lan can giao cột đã cắt bỏ phần cột: 2 chỗ; cặp chồng: [] |
| Chiều dày sàn trên mặt cắt 1-1 (KT-04) | Khớp | 7 dải sàn dày 120 mm (layer MAT-CAT) so với bảng thông số 120 |
| Mặt dưới mái M1: bảng mái + thông số so với mặt cắt 1-1 | Khớp | Tính: 9880 / 12680 mm; mặt cắt: 9880 / 12680 mm (handle 2084A) |
| Mặt dưới mái M2: bảng mái + thông số so với mặt cắt 1-1 | Khớp | Tính: 6080 / 6880 mm; mặt cắt: 6080 / 6880 mm (handle 2084C) |
| Đỉnh cột T2 đầu nhà (đỡ mái M2) so với mặt đứng chính KT-03 | Khớp | Tính 6360 mm; mặt đứng 6360 mm |
| Tường hồi T3 dưới mái M1: đỉnh cao nhất so với mặt đứng bên KT-03 | Khớp | Tính 12680 mm; mặt đứng 12680 mm (handle 207AB) |
| Tường chắn mái tum trên mặt cắt 1-1 | Có thể hiện | 2 đoạn cao 400, dày 200, 200 mm; không vẽ trên mặt bằng KT-02, chiều dài lấy theo chu vi mái M3 |
| Đối chiếu 03_mo-ta-tu-ban-ve.json (tường, cột, lan can, sàn, lỗ sàn, cửa, cao độ) | Khớp | Toàn bộ hình chữ nhật trùng tọa độ |
| Số đoạn tường (TUONG), cột (COT), lỗ cửa (CUA) trên mặt bằng | Đã đếm | TUONG 71 polyline; COT 32; CUA 30 hcn, 30 lỗ khớp 30 ký hiệu |
| Tường xây (200 + 100, không kể lan can) / m2 sàn | 0.355 m3/m2 | 78.746 m3 / 222.000 m2 (sàn T1, T2, T3 + mái tum) |
| Bê tông cột + sàn + mái tum + chiếu nghỉ / m2 sàn | 0.109 m3/m2 | 24.217 m3 / 222.000 m2. Thấp vì chưa có dầm, móng, bản thang (Tài liệu không đề cập) |
| Hàm lượng thép khung (20 đến 45 kg/m2 sàn), móng (50 đến 100 kg/m3) | Không kiểm được | Không có bảng thống kê thép |

**Đối chiếu cửa (đếm trên mặt bằng, bảng KT-02, file 14_):**

| Mã | Rộng x cao (mm) | Theo tầng | Đếm | KT-02 | 14_ | Kết quả |
|---|---|---|---:|---:|---:|---|
| D1 | 3600 x 2800 | T1: 1 | 1 | 1 | 1 | Khớp |
| D2 | 900 x 2200 | T1: 1, T2: 2, T3: 2, MAI: 1 | 6 | 6 | 6 | Khớp |
| D3 | 2400 x 2600 | T2: 1 | 1 | 1 | 1 | Khớp |
| D4 | 800 x 2100 | T1: 1, T2: 1, T3: 1 | 3 | 3 | 3 | Khớp |
| S1 | 1600 x 2200 | T1: 1, T2: 1, T3: 1 | 3 | 3 | 3 | Khớp |
| S2 | 1200 x 1400 | T1: 2, T2: 3, T3: 3 | 8 | 8 | 8 | Khớp |
| S3 | 600 x 1800 | T1: 1, T2: 1, T3: 1, MAI: 1 | 4 | 4 | 4 | Khớp |
| S4 | 600 x 600 | T1: 1, T2: 1, T3: 1 | 3 | 3 | 3 | Khớp |
| S5 | 3600 x 1800 | T3: 1 | 1 | 1 | 1 | Khớp |

## 7. So với đáp án cũ (buổi 05, chỉ để đối chiếu lỗi)

| Nhóm | Đáp án cũ | Bản này | Chênh | Lý do chính |
|---|---:|---:|---:|---|
| Tường xây (m3) | 65.93 (chỉ tường 200) | 78.75 (200 + 100) | +12.81 | Thêm tường 100 (10.16 m3) và 7 lỗ cửa trên tường mỏng; tường hồi T3 dưới mái M1 tính hình thang; lan can, chắn mái tách dòng riêng |
| Bê tông sàn + mái tum (m3) | 27.78 (gộp nền T1) | 19.38 | -8.40 | Tách nền T1 (8.40 m3) ra Phần I |
| Bê tông cột (m3) | 4.23 | 4.16 | -0.07 | Cột T2 đầu nhà tới mặt dưới mái M2 (2.760 m), cột T3 mặt tiền tới mặt dưới mái M1 (3.152 m); bản cũ lấy 3.400 m |

Đáp án cũ cộng tay từ các dòng chi tiết của file cũ (ô tổng không có giá trị cache).

## 8. Nguồn dữ liệu kiểm chứng

| Loại | File / layer | Tờ | Ghi chú |
|---|---|---|---|
| DWG (nguồn chính) | `F:\GitHub\Tai-lieu-khoa-hoc-ai-xay-dung\04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m\01_ban-ve-nha-pho-lo-7x20m.dwg` | KT-01..KT-04 (Model) | Đang mở trong AutoCAD, DBMOD = 29; đọc qua COM, chỉ đọc |
| Ảnh chụp dữ liệu DWG | `F:\GitHub\Tai-lieu-khoa-hoc-ai-xay-dung\04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m\17-boc-khoi-luong-phan-tho\03_du-lieu-doc-tu-dwg-dang-mo.json` |  | 2026-10-11 21:43:37 |
| DXF (đối chiếu) | `F:\GitHub\Tai-lieu-khoa-hoc-ai-xay-dung\04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m\02_ban-ve-nha-pho-lo-7x20m.dxf` |  | So theo handle |
| JSON mô tả (đối chiếu) | `F:\GitHub\Tai-lieu-khoa-hoc-ai-xay-dung\04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m\03_mo-ta-tu-ban-ve.json` |  | Các trường: cao_do, cua, mat_bang.*.tuong/cot/lan_can/san/lo_san/cua |
| Bảng thống kê cửa (đối chiếu) | `F:\GitHub\Tai-lieu-khoa-hoc-ai-xay-dung\04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m\14_bang-thong-ke-cua-nha-7x20m.xlsx` |  | Sheet 'Thong ke cua' |
| PDF A3 | `F:\GitHub\Tai-lieu-khoa-hoc-ai-xay-dung\04_Buoi_04_Agent_ClaudeMD_Blender_3D\demo\07-nha-pho-lo-7x20m\08_ban-ve-a3-kt01-kt04.pdf` | KT-01 MB tầng 1, 2, 3; KT-02 MB mái, tum + các bảng; KT-03 mặt đứng; KT-04 mặt cắt 1-1 | Dùng để xác định mã tờ |
| Mặt cắt 1-1 (KT-04) | `layer MAT-CAT, MAT-DUNG` |  | Quy đổi: x_mc = 45000 + y_mb; z = y_mc + 25000 |
| Mặt đứng (KT-03) | `layer MAT-DUNG` |  | Mặt đứng chính x = x_mb; mặt đứng bên x = 26000 - y_mb |

Đề nghị chạy agent `kiem-tra-khoi-luong` trên file này và `boc-khoi-luong.py` trước khi gửi khách.
