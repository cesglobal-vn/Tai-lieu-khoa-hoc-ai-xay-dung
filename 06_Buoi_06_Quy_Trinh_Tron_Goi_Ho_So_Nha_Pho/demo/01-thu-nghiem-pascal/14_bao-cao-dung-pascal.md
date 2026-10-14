# Báo cáo dựng mô hình Pascal: Nhà phố lô 7x20m, Buổi 04 CES

Ngày dựng: 10/10/2026. Nguồn hình học: `ke-hoach-pascal.json` (cùng thư mục). Trục: x bản vẽ thành X Pascal, y bản vẽ thành Z Pascal, Y hướng lên, đơn vị mét.

## 1. Thông tin project

| Mục | Giá trị |
|---|---|
| Tên project | Nha pho lo 7x20m - Buoi 04 CES (private) |
| Project id | `40bc6b305fbc` |
| editorUrl (chính) | http://pascal.localhost:59979/scene/40bc6b305fbc |
| Phiên bản hiển thị | 100 (publishedVersion = latestVersion = browserVisibleVersion) |
| Số node | 114 |
| graphHash | `b4b8839a5f24dfc8...f406` |
| Checkpoint đã lưu | scene id `9b5b3bedb170`, version 1, cùng graphHash, URL http://pascal.localhost:59979/scene/9b5b3bedb170 |

Ghi chú: lệnh `save_scene` (checkpoint) không truyền `id` nên server tạo thêm một bản ghi scene `9b5b3bedb170` thuộc cùng project. Hai bản giống hệt nhau (cùng graphHash, 114 node). Em chưa xóa bản thừa này; anh muốn gộp thì báo em.

## 2. Tầng

| Tầng | Cao tầng (m) | Cao độ sàn (m) | Level id |
|---|---|---|---|
| T1 | 3.6 | 0.0 | `level_dkrn0f14l5jr1lz4` |
| T2 | 3.4 | 3.6 | `level_56id95hvxclte90o` |
| T3 | 3.4 | 7.0 | `level_xoa0lw6ngb2ry7wb` |
| MAI | 3.0 | 10.4 | `level_745sqlmvbwfojq48` |
| Mái tum (tầng đỡ mái, không tính là tầng ở) | 0.35 | 13.4 | `level_byqz77smcnu3h5wm` |

Building lấy từ project mới (có sẵn site, building và một level trống); em đổi level đó thành T1, cao 3.6 m, không dùng template nên không phải xóa nội dung mẫu.

## 3. Đếm theo tầng (dựng / theo plan)

| Tầng | Tường | Cửa đi | Cửa sổ | Lan can | Nội thất |
|---|---|---|---|---|---|
| T1 | 7 / 7 | 3 / 3 | 5 / 5 | 0 / 0 | 6 / 19 |
| T2 | 8 / 8 | 4 / 4 | 6 / 6 | 3 / 3 | 8 / 18 |
| T3 | 8 / 8 | 3 / 3 | 7 / 7 | 0 / 0 | 4 / 12 |
| MAI | 4 / 4 | 1 / 1 | 1 / 1 | 3 / 3 | 1 / 8 |
| **Tổng** | **27 / 27** | **11 / 11** | **19 / 19** | **6 / 6** | **19 / 57** |

Tổng cửa đi + cửa sổ: **30 / 30** (khớp plan). Số liệu dựng lấy từ kết quả `verify_scene`; verify đếm lan can chung với tường (T2: 11 tường, MAI: 7 tường).

Sàn: 4 sàn theo `san`, lỗ sàn theo `lo_san` [0.2, 8.15, 3.45, 10.25] trên T2, T3, MAI (schema slab có trường `holes`, đã dùng). Thêm 3 tấm chiếu nghỉ (xem mục 5).

## 4. Nội thất đã đặt

