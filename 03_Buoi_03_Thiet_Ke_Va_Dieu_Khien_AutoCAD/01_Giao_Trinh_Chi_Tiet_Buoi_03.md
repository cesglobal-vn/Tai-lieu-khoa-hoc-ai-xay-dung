# GIÁO TRÌNH CHI TIẾT — BUỔI 03
## TỪ YÊU CẦU CÔNG NĂNG ĐẾN Ý TƯỞNG THIẾT KẾ & ĐIỀU KHIỂN AUTOCAD
**Chuyên đề:** AI hỗ trợ lập Nhiệm vụ thiết kế, phân khu công năng và sinh mã lệnh điều khiển AutoCAD  
**Thời lượng chuẩn:** 150 phút (30% Lý thuyết & Kiến trúc — 70% Thực hành thực chiến)  
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. MỤC TIÊU BÀI HỌC (LEARNING OBJECTIVES)

Sau khi hoàn thành Buổi 03, học viên đạt được các năng lực chuyên môn sau:
1. **Chuyển hóa bài toán kinh doanh thành Nhiệm vụ thiết kế (Design Brief):** Sử dụng AI để hệ thống hóa các yêu cầu của Chủ đầu tư thành bảng cơ cấu diện tích, tiêu chuẩn kỹ thuật áp dụng và sơ đồ dây chuyền công năng tối ưu.
2. **Khai thác AI sinh ý tưởng không gian & Phối cảnh:** Soạn thảo các câu lệnh (prompts) chuyên biệt để mô tả vật liệu, ánh sáng, hình khối kiến trúc phục vụ trình diễn phương án sơ bộ.
3. **Làm chủ kỹ thuật điều khiển AutoCAD bằng AI (AutoLISP & Script):** Hiểu rõ cơ chế AI biên dịch yêu cầu hình học thành đoạn mã lập trình AutoLISP (`.lsp`) hoặc tập lệnh Command Script (`.scr`), giúp tự động hóa 100% các tác vụ vẽ lặp lại: vẽ lưới trục, bố trí cột, tạo layer, đặt kiểu kích thước (dimstyle) và đánh số phòng.
4. **Quy trình kiểm soát an toàn bản vẽ CAD:** Thực hành nguyên tắc Human-in-the-loop: Kiểm thử script trên file nháp, rà soát tỷ lệ bản vẽ, kiểm tra va chạm lưới trục trước khi tích hợp vào hồ sơ chính thức.
5. **Cấu hình Agent 03:** Thiết lập **Agent 03 - Hỗ trợ thiết kế & CAD (Design & CAD Assistant)** sẵn sàng hỗ trợ các kiến trúc sư và kỹ sư thiết kế.

---

## 2. TIẾN TRÌNH GIẢNG DẠY 150 PHÚT (PEDAGOGICAL TIMELINE)

```
00:00 ─── 00:15 (15') : Ôn tập Buổi 02 & Nghiệm thu sản phẩm D2 (Phiếu RFI & Ma trận kỹ thuật)
00:15 ─── 00:45 (30') : Kiến thức cốt lõi: Từ Design Brief đến Ý tưởng kiến trúc & Cơ chế AI điều khiển AutoCAD
00:45 ─── 01:15 (30') : Giảng viên thị phạm (Live Demo): Yêu cầu Agent 03 viết AutoLISP vẽ lưới trục cột GreenTech Tower trên AutoCAD
01:15 ─── 02:10 (55') : Học viên thực hành Lab 03: Lập Design Brief, chạy AutoLISP trên AutoCAD cá nhân & Xuất bản vẽ
02:10 ─── 02:30 (20') : Trình chiếu các bản vẽ xuất ra từ script AI, rà soát lỗi cú pháp LISP & Giao nhiệm vụ Buổi 04
```

---

## 3. KIẾN THỨC CỐT LÕI (CORE KNOWLEDGE — 30 PHÚT)

### 3.1. Quy Trình Thiết Kế Ý Tưởng Hỗ Trợ Bởi AI

Trong quy trình truyền thống, từ ý tưởng của Chủ đầu tư đến bản vẽ sơ bộ thường mất từ 1-2 tuần làm việc thủ công. Với sự trợ giúp của Agent 03, quy trình được rút ngắn còn vài giờ:

```mermaid
flowchart LR
    A["Nhu cầu thô của Chủ đầu tư"] --> B["Agent 03: Soạn Design Brief & Cơ cấu diện tích"]
    B --> C["Agent 03: Đề xuất 02 Phương án mặt bằng sơ bộ"]
    C --> D["Agent 03: Sinh mã AutoLISP / Script cho AutoCAD"]
    D --> E["Kỹ sư: Chạy script trên AutoCAD & Tinh chỉnh bản vẽ"]
```

### 3.2. Bản Chất Kỹ Thuật: Làm Sao AI Điều Khiển Được AutoCAD?

Người dùng không cần biết lập trình chuyên sâu, nhưng cần hiểu cơ chế tương tác:
1. **Tập lệnh AutoCAD Script (`.scr`):**
   - Là một tệp văn bản thuần túy chứa chuỗi các lệnh của AutoCAD được thực thi tuần tự từ trên xuống dưới hệt như người dùng gõ vào dòng Command Line.
   - Thích hợp cho: Tạo hệ thống Layer chuẩn công ty, thiết lập màu sắc, nét in (lineweight), kiểu chữ (text style) và kiểu kích thước (dimstyle).
