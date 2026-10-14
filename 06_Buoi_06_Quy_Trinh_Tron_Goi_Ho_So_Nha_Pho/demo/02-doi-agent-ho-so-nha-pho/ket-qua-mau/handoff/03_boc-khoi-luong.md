# Bàn giao 03: Bảng khối lượng phần thô sơ bộ

- **Agent:** ky-su-boc-khoi-luong (sonnet, high)
- **Ngày lập:** 14/10/2026
- **Công trình:** nhà phố lô 7x20m, khách Nguyễn Văn A (tình huống giả định)

## 1. Việc được giao

Theo `00_phieu-giao-viec.md` (dòng phân công boc-kl):
1. Lập bảng khối lượng phần thô sơ bộ để trình khách, giữ nguyên số của BOQ.
2. Đếm tổng số bộ cửa theo bảng thống kê cửa, so với file mô tả bản vẽ.
3. Soát BOQ theo các bẫy bóc khối lượng hay gặp.
4. Hao hụt, đơn giá, thành tiền: để [Chờ bổ sung].

## 2. Đầu vào đã đọc

| File | Dùng để |
|---|---|
| `dau-vao/04_tom-tat-boq-phan-tho.md` | Nguồn số khối lượng, giả thiết, danh mục "Tài liệu không đề cập" |
| `dau-vao/03_bang-thong-ke-cua.md` (bản đọc của `.xlsx` cùng tên) | Đếm bộ cửa |
| `dau-vao/01_mo-ta-tu-ban-ve.json` (đơn vị mm, trường `don_vi`) | Đối chiếu số lượng cửa, cao độ, tường, mái |
| `00_phieu-giao-viec.md`, `CLAUDE.md`, `.claude/rules/so-lieu.md`, `.claude/rules/ban-giao.md` | Quy tắc làm việc |

Không đọc: `02_ban-ve-a3-kt01-kt04` (không nằm trong danh sách đầu vào được giao cho việc này).

## 3. Kết quả

### 3.1. Bảng khối lượng phần thô sơ bộ

Số lấy nguyên từ `04_tom-tat-boq-phan-tho.md`, mục 1 (bảng tổng theo nhóm), hiển thị 2 chữ số thập phân. Cột "Nhãn" lấy từ các dòng chi tiết cùng nhóm ở mục 2 của BOQ. Hao hụt, đơn giá, thành tiền chưa có nguồn nên để [Chờ bổ sung].