| Tầng | Món trong plan | Asset catalog | Tâm [x, z] |
|---|---|---|---|
| T1 | SOFA | sofa | 0.75, 3.5 |
| T1 | BÀN TRÀ | coffee-table | 2.0, 3.5 |
| T1 | KỆ TV | tv-stand | 4.575, 3.5 |
| T1 | BÀN ĂN | dining-table | 2.85, 6.3 |
| T1 | TỦ BẾP DƯỚI | kitchen | 2.5, 13.5 |
| T1 | BỒN CẦU | toilet | 1.35, 11.3 |
| T2 | GIƯỜNG ĐÔI | double-bed | 3.8, 4.1 |
| T2 | TAB (2 cái) | bedside-table | 4.575, 2.925 và 4.575, 5.275 |
| T2 | TỦ ÁO (phòng ngủ trước) | closet | 1.3, 7.75 |
| T2 | BÀN TRANG ĐIỂM | dresser | 0.425, 5.0 |
| T2 | BÀN NHỎ (ban công) | bedside-table | 2.5, 0.8 |
| T2 | GIƯỜNG ĐƠN | single-bed | 1.2, 13.1 |
| T2 | BỒN CẦU | toilet | 1.35, 11.3 |
| T3 | SOFA | sofa | 4.35, 4.9 |
| T3 | BÀN TRÀ | coffee-table | 3.0, 4.9 |
| T3 | KỆ TV | tv-stand | 0.425, 4.9 |
| T3 | BỒN CẦU | toilet | 1.35, 11.3 |
| MAI | BÀN NHỎ | bedside-table | 3.8, 12.8 |

Hướng xoay theo cột `lung` (lưng tựa tường): T quay 90°, P quay -90°, S quay 180°, D giữ 0°. Nội thất dùng 28 lệnh (9 search_assets, 19 place_item), dưới hạn 40.

## 5. Đơn giản hóa và chỗ chưa làm được

1. **Cầu thang chữ U:** công cụ chỉ dựng được thang một vế thẳng. Em ghép mỗi cầu thang từ 2 vế thẳng và 1 chiếu nghỉ:
   - Vế 1: từ x = 3.45 đi về x = 1.11, tim z = 8.675, rộng 0.95 m, dài 2.34 m, 9 bậc.
   - Chiếu nghỉ: một tấm sàn [0.2, 8.2, 1.11, 10.25], dày 0.15 m.
   - Vế 2: từ x = 1.11 đi về x = 3.45, tim z = 9.775, rộng 0.95 m, 9 bậc.
   - Cao độ chiếu nghỉ: 1.8 m ở T1 (3.6 / 2) và 1.7 m ở T2, T3 (3.4 / 2).
   
   Thang được tách thành 6 node stair và 3 tấm chiếu nghỉ, không phải một khối liền.
2. **Lỗ sàn thang:** đã khoét theo `lo_san` trên từng sàn. Khi tạo thang em tắt chế độ tự khoét lỗ để không bị trùng lỗ.
3. **Hướng dốc mái M1, M2:** kiểu mái `shed`, độ dốc 21.25° (M1) và 21.8° (M2), đặt ở đúng hình chữ nhật trong plan, `wallHeight` = 0. Pascal không có thông số chọn phía thấp. Em chưa có ảnh render nên **chưa kiểm được phía thấp có nằm ở phía trước (z nhỏ) hay không**: `Cần xác nhận lại` trên editor. Nếu bị ngược, đặt rotation của roof bằng 3.1416.
4. **Cao độ tuyệt đối của mái:**
   - M1 đặt trên T3, tâm y = 3.0. Mép mái = 7.0 + 3.0 = 10.0 m; đỉnh = 10.0 + 7.2 × tan(21.25°) = 12.80 m.
   - M2 đặt trên T2, tâm y = 2.6. Mép = 3.6 + 2.6 = 6.2 m; đỉnh = 6.2 + 2.0 × tan(21.8°) = 7.00 m.
   - M3 là mái bằng trên tầng mái riêng, cao độ 13.4 m.
   
   Các số này tính với giả định y của roof tính từ sàn tầng chứa nó: `Cần xác nhận lại` trên editor. Mái M4 (pergola) không có trong `mai_hcn` và không nằm trong yêu cầu nên không dựng.