2. **Ngôn ngữ AutoLISP (`.lsp`):**
   - Là ngôn ngữ lập trình tích hợp sẵn trong AutoCAD từ hàng chục năm qua.
   - Cho phép xử lý logic tính toán hình học: Vòng lặp vẽ hàng loạt cột theo tọa độ $(X, Y)$, tự động tính khoảng cách bước cột, tự động gắn nhãn chữ (Text Tag) và tự động đóng block.
   - AI (ChatGPT, Claude) cực kỳ thành thạo cú pháp LISP vì đã được huấn luyện trên hàng triệu dòng mã nguồn AutoCAD mở.

**Cấu trúc một hàm AutoLISP do AI sinh ra:**
```lisp
;; Ham tu dong ve luoi truc va cot vuong
(defun c:VeHeTrucCot ()
  (setq old_os (getvar "OSMODE"))
  (setvar "OSMODE" 0) ; Tat bat diem de tranh sai toa do khi ve
  (command "-LAYER" "M" "L_TRUC" "C" "1" "" "") ; Tao layer truc mau do
  ;; Vong lap ve cac duong truc X cach nhau 8400mm
  ;; ...
  (setvar "OSMODE" old_os)
  (princ "\nHoan tat ve he truc cot!")
  (princ)
)
```

### 3.3. Nguyên Tắc An Toàn Khi Sử Dụng Script AI Trên Bản Vẽ Kỹ Thuật

- **Quy tắc 1:** Luôn mở một bản vẽ trắng (`New Drawing - acadiso.dwt`) để chạy thử nghiệm mã lệnh trước; tuyệt đối không chạy script trực tiếp trên tệp bản vẽ hồ sơ đang phát hành.
- **Quy tắc 2:** Luôn yêu cầu AI thêm đoạn mã lưu và khôi phục biến hệ thống (`OSMODE`, `CMDECHO`, `CLAYER`) để không làm thay đổi các thiết lập mặc định của AutoCAD sau khi script chạy xong.
- **Quy tắc 3:** Kỹ sư phải là người kiểm tra lại kích thước bằng lệnh `DIST` hoặc `DLI` để xác nhận độ chuẩn xác của tọa độ.

---

## 4. HƯỚNG DẪN THỊ PHẠM TRỰC TIẾP (LIVE DEMO — 30 PHÚT)

Giảng viên thao tác trên màn hình:
1. Mở cửa sổ ChatGPT/Claude có **Agent 03**.
2. Nhập lệnh yêu cầu: *"Dự án GreenTech Tower có mặt bằng hình chữ nhật kích thước 42m x 33.6m. Hãy viết một đoạn mã AutoLISP để vẽ hệ lưới trục kết cấu gồm 6 trục chữ (A đến F, cách nhau 8.4m) và 5 trục số (1 đến 5, cách nhau 8.4m). Tại mỗi giao điểm lưới trục, vẽ một cột bê tông tiết diện 800x800mm, tô hatch bê tông đặc và tự động gắn dim tổng thể."*
3. Agent 03 sinh mã AutoLISP hoàn chỉnh trong 15 giây.
4. Giảng viên lưu mã vào tệp `VeHeTrucGreenTech.lsp`.
5. Mở AutoCAD, gõ lệnh `APPLOAD`, chọn tệp `.lsp`, sau đó gõ lệnh tắt để thực thi. Hệ thống lưới trục và 30 cột bê tông xuất hiện chính xác trên AutoCAD trong vòng 1 giây!
6. Giảng viên hướng dẫn cách rà soát layer và dimstyle chuẩn hồ sơ kỹ thuật.

---

## 5. NỘI DUNG BÀI THỰC HÀNH LAB 03 (55 PHÚT)

Học viên làm theo tài liệu [03_Huong_Dan_Thuc_Hanh_Lab_03_AutoCAD.md](file:///f:/GitHub/Tai-lieu-khoa-hoc-ai-xay-dung/03_Buoi_03_Thiet_Ke_Va_Dieu_Khien_AutoCAD/03_Huong_Dan_Thuc_Hanh_Lab_03_AutoCAD.md):
- Thiết lập System Prompt cho Agent 03.
- Soạn thảo Design Brief cho khu vực Sảnh thương mại tầng 1.
- Yêu cầu Agent sinh mã AutoLISP và chạy trực tiếp trên phần mềm AutoCAD cá nhân.
- Xuất bản vẽ CAD kết quả và lập Checklist rà soát bản vẽ.

---

## 6. NGHIỆM THU VÀ BÀI TẬP VỀ NHÀ (20 PHÚT)

- Chấm điểm sản phẩm D3 theo [04_Tieu_Chi_Nghiem_Thu_San_Pham_D3.md](file:///f:/GitHub/Tai-lieu-khoa-hoc-ai-xay-dung/03_Buoi_03_Thiet_Ke_Va_Dieu_Khien_AutoCAD/04_Tieu_Chi_Nghiem_Thu_San_Pham_D3.md).
- Chuẩn bị cho Buổi 04: Từ bản vẽ hệ lưới trục và cột vừa vẽ, học viên sẽ dùng Agent 04 để bóc tách khối lượng bê tông và cốt thép.
