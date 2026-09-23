# THƯ VIỆN PROMPT THỰC CHIẾN — BUỔI 06
## BỘ CÂU LỆNH ĐIỀU PHỐI ĐA TÁC NHÂN (MULTI-AGENT ORCHESTRATION) & SOP DOANH NGHIỆP
**Áp dụng cho:** Hệ sinh thái 6 AI Agent trên ChatGPT, Claude, Gemini  
**Đơn vị phát triển:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. MASTER ORCHESTRATION PROMPT (CÂU LỆNH CHỈ HUY TỐI CAO)

*Hướng dẫn sử dụng:* Sử dụng câu lệnh này khi bạn (vai trò Giám đốc Dự án / Chỉ huy trưởng) tiếp nhận một bài toán lớn và muốn kích hoạt toàn bộ chuỗi 6 Agent phối hợp giải quyết đồng thời.

```markdown
[VAI TRÒ]: CHỈ HUY TRƯỞNG HỆ THỐNG ĐA TÁC NHÂN (MASTER AI ORCHESTRATOR).
[BỐI CẢNH DỰ ÁN]: Dự án Tòa nhà phức hợp GreenTech Tower đang trong giai đoạn triển khai thì phát sinh yêu cầu đặc biệt từ Chủ đầu tư:
"{Dán nội dung yêu cầu phát sinh của Chủ đầu tư vào đây, ví dụ: Chuyển đổi 500m² sàn tầng 3 thành Phòng Máy chủ / Data Center chuẩn Tier III}".
[NHIỆM VỤ ĐIỀU PHỐI LIÊN TÁC NHÂN]:
Hãy tự động kích hoạt và phân công nhiệm vụ cho mạng lưới 5 Agent chuyên môn theo chu trình khép kín:
1. GIAO CHO AGENT 02 (Hồ sơ kỹ thuật):
   - Rà soát các tiêu chuẩn Việt Nam và quốc tế liên quan (TCVN 2737:2023 về tải trọng sàn $1200\text{ kg/m²}$, TCVN 9385 về chống sét tiếp địa, tiêu chuẩn PCCC khí sạch FM200).
   - Lập danh mục các điều khoản kỹ thuật cần làm rõ với Tư vấn thiết kế.
2. GIAO CHO AGENT 03 (Thiết kế & CAD):
   - Đề xuất giải pháp phân khu mặt bằng: Phòng Server, phòng UPS ắc quy, phòng điều khiển NOC và sảnh đệm.
   - Sinh đoạn mã AutoLISP hoặc phác thảo lưới dầm phụ gia cường sàn bê tông.
3. GIAO CHO AGENT 04 (QS & Chi phí):
   - Lập danh mục bóc tách tiên lượng khối lượng phát sinh (Hệ sàn nâng chịu tải nặng, vách ngăn chống cháy EI 120, hệ chữa cháy khí FM200, hệ thống điều hòa chính xác PAC).
   - Ước tính tổng chi phí phát sinh bổ sung và phân tích biến động so với gói thầu ban đầu.
4. GIAO CHO AGENT 05 (Tiến độ & Báo cáo):
   - Phân tích ảnh hưởng của công tác gia cường sàn đến mốc tiến độ cất nóc.
   - Lập kế hoạch tiến độ Lookahead chi tiết để bù đắp tiến độ (tăng ca ban đêm, đẩy nhanh đặt hàng thiết bị nhập khẩu).
5. GIAO CHO AGENT 06 (QA/QC & An toàn HSE):
   - Nhận diện các mối nguy hiểm đặc thù: Rò rỉ khí chữa cháy FM200, an toàn cháy nổ giàn ắc quy axít chì, tải trọng tập trung cục bộ khi vận chuyển máy biến áp.
   - Cập nhật các rủi ro này vào Bảng Risk Register và xuất Checklist nghiệm thu phòng máy.
[TỔNG HỢP CUỐI CÙNG]:
Agent 01 tổng hợp toàn bộ kết quả trên thành một bản "TỜ TRÌNH PHƯƠNG ÁN XỬ LÝ PHÁT SINH KỸ THUẬT & CHI PHÍ" gửi Ban Giám đốc phê duyệt.
```

---

## 2. PROMPT BAN HÀNH QUY TRÌNH VẬN HÀNH CHUẨN (SOP GENERATOR)

Dùng để chuẩn hóa quy chế ứng dụng AI trong công ty xây dựng, trình Tổng Giám đốc ký ban hành.

