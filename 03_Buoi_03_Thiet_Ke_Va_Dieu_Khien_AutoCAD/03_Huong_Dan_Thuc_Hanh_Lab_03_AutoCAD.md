# TÀI LIỆU HƯỚNG DẪN BÀI THỰC HÀNH LAB 03
## LẬP DESIGN BRIEF & TỰ ĐỘNG HÓA DỰNG BẢN VẼ TRÊN AUTOCAD BẰNG AI
**Thời lượng thực hành:** 55 phút  
**Sản phẩm nghiệm thu (Deliverable D3):** Design Brief + File mã nguồn AutoLISP + Bản vẽ AutoCAD (.dwg/.pdf) + Checklist rà soát  
**Đơn vị đào tạo:** CES Global ([https://aec.cesglobal.com.vn/](https://aec.cesglobal.com.vn/))

---

## 1. MỤC TIÊU BÀI LAB 03
- Chuyển hóa yêu cầu kinh doanh của Chủ đầu tư thành tài liệu Design Brief hoàn chỉnh cho tầng 1 GreenTech Tower.
- Kích hoạt **Agent 03** để sinh đoạn mã lập trình AutoLISP tự động hóa dựng hệ kết cấu lưới trục và cột.
- Thực hành nạp mã lệnh vào phần mềm AutoCAD trên máy tính cá nhân và chứng thực kết quả vẽ tự động trong 1 giây.
- Rà soát bản vẽ CAD theo Checklist kỹ thuật trước khi bàn giao cho bộ phận QS bóc tách khối lượng ở Buổi 04.

---

## 2. NỘI DUNG MÃ NGUỒN AUTOLISP MẪU ĐƯỢC AI SINH RA

Dưới đây là đoạn mã AutoLISP chuẩn đã được kiểm thử để học viên đối chiếu hoặc tải về sử dụng:

```lisp
;;; =========================================================================
;;; CHUONG TRINH AUTOLISP: TU DONG VE HE LUOI TRUC VA COT DUC GREENTECH TOWER
;;; Phap danh lenh: VE_HETRUC_COT
;;; Ban quyen: CES Global - Dao tao AI Agent trong Ky thuat & Xay dung
;;; =========================================================================

(defun c:VE_HETRUC_COT ( / old_os old_layer old_echo x_dist y_dist x_count y_count i j pt_orig pt1 pt2 pt_col)
  ;; 1. Luu tru va thiet lap moi truong an toan
  (setq old_os (getvar "OSMODE"))
  (setq old_layer (getvar "CLAYER"))
  (setq old_echo (getvar "CMDECHO"))
  (setvar "CMDECHO" 0)
  (setvar "OSMODE" 0) ; Tat bat diem de tranh sai lech toa do tuyet doi

  ;; 2. Khoi tao cac Layer chuyen dung neu chua co
  (if (null (tblsearch "LAYER" "L_TRUC"))
    (command "-LAYER" "M" "L_TRUC" "C" "1" "" "")
  )
  (if (null (tblsearch "LAYER" "L_COT"))
    (command "-LAYER" "M" "L_COT" "C" "4" "" "")
  )
  (if (null (tblsearch "LAYER" "L_TEXT"))
    (command "-LAYER" "M" "L_TEXT" "C" "3" "" "")
  )

  ;; 3. Dinh nghia thong so hinh hoc (Don vi: mm)
  (setq pt_orig '(0.0 0.0 0.0)) ; Toa do goc toa do (Giao truc 1 va A)
  (setq x_dist 8400.0)          ; Buoc cot phuong X: 8.4m
  (setq y_dist 8400.0)          ; Buoc cot phuong Y: 8.4m
  (setq x_count 5)              ; 5 truc so: 1, 2, 3, 4, 5
  (setq y_count 6)              ; 6 truc chu: A, B, C, D, E, F
  (setq col_w 800.0)            ; Be rong cot: 800mm
  (setq col_h 800.0)            ; Chieu dai cot: 800mm

  ;; 4. Ve cac duong truc doc (Phuong Y - Truc so 1 den 5)
  (setvar "CLAYER" "L_TRUC")
  (setq i 0)
  (while (< i x_count)
    (setq pt1 (list (+ (car pt_orig) (* i x_dist)) (- (cadr pt_orig) 2000.0) 0.0))
    (setq pt2 (list (+ (car pt_orig) (* i x_dist)) (+ (cadr pt_orig) (* (1- y_count) y_dist) 2000.0) 0.0))
    (command "LINE" pt1 pt2 "")
    ;; Ve ky hieu truc tron o dau
    (command "CIRCLE" (list (car pt1) (- (cadr pt1) 600.0) 0.0) 600.0)
    (setvar "CLAYER" "L_TEXT")
    (command "TEXT" "M" (list (car pt1) (- (cadr pt1) 600.0) 0.0) 400.0 "0" (itoa (1+ i)))
    (setvar "CLAYER" "L_TRUC")
    (setq i (1+ i))
  )

  ;; 5. Ve cac duong truc ngang (Phuong X - Truc chu A den F)
  (setq j 0)
  (setq list_name '("A" "B" "C" "D" "E" "F"))
  (while (< j y_count)
    (setq pt1 (list (- (car pt_orig) 2000.0) (+ (cadr pt_orig) (* j y_dist)) 0.0))
    (setq pt2 (list (+ (car pt_orig) (* (1- x_count) x_dist) 2000.0) (+ (cadr pt_orig) (* j y_dist)) 0.0))
    (command "LINE" pt1 pt2 "")
    ;; Ve ky hieu truc tron o dau
    (command "CIRCLE" (list (- (car pt1) 600.0) (cadr pt1) 0.0) 600.0)
    (setvar "CLAYER" "L_TEXT")
    (command "TEXT" "M" (list (- (car pt1) 600.0) (cadr pt1) 0.0) 400.0 "0" (nth j list_name))
    (setvar "CLAYER" "L_TRUC")
    (setq j (1+ j))
  )

  ;; 6. Ve he cot be tong 800x800mm tai cac nut giao
  (setvar "CLAYER" "L_COT")
  (setq i 0)
  (while (< i x_count)
    (setq j 0)
    (while (< j y_count)
      (setq pt_col (list (+ (car pt_orig) (* i x_dist)) (+ (cadr pt_orig) (* j y_dist)) 0.0))
      ;; Ve hinh chu nhat cot tam tai pt_col
      (command "RECTANG" 
               (list (- (car pt_col) (/ col_w 2.0)) (- (cadr pt_col) (/ col_h 2.0)) 0.0)
               (list (+ (car pt_col) (/ col_w 2.0)) (+ (cadr pt_col) (/ col_h 2.0)) 0.0)
      )
      (setq j (1+ j))
    )
    (setq i (1+ i))
  )

  ;; 7. Khoi phuc bien moi truong he thong
  (setvar "OSMODE" old_os)
  (setvar "CLAYER" old_layer)
  (setvar "CMDECHO" old_echo)
  (command "ZOOM" "E")
  (princ "\n[CES GLOBAL] - DA DUNG HOAN TAT 30 COT VA HE LUOI TRUC KET CAU!")
  (princ)
)
```

---

## 3. CÁC BƯỚC THỰC HÀNH TỪNG BƯỚC (STEP-BY-STEP)

### Bước 1: Soạn Thảo Design Brief Bằng Agent 03 (Thời gian: 15 phút)
1. Trong Workspace, gọi **Agent 03** bằng câu lệnh Prompt 3.1.
2. Kiểm tra tài liệu Design Brief được sinh ra: Đảm bảo có đầy đủ cơ cấu diện tích sảnh đón, khu thương mại, thang máy và luồng giao thông.
3. Lưu kết quả thành file `Design_Brief_Tang_1_GreenTech.md`.

### Bước 2: Tải Mã Lệnh AutoLISP Về Máy (Thời gian: 10 phút)
1. Sao chép đoạn mã AutoLISP ở Mục 2 (hoặc yêu cầu Agent 03 sinh mã tùy chỉnh).
2. Mở trình soạn thảo Notepad, dán toàn bộ đoạn mã vào.
3. Chọn **File ➔ Save As**, đặt tên file là `Ve_HeTruc_Cot_GreenTech.lsp` (Lưu ý: tại mục *Save as type*, chọn *All Files (*.*)* và mã hóa *UTF-8* hoặc *ANSI*).

### Bước 3: Nạp Và Thực Thi Mã Trên AutoCAD (Thời gian: 15 phút)
1. Khởi động phần mềm **AutoCAD** trên máy tính.
2. Tạo một bản vẽ mới từ mẫu chuẩn mét: Gõ lệnh `NEW` ➔ Chọn `acadiso.dwt`.
3. Tại thanh Command Line của AutoCAD, gõ lệnh: `APPLOAD` rồi nhấn **Enter**.
4. Cửa sổ *Load/Unload Applications* hiện ra, duyệt tìm đến tệp `Ve_HeTruc_Cot_GreenTech.lsp` vừa lưu ➔ Nhấn nút **Load** (nhìn dòng thông báo phía dưới hiển thị *"Ve_HeTruc_Cot_GreenTech.lsp successfully loaded"*). Nhấn **Close**.
5. Trên dòng lệnh AutoCAD, gõ lệnh: `VE_HETRUC_COT` rồi nhấn **Enter**.
6. **Quan sát kết quả:** Toàn bộ hệ thống 5 trục số, 6 trục chữ, các vòng tròn định danh trục và 30 cột bê tông 800x800mm xuất hiện chuẩn xác 100% trên màn hình trong nháy mắt!

### Bước 4: Kiểm Tra Kích Thước & Rà Soát Checklist (Thời gian: 15 phút)
1. Dùng lệnh `DIST` kiểm tra khoảng cách giữa hai trục liên tiếp: Đảm bảo đúng `8400.0000`.
2. Dùng lệnh `DIST` kiểm tra cạnh cột: Đảm bảo đúng `800.0000 x 800.0000`.
3. Lưu bản vẽ thành tệp `Mat_Bang_Luoi_Truc_Cot_GreenTech.dwg` và xuất một bản PDF in thử.
4. Chạy Prompt 3.5 để lập bảng Checklist rà soát chất lượng bản vẽ.

---

## 4. TỔNG KẾT SẢN PHẨM NỘP BÀI LAB 03
Học viên nộp:
1. File `Design_Brief_Tang_1_GreenTech.md`
2. File mã nguồn `Ve_HeTruc_Cot_GreenTech.lsp`
3. Ảnh chụp màn hình AutoCAD hiển thị bản vẽ vừa được dựng tự động.
4. Bảng `Checklist_Ra_Soat_Ban_Ve_CAD.md`.
