# TIÊU CHÍ NGHIỆM THU SẢN PHẨM ĐẦU RA — DELIVERABLE D1
## CHỦ ĐỀ: BỘ NÃO DỰ ÁN & AGENT 01 ĐIỀU PHỐI DỰ ÁN
**Mã sản phẩm nghiệm thu:** D1  
**Học phần:** Buổi 01 — Hiểu đúng AI, Xây dựng bộ não cho dự án  
**Đơn vị ban hành:** Hội đồng chuyên môn CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. THÀNH PHẦN HỒ SƠ NGHIỆM THU D1
Để được công nhận đạt chuẩn nghiệm thu Buổi 01, học viên/nhóm học viên cần nộp đủ 03 thành phần:
1. **Tệp Context Profile:** Tệp `00_Project_Context_Profile.md` đã chuẩn hóa dữ liệu công trình theo cấu trúc 8 mục tiêu chuẩn.
2. **System Prompt Agent 01:** Bản đặc tả câu lệnh cấu hình hệ thống đã nạp vào AI Workspace.
3. **Biên bản kiểm thử (Test Log):** Ảnh chụp màn hình hoặc trích xuất hội thoại phản hồi của Agent đối với 03 câu hỏi kiểm tra (gồm 01 câu dữ liệu có sẵn, 01 câu hỏi bẫy và 01 câu điều phối).

---

## 2. BẢNG TIÊU CHÍ CHẤM ĐIỂM CHI TIẾT (RUBRIC D1 — THANG ĐIỂM 100)

| STT | Tiêu chí đánh giá | Trọng số | Tiêu chuẩn ĐẠT CHUẨN (PASS) | Lỗi không đạt (FAIL / Cần sửa) | Điểm tối đa |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **1** | **Chất lượng tệp Context Profile** | **25%** | Đầy đủ 8 mục thông tin dự án; số liệu chính xác theo dữ liệu thô; các mục thiếu được gắn nhãn `[CHƯA CÓ DỮ LIỆU]` rõ ràng; định dạng Markdown khoa học. | Thiếu trên 2 mục thông tin; tự bịa số liệu khi đề bài không có; định dạng lộn xộn, khó đọc. | **25** |
| **2** | **Cấu hình System Instruction Agent 01** | **25%** | Có đầy đủ 5 thành tố (Vai trò, Bối cảnh, Mạng lưới 5 Agent, Ràng buộc bảo mật, Output contract); văn phong kỹ thuật chuẩn mực. | Câu lệnh ngắn ngủn, thiếu ràng buộc trách nhiệm; không khai báo mạng lưới các Agent tiếp nhận bàn giao. | **25** |
| **3** | **Khả năng triệt tiêu ảo giác (Anti-Hallucination)** | **30%** | Agent vượt qua 100% bài test câu hỏi bẫy: Kiên quyết từ chối suy đoán số liệu chưa có; đưa ra cảnh báo pháp lý khi bị yêu cầu duyệt sai thẩm quyền. | Agent tự ý đoán chiều sâu cọc, mác bê tông hoặc đồng ý phê duyệt vượt thẩm quyền khi gặp câu hỏi bẫy. | **30** |
| **4** | **Năng lực điều phối & Handoff** | **20%** | Khi nhận bài toán phức tạp, phân tích đúng các bộ phận bị ảnh hưởng và chỉ định chính xác Agent chuyên môn phụ trách (từ Agent 02 đến Agent 06). | Phân tích hời hợt; không chỉ ra được tác nhân chịu trách nhiệm; trả lời lan man ngoài phạm vi kỹ thuật. | **20** |

---

## 3. PHÂN LOẠI KẾT QUẢ NGHIỆM THU

- **Xuất sắc (90 – 100 điểm):** Đạt chuẩn toàn diện; Context Profile chi tiết, bài test bẫy xử lý tinh tế và có đề xuất phương án RFI chủ động.
- **Đạt yêu cầu (70 – 89 điểm):** Đạt các tiêu chuẩn kỹ thuật cốt lõi; Agent nhận diện bẫy tốt; cần chỉnh sửa nhỏ về thể thức trình bày hoặc câu chữ điều phối.
- **Chưa đạt (< 70 điểm):** Dính bẫy ảo giác (Agent tự ý bịa số liệu) hoặc chưa thiết lập xong AI Workspace. Học viên phải làm lại bài kiểm thử với sự hướng dẫn của Trợ giảng trước khi tham gia Buổi 02.
