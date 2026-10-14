# 02. Bàn giao phần kiến trúc: nhà phố lô 7x20m

- **Người làm:** agent `kien-truc-su` (opus, high)
- **Ngày:** 14/10/2026
- **Quy ước nguồn:** `[JSON: tên.trường]` là `dau-vao/01_mo-ta-tu-ban-ve.json` (đơn vị mm); `[KT-0x]` là tờ bản vẽ trong `dau-vao/02_ban-ve-a3-kt01-kt04.md`, đã đối chiếu hình tờ trong file PDF cùng tên vì bản `.md` bị vỡ bảng. Số em tự tính ghi rõ "tự tính" kèm phép tính.

---

## 1. Việc được giao

Theo `00_phieu-giao-viec.md` (dòng `kien-truc`) và `.claude/agents/kien-truc-su.md`:
1. Viết thuyết minh phương án ngắn cho chủ nhà: lô đất, khối nhà, công năng và cao độ từng tầng, mái, tum, sân thượng, vật liệu hoàn thiện.
2. Soát nhanh lỗi kiến trúc dễ thấy: phòng thờ dựa lưng WC; lan can ban công, lỗ thông tầng thấp hơn 900 mm; cao độ ghi không đủ 3 chữ số thập phân.
3. Không sửa bản vẽ, không tính khối lượng (việc của `boc-kl`).

## 2. Đầu vào đã đọc

| File | Ghi chú |
|---|---|
| `dau-vao/01_mo-ta-tu-ban-ve.json` | Đọc trực tiếp các trường `cao_do`, `cua`, `mai`, `thong_so`, `vat_lieu`, `mat_bang.T1/T2/T3/MAI` |
| `dau-vao/02_ban-ve-a3-kt01-kt04.md` | Bản đọc PDF, 4 tờ KT-01 đến KT-04 |
| `dau-vao/02_ban-ve-a3-kt01-kt04.pdf` | Mở hình từng tờ để đối chiếu tên phòng, cao độ, bảng KT-02 |
| `00_yeu-cau-khach-hang.md` | Chỉ đọc để đối chiếu công năng với mong muốn của khách |

## 3. Kết quả

### 3.1. Thuyết minh phương án (cho chủ nhà)

**Lô đất và khối nhà**
- Lô đất 7 x 20 m [KT-01 tên công trình "NHÀ PHỐ MẪU LÔ 7x20M"]; ranh đất trong JSON từ x = -2000 tới 5000, y = -5000 tới 15000 [JSON: mat_bang.T1.ranh_dat], tự tính: 5000 - (-2000) = 7000 mm, 15000 - (-5000) = 20000 mm, khớp 7 x 20 m.
- Khối nhà 5000 x 14000 mm [JSON: mat_bang.T1.san = 0, 0, 5000, 14000; KT-01 kích thước 5000 và 14000], áp sát ranh phải (mép nhà x = 5000 trùng mép ranh x = 5000) [JSON: mat_bang.T1.ranh_dat, mat_bang.T1.san].
- Khoảng lùi: lối đi hông bên trái rộng 2000 mm [KT-01 kích thước 2000; JSON: mat_bang.T1.san_vuon = -2000..0]; sân trước sâu 5000 mm [KT-01 kích thước 5000; JSON: san_vuon y = -5000..0]; sân sau 1000 mm [KT-01 kích thước 1000; JSON: san_vuon y = 14000..15000].
- Lưới trục: trục ngang 1, 2; trục dọc A, B, C, D, E; nhịp A-B 1400, B-C 6600, C-D 3600, D-E 2200 mm [KT-01, KT-02 đường kích thước trục].
- Khối nhà gồm 3 tầng, sân thượng và tum thang [KT-04 mặt cắt 1-1].

**Cao độ và chiều cao tầng**

| Mốc | Cao độ [KT-02 Bảng cao độ] | Trường JSON | Chiều cao tầng (tự tính) |
|---|---|---|---|
| Sân | -0.450 | cao_do.SAN = -450 | |
| Tầng 1 | ±0.000 | cao_do.T1 = 0 | Sân lên T1: 0 - (-450) = 450 mm |
| Tầng 2 | +3.600 | cao_do.T2 = 3600 | T1 lên T2: 3600 - 0 = 3600 mm |
| Tầng 3 | +7.000 | cao_do.T3 = 7000 | T2 lên T3: 7000 - 3600 = 3400 mm |
| Sân thượng | +10.400 | cao_do.ST = 10400 | T3 lên ST: 10400 - 7000 = 3400 mm |
| Mái tum | +13.400 | cao_do.TUM = 13400 | ST lên mái tum: 13400 - 10400 = 3000 mm |

