# HƯỚNG DẪN CÀI ĐẶT BLENDER MCP (vn-mcp-blender)

**Đối tượng:** học viên chưa từng cài MCP. Làm lần lượt từng bước, bước nào cũng có cách kiểm tra **đạt hay chưa** trước khi sang bước sau.
**Nguồn:** README và thư mục `docs/` (`cai-dat.md`, `xu-ly-loi.md`) của repo `https://github.com/andyluu98/vn-mcp-blender`, tra ngày 07/10/2026. Đã cài thử trên Windows 11 với Blender 5.2, Python 3.12, `vn-mcp-blender` 0.1.0.
**Thời gian:** khoảng 15 phút nếu máy đã có Python và Git.

---

## 0. HIỂU TRƯỚC KHI CÀI

Anh/chị cài **hai** thứ, không phải một:

| Thứ cài | Là gì | Ai khởi động |
|---|---|---|
| MCP server `vn-mcp-blender` | Chương trình Python | Claude tự khởi động khi cần |
| Addon **MCP Xây Dựng** | Một file Python nạp vào Blender | Anh/chị bấm **Bật kết nối** trong Blender |

Hai thứ nói chuyện với nhau qua **cổng 9877** trên chính máy anh/chị.

```
Claude  <--MCP-->  vn-mcp-blender  <--cổng 9877-->  Addon "MCP Xây Dựng" trong Blender
```

Ví như gọi điện vào phòng kín: MCP server là tổng đài, addon là người cầm máy trong phòng. Thiếu một bên là không nói chuyện được.

Bộ công cụ này **không gửi dữ liệu ra ngoài máy**, không có telemetry (theo README).

---

## 1. CHUẨN BỊ PHẦN MỀM

| Phần mềm | Yêu cầu | Lấy ở đâu | Kiểm tra |
|---|---|---|---|
| Blender | Bản 3.0 trở lên | blender.org, mục Download | Mở Blender, `Help > About Blender` |
| Python | Bản 3.10 trở lên | python.org. Khi cài trên Windows **tích ô "Add Python to PATH"** | `python --version` |
| Git | Bản bất kỳ | git-scm.com | `git --version` |
| Claude Code | Đã đăng nhập | Bản desktop hoặc dòng lệnh | Mở được Claude Code |

Mở cửa sổ dòng lệnh (Windows: gõ `cmd` hoặc `PowerShell` ở ô tìm kiếm) và chạy:

```bash
python --version
```

```bash
git --version
```

**Đạt khi:** Python ra từ `3.10` trở lên, Git ra số phiên bản.

**Chưa đạt:**
- Gõ `python` mà mở ra Microsoft Store: Python chưa cài hoặc chưa vào PATH. Cài lại từ python.org, nhớ tích "Add Python to PATH".
- Máy có nhiều bản Python: dùng đúng một bản cho mọi lệnh ở dưới. Có thể thay `python` bằng đường dẫn đầy đủ, ví dụ `C:\Python312\python.exe`.

---

## 2. CÀI GÓI vn-mcp-blender

Chọn một thư mục để chứa công cụ, ví dụ `C:\tools`, rồi chạy lần lượt:

```bash
cd C:\tools
```

```bash
git clone https://github.com/andyluu98/vn-mcp-blender
```

```bash
cd vn-mcp-blender
```

```bash
python -m pip install -e .
```

**Kiểm tra:**

```bash
vn-mcp-blender --version
```

**Đạt khi:** ra số phiên bản (ví dụ `0.1.0`).

**Báo "command not found" hoặc "không nhận ra lệnh":** thư mục script của Python chưa nằm trong PATH. Không sao, dùng cách gọi qua Python:

```bash
python -m vn_mcp_blender.cli --version
```

Cách này chạy được thì ở bước 4 khai báo bằng `python -m vn_mcp_blender.cli` thay cho tên lệnh. Các lệnh `vn-mcp-blender ...` ở dưới cũng thay bằng `python -m vn_mcp_blender.cli ...`.

> Có thể nhờ Claude làm bước này: "Tải repo andyluu98/vn-mcp-blender về C:\tools, cài bằng python -m pip install -e ., rồi chạy lệnh kiểm tra phiên bản và báo tôi kết quả."

---

## 3. CÀI ADDON VÀO BLENDER

### 3.1. Chép addon

**Cách a, để lệnh tự làm** (nên dùng):

```bash
vn-mcp-blender install-addon
```