5. **Mái M1, M2 nằm chung tầng ở:** verify cảnh báo nên đưa mái lên tầng mái riêng. Em giữ trên T3, T2 để đúng cao độ plan.
6. **Tên cửa:** add_door, add_window không có tham số tên. Em đặt tên sau bằng apply_patch, dạng "D1 - T1", "S2 - T2"... Lan can cũng được đặt tên.
7. **Lan can:** dựng bằng tường cao 1.0 m, dày 0.2 m, không phải lan can song sắt.
8. **Nội thất bỏ qua (38 món):**
   - Tìm "desk" không có kết quả: bỏ bàn học (T2), bàn làm việc (T3).
   - Không có asset hợp lý (em không tìm riêng): bàn thờ (T3).
   - Lavabo (3 cái): catalog chỉ có `bathroom-sink` 2.0 × 1.5 m, plan là 0.5 × 0.45 m, không hợp nên bỏ.
   - Tủ áo phòng ngủ sau T2 (0.55 × 1.0 m): closet 2.0 × 1.0 m sẽ lấn qua tường, nên bỏ.
   - Ngoài nhóm món chính anh liệt kê, bỏ để giữ hạn khoảng 40 lệnh (em không tìm trong catalog): thảm, ghế, tủ lạnh (catalog có `fridge`), ô tô, chậu cây, sen tắm, tủ bếp trên, kệ sách, máy giặt, giàn phơi.
9. **Kích thước nội thất:** asset catalog có kích thước cố định, lớn hơn plan:
   - bàn trà 2.0 × 1.5 so với 0.6 × 1.1;
   - giường đôi 2.0 × 2.5 so với 2.0 × 1.8;
   - bếp sâu 1.0 so với 0.6;
   - closet sâu 1.0 so với 0.6;
   - bồn cầu 1.0 × 1.0 so với 0.4 × 0.7.
   
   Vì vậy có chồng lấn (xem mục 6). Tâm đặt vẫn đúng `tam` trong plan.
10. **Zone/phòng:** plan không có polygon phòng nên em không tạo zone (không bịa hình học). verify vì thế báo "has walls but no zones/rooms".

## 6. Kết quả kiểm tra

**validate_scene:** valid = true, 0 lỗi, 0 cảnh báo.

**verify_scene:** valid = true, hasIssues = true, 14 cảnh báo:

| Nhóm | Chi tiết |
|---|---|
| Không có zone | T1, T2, T3, MAI (mục 5.10) |
| Mái trên tầng ở | T2 (M2), T3 (M1) (mục 5.5) |
| Đồ chắn cửa WC | Bồn cầu chắn cửa D4 ở T1, T2, T3 (asset 1.0 m rộng hơn plan 0.4 m) |
| Đồ chắn cửa ban công | Bàn nhỏ T2 tại [2.5, 0.8] chắn cửa D3 (vị trí theo plan) |
| Chồng lấn | Sofa và bàn trà ở T1, T3; giường đôi và 2 tab ở T2 (do asset to hơn plan) |

Em không sửa các cảnh báo về nội thất: muốn hết thì phải dời đồ khỏi tọa độ `tam` hoặc bỏ đồ, tức là lệch plan.

**get_project_status (40bc6b305fbc):** nodeCount 114, isEmpty false, version 100.

## 7. Nguồn dữ liệu kiểm chứng

| Số liệu | Nguồn |
|---|---|
| Tường, cửa, lan can, sàn, lỗ sàn, thang, nội thất | `ke-hoach-pascal.json`, `levels[].walls/openings/lan_can/san/lo_san/thang/noi_that` |
| Cao tầng 3.6 / 3.4 / 3.4 / 3.0 | `ke-hoach-pascal.json`, `levels[].cao_tang` |
| Mái M1, M2, M3 (cao độ, hình chữ nhật) | `ke-hoach-pascal.json`, `mai`, `mai_hcn`; yêu cầu của anh ngày 10/10 |
| Số đã dựng | Kết quả `verify_scene` và `get_project_status` ngày 10/10/2026 |
| Độ dốc 21.25° | atan(2.8 / 7.2), với 2.8 = 12.8 - 10.0 và 7.2 = 8.0 - 0.8 (em tự tính) |
| Độ dốc 21.8° | atan(0.8 / 2.0), với 0.8 = 7.0 - 6.2 và 2.0 = 1.4 - (-0.6) (em tự tính) |

Quy tắc làm tròn: góc làm tròn 2 chữ số thập phân, cao độ làm tròn 2 chữ số thập phân.

## 8. Bo sung san vuon va nha xe

Ngày làm: 10/10/2026. Nguồn hình học: `ke-hoach-san-vuon.json` (cùng thư mục). Project giữ nguyên id `40bc6b305fbc`, không tạo project hay scene mới. Mọi phần mới nằm trên tầng T1 (`level_dkrn0f14l5jr1lz4`).