Chiều cao tầng tự tính khớp đường kích thước 450, 3600, 3400, 3400, 3000 trên KT-03 và KT-04. Sàn BTCT dày 120 mm [JSON: thong_so."Sàn BTCT dày"; KT-02 Bảng thông số].

**Công năng từng tầng**

| Tầng | Cao độ sàn | Phòng, khu vực | Nguồn |
|---|---|---|---|
| Sân trước | -0.450 | Sân để xe (ô tô) dốc i=4%, pergola mái polycarbonate M4, cổng chính, cổng phụ ra lối đi hông, 3 bậc tam cấp lên T1 | KT-01; JSON: mat_bang.T1.bac (3 bậc), thong_so."Bậc tam cấp cao" = 150 |
| Tầng 1 | ±0.000 | Phòng khách (A-C), cầu thang (C-D), sảnh ±0.000, WC ±0.000, bếp ăn ±0.000 (D-E); cửa D2 ra lối đi hông | KT-01, KT-04 |
| Tầng 2 | +3.600 | Ban công +3.550 (A-B), phòng ngủ 1 có giường đôi (B-C), cầu thang, WC +3.600, phòng ngủ 2 có giường đơn và bàn học (D-E) | KT-01, KT-04; JSON: mat_bang.T2.noi_that |
| Tầng 3 | +7.000 | Phòng sinh hoạt +7.000 kèm bàn làm việc, kệ sách (B-C), cầu thang, WC +7.000, phòng thờ +7.000 (D-E); mặt tiền lùi về trục B, cửa sổ băng S5 | KT-01, KT-04; JSON: mat_bang.T3.san = 0, 1400, 5000, 14000 |
| Sân thượng, tum | +10.400 | Tum thang (C-D) có máy giặt, bồn nước inox đặt trên mái tum; sân thượng (D-E) có giàn phơi, bàn nhỏ, ghế, chậu cây | KT-02, KT-04; JSON: mat_bang.MAI.noi_that, mat_bang.MAI.bon_nuoc |

- Cầu thang: mỗi tầng 2 vế, mỗi vế 9 bậc, chiếu nghỉ phía tường trái [JSON: mat_bang.T1.thang.so_bac_moi_ve = 9, 9; thang.chieu_nghi]. Vế thang rộng tự tính 9150 - 8200 = 950 mm [JSON: thang.ve1].
- Cửa: 9 loại, D1 đến D4 và S1 đến S5, số lượng theo Bảng thống kê cửa [KT-02; JSON: cua]. Đếm cửa chi tiết là việc của `boc-kl`.

**Mái**

| Mã | Tên | Áp cho | Đỉnh | Mép | Độ dốc ghi trên bản vẽ | Nguồn |
|---|---|---|---|---|---|---|
| M1 | Mái tôn dốc 1 phía | Tầng 3 | +12.800 | +10.000 | i=39% | KT-02 Bảng mái; JSON: mai.M1 |
| M2 | Mái tôn che ban công | Tầng 2 | +7.000 | +6.200 | i=40% | KT-02 Bảng mái; JSON: mai.M2 |
| M3 | Mái bằng tum BTCT | Tum | +13.400 | +13.400 | | KT-02 Bảng mái; JSON: mai.M3 |
| M4 | Mái pergola tấm polycarbonate | Sân trước | +3.200 | +3.000 | | KT-02 Bảng mái; JSON: mai.M4 |

- Mái dốc về phía mặt tiền [KT-02 tiêu đề "BẢNG MÁI (DỐC VỀ PHÍA MẶT TIỀN)"].
- Kiểm tra độ dốc (tự tính): M1 = (12800 - 10000) / (8000 - 800) = 38.9%, khớp i=39% [JSON: mai.M1, mat_bang.MAI.mai M1.hcn]; M2 = (7000 - 6200) / (1400 - (-600)) = 40.0%, khớp i=40% [JSON: mai.M2, mat_bang.MAI.mai M2.hcn].
- Lan can, tường chắn mái cao 1000 mm; tường chắn mái tum cao 400 mm [JSON: thong_so; KT-02 Bảng thông số].

**Vật liệu hoàn thiện** [JSON: vat_lieu; KT-02 Ghi chú vật liệu hoàn thiện; KT-03 ghi lại mục 1 đến 4]
1. Tường tầng 1, 2: sơn nước màu kem.
2. Tường tầng 3, tum, lan can, tường chắn mái: ốp tấm gỗ nhựa màu nâu.
3. Cột, chỉ tường ở cốt sàn: sơn màu xám nhạt (chỉ tường đua ra 50 mm [JSON: thong_so."Chỉ tường đua ra"]).
4. Mái M1, M2: tôn sóng màu đỏ nâu.
5. Cửa: khung nhôm xám, kính xanh nhạt.
6. Ống xối PVC màu xanh lá; cục nóng máy lạnh màu trắng.
7. Pergola, tường rào: khung thép sơn nâu đỏ, mái tấm polycarbonate.
8. Sân, lối đi: bê tông xám; bồn nước inox.

