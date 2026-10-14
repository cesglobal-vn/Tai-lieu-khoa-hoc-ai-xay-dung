# Phiếu giao việc: hồ sơ trình phương án nhà phố lô 7x20m

- **Ngày giao:** 14/10/2026
- **Người giao:** agent chính (theo yêu cầu của anh Tuấn Anh)
- **Khách hàng:** Nguyễn Văn A (tình huống giả định cho bài thực hành)

## Mục tiêu

Lập bộ thông tin trình phương án cho khách: thuyết minh phương án kiến trúc và bảng khối lượng phần thô sơ bộ. Mọi số liệu lấy từ tài liệu trong `dau-vao/`, có nguồn, đã qua soát chéo.

## Đầu vào

| File | Nội dung |
|---|---|
| `dau-vao/01_mo-ta-tu-ban-ve.json` | Mô tả bản vẽ: cao độ, cửa, mái, thông số, vật liệu, mặt bằng từng tầng |
| `dau-vao/02_ban-ve-a3-kt01-kt04.pdf` (bản đọc: `.md`) | Bộ bản vẽ KT-01 đến KT-04 |
| `dau-vao/03_bang-thong-ke-cua.xlsx` (bản đọc: `.md`) | Bảng thống kê cửa |
| `dau-vao/04_tom-tat-boq-phan-tho.md` | BOQ phần thô đã bóc bằng script |
| `00_yeu-cau-khach-hang.md` | Yêu cầu của khách |

Không sửa file nào trong `dau-vao/`.

## Phân công

| Tên | Agent | Việc | Model, mức suy luận | Ghi file |
|---|---|---|---|---|
| kien-truc | kien-truc-su | Thuyết minh phương án, soát lỗi kiến trúc dễ thấy | opus, high | `handoff/02_kien-truc.md` |
| boc-kl | ky-su-boc-khoi-luong | Bảng khối lượng phần thô sơ bộ, đếm cửa, soát bẫy bóc khối lượng | sonnet, high | `handoff/03_boc-khoi-luong.md` |
| kiem-tra | ky-su-kiem-tra | Soát chéo 2 file bàn giao với tài liệu gốc, chỉ đọc | sonnet, high | Agent chính ghi `handoff/04_kiem-tra.md` |

## Thứ tự

1. `kien-truc` và `boc-kl` chạy **song song**. Mỗi người chỉ ghi file của mình.
2. Hai người xong thì `kiem-tra` mới chạy.
3. Agent chính gộp vào `99_bao-cao-tong-hop.md`.

## Mẫu bàn giao (6 mục)

1. Việc được giao  2. Đầu vào đã đọc  3. Kết quả  4. Giả định đã dùng  5. Chỗ chưa chắc  6. Việc người sau cần làm

## Quy tắc chung

- Số liệu có nguồn ngay cạnh. Không có trong tài liệu: "Tài liệu không đề cập". Lệch nhau: "Cần xác nhận lại". Đơn giá, hao hụt: "[Chờ bổ sung]".
- Không tự tính lại khối lượng bằng tay, không tự điền giá.
