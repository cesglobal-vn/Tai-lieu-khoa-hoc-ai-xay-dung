# ĐỀ CƯƠNG CHI TIẾT CHƯƠNG TRÌNH ĐÀO TẠO
## ỨNG DỤNG AI AGENT TRONG KỸ THUẬT & XÂY DỰNG
*(Ban hành kèm theo chương trình đào tạo chuyên sâu của CES Global)*

---

## 1. MỤC TIÊU VÀ CHUẨN ĐẦU RA CỦA KHÓA HỌC

### 1.1. Mục tiêu đào tạo (Course Objectives)
Khóa học nhằm trang bị cho Kỹ sư, Kiến trúc sư, Chỉ huy trưởng, Chuyên viên QS, QA/QC và Ban Quản lý dự án xây dựng:
1. **Tư duy kiến trúc hệ thống AI:** Chuyển đổi từ cách dùng AI dạng "chat ngẫu hứng" sang việc thiết lập **AI Workspace dự án** với bối cảnh kỹ thuật chặt chẽ.
2. **Kỹ năng làm chủ 6 AI Agent chuyên môn:** Tự tay cấu hình, huấn luyện và kiểm soát 6 tác nhân AI phục vụ toàn bộ vòng đời dự án: Quản lý hồ sơ, Hỗ trợ thiết kế, Bóc tách khối lượng & dự toán, Quản lý tiến độ - báo cáo, Kiểm soát chất lượng & an toàn.
3. **Khai thác công cụ chuyên ngành không cần lập trình:** Nắm vững phương pháp điều khiển AutoCAD bằng AutoLISP/Script sinh từ AI, bóc tách hồ sơ PDF bằng OCR và tối ưu hóa bảng tính BOQ trên Excel.
4. **Vận hành quy trình Human-in-the-loop (HITL):** Thiết lập ranh giới an toàn thông tin, kiểm soát rủi ro ảo giác (Zero-hallucination) và đảm bảo tính pháp lý của hồ sơ kỹ thuật.

### 1.2. Chuẩn đầu ra năng lực (Competency Standards)
Sau khi hoàn thành khóa học, học viên có khả năng:
- **PLO 1:** Xây dựng và quản trị được một AI Workspace chuẩn hóa cho một công trình xây dựng thực tế.
- **PLO 2:** Trích xuất, tóm tắt và đối chiếu tự động hàng trăm trang hồ sơ mời thầu, tiêu chuẩn kỹ thuật trong vòng dưới 10 phút.
- **PLO 3:** Chuyển hóa yêu cầu công năng (Design Brief) thành phương án mặt bằng và sinh mã lệnh điều khiển AutoCAD để vẽ tự động các cấu kiện mẫu.
- **PLO 4:** Bóc tách khối lượng từ hồ sơ và lập bảng BOQ tiêu chuẩn, thực hiện so sánh đối chiếu đa báo giá nhà thầu với độ chính xác cao.
- **PLO 5:** Tự động hóa việc tổng hợp nhật ký thi công, lập biên bản họp và xây dựng bảng quản trị rủi ro (Risk Register) cho công trường.
- **PLO 6:** Vận hành luồng trao đổi thông tin liên tác nhân (Multi-Agent Workflow), bàn giao dữ liệu gãy gọn giữa các phòng ban trong doanh nghiệp.

---

## 2. CƠ CẤU PHÂN PHỔI THỜI GIAN MỖI BUỔI HỌC (CHUẨN 150 PHÚT)

Mỗi buổi học kéo dài 150 phút (2 giờ 30 phút), áp dụng triệt để phương pháp giảng dạy tích cực theo tỷ lệ **30% Lý thuyết nền tảng & Kiến trúc — 70% Thực hành tác nghiệp**:

