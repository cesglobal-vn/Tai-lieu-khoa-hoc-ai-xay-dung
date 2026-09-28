# TÀI LIỆU HƯỚNG DẪN BÀI THỰC HÀNH LAB 02
## TỰ TAY ĐÓNG GÓI SKILL RÀ SOÁT HỒ SƠ KỸ THUẬT & CHỐNG BỊA SỐ
**Thời lượng thực hành:** 35 - 55 phút  
**Sản phẩm nghiệm thu (Deliverable D2):**
1. 01 Skill `soat-ho-so-ky-thuat` hoạt động được trong thư mục `.claude/skills/`.
2. 01 Bảng Ma trận Yêu cầu Kỹ thuật (`Ma_Tran_Yeu_Cau_Ky_Thuat.md`).
3. 01 Phiếu Yêu cầu Làm rõ Thông tin (`Phieu_RFI_01_Lam_Ro_Thong_Tin.md`).
**Đơn vị đào tạo:** CES Global AEC ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. DỮ LIỆU ĐẦU VÀO CHO BÀI THỰC HÀNH

Học viên sử dụng bộ file PDF mẫu tại thư mục `demo/` của khóa học:
- **Cặp thực hành 1 (Kiến trúc & PCCC):**
  - Chỉ dẫn kỹ thuật: `demo/01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf` (Yêu cầu cửa thoát nạn EI 90)
  - Thuyết minh bản vẽ: `demo/02_Thuyet_Minh_Ban_Ve_KT102.pdf` (Bảng thống kê ghi cửa D-08 là EI 60)
- **Cặp thực hành 2 (Kết cấu phần ngầm):**
  - Chỉ dẫn kỹ thuật: `demo/03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf` (Bê tông B35, chống thấm W10, lớp bảo vệ 40mm)
  - Thuyết minh bản vẽ: `demo/04_Thuyet_Minh_Ban_Ve_Vach_Ham_KC02.pdf` (Bản vẽ ghi B30, chống thấm W8, lớp bảo vệ 25mm)
- **Cặp thực hành 3 (Kết cấu thép & Sơn chống cháy - Đề bài nâng cao):**
  - Chỉ dẫn kỹ thuật: `demo/05_Chi_Dan_Ky_Thuat_Son_Chong_Chay_Ket_Cau_Thep.pdf` (Quy định bắt buộc R120 per QCVN 06:2022)
  - Thuyết minh bản vẽ: `demo/06_Thuyet_Minh_Ban_Ve_Ket_Cau_Thep_KC105.pdf` (Bản vẽ thép ghi chú R60 màng mỏng 1.2mm)

*(Học viên cũng có thể sử dụng chính tập hồ sơ PDF công việc thực tế của công ty mình).*

---

## 2. CÁC BƯỚC THỰC HIỆN TỪNG BƯỚC (STEP-BY-STEP)

### BƯỚC 1: Khởi tạo Cấu trúc Thư mục Skill (5 phút)
Mở Claude Code tại thư mục dự án đã tạo từ Buổi 01, thực hiện lệnh tạo thư mục:
```bash
mkdir -p .claude/skills/soat-ho-so-ky-thuat
```

---

### BƯỚC 2: Tạo File Cấu hình `SKILL.md` (10 phút)
Yêu cầu Claude Code tạo file `.claude/skills/soat-ho-so-ky-thuat/SKILL.md` hoặc sao chép nội dung từ file mẫu tại `demo/skill-mau/SKILL.md`.

**Điểm kiểm tra bắt buộc trong file SKILL.md:**
- Có đủ 2 trường YAML: `name: soat-ho-so-ky-thuat` và `description` rõ ràng mô tả *"Dùng khi rà soát chỉ dẫn kỹ thuật, đối chiếu mâu thuẫn bản vẽ và lập phiếu RFI"*.
- Có quy tắc chống bịa: Chỗ nào tài liệu không có ghi *"Tài liệu không đề cập"*, trích dẫn số trang đầy đủ.

---

### BƯỚC 3: Chạy Skill Trên Hồ Sơ Thực Tế (15 phút)
Thử kích hoạt Skill bằng câu lệnh tự nhiên (không cần gõ tên skill):

```markdown
Rà soát và đối chiếu mâu thuẫn kỹ thuật giữa hai tài liệu:
1. demo/01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf
2. demo/02_Thuyet_Minh_Ban_Ve_KT102.pdf
Xuất kết quả ra file Ma_Tran_Yeu_Cau_Ky_Thuat.md và Phieu_RFI_01_Lam_Ro_Thong_Tin.md
```

**Quan sát trên màn hình:**
- Claude Code sẽ hiển thị thông báo đang kích hoạt skill: `Using skill: soat-ho-so-ky-thuat`.
- AI tự động trích xuất bảng ma trận 6 cột, chỉ ra điểm mâu thuẫn **EI 90 (Trang 42)** vs **EI 60 (Trang 15)**, và lập 01 Phiếu RFI số `RFI-ARC-001` chuẩn thể thức.

---

### BƯỚC 4: Kiểm Chứng Tính Tái Sử Dụng Thần Tốc (5 - 10 phút)
Đưa vào các cặp tài liệu tiếp theo để kiểm tra năng lực tự động hóa:
- **Test Case A (Kết cấu vách hầm):**
  ```markdown
  Rà soát và đối chiếu mâu thuẫn giữa:
  1. demo/03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf
  2. demo/04_Thuyet_Minh_Ban_Ve_Vach_Ham_KC02.pdf
  Lập bảng so sánh B35-W10 vs B30-W8 và đề xuất phương án xử lý rủi ro thấm ngầm.
  ```
- **Test Case B (Thử thách nâng cao - Sơn chống cháy thép):**
  ```markdown
  Rà soát và đối chiếu mâu thuẫn giữa:
  1. demo/05_Chi_Dan_Ky_Thuat_Son_Chong_Chay_Ket_Cau_Thep.pdf
  2. demo/06_Thuyet_Minh_Ban_Ve_Ket_Cau_Thep_KC105.pdf
  Xuất phiếu RFI và tính toán chênh lệch ngân sách giữa định mức R120 và R60.
  ```

---

## 3. TỔNG KẾT & NỘP BÀI DELIVERABLE D2
Chụp ảnh màn hình terminal Claude Code hiển thị dòng `Using skill: soat-ho-so-ky-thuat` và nộp 02 file kết quả (`Ma_Tran_Yeu_Cau_Ky_Thuat.md` và `Phieu_RFI_01_Lam_Ro_Thong_Tin.md`) vào nhóm Zalo lớp để Giảng viên và Trợ giảng chấm điểm nghiệm thu.