| STT | Nhóm công tác | KL thiết kế | ĐVT | Hao hụt | Đơn giá | Thành tiền | Nguồn (BOQ mục 1; tờ, layer) | Nhãn |
|---:|---|---:|---|---|---|---|---|---|
| 1 | Bê tông nền tầng 1 (dày 120, tách khỏi sàn BTCT) | 8.40 | m3 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 13; KT-01 SAN; KT-04 MAT-CAT; chi tiết STT 9 | Cần xác nhận lại |
| 2 | Bê tông cột | 4.16 | m3 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 14; KT-01, KT-02 COT; bảng cao độ KT-02; STT 11 đến 14 | |
| 3 | Ván khuôn cột | 83.25 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 15; KT-01, KT-02 COT; STT 15 đến 18 | |
| 4 | Bê tông sàn, mái BTCT | 19.38 | m3 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 16; KT-01, KT-02 SAN, SAN-LO, MAI (M3); KT-04; STT 19 đến 22 | M3 dày 120: Cần xác nhận lại (Giả thiết 14) |
| 5 | Ván khuôn sàn, mái BTCT | 160.41 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 17; KT-01, KT-02 SAN, SAN-LO, COT, MAI; STT 23 đến 26 | |
| 6 | Cầu thang (diện tích bản xiên) | 16.60 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 18; KT-01 CAU-THANG; KT-04; STT 33 đến 35 | Cần xác nhận lại |
| 7 | Cầu thang (chiếu nghỉ, khối bậc) | 1.96 | m3 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 19; KT-01 CAU-THANG; KT-04; STT 30 đến 32, 36 đến 38 | Cần xác nhận lại |
| 8 | Xây tường dày 200 | 68.59 | m3 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 20; KT-01, KT-02 TUONG, CUA, KY-HIEU-CUA; BANG-CUA; STT 42, 44, 46, 48 | |
| 9 | Xây tường dày 100 | 10.16 | m3 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 21; KT-01 TUONG, CUA, KY-HIEU-CUA; BANG-CUA; STT 43, 45, 47 | |
| 10 | Xây lan can, chắn mái (kèm bậc tam cấp, xem mục 5) | 5.52 | m3 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 22; KT-01, KT-02 LAN-CAN, BAC-THEM; KT-03, KT-04; STT 49 đến 51 | Cần xác nhận lại |
| 11 | Trát tường trong | 561.56 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 23; KT-01, KT-02 TUONG, COT, CUA; STT 52 đến 55 | Cần xác nhận lại (Giả thiết 18: chưa tính má cửa, gờ chỉ) |
| 12 | Trát tường ngoài | 254.48 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 24; KT-01, KT-02 TUONG, COT, LAN-CAN; ghi chú vật liệu; STT 56, 57 | Cần xác nhận lại (STT 57) |
| 13 | Trát trần | 159.27 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 26; KT-01, KT-02 SAN, SAN-LO, MAI, CAU-THANG; STT 59 đến 65 | |
| 14 | Mái tôn (diện tích xiên M1 + M2) | 52.36 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 27; KT-02 MAI; bảng mái; STT 66, 67 | Cần xác nhận lại |
| 15 | Ngoài nhà: tường rào mặt tiền (đoạn đặc) | 1.70 | m | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 28; KT-01 SAN-VUON, RAO; STT 75 | Cần xác nhận lại |
| 16 | Ngoài nhà: sân, lối đi bê tông (cốt -0.450) | 70.00 | m2 | [Chờ bổ sung] | [Chờ bổ sung] | [Chờ bổ sung] | dòng 29; KT-01 SAN-VUON, RAO; STT 74 | Cần xác nhận lại |

Dòng thông tin, **không cộng vào tổng**: mặt tường giáp ranh đất bên phải, không trát, 155.16 m2 (BOQ mục 1 dòng 25; mục 2 STT 58; KT-01 RANH-DAT, TUONG), Cần xác nhận lại.

Mọi dòng trong bảng này mới là khối lượng thiết kế phần kiến trúc. Hồ sơ chưa có móng, dầm, thép, bản thang, lanh tô (xem 3.4), nên tổng bê tông và tường chưa phải số đủ để ký hợp đồng (BOQ mục 5, cảnh báo 1).

### 3.2. Số bộ cửa

Đếm từ `dau-vao/03_bang-thong-ke-cua.md` cột "Số lượng" (dòng 8 đến 16) và đối chiếu `dau-vao/01_mo-ta-tu-ban-ve.json` (trường `cua.*.so_luong` và các mục `mat_bang.*.cua`, đếm từng ô cửa).

| Mã | Rộng x cao (mm) | Cao bệ (mm) | Bảng thống kê | JSON `so_luong` | JSON đếm trên mặt bằng (T1 / T2 / T3 / MAI) | Kết quả |
|---|---|---:|---:|---:|---|---|
| D1 | 3600 x 2800 | 0 | 1 | 1 | 1 / 0 / 0 / 0 = 1 | Khớp |
| D2 | 900 x 2200 | 0 | 6 | 6 | 1 / 2 / 2 / 1 = 6 | Khớp |
| D3 | 2400 x 2600 | 0 | 1 | 1 | 0 / 1 / 0 / 0 = 1 | Khớp |
| D4 | 800 x 2100 | 0 | 3 | 3 | 1 / 1 / 1 / 0 = 3 | Khớp |
| S1 | 1600 x 2200 | 400 | 3 | 3 | 1 / 1 / 1 / 0 = 3 | Khớp |
| S2 | 1200 x 1400 | 900 | 8 | 8 | 2 / 3 / 3 / 0 = 8 | Khớp |
| S3 | 600 x 1800 | 1200 | 4 | 4 | 1 / 1 / 1 / 1 = 4 | Khớp |
| S4 | 600 x 600 | 1500 | 3 | 3 | 1 / 1 / 1 / 0 = 3 | Khớp |
| S5 | 3600 x 1800 | 600 | 1 | 1 | 0 / 0 / 1 / 0 = 1 | Khớp |
| **Tổng** | | | **30** | **30** | T1 8, T2 10, T3 10, MAI 2 = **30** | **Khớp** |