Ghi chú trên KT-02: phương án kiến trúc mẫu để dựng 3D, kết cấu chưa tính toán, cần kỹ sư duyệt.

### 3.2. Soát lỗi kiến trúc theo danh mục

| # | Hạng mục soát | Kết quả | Tờ, vị trí, căn cứ |
|---|---|---|---|
| 1 | Phòng thờ dựa lưng WC | **Đạt.** Bàn thờ đặt sát tường hậu trục E, không dựa tường WC. Phòng thờ chỉ chung vách ngăn với WC tầng 3 ở cạnh trục D (vách có cửa D2 vào phòng thờ). | KT-01 MB tầng 3, giữa trục D-E; JSON: mat_bang.T3.noi_that "BÀN THỜ" hcn 3300, 13200, 4700, 13800, lưng "S"; tường WC y = 11650..11750 |
| 2 | Lan can ban công thấp hơn 900 mm | **Đạt theo số ghi.** Lan can cao 1000 mm. Bản vẽ mặt đứng, mặt cắt không ghi kích thước riêng cho lan can. | KT-02 Bảng thông số; JSON: thong_so."Lan can, tường chắn mái cao" = 1000; ban công T2 trục A-B (KT-01), sân thượng D-E (KT-02) |
| 3 | Lỗ thông tầng có lan can thấp hơn 900 mm | **Không có thông tầng.** Lỗ sàn duy nhất là ô cầu thang. Chiều cao tay vịn cầu thang: Tài liệu không đề cập. | JSON: mat_bang.T2/T3/MAI.lo_san = 200, 8150, 3450, 10250 (trùng vùng thang); KT-01 |
| 4 | Cao độ ghi không đủ 3 chữ số thập phân | **Đạt.** Mọi cao độ trên 4 tờ đều 3 số lẻ: -0.450, ±0.000, +3.550, +3.600, +6.200, +7.000, +10.000, +10.400, +12.800, +13.400, +3.000, +3.200. | KT-01, KT-02, KT-03, KT-04 |

### 3.3. Lỗi, điểm lệch phát hiện thêm (ngoài danh mục)

| # | Vấn đề | Tờ, vị trí | Căn cứ số liệu |
|---|---|---|---|
| A | **Mái vượt ranh đất bên phải.** Mép mái M1, M2 tới x = 5150, xà pergola và M4 tới x = 5100, trong khi ranh đất phải ở x = 5000. Tự tính: mái M1, M2 lấn 150 mm; M4, xà pergola lấn 100 mm sang đất bên cạnh. | KT-02 MB mái (mép mái phía trục 2); KT-01 pergola | JSON: mat_bang.MAI.mai M1.hcn, M2.hcn (x tới 5150); mat_bang.T1.mai M4.hcn (x tới 5100); mat_bang.T1.pergola_xa (x tới 5100); mat_bang.T1.ranh_dat (x tới 5000) |
| B | **Chỉ có 2 phòng ngủ, khách cần 3.** Tầng 2 có PN1, PN2; tầng 3 là phòng sinh hoạt và phòng thờ. | KT-01, KT-04 | `00_yeu-cau-khach-hang.md` mong muốn 1 |
| C | **Vật liệu cửa D2 lệch ghi chú.** Ghi chú chung "Cửa: khung nhôm xám, kính xanh nhạt" nhưng D2 là "Cửa đi gỗ 1 cánh". | KT-02 Bảng thống kê cửa và Ghi chú vật liệu mục 5 | JSON: cua.D2.ten; vat_lieu mục 5 |
| D | **Ban công +3.550 trong khi tầng 2 +3.600.** Ban công hạ 50 mm (tự tính 3600 - 3550). JSON không có trường cao độ ban công nên không đối chiếu được. | KT-01 MB tầng 2, trục A-B | JSON: cao_do.T2 = 3600 |
| E | **WC không hạ cốt.** WC tầng 1, 2, 3 ghi cùng cốt sàn phòng (±0.000, +3.600, +7.000). | KT-01 cả 3 mặt bằng, trục C-D | JSON: cao_do.T1, T2, T3 |
| F | **Mái tum có bồn nước nhưng tường chắn mái tum chỉ 400 mm.** Lối lên mái tum để bảo trì bồn nước: Tài liệu không đề cập. | KT-02 MB mái, M3 | JSON: thong_so."Tường chắn mái tum cao" = 400; mat_bang.MAI.bon_nuoc |
| G | **Phía trên phòng thờ là sân thượng** có bàn ghế, chậu cây, giàn phơi (người đi lại, phơi đồ trên đầu phòng thờ). | KT-02 MB mái trục D-E; KT-04 mặt cắt | JSON: mat_bang.MAI.noi_that |
| H | **Cầu thang 9 + 9 bậc dùng chung cho tầng cao 3600 và 3400.** Nếu 18 là số bậc đứng thì chiều cao bậc tự tính: 3600 / 18 = 200 mm (T1 lên T2), 3400 / 18 = 188.9 mm (T2 lên T3, T3 lên ST). | KT-01 cầu thang trục C-D | JSON: mat_bang.T1/T2/T3.thang.so_bac_moi_ve = 9, 9; cao_do |