Lệnh tự tìm mọi bản Blender trên máy rồi chép addon vào, in ra đường dẫn đã chép.

**Cách b, cài tay** (khi cách a không tìm thấy Blender): lấy đường dẫn file addon

```bash
vn-mcp-blender addon-path
```

rồi trong Blender: `Edit > Preferences > Add-ons > Install...`, chọn đúng file đó.

### 3.2. Bật addon

1. Mở Blender, vào `Edit > Preferences > Add-ons`.
2. Gõ "MCP" vào ô tìm kiếm.
3. Thấy dòng **Interface: MCP Xây Dựng**, tích vào ô vuông bên trái.
4. Đóng cửa sổ Preferences.

### 3.3. Bật kết nối (bước hay quên nhất)

1. Đưa chuột vào khung nhìn 3D, bấm phím **N**. Một thanh dọc hiện ra bên phải.
2. Chọn tab **MCP Xây Dựng**.
3. Bấm nút **Bật kết nối**.
4. Dòng chữ đổi thành **"Đang chạy ở cổng 9877"** kèm dấu tích.

**Kiểm tra:** giữ Blender đang mở, mở một cửa sổ dòng lệnh khác:

```bash
vn-mcp-blender check
```

**Đạt khi:** in ra thông tin Blender.
**Báo "Chưa nối được ... localhost:9877":** xem mục 7, dòng 1 đến 4.

---

## 4. KHAI BÁO VỚI CLAUDE

### 4.1. Claude Code: một lệnh (nên dùng)

```bash
claude mcp add vn-blender -s user -- vn-mcp-blender
```

Nếu ở bước 2 phải dùng `python -m`, thay bằng:

```bash
claude mcp add vn-blender -s user -- python -m vn_mcp_blender.cli
```

`-s user` nghĩa là khai báo cho **mọi dự án** trên máy, không phải chỉ thư mục đang đứng.

**Kiểm tra:**

```bash
claude mcp list
```

**Đạt khi:** có dòng `vn-blender ... Connected`.

### 4.2. Claude Code: sửa file cấu hình (cách thay thế)

Mở file `C:\Users\<tên>\.claude.json`, tìm mục `mcpServers`, thêm:

```json
{
  "mcpServers": {
    "vn-blender": {
      "type": "stdio",
      "command": "vn-mcp-blender",
      "args": []
    }
  }
}
```

Nếu tên lệnh không chạy được thì đổi thành `"command": "python", "args": ["-m", "vn_mcp_blender.cli"]`.
**Chép bản cũ của file ra chỗ khác trước khi sửa:** file này chứa toàn bộ cấu hình Claude Code, sai một dấu phẩy là Claude không mở được.

### 4.3. Claude Desktop (tab Chat)

| Hệ điều hành | File cấu hình |
|---|---|
| Windows | `%APPDATA%\Claude\claude_desktop_config.json` |
| macOS | `~/Library/Application Support/Claude/claude_desktop_config.json` |

Nội dung mục `mcpServers` giống mục 4.2. Sao lưu file trước khi sửa.

### 4.4. Kiểm tra cuối cùng

Khởi động lại Claude, mở phiên mới, gõ:

```
Kiểm tra kết nối Blender.
```

**Đạt khi:** Claude trả về phiên bản Blender, phiên bản addon và số đối tượng trong cảnh.
Trong Claude Code có thể gõ `/mcp` để xem `vn-blender` đã nối và danh sách 30 công cụ.

---

## 5. THỨ TỰ MỞ MỖI LẦN LÀM VIỆC

1. Mở Blender.
2. Bấm **Bật kết nối** ở tab MCP Xây Dựng (phím N).
3. Mở Claude.

Lỡ mở Claude trước cũng không sao: mở Blender, bấm Bật kết nối là dùng được, không phải khởi động lại Claude.

---

## 6. BỘ CÔNG CỤ SAU KHI CÀI (30 CÔNG CỤ, ĐƠN VỊ MÉT)