- Kích thước, cao bệ trong bảng thống kê và JSON giống nhau ở cả 9 mã.
- Ô "Tổng" trong file bảng thống kê (`03_bang-thong-ke-cua.md`, dòng 17) để trống, nên 30 là tổng em cộng cột "Số lượng", không phải số có sẵn trong file.
- Đối chiếu với BOQ: mục "Tài liệu không đề cập" ghi 30 lỗ cửa, tổng bề rộng lỗ 36.000 m (BOQ mục 3, dòng lanh tô). Cộng bề rộng x số lượng từ bảng thống kê cũng ra 36 000 mm. Mục 6 BOQ cũng có bảng đối chiếu cửa cùng số lượng (D1..S5 đều Khớp).
- Số ô cửa nằm trên tường 100 theo JSON: D4 ở T1, T2, T3 (3 ô, dày 100 theo tọa độ) + D2 ở T2 và T3 (4 ô, y 8050 đến 8150 và 11650 đến 11750) = 7 ô; khớp con số "7 lỗ cửa trên tường mỏng" ghi ở BOQ mục 7.

Kết luận: số cửa không lệch giữa bảng thống kê, file mô tả JSON và BOQ.

### 3.3. Bảng soát bẫy bóc khối lượng

Em không tính lại khối lượng. Cột "Căn cứ" là chỗ BOQ tự khai hoặc em đếm được trong đầu vào. Dòng nào chưa kiểm được độc lập thì nói rõ.

| # | Bẫy | Kết quả | Căn cứ |
|---:|---|---|---|
| 1 | Tách tường 200 và tường 100 | Đạt | Hai nhóm riêng 68.59 m3 và 10.16 m3 (BOQ mục 1 dòng 20, 21); chi tiết STT 42 đến 48. Tum, sân thượng chỉ có dòng tường 200 (STT 48). |
| 2 | Cửa trên tường mỏng có được trừ | Đạt theo khai báo, chưa kiểm độc lập | BOQ mục 7 ghi thêm "7 lỗ cửa trên tường mỏng"; em đếm trong JSON đúng 7 ô (mục 3.2). BOQ Giả thiết 10 nêu trừ theo đoạn tường chứa lỗ, cùng chiều dày. Số m3 thực trừ không có trong BOQ nên không kiểm được. Đề nghị chạy lại script. |
| 3 | Mỗi lỗ cửa chỉ trừ một lần | Đạt theo khai báo, chưa kiểm độc lập | BOQ Giả thiết 10 "Mỗi lỗ trừ một lần"; BOQ mục 6: 30 hcn CUA, 30 lỗ khớp 30 ký hiệu, không chồng lấn tường, cột. Em đếm 30 ô cửa (mục 3.2). |
| 4 | Ngưỡng trừ lỗ | Chưa chắc | BOQ Giả thiết 9: chỉ trừ lỗ lớn hơn 0.5 m2, S4 (0.36 m2) không trừ, nguồn ghi "Thông lệ", không có định mức trong tài liệu. Cần xác nhận lại. |
| 5 | Tường dưới mái dốc, tường thu hồi (hình thang, tam giác) | Đạt theo khai báo | BOQ Giả thiết 7: tường hồi T3 dưới mái M1 tính hình thang; BOQ mục 6: đỉnh 12 680 mm khớp mặt đứng bên KT-03. Cột T2 đầu nhà tới mặt dưới mái M2 (Giả thiết 8). Tường chắn mái tum 400 tính riêng (STT 50). |
| 6 | Sàn nền tầng 1 tách khỏi sàn BTCT các tầng | Đạt | Nền T1 8.40 m3 ở Phần I (STT 9), sàn BTCT tầng 2, 3, thượng, tum ở Phần II (STT 19 đến 22). BOQ mục 7 nói rõ đã tách 8.40 m3. Vật liệu, lớp lót, đầm nền chưa ghi: Cần xác nhận lại (Giả thiết 13). |
| 7 | Dầm, tường tính tới đáy sàn | Chưa đạt, đã cảnh báo | Không có layer DAM, nên tường tính tới đáy sàn; khi có hồ sơ KC thì tường giảm theo chiều cao dầm và thêm bê tông dầm (BOQ Giả thiết 5; mục 5, cảnh báo 3). |
| 8 | Chồng lấn tường với cột | Đạt theo khai báo | BOQ Giả thiết 11 và mục 6: "Không có" chồng lấn, 2 chỗ tường, lan can giao cột đã cắt phần cột. |