### 8.1. Kết quả

| Mục | Giá trị |
|---|---|
| editorUrl | http://pascal.localhost:59979/scene/40bc6b305fbc |
| Phiên bản | 113 (publishedVersion = latestVersion = browserVisibleVersion) |
| Số node | 138 (trước khi bổ sung: 114, thêm 24) |
| graphHash | `1e2b2ba3545cfe34...737a` |
| validate_scene | valid = true, 0 lỗi, 0 cảnh báo |
| verify_scene | valid = true, hasIssues = true, 15 cảnh báo (xem 8.5) |

### 8.2. Đã thêm (24 node)

| Hạng mục | Số node | Loại node | Cách dựng |
|---|---|---|---|
| Sân vườn | 3 | slab | 3 hình chữ nhật `san_vuon`, mặt trên -0.45, dày 0.1 |
| Rào | 3 | fence | Tim z = -4.9, dày 0.2, cao 1.8, kiểu `privacy` (đặc), màu kem |
| Cổng sắt | 2 | fence | Tim z = -4.9, dày 0.1, cao 1.6, kiểu `slat` (song), màu #2B2B2B. Cánh trái rộng 0.9, cánh phải 4.4 |
| Bậc tam cấp | 3 | slab | x 0.7..4.3; mặt trên -0.30, -0.15, 0.00 từ ngoài vào; dày 0.15, 0.30, 0.45 để chạm mặt sân -0.45 |
| Cột pergola | 2 | wall | Đoạn tường 0.15 x 0.15, cao 2.8 |
| Xà pergola | 9 | slab | Xà dọc 2 cái rộng 0.15, mặt trên 3.0; xà ngang 7 cái rộng 0.1, x -0.1..5.1; tất cả cao 0.2 |
| Mái M4 | 2 | roof + roof-segment | Mái `shed` 5.2 x 4.9, tâm [2.5, 3.0, -2.45], dốc 2.34°, không đua |

Rào và cổng dùng node `fence` có sẵn của Pascal (không phải asset catalog), đúng loại hơn tường mỏng.

Bậc tam cấp làm bằng 3 tấm sàn, không dùng cầu thang thẳng, vì 3 bậc cần đúng cao độ tuyệt đối.

### 8.3. Không làm được, bỏ qua

| Hạng mục | Lý do |
|---|---|
| Ô tô `xe_o_to` | Catalog chỉ có 23 món nội thất (giường, sofa, bếp, thiết bị vệ sinh, máy giặt...). Tìm "car", "vehicle" ra 0 kết quả |
| 2 chậu cây `chau_cay` | Tìm "plant", "pot", "tree", "outdoor" ra 0 kết quả |
| 4 cục nóng máy lạnh `may_lanh` | Tìm "air conditioner", "ac unit" ra 0 kết quả |
| 5 ống xối `ong_xoi` | Pascal không có node cột hay ống. Tường chỉ dựng trong một tầng nên không kéo được một ống liền tới 10.4 |

### 8.4. Đơn giản hóa và chỗ cần xác nhận

1. **Chân rào, cổng, cột ở cao độ 0, không phải -0.45.** Node `wall` và `fence` không có trường cao độ chân, luôn đứng trên sàn tầng T1 (0.0). Vì vậy:
   - đỉnh rào ở 1.8 (bản vẽ: 1.35), đỉnh cổng ở 1.6 (bản vẽ: 1.15);
   - giữa chân rào, cột và mặt sân -0.45 có thể hở 0.45 m. `Cần xác nhận lại` trên editor; nếu hở thì một cách sửa là hạ chiều cao rào xuống 1.35 để đỉnh khớp bản vẽ.
