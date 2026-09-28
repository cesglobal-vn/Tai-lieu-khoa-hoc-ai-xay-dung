# THƯ VIỆN PROMPT THỰC CHIẾN — BUỔI 02
## BỘ CÂU LỆNH RÀ SOÁT HỒ SƠ KỸ THUẬT, ĐÓNG GÓI SKILL & KHAI THÁC VN-AUTOCAD-SKILL
**Áp dụng cho:** Claude Code, ChatGPT Projects, Google Gemini  
**Hồ sơ thực hành:** Bộ file PDF tại thư mục `demo/`  
**Đơn vị phát triển:** CES Global AEC ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. BỘ 5 CÂU LỆNH DEMO THỊ PHẠM (DÙNG CHO GIẢNG VIÊN & HỌC VIÊN)

### Lượt 1: Tóm Tắt Khảo Sát Thô (Thấy ngay điểm hạn chế của cách hỏi thường)
```markdown
Tóm tắt giúp tôi các yêu cầu kỹ thuật đối với hệ thống cửa chống cháy trong tệp tài liệu:
demo/01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf
```

---

### Lượt 2: Bóc Tách Chi Tiết Quy Cách Cấu Tạo Vật Liệu
```markdown
Chưa đủ chi tiết. Hãy đọc kỹ Mục 5 (Điều 5.3) và bóc tách cụ thể:
1. Độ dày thép khung và thép cánh.
2. Quy cách lõi cách nhiệt (loại vật liệu, tỷ trọng kg/m³, tấm chống cháy bổ sung).
3. Các phụ kiện kim khí bắt buộc (bản lề, tay co thủy lực, thanh thoát hiểm).
4. Tiêu chuẩn thử nghiệm chịu lửa viện dẫn áp dụng.
```

---

### Lượt 3: Lập Ma Trận Yêu Cầu Kỹ Thuật & Nghiệm Thu Đầu Vào 6 Cột
```markdown
Hãy lập "Ma trận Yêu cầu Kỹ thuật và Nghiệm thu Vật tư" cho hệ cửa chống cháy thành bảng gồm 6 cột:
1. STT
2. Hạng mục / Cấu phần
3. Quy cách kỹ thuật yêu cầu
4. Tiêu chuẩn viện dẫn (TCVN / QCVN)
5. Hồ sơ / Chứng chỉ thí nghiệm nghiệm thu bắt buộc phải có
6. Vị trí trích dẫn số trang trong tài liệu gốc (Tên file, Mục, Số trang)
[RÀNG BUỘC]: Bóc tách chính xác các chỉ số kỹ thuật, không tóm tắt chung chung.
```

---

### Lượt 4: Rà Soát Mâu Thuẫn Đa Tài Liệu (Bắt lỗi vênh EI 90 vs EI 60)
```markdown
Tôi nạp thêm tệp: demo/02_Thuyet_Minh_Ban_Ve_KT102.pdf.
Hãy thực hiện đối chiếu chéo giữa file 01 (Chỉ dẫn PCCC) và file 02 (Bản vẽ KT-102) đối với cửa thoát nạn buồng thang ký hiệu D-08:
1. Chỉ ra điểm mâu thuẫn về Giới hạn chịu lửa (EI), tỷ trọng bông cách nhiệt và cấu tạo lõi.
2. Đánh giá mức độ rủi ro: Nếu Nhà thầu thi công theo bản vẽ KT-102 (EI 60) thì công trình có nguy cơ bị đình chỉ nghiệm thu PCCC khi bàn giao không?
3. Đánh giá chênh lệch chi phí giữa hai phương án.
```

---

### Lượt 5: Kiểm Tra Quy Tắc Chống Bịa (Anti-Hallucination) & Sinh Phiếu RFI
```markdown
Câu hỏi kiểm tra: Trong hai tài liệu trên, mức phạt tiền nếu nhà thầu giao chậm cửa chống cháy là bao nhiêu?
[QUY TẮC]: Chỉ dùng thông tin có trong tài liệu. Nếu tài liệu không nói, BẮT BUỘC ghi "Tài liệu không đề cập", tuyệt đối KHÔNG suy đoán.
Sau đó, hãy soạn thảo 01 "PHIẾU YÊU CẦU LÀM RÕ THÔNG TIN (RFI-ARC-001)" gửi Tư vấn thiết kế V-Design và Ban QLDA đề xuất thống nhất phương án xử lý cửa D-08 theo chuẩn EI 90 để đảm bảo nghiệm thu công trình.
```

---