### 3.4. Hạng mục hay sót

| Hạng mục | Tình trạng trong BOQ | Nguồn |
|---|---|---|
| Cọc, đài cọc | Tài liệu không đề cập | BOQ mục 2 STT 1; mục 3 |
| Móng, giằng móng (bê tông, ván khuôn, thép, lót) | Tài liệu không đề cập | STT 3 đến 6; mục 3 |
| Cổ cột, tường móng dưới ±0.000 | Tài liệu không đề cập | STT 7 |
| Dầm các tầng (bê tông, ván khuôn) | Tài liệu không đề cập | STT 27, 28 |
| Lanh tô | Tài liệu không đề cập (BOQ ghi tham khảo: 30 lỗ cửa, tổng bề rộng lỗ 36.000 m, chưa kể gối) | STT 29; mục 3 |
| Lan can | Có: 3.20 m3 (ban công T2, sân thượng, dày 200, cao 1000), Cần xác nhận lại | STT 49 |
| Tường chắn mái tum | Có: 1.34 m3 (dày 200, cao 400), Cần xác nhận lại | STT 50 |
| Bậc tam cấp | Có: 0.97 m3 (3 bậc, khối đặc từ cốt -0.450), Cần xác nhận lại | STT 51 |
| Bể phốt, bể nước ngầm | Tài liệu không đề cập | STT 10 |
| Chân bồn nước mái tum | Tài liệu không đề cập (bảng thông số chỉ ghi chân bồn cao 300) | STT 70; JSON `thong_so` |
| Tường rào | Có phần đặc mặt tiền: 1.70 m, Cần xác nhận lại. Móng tường rào, móng trụ pergola: Tài liệu không đề cập | STT 75, 76 |
| Cốt thép khung, sàn, thang (D ≤ 10 và D > 10) | Tài liệu không đề cập | STT 40, 41 |
| Bê tông bản thang (theo chiều dày) | Tài liệu không đề cập; chỉ có diện tích bản xiên | STT 33 đến 35, 39 |
| Đào, đắp đất, cát tôn nền | Tài liệu không đề cập | STT 2, 8 |
| Xà gồ mái tôn | Tài liệu không đề cập | STT 68 |
| Sênô, máng xối BTCT | Tài liệu không đề cập | STT 69 |
| Cơ điện phần ống âm (điện, nước, tiếp địa) | Tài liệu không đề cập | STT 71 đến 73 |

### 3.5. Đối chiếu phép cộng số hiển thị (BOQ mục 1 và mục 2)

Đây chỉ là cộng các số hiển thị 2 chữ số của chính BOQ để xem dòng nhóm có khớp dòng chi tiết không, không phải tính lại khối lượng từ bản vẽ.