```markdown
[VAI TRÒ]: Chuyên gia Tư vấn Chuyển đổi số & Kiến trúc Doanh nghiệp Xây dựng.
[BỐI CẢNH]: Công ty Xây dựng đang đưa bộ công cụ AI Workspace và 6 AI Agent vào ứng dụng thực tế tại tất cả các công trường và phòng ban chuyên môn.
[NHIỆM VỤ]:
Hãy soạn thảo "QUY TRÌNH VẬN HÀNH TIÊU CHUẨN (SOP) — ỨNG DỤNG TRÍ TUỆ NHÂN TẠO TRONG QUẢN LÝ DỰ ÁN XÂY DỰNG".
[CẤU TRÚC TÀI LIỆU SOP BẮT BUỘC]:
1. MỤC ĐÍCH & PHẠM VI ÁP DỤNG (Áp dụng cho Phòng Đấu thầu, Thiết kế, QS, Ban Chỉ huy).
2. QUY ĐỊNH BẢO MẬT & BẢO TOÀN DỮ LIỆU CÔNG TY:
   - Các loại dữ liệu tuyệt đối không được nạp vào AI công cộng (Chiết tính đơn giá bí mật, thông tin khách hàng, chữ ký số).
   - Quy định sử dụng tính năng Data Masking trước khi xử lý.
3. QUY TRÌNH KIỂM SOÁT CHẤT LƯỢNG 3 CỬA (HUMAN-IN-THE-LOOP):
   - Cửa 1: AI sinh bản thảo (Draft).
   - Cửa 2: Kỹ sư chuyên môn trực tiếp kiểm tra 100% công thức, kích thước và cơ sở pháp lý.
   - Cửa 3: Trưởng phòng / Chỉ huy trưởng thẩm định và ký phát hành.
4. CHẾ TÀI VÀ TRÁCH NHIỆM PHÁP LÝ:
   - Khẳng định rõ: AI không chịu trách nhiệm pháp lý. Kỹ sư ký tên trên hồ sơ chịu trách nhiệm 100% trước Pháp luật và Chủ đầu tư.
[THỂ THỨC]: Chuẩn thể thức văn bản quản trị nội bộ doanh nghiệp.
```

---

## 3. PROMPT TỔNG HỢP ĐỒ ÁN TỐT NGHIỆP CAPSTONE PROJECT

Dùng để xuất bản báo cáo tổng kết toàn khóa học gửi Hội đồng chuyên môn CES Global.

```markdown
[VAI TRÒ]: Trưởng nhóm Đồ án Tốt nghiệp / Giám đốc Quản lý Dự án GreenTech Tower.
[BỐI CẢNH]: Nhóm học viên vừa hoàn thành toàn bộ chuỗi tác nghiệp 6 buổi đào tạo ứng dụng AI Agent trong Kỹ thuật & Xây dựng.
[NHIỆM VỤ]:
Hãy biên soạn bản "BÁO CÁO TỔNG KẾT ĐỒ ÁN TỐT NGHIỆP: HỆ THỐNG AI AGENT ĐIỀU HÀNH DỰ ÁN GREENTECH TOWER".
[NỘI DUNG BÁO CÁO GỒM 6 PHẦN TƯƠNG ỨNG 6 ĐẦU RA]:
- PHẦN 1: BỘ NÃO DỰ ÁN (Context Profile & Agent 01 Orchestrator).
- PHẦN 2: KHAI THÁC HỒ SƠ THẦU & XỬ LÝ MÂU THUẪN (Ma trận yêu cầu kỹ thuật & Phiếu RFI-ARC-001 về cửa chống cháy).
- PHẦN 3: THIẾT KẾ & TỰ ĐỘNG HÓA AUTOCAD (Design Brief & Đoạn mã AutoLISP vẽ hệ 30 cột lưới trục).
- PHẦN 4: TIÊN LƯỢNG BOQ & KIỂM SOÁT CHI PHÍ (Bảng BOQ 103.68m3 bê tông cột & Ma trận đối soát 3 bảng chào thầu).
- PHẦN 5: ĐIỀU ĐỘ HIỆN TRƯỜNG & AN TOÀN (Nhật ký thi công tự động từ tin nhắn Zalo & Bảng Risk Register).
- PHẦN 6: KẾT QUẢ VẬN HÀNH CHUỖI MULTI-AGENT VÀ ĐỀ XUẤT LỘ TRÌNH TRIỂN KHAI TẠI DOANH NGHIỆP.
[VĂN PHONG]: Chuyên nghiệp, cô đọng, giàu sức thuyết phục đối với Ban Lãnh đạo cấp cao.
```