2. **Sàn cao độ âm được chấp nhận:** sân đặt đúng -0.45 (em đã thử trước khi dựng, schema nhận giá trị âm).
3. **Xà dùng node slab** (Pascal không có node dầm). Mặt trên mỗi xà ngang lấy theo mặt mái tại vị trí z của xà, công thức `3.0 + 0.2 x (z + 4.9) / 4.9`, làm tròn 3 chữ số: 3.011; 3.041; 3.069; 3.098; 3.127; 3.155; 3.184. Hai xà dọc là tấm phẳng mặt trên 3.0, không nghiêng theo mái.
4. **Cột dùng node wall** dài 0.15, dày 0.15, cao 2.8: đỉnh cột 2.8 = đáy xà (3.0 - 0.2).
5. **Mái M4:** dốc 2.34° = atan(0.2 / 4.9), với 0.2 = 3.2 - 3.0 và 4.9 = 0 - (-4.9). Mái đặt trên tầng T1 (không tách tầng mái riêng) để giữ đúng cao độ. Phía thấp có nằm ở phía cổng (z = -4.9) hay không: `Cần xác nhận lại`, cùng lưu ý như M1, M2 ở mục 5.3.
6. **Thép sơn đen và polycarbonate là vật liệu tự định nghĩa**, không phải preset (xem 8.6).

### 8.5. Cảnh báo verify_scene

15 cảnh báo, gồm 14 cảnh báo cũ (mục 6) và 1 cảnh báo mới: "T1 mixes roof geometry with occupied-level content" do mái M4 nằm trên T1. Verify đếm T1: 9 tường (7 cũ + 2 cột), 17 sàn (2 cũ + 3 sân + 3 bậc + 9 xà), 1 mái; rào và cổng không nằm trong bảng đếm của verify.

### 8.6. Vật liệu

Pascal không cho xem danh sách preset vật liệu: trường `materialPreset` nhận chuỗi bất kỳ mà không kiểm tra, không công cụ nào trả về tên preset hợp lệ. Vì vậy em **không thấy preset nào** và không đoán tên. Thay vào đó em dùng trường `material` (schema có kiểm tra: `id`, `properties.color`, `roughness`, `metalness`, `opacity`, `transparent`, `side`):

| Vật liệu (id) | Màu | Thông số khác | Áp cho |
|---|---|---|---|
| `son-ve-kem` | #F2EAD3 | roughness 0.9 | 17 tường ngoài: T1 4 tường bao; T2 4 tường bao và 3 lan can; T3 tường sau, trái, phải; MAI 3 lan can |
| `op-go-nau` | #8B5A2B | roughness 0.7 | 5 tường: T3 mặt tiền (z = 1.5), 4 tường tum MAI |
| `thep-son-den` | #2B2B2B | roughness 0.4, metalness 0.8 | 2 cột, 9 xà |
| `polycarbonate-trong` | #E6F2F8 | opacity 0.35, transparent, 2 mặt | Mái M4 |
| `gach-san-vuon` | #B8B2A7 | roughness 0.9 | 3 tấm sân |

Rào và cổng dùng trường `color` của node fence (kem #F2EAD3 và đen #2B2B2B). Bậc tam cấp giữ vật liệu mặc định.

Ghi chú: "ốp gỗ nâu" chỉ là màu nâu trơn, không có vân gỗ. Vật liệu áp cho cả hai mặt tường nên mặt trong các tường này cũng đổi màu.

### 8.7. Nguồn dữ liệu kiểm chứng

| Số liệu | Nguồn |
|---|---|
| Sân, rào, cổng, bậc, cột, xà, mái M4 | `ke-hoach-san-vuon.json`: `san_vuon`, `rao`, `cong`, `bac`, `pergola` |
| Cao độ sân -0.45 | `ke-hoach-san-vuon.json`, `cot_san` |
| Cao độ mái 3.0 / 3.2 | `ke-hoach-san-vuon.json`, `pergola.mai_M4.mep`, `.dinh` |
| Danh sách catalog 23 món | `search_assets` ngày 10/10/2026 |
| Node count, version, kết quả kiểm tra | `get_project_status`, `validate_scene`, `verify_scene` ngày 10/10/2026 |

Quy tắc làm tròn: góc 2 chữ số thập phân, cao độ xà 3 chữ số thập phân.

### 8.8. Ghi chú cao độ sân

Cốt sân lấy +0.02 thay vì -0.45 vì mặt đất Pascal cố định ở cốt 0; bản vẽ thật sân thấp hơn nền tầng 1 là 0.45 m. Ba bậc tam cấp (-0.30, -0.15, 0.00) đã xóa vì nằm dưới mặt sân mới và trùng footprint sân trước; sàn T1 (+0.05) chỉ cao hơn sân 3 cm nên không cần bậc.