## 2. PROMPT ĐÓNG GÓI TOÀN BỘ QUY TRÌNH THÀNH SKILL TRONG CLAUDE CODE

Sau khi hoàn thành chuỗi 5 câu lệnh, gõ prompt sau vào Claude Code để tự động sinh file Skill:

```markdown
Tôi thấy kết quả rà soát vừa rồi rất chuẩn xác. Bây giờ hãy đóng gói toàn bộ quy trình này thành một Skill cho tôi, để sau này khi tôi đưa bất kỳ hồ sơ kỹ thuật nào vào, bạn đều tự động chạy ra kết quả chuẩn mà tôi không cần phải chat nhiều lượt nữa.

Hãy tạo file tại: .claude/skills/soat-ho-so-ky-thuat/SKILL.md
Nội dung gồm:
1. YAML Frontmatter:
   name: soat-ho-so-ky-thuat
   description: Dùng khi cần rà soát chỉ dẫn kỹ thuật, đối chiếu mâu thuẫn giữa bản vẽ và thuyết minh, lập ma trận nghiệm thu vật tư và sinh phiếu RFI.

2. Cấu trúc xuất kết quả chuẩn 5 phần:
   - PHẦN 1: TÓM TẮT QUY CÁCH VẬT TƯ & THÔNG SỐ CỐT LÕI
   - PHẦN 2: MA TRẬN YÊU CẦU NGHIỆM THU (bảng 6 cột kèm TCVN và chứng chỉ)
   - PHẦN 3: BẢNG ĐỐI CHIẾU MÂU THUẪN (nêu rõ tài liệu, số trang, điểm sai lệch)
   - PHẦN 4: DỰ THẢO PHIẾU RFI LÀM RÕ (chuẩn thể thức hành chính kỹ thuật)
   - PHẦN 5: QUY TẮC CHỐNG BỊA (thông tin không có ghi 'tài liệu không đề cập', trích dẫn số trang đầy đủ).
```

---

## 3. PROMPT KIỂM CHỨNG TÁI SỬ DỤNG SKILL (CÁC TEST CASE MỞ RỘNG)

### Test Case 1: Đối chiếu Bê tông Vách hầm (Demo 03 & Demo 04)
```markdown
Rà soát và đối chiếu mâu thuẫn kỹ thuật giữa:
1. demo/03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf
2. demo/04_Thuyet_Minh_Ban_Ve_Vach_Ham_KC02.pdf

Yêu cầu xuất ra:
- Ma trận so sánh mác bê tông B35 vs B30, chống thấm W10 vs W8, lớp bảo vệ cốt thép 40mm vs 25mm.
- Đánh giá rủi ro thấm nứt công trình ngầm và phát sinh chi phí vật tư dự toán.
- Soạn thảo Phiếu RFI số RFI-STR-002 gửi Tư vấn Thiết kế Kết cấu.
```

### Test Case 2 (Đề bài nâng cao): Đối chiếu Sơn chống cháy kết cấu thép (Demo 05 & Demo 06)
```markdown
Rà soát và đối chiếu mâu thuẫn kỹ thuật giữa:
1. demo/05_Chi_Dan_Ky_Thuat_Son_Chong_Chay_Ket_Cau_Thep.pdf
2. demo/06_Thuyet_Minh_Ban_Ve_Ket_Cau_Thep_KC105.pdf

Yêu cầu xuất ra:
- Đối chiếu giới hạn chịu lửa R120 (Chỉ dẫn kỹ thuật) vs R60 (Bản vẽ KC-105).
- Cảnh báo rủi ro cơ quan Cảnh sát PCCC từ chối nghiệm thu công trình.
- Tính toán chênh lệch ngân sách phát sinh cho diện tích 1.450 m² thép sảnh.
- Xuất dự thảo Phiếu RFI số RFI-PCCC-003 gửi Chủ đầu tư và Tư vấn Giám sát.
```

---

## 4. BỘ LỆNH CÀI ĐẶT & KHÁM PHÁ REPO VN-AUTOCAD-SKILL (NORTH STAR)

### Cài đặt Plugin qua Claude Code:
```bash
/plugin marketplace add andyluu98/vn-autocad-skill
/plugin install vn-autocad-skill@vn-autocad
```

### Kích hoạt lệnh dựng hồ sơ mới:
```
/ho-so-moi nhà phố 4x16m, 3 tầng, 3 phòng ngủ, có gara ô tô
```

### Kích hoạt lệnh soát lỗi 3 tầng tự động:
```
/soat-ban-ve
```

### Kích hoạt xuất DWG qua AutoCAD:
```
/xuat-dwg
```