| Khoảng thời gian | Phân kỳ đào tạo | Nội dung tác nghiệp trọng tâm | Phương pháp sư phạm |
| :---: | :--- | :--- | :--- |
| **00:00 - 00:15 (15')** | **Khởi động & Đánh giá** | Ôn tập kiến thức mấu chốt buổi trước, rà soát bài tập về nhà của học viên, giải đáp khúc mắc và đặt bài toán cho buổi học mới. | Q&A tương tác, chữa bài mẫu điển hình |
| **00:15 - 00:45 (30')** | **Kiến thức cốt lõi** | Trình bày nguyên lý kỹ thuật, phương pháp luận quản trị dự án, ranh giới pháp lý, cấu trúc Prompt và cơ chế vận hành của Agent. | Thuyết trình kết hợp sơ đồ tư duy (Visual Diagram) |
| **00:45 - 01:15 (30')** | **Thị phạm trực tiếp (Live Demo)** | Giảng viên thao tác trực tiếp trên hồ sơ dự án mẫu thực tế: Nạp dữ liệu, ra lệnh, xử lý lỗi kỹ thuật phát sinh và đối soát. | Giảng viên chia sẻ màn hình, thị phạm từng bước |
| **01:15 - 02:10 (55')** | **Thực hành chuyên sâu (Hands-on Lab)** | Học viên tự tay thao tác trên máy tính cá nhân theo tài liệu Lab Guide: Tạo Agent, viết lệnh, xuất sản phẩm nghiệm thu. | Giảng viên & Trợ giảng hỗ trợ 1-1, sửa lỗi tại chỗ |
| **02:10 - 02:30 (20')** | **Nghiệm thu & Giao bài tập** | Trình bày chéo sản phẩm giữa các nhóm, chấm điểm nhanh theo Bảng Rubric, tổng kết cạm bẫy cần tránh và giao đề bài về nhà. | Thuyết trình nhóm, đánh giá đồng đẳng (Peer Review) |

---

## 3. KHUNG CHƯƠNG TRÌNH CHI TIẾT 6 BUỔI HỌC

### Buổi 01: HIỂU ĐÚNG AI — XÂY DỰNG BỘ NÃO CHO DỰ ÁN
- **Mục tiêu:** Định hình tư duy kiến trúc AI, thiết lập môi trường làm việc an toàn và cấu hình Agent 01 điều phối toàn bộ dự án.
- **Nội dung lý thuyết (30'):**
  - Phân định rạch ròi 3 cấp độ: AI Chatbot (hỏi đáp đơn thuần) vs AI Workspace (kho dữ liệu dự án) vs AI Agent (tác nhân có mục tiêu và quy trình).
  - Vấn đề bảo mật dữ liệu công trình: Nguyên tắc Zero-training trên tài khoản Doanh nghiệp/Nhóm, kỹ thuật che giấu thông tin nhạy cảm (Data Masking).
  - Bản chất hiện tượng "ảo giác" (Hallucination) và cơ chế khóa chặt dữ liệu: Không đủ dữ liệu phải hỏi lại, tuyệt đối không bịa số liệu.
- **Nội dung thực hành (55'):**
  - **Lab 01:** Thiết lập Hồ sơ bối cảnh dự án (Project Context Profile) cho công trình mẫu. Cấu hình System Prompt cho **Agent 01 - Điều phối dự án (Project Orchestrator)**.
- **Sản phẩm nghiệm thu (Deliverable D1):**
  - Bản Context Profile hoàn chỉnh + System Instruction Agent 01 + Checklist kiểm soát tính chân thực của câu trả lời.

---

### Buổi 02: HỎI ĐÁP HÀNG TRĂM TRANG HỒ SƠ KỸ THUẬT TRONG VÀI PHÚT
- **Mục tiêu:** Biến hồ sơ thầu, tiêu chuẩn kỹ thuật (TCVN, ASTM, Eurocode) và chỉ dẫn kỹ thuật dày cộp thành kho tri thức tra cứu tức thì.
- **Nội dung lý thuyết (30'):**
  - Xử lý dữ liệu đầu vào hỗn hợp: PDF scan, bản vẽ chuyển đổi, bảng biểu Excel, văn bản Word; công nghệ OCR và ranh giới khả năng đọc của AI.
  - Kỹ thuật Grounded Search & Retrieval: Cơ chế trích xuất có dẫn nguồn số trang, điều khoản cụ thể.
  - Phương pháp rà soát mâu thuẫn giữa Hồ sơ mời thầu (HSMT), Chỉ dẫn kỹ thuật (Technical Specs) và Bản vẽ thiết kế.
- **Nội dung thực hành (55'):**
  - **Lab 02:** Nạp hồ sơ kỹ thuật vào hệ thống. Sử dụng **Agent 02 - Hồ sơ kỹ thuật (Document & Spec Auditor)** để lập Ma trận yêu cầu kỹ thuật (Requirements Matrix), so sánh 2 phiên bản sửa đổi và soạn thảo Phiếu yêu cầu làm rõ thông tin (RFI).
- **Sản phẩm nghiệm thu (Deliverable D2):**
  - Ma trận yêu cầu kỹ thuật dự án mẫu + Phiếu RFI chuẩn hóa gửi Tư vấn thiết kế/Chủ đầu tư.

---

### Buổi 03: TỪ YÊU CẦU CÔNG NĂNG ĐẾN Ý TƯỞNG THIẾT KẾ & ĐIỀU KHIỂN AUTOCAD
- **Mục tiêu:** Ứng dụng AI từ khâu tiền khả thi, lập nhiệm vụ thiết kế, đề xuất phương án không gian đến việc sinh mã lệnh tự động hóa trên AutoCAD.
- **Nội dung lý thuyết (30'):**
  - Quy trình từ Nhiệm vụ thiết kế (Design Brief) đến bảng cơ cấu diện tích và sơ đồ dây chuyền công năng.
  - Kỹ thuật tạo prompt mô tả hình khối, không gian, vật liệu kiến trúc để sinh ảnh phối cảnh concept phục vụ thuyết minh ban đầu.
  - **Điểm nhấn đặc biệt:** Nguyên lý điều khiển AutoCAD bằng AI thông qua sinh mã AutoLISP (.lsp) hoặc Script (.scr) tự động dựng lưới trục, vẽ cột, gắn dim, tạo layer và chèn block tiêu chuẩn.
- **Nội dung thực hành (55'):**
  - **Lab 03:** Sử dụng **Agent 03 - Hỗ trợ thiết kế & CAD (Design & CAD Assistant)** để sinh 02 phương án mặt bằng sơ bộ và viết đoạn mã AutoLISP tự động vẽ lưới trục kết cấu + mặt bằng tường trên AutoCAD.
- **Sản phẩm nghiệm thu (Deliverable D3):**
  - Design Brief chuẩn hóa + Bảng phân tích 02 phương án ý tưởng + File script AutoLISP chạy thành công trên AutoCAD + Checklist kiểm tra bản vẽ.

---

### Buổi 04: AI CHO BOQ, DỰ TOÁN VÀ KIỂM SOÁT CHI PHÍ ĐẦU TƯ
- **Mục tiêu:** Tự động hóa công tác lập danh mục bóc tách, chuẩn hóa bảng tiên lượng khối lượng (BOQ) và kiểm soát sai lệch ngân sách thi công.
- **Nội dung lý thuyết (30'):**
  - Kỹ thuật bóc tách khối lượng từ thuyết minh kỹ thuật và bảng thống kê bản vẽ; ranh giới an toàn: AI không tự "đoán" khối lượng khi thiếu kích thước chi tiết.
  - Phương pháp chuẩn hóa mã hiệu công tác, phân loại hạng mục theo định mức và tiêu chuẩn đo bóc hiện hành.
  - Kỹ thuật đối soát báo giá thầu phụ/nhà cung cấp: Bóc tách đơn giá, điều kiện thương mại, thời gian giao hàng và phát hiện các chi phí ẩn.
- **Nội dung thực hành (55'):**
  - **Lab 04:** Triển khai **Agent 04 - Kỹ sư QS & Chi phí (Cost & QS Specialist)** để rà soát bản vẽ kết cấu/hoàn thiện, lập bảng tính BOQ chuẩn hóa trên Excel và phân tích chênh lệch giữa 3 báo giá nhà thầu phụ.
- **Sản phẩm nghiệm thu (Deliverable D4):**
  - Bảng BOQ Excel chuẩn hóa công thức + Bảng phân tích so sánh chào giá đa nhà thầu + Bảng cảnh báo vượt ngân sách đầu tư.

---

### Buổi 05: TRỢ LÝ AI QUẢN LÝ DỰ ÁN, TIẾN ĐỘ, QA/QC & AN TOÀN LAO ĐỘNG
- **Mục tiêu:** Thiết lập hệ thống giám sát hiện trường thông minh: Lập tiến độ thi công tuần, tự động hóa nhật ký công trường, kiểm soát lỗi thi công và quản trị rủi ro an toàn (HSE).
- **Nội dung lý thuyết (30'):**
  - Phương pháp phân rã công việc (WBS) và lập kế hoạch thi công cuốn chiếu (Lookahead Schedule).
  - Tự động hóa tổng hợp dữ liệu từ ghi chú công trường thành Nhật ký thi công và Biên bản họp giao ban công trường chuyên nghiệp.
  - Ứng dụng AI phân tích hình ảnh và biên bản hiện trường để rà soát lỗi thi công (Defect Tracking) và lập bảng danh mục rủi ro (Risk Register).
- **Nội dung thực hành (55'):**
  - **Lab 05:** Cấu hình **Agent 05 - Tiến độ & Báo cáo** và **Agent 06 - QA/QC & HSE** để tạo báo cáo tiến độ tuần, sinh nhật ký thi công từ dữ liệu thô và xuất Checklist kiểm tra an toàn giàn giáo/cốt thép.
- **Sản phẩm nghiệm thu (Deliverable D5):**
  - Báo cáo tuần dự án chuẩn format + Mẫu nhật ký thi công tự động + Checklist nghiệm thu hiện trường + Bảng Risk Register dự án.

---

### Buổi 06: XÂY DỰNG ĐỘI NGŨ AI AGENT CHO DOANH NGHIỆP XÂY DỰNG
- **Mục tiêu:** Kết nối toàn bộ 6 Agent thành một quy trình tự động hóa khép kín (Multi-Agent Ecosystem) và thực hiện Đồ án tốt nghiệp khóa học.
- **Nội dung lý thuyết (30'):**
  - Thiết kế luồng phối hợp đa tác nhân (Multi-Agent Orchestration): Luồng chuyển giao dữ liệu (Handoff Protocol) từ Hồ sơ thầu ➔ Thiết kế ➔ QS ➔ Hiện trường ➔ Quản lý.
  - Chiến lược bảo mật dữ liệu doanh nghiệp, phân quyền truy cập theo vai trò (Role-based Access Control - RBAC).
  - Quy trình vận hành tiêu chuẩn (SOP) khi áp dụng AI trong doanh nghiệp xây dựng: Kiểm soát chất lượng 3 vòng.
- **Nội dung thực hành (55'):**
  - **Lab 06 - Đồ án tốt nghiệp:** Học viên/Nhóm học viên đóng vai Ban Quản trị dự án, vận hành hệ thống 6 Agent để xử lý một tình huống thay đổi thiết kế và phát sinh khối lượng khẩn cấp của công trình.
- **Sản phẩm nghiệm thu (Deliverable D6 - Capstone Project):**
  - Bản báo cáo Đồ án tốt nghiệp: Bộ AI Workspace tích hợp 6 Agent + Thư viện Promptbook doanh nghiệp + Video/Biên bản trình diễn luồng vận hành.

---

## 4. YÊU CẦU CÔNG CỤ VÀ HẠ TẦNG KỸ THUẬT

Để tham gia khóa học hiệu quả, học viên cần chuẩn bị:
1. **Thiết bị cá nhân:**
   - Laptop/PC chạy hệ điều hành Windows 10/11 hoặc macOS, tối thiểu 8GB RAM (khuyến nghị 16GB RAM).
   - Kết nối Internet ổn định phục vụ truy cập các nền tảng đám mây.
2. **Tài khoản phần mềm AI:**
   - Ít nhất 01 tài khoản trả phí trong các nền tảng: ChatGPT Plus/Team (GPT-4o), Claude Pro (Claude 3.5 Sonnet) hoặc Google Gemini Advanced.
   - Tài khoản Google miễn phí để sử dụng Google Drive, Google Sheets và Google NotebookLM.
3. **Phần mềm chuyên ngành:**
   - AutoCAD (phiên bản 2020 trở lên, bản quyền hoặc dùng thử) để thực hành chạy mã AutoLISP/Script.
   - Microsoft Excel hoặc Google Sheets để làm việc với bảng tính BOQ và dữ liệu ngân sách.