| Nhóm | Dòng nhóm | Cộng các dòng chi tiết đã hiển thị | Lệch |
|---|---:|---:|---:|
| Bê tông cột (m3) | 4.16 | 4.16 | 0.00 |
| Bê tông sàn, mái (m3) | 19.38 | 19.38 | 0.00 |
| Tường 200 (m3) | 68.59 | 68.59 | 0.00 |
| Trát tường trong (m2) | 561.56 | 561.56 | 0.00 |
| Trát tường ngoài (m2) | 254.48 | 254.48 | 0.00 |
| Mái tôn (m2) | 52.36 | 52.36 | 0.00 |
| Tường 100 (m3) | 10.16 | 10.15 | 0.01 |
| Ván khuôn cột (m2) | 83.25 | 83.26 | 0.01 |
| Ván khuôn sàn, mái (m2) | 160.41 | 160.40 | 0.01 |
| Cầu thang diện tích (m2) | 16.60 | 16.61 | 0.01 |
| Trát trần (m2) | 159.27 | 159.26 | 0.01 |
| Lan can, chắn mái, bậc tam cấp (m3), cộng STT 49 đến 51 | 5.52 | 5.51 | 0.01 |
| Cầu thang khối (m3), cộng STT 30 đến 32 và 36 đến 38 | 1.96 | 1.94 | 0.02 |

Mọi chênh lệch này nhỏ hơn tổng biên làm tròn của các số hạng đã hiển thị (mỗi số hạng làm tròn tối đa 0.005), phù hợp với việc BOQ tính trên số đầy đủ rồi mới làm tròn. Không coi là lỗi, nhưng nên lưu ý khi khách tự cộng tay.

## 4. Giả định đã dùng

1. Lấy nguyên số của `04_tom-tat-boq-phan-tho.md` làm khối lượng thiết kế; không tự đo, không tự tính lại.
2. Nhóm công tác ở bảng 3.1 là nhóm của BOQ mục 1; em chỉ đánh lại STT cho bảng khách (không trùng STT BOQ mục 2) và bỏ qua dòng "Thông tin (không cộng)" khi tính tổng.
3. Hao hụt, đơn giá, thành tiền, mã hiệu: [Chờ bổ sung]. Thư viện `04-dinh-muc-tieu-chuan` trống và chưa có công bố giá Sở Xây dựng TP.HCM đúng kỳ (theo BOQ Giả thiết 20 đến 22).
4. Số cửa 30 là tổng em cộng cột "Số lượng" của bảng thống kê; kích thước đọc theo mm.
5. Mọi giả thiết kỹ thuật (chiều cao tường, ngưỡng trừ lỗ, tường dưới mái, cầu thang, trát...) là của BOQ mục 4; em chỉ chuyển nhãn "Cần xác nhận lại" lên bảng 3.1, không thêm giả thiết mới.

## 5. Chỗ chưa chắc (Cần xác nhận lại)

