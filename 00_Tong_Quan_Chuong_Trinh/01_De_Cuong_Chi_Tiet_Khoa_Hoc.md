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

### Buổi 04: AGENT VÀ SUBAGENT, CLAUDE.MD AN TOÀN CHO KỸ SƯ, TỪ BẢN VẼ AUTOCAD ĐẾN MÔ HÌNH 3D BLENDER
- **Mục tiêu:** Phân biệt và sử dụng Agent, Subagent; thiết lập CLAUDE.md Global với các nguyên tắc an toàn dữ liệu cho kỹ sư; cài MCP Blender; đi trọn đường ống bản vẽ AutoCAD (vẽ bằng MCP) sang mô hình 3D Blender có nội thất, tách tầng, đúng kích thước theo bản vẽ.
- **Nội dung lý thuyết (55'):**
  - Agent và Subagent: ngữ cảnh riêng, giới hạn công cụ, chạy song song; vị trí file `.claude/agents/` và `~/.claude/agents/`.
  - CLAUDE.md 3 tầng (Global, dự án, thư mục con); 6 nguyên tắc an toàn: cấm xóa, tự sao lưu `_backup/`, đánh số file, đọc trước sửa sau, chống bịa số liệu, hỏi trước khi gửi ra ngoài. Phân biệt nội quy (CLAUDE.md) và chặn cứng (hook).
  - Kiến trúc MCP Blender (`vn-mcp-blender`): Claude, MCP server, addon trong Blender qua cổng 9877.
  - Đường ống 4 chặng: vẽ AutoCAD qua MCP, xuất DXF, đọc bản vẽ thành file mô tả, dựng Blender. Bản vẽ "máy đọc được": layer đúng đối tượng, chiều cao nằm trong bảng.
- **Nội dung thực hành (70'):**
  - **Lab 04:** Tạo subagent soát 3 cặp hồ sơ song song; gài và thử CLAUDE.md an toàn; dựng nhà phố lô 7x20m (3 tầng, tum, nội thất) từ bản vẽ AutoCAD vào Blender, tách tầng, render; sửa một thông số trên bản vẽ rồi dựng lại, kiểm chéo số cửa với bảng thống kê.
- **Sản phẩm nghiệm thu (Deliverable D4):**
  - File subagent + CLAUDE.md đã gài nguyên tắc và kết quả thử + Ảnh phối cảnh và ảnh bung tầng + Cặp ảnh trước, sau khi sửa bản vẽ kèm kiểm chéo số cửa.
- **Ghi chú:** Nội dung BOQ, dự toán và kiểm soát chi phí (bản cũ của Buổi 04) giữ nguyên tại thư mục `04_Buoi_04_Boc_Tach_Khoi_Luong_BOQ_Du_Toan`, chờ xếp vào buổi sau.

---

### Buổi 05: ĐỘI NGŨ AGENT CHO HỒ SƠ NHÀ PHỐ: AGENT CHUYÊN TRÁCH, RENDER AI ĐỔI PHONG CÁCH VÀ BÓC KHỐI LƯỢNG
- **Mục tiêu:** Lập đội agent chuyên trách cho văn phòng thiết kế nhỏ, giao nhiều agent làm cùng một lượt; cài MCP ChatGPT tạo ảnh để đổi phong cách ảnh render Blender mà giữ đúng kiến trúc; bóc khối lượng phần thô từ chính file mô tả bản vẽ ra Excel BOQ.
- **Nội dung lý thuyết (45'):**
  - Agent chuyên trách (có file trong `.claude/agents/`, dùng lại) và subagent tạm (giao theo đầu việc); giới hạn quyền bằng trường `tools`.
  - Phối hợp nhiều agent cùng một lượt: song song cho việc độc lập, nối chuỗi cho việc phải chờ, gộp một báo cáo. Agent team: thử nghiệm, chỉ có ở terminal.
  - MCP ChatGPT tạo ảnh (`chatgpt-image-mcp`), chế độ `ref_mode="render"`; ảnh AI để trao đổi phong cách, không phải hồ sơ kỹ thuật; rủi ro tài khoản khi dùng đăng nhập ChatGPT web.
  - Bóc khối lượng từ file mô tả bản vẽ: diễn giải, nguồn, tách khối lượng thiết kế, hao hụt, khối lượng mua; không tự điền đơn giá; các bẫy trừ cửa hai lần, chiều cao tường.
- **Nội dung thực hành (70'):**
  - **Lab 05:** Tạo 3 agent `boc-khoi-luong`, `kiem-tra-khoi-luong` (chỉ đọc), `render-phong-cach`; thử phá agent chỉ đọc; đội agent chạy song song render 2 phong cách và bóc khối lượng nhà phố lô 7x20m, agent kiểm tra soát lại.
- **Sản phẩm nghiệm thu (Deliverable D5):**
  - 3 file agent + Ảnh đổi phong cách kèm bảng so sánh với ảnh Blender + Excel BOQ phần thô (sheet BOQ, kiểm chéo cửa, giả thiết) + Báo cáo đội agent.
- **Ghi chú:** Nội dung quản lý dự án, tiến độ, QA/QC, HSE (bản cũ của Buổi 05) và hệ thống 6 agent doanh nghiệp (bản cũ của Buổi 06) chuyển vào `_backup\` ở gốc tài liệu ngày 10/10/2026, chờ xếp vào khóa nâng cao.

---

### Buổi 06: RÁP TRỌN QUY TRÌNH: TỪ Ý TƯỞNG CỦA CHỦ NHÀ ĐẾN BỘ HỒ SƠ GỬI KHÁCH (ĐỒ ÁN CUỐI KHÓA)
- **Mục tiêu:** Chạy trọn dây chuyền 7 chặng trên căn nhà của học viên: đầu vào, chốt thông số, bản vẽ AutoCAD, mô hình Blender, phối cảnh AI, khối lượng, hồ sơ gửi khách; đặt 3 cổng duyệt người; xử lý một yêu cầu đổi ý của chủ nhà; đóng gói quy trình thành skill.
- **Nội dung lý thuyết (20'):**
  - Bàn giao giữa các chặng bằng file; thư mục hồ sơ chuẩn cho một công trình; thư mục phát hành `yymmdd_lan-N` không sửa, không xóa.
  - Ba cổng duyệt người: chốt thông số, duyệt bản vẽ, duyệt trước khi gửi khách; AI không tự gửi ra ngoài.
  - Điều phối đội agent bằng CLAUDE.md dự án, `/plan`, `/goal`; nguyên tắc "bản vẽ là nguồn" khi chủ nhà đổi ý.
- **Nội dung thực hành (95'):**
  - **Lab 06, đồ án cuối khóa:** Học viên chạy 7 chặng trên căn nhà của mình, phát hành hồ sơ lần 1; xử lý tình huống đổi ý, phát hành lần 2 kèm so sánh khối lượng; đóng gói skill `ho-so-nha-pho`.
- **Sản phẩm nghiệm thu (Deliverable D6, Capstone Project):**
  - Thư mục công trình chuẩn + Hồ sơ phát hành lần 1 và lần 2 (PDF gộp gửi khách, thư nháp) + Nhật ký quy trình có 3 cổng duyệt + Skill hoặc sổ prompt dùng lại.

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