| Nhóm | Công cụ |
|---|---|
| Kết nối, xem cảnh | `kiem_tra_ket_noi`, `huong_dan`, `xem_canh`, `xem_doi_tuong`, `nhin` |
| Đọc bản vẽ | `doc_layer_dxf`, `doc_mat_bang_dxf`, `dung_nha_tu_dxf` |
| Dựng cấu kiện | `dung_tuong`, `dung_san`, `dung_cot`, `dung_dam`, `khoet_cua`, `dung_cau_thang`, `dung_mai`, `dung_tu_mo_ta` |
| Sửa | `sua_doi_tuong`, `nhan_ban`, `xoa_doi_tuong`, `xoa_toan_bo` |
| Vật liệu, ánh sáng, ảnh | `tao_vat_lieu`, `gan_vat_lieu`, `tao_den`, `anh_sang_moi_truong`, `tao_camera`, `cai_dat_render`, `render_anh` |
| Xuất, khối lượng | `xuat_file` (glb, fbx, obj, stl), `boc_khoi_luong` |
| Chạy mã | `chay_python` (dùng ở Prompt 5.3 để dựng nhà 7x20m) |

**Về an toàn của `chay_python`:** mã được soát trước khi chạy, chặn các lệnh xóa file, chạy lệnh hệ thống, mở file Blender khác. Bộ soát chặn lỗi rõ ràng, **không phải tường lửa**. Lưu file Blender trước khi chạy việc lớn. Script dựng nhà 7x20m của khóa đã qua bộ soát này.

---

## 7. XỬ LÝ LỖI THƯỜNG GẶP

| # | Hiện tượng | Cách xử lý |
|---|---|---|
| 1 | "Không nối được tới Blender ở localhost:9877" | Blender chưa mở; hoặc chưa bấm **Bật kết nối** (bật addon trong Preferences **chưa đủ**) |
| 2 | Không thấy dòng MCP Xây Dựng trong Add-ons | Addon chưa được chép: chạy lại `vn-mcp-blender install-addon`, khởi động lại Blender |
| 3 | Bấm Bật kết nối báo lỗi | Có chương trình khác giữ cổng 9877. Xem bằng `netstat -ano \| findstr 9877`. Đổi cổng ở ô "Cổng" ngay trên nút |
| 4 | Mở hai cửa sổ Blender | Chỉ một cửa sổ giữ được cổng. Đóng bớt còn một |
| 5 | Claude không thấy công cụ Blender | Chưa khởi động lại Claude sau khi khai báo; `claude mcp list` không có `vn-blender` thì làm lại mục 4 |
| 6 | Máy có cả addon `blender-mcp` phổ biến | Không sao: addon đó dùng cổng 9876, bộ này 9877, chạy song song được. Khi ra lệnh nói rõ "dùng vn-blender" |
| 7 | "Blender không trả lời lệnh ... trong 120 giây" | Lệnh nặng làm Blender đứng hình tạm thời. Đợi thêm; xem `Window > Toggle System Console`. Treo hẳn thì tắt mở lại Blender |
| 8 | "Code bị chặn vì các lý do sau..." | `chay_python` chặn lệnh nguy hiểm. Đọc lý do, sửa đoạn mã. Chỉ tắt bộ soát (`VN_MCP_UNSAFE=1`) khi hiểu rõ rủi ro |
| 9 | Đọc DXF báo lỗi | File phải là `.dxf` (ezdxf không đọc `.dwg`); đường dẫn Windows dùng `F:/ban-ve/a.dxf` hoặc nhân đôi gạch chéo ngược |
| 10 | Mô hình to gấp nghìn lần hoặc bé như hạt gạo | Sai tỷ lệ đơn vị: bản vẽ mm dùng `ty_le=0.001`, bản vẽ mét dùng `ty_le=1.0` |
| 11 | Ảnh render tối om | Thiếu ánh sáng môi trường: gọi cả `tao_den` và `anh_sang_moi_truong` |

---

## 8. GỠ CÀI ĐẶT

```bash
python -m pip uninstall vn-mcp-blender
```

```bash
claude mcp remove vn-blender -s user
```

Addon trong Blender gỡ riêng: `Edit > Preferences > Add-ons`, tìm MCP Xây Dựng, mở rộng dòng đó rồi chọn Remove.

---

## 9. CÀI THÊM CHO PHẦN AUTOCAD (NẾU CHƯA CÓ TỪ BUỔI 03)

Phần vẽ bản vẽ (Prompt Phần 4) cần `autocad-mcp` từ repo `andyluu98/vn-autocad-claude`. Hướng dẫn đầy đủ ở:
`03_Buoi_03_Thiet_Ke_Va_Dieu_Khien_AutoCAD\05_Noi_Dung_Chuong_Trinh_Buoi_03_AutoCAD_MCP.md`, mục cài đặt.

Học viên không có AutoCAD vẫn học được Phần 5: file DXF của nhà 7x20m có sẵn trong thư mục demo.