1. **Phạm vi "phần thô":** chủ dự án chốt ngày 11/10/2026 nhưng danh mục chi tiết trong phạm vi chưa liệt kê (BOQ Giả thiết 1). Pergola M4 và cổng có trong JSON (`mai.M4`, `mat_bang.T1.cong`) nhưng bị loại khỏi phạm vi; cần khách, anh Tuấn Anh xác nhận.
2. **Nguồn BOQ không phải file trong `dau-vao/`:** BOQ căn cứ DWG đang mở trong AutoCAD (DBMOD = 29, có thay đổi chưa lưu), DXF, và hai file ghi tên `03_mo-ta-tu-ban-ve.json`, `14_bang-thong-ke-cua-nha-7x20m.xlsx`; các file này không có tên trùng trong `dau-vao/` (ở đây là `01_mo-ta-tu-ban-ve.json`, `03_bang-thong-ke-cua.xlsx`). BOQ mục 6 ghi JSON và bảng cửa khớp bản vẽ. Em chỉ kiểm được phần cửa (mục 3.2) giữa các file trong `dau-vao/`. Đề nghị lưu DWG và chạy lại `boc-khoi-luong.py` rồi so lại.
3. **Mốc ngày khác nhau:** bảng thống kê cửa ghi đọc từ DXF ngày 07/10/2026 (`03_bang-thong-ke-cua.md`, dòng 4); BOQ lập 11/10/2026 21:57; phương án mẫu ngày 07/10/2026, chưa có lần phát hành (BOQ phần đầu). Chưa thấy lệch số, nhưng nên chốt lại phiên bản bản vẽ.
4. **Cửa S3 Tum, sân thượng:** cao bệ 1200 + cao 1800 = 3000 mm, lớn hơn chiều cao tường 2880 mm; BOQ chỉ trừ phần lỗ nằm trong tường (BOQ mục 5, cảnh báo 5; JSON `cua.S3`). Cần xác nhận lại kích thước cửa hoặc cao độ.
5. **Bản thang:** chỉ có diện tích bản xiên, chưa có chiều dày; khối bậc tính theo giả thiết số bậc (BOQ Giả thiết 17). Khối lượng cầu thang 1.96 m3 chưa phải bê tông bản thang.
6. **Nền tầng 1:** vật liệu, lớp lót, đầm nền không ghi (Giả thiết 13). **Mái tum M3 dày 120** lấy như sàn (Giả thiết 14).
7. **Nhóm "Xây lan can, chắn mái" 5.52 m3** có nguồn layer BAC-THEM, tức khả năng gồm cả bậc tam cấp 0.97 m3 (STT 51); BOQ không nói rõ tên nhóm gồm những gì. Cần xác nhận lại trước khi gửi khách, hoặc tách bậc tam cấp thành dòng riêng.
8. **Ngưỡng trừ lỗ 0.5 m2** chỉ dựa "thông lệ" (xem 3.3, mục 4).
9. **Trát:** chưa tính má cửa, gờ chỉ, mặt trên lan can (Giả thiết 18). Mặt tường giáp ranh đất 155.16 m2 được coi là không trát.
10. **Các điểm này em không kiểm lại được vì không tự tính lại:** khối lượng tường sau khi trừ lỗ cửa, tường hình thang dưới mái, trát. Chỉ có thể tin BOQ hoặc chạy lại script.

## 6. Việc người sau cần làm

**Agent ky-su-kiem-tra:**
1. Soát chéo mục 3.1 với `04_tom-tat-boq-phan-tho.md` mục 1 và 2 (đúng số, đúng đơn vị, đúng nguồn).
2. Soát số cửa 30 (mục 3.2) với `03_bang-thong-ke-cua.md` và `01_mo-ta-tu-ban-ve.json`.
3. Soát các nhãn "Tài liệu không đề cập" ở mục 3.4 với BOQ mục 3.
4. Kiểm file `kien-truc` (`handoff/02_kien-truc.md`): các số về cao độ, số cửa, mái có khớp bảng này không; lệch thì ghi "Cần xác nhận lại", không tự chọn bên.

**Anh Tuấn Anh / agent chính:**
1. Lưu DWG, chạy lại `boc-khoi-luong.py` và `doc-dwg-dang-mo.py` để chốt số trước khi gửi khách.
2. Chạy agent `kiem-tra-khoi-luong` trên BOQ (BOQ mục 8 đề nghị).
3. Cung cấp: hao hụt (định mức), đơn giá theo công bố giá Sở Xây dựng TP.HCM (ghi rõ tháng, quý), hồ sơ KC (móng, dầm, thép, lanh tô, bản thang).
4. Quyết định phạm vi phần thô (mục 5, điểm 1) và xử lý cửa S3 tum (điểm 4).
5. Khi gửi khách, ghi rõ: đây là khối lượng sơ bộ phần kiến trúc, chưa gồm móng, dầm, thép, lanh tô, bản thang.