## 4. Giả định đã dùng

1. Gốc tọa độ JSON: x = 0 tại mép ngoài tường trục 1, y = 0 tại mép trục A (mặt tiền), y tăng về phía trục E (hậu). Suy ra từ việc tường, cột JSON khớp kích thước trục trên KT-01.
2. Trường `lung` trong `noi_that` là phía lưng đồ đạc tựa vào; "S" là phía hậu (trục E). Suy ra từ tủ bếp dưới, tủ bếp trên cũng có `lung` = "S" và nằm sát tường trục E.
3. Tên phòng đọc từ hình tờ PDF (bản `.md` bị dính chữ, ví dụ "SÂNÔ TĐÔỂ XE" là "SÂN ĐỂ XE", "LỐI ĐI HÔDN2G" là "LỐI ĐI HÔNG" chồng ký hiệu D2).
4. Phòng ngủ 1 (giường đôi) là phòng bố mẹ, phòng ngủ 2 (giường đơn, bàn học) là phòng con: theo đồ đạc vẽ trên KT-01, bản vẽ không ghi tên chủ phòng.
5. Không tính diện tích sàn, khối lượng; phần này thuộc `boc-kl`.

## 5. Chỗ chưa chắc (Cần xác nhận lại)

1. **Cần xác nhận lại:** mái M1, M2, M4 và xà pergola lấn ranh đất phải 100 đến 150 mm (mục 3.3.A). Nếu tọa độ ranh trong JSON đúng thực địa thì phải thu mái về trong ranh.
2. **Cần xác nhận lại:** số phòng ngủ: bản vẽ 2 phòng, yêu cầu khách 3 phòng (mục 3.3.B).
3. **Cần xác nhận lại:** vật liệu cửa D2 là gỗ hay khung nhôm xám (mục 3.3.C).
4. **Cần xác nhận lại:** cao độ ban công +3.550 là chủ ý hạ cốt chống tràn hay ghi nhầm; JSON không có số để đối chiếu (mục 3.3.D).
5. **Cần xác nhận lại:** WC có hạ cốt so với sàn phòng hay không (mục 3.3.E).
6. **Cần xác nhận lại:** lối lên mái tum và chiều cao bảo vệ khi bảo trì bồn nước (mục 3.3.F).
7. **Cần xác nhận lại:** chủ nhà có chấp nhận sân thượng, giàn phơi nằm trên phòng thờ hay không (mục 3.3.G).
8. **Cần xác nhận lại:** "9 bậc mỗi vế" là bậc đứng hay bậc ngang, và có dùng chung cho cả tầng cao 3600 và 3400 hay không (mục 3.3.H). Chiều cao tay vịn cầu thang: Tài liệu không đề cập.
9. **Cần xác nhận lại:** khách thích phong cách Indochine; ghi chú vật liệu hiện tại (tôn sóng đỏ nâu, ốp gỗ nhựa, sơn kem) không nêu phong cách. Tài liệu không đề cập chi tiết Indochine trên 4 tờ KT.

## 6. Việc người sau cần làm

1. **`kiem-tra`:** soát chéo bảng 3.1 và 3.2 với KT-01 đến KT-04 và JSON; kiểm lại phép tính lấn ranh ở mục 3.3.A và độ dốc mái M1, M2.
2. **`boc-kl`:** lưu ý mái M1, M2, M4 có phần đua vượt ranh (mục 3.3.A) và ban công hạ cốt 50 mm (mục 3.3.D) khi bóc mái và sàn; nếu phương án đổi để thu mái về ranh thì khối lượng mái sẽ đổi.
3. **Agent chính:** đưa 9 điểm ở mục 5 cho anh và chủ nhà quyết, ưu tiên điểm 1 (lấn ranh) và điểm 2 (thiếu phòng ngủ) vì ảnh hưởng phương án.
4. **Kiến trúc sư (vòng sau):** sau khi chủ nhà trả lời, sửa bản vẽ đang làm rồi phát hành lần mới; file này không sửa bản vẽ.
