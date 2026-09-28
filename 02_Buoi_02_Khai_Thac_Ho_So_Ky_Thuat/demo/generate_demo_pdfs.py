# -*- coding: utf-8 -*-
"""
Script tạo 3 file PDF demo thực tế cho Buổi 02:
1. 01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf (Chỉ dẫn kỹ thuật PCCC - quy định EI 90)
2. 02_Thuyet_Minh_Ban_Ve_KT102.pdf (Thuyết minh & thống kê cửa KT-102 - ghi chú EI 60)
3. 03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf (Chỉ dẫn bê tông vách hầm - dùng test tái sử dụng)

100% Phông chữ: Times New Roman tuân thủ quy tắc toàn cục.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

TARGET_DIR = r"f:\GitHub\Tai-lieu-khoa-hoc-ai-xay-dung\02_Buoi_02_Khai_Thac_Ho_So_Ky_Thuat\demo"
os.makedirs(TARGET_DIR, exist_ok=True)

# Register Times New Roman fonts
TIMES_REG = r"C:\Windows\Fonts\times.ttf"
TIMES_BOLD = r"C:\Windows\Fonts\timesbd.ttf"
TIMES_ITALIC = r"C:\Windows\Fonts\timesi.ttf"
TIMES_BOLD_ITALIC = r"C:\Windows\Fonts\timesbi.ttf"

pdfmetrics.registerFont(TTFont('TimesNewRoman', TIMES_REG))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold', TIMES_BOLD))
pdfmetrics.registerFont(TTFont('TimesNewRoman-Italic', TIMES_ITALIC))
pdfmetrics.registerFont(TTFont('TimesNewRoman-BoldItalic', TIMES_BOLD_ITALIC))

def draw_header_footer(c, width, height, project_title, doc_title, page_num, total_pages):
    # Header
    c.setFont("TimesNewRoman-Italic", 9)
    c.setFillColor(colors.HexColor("#555555"))
    c.drawString(54, height - 36, project_title)
    c.drawRightString(width - 54, height - 36, doc_title)
    c.setLineWidth(0.6)
    c.setStrokeColor(colors.HexColor("#CCCCCC"))
    c.line(54, height - 42, width - 54, height - 42)

    # Footer
    c.line(54, 45, width - 54, 45)
    c.drawString(54, 32, "CES Global — Chương trình Đào tạo AI Xây dựng Chuyên sâu")
    c.drawRightString(width - 54, 32, f"Trang {page_num} / {total_pages}")

# =========================================================================
# FILE 1: CHỈ DẪN KỸ THUẬT PCCC (EI 90)
# =========================================================================
def generate_pdf_pccc():
    pdf_path = os.path.join(TARGET_DIR, "01_Chi_Dan_Ky_Thuat_PCCC_GreenTech_Tower.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4 # 595.28 x 841.89 pt

    # Trang 1: Bìa & Thông tin chung
    draw_header_footer(c, width, height, "DỰ ÁN TỔ HỢP GREENTECH TOWER", "TẬP 03: CHỈ DẪN PCCC", 1, 3)

    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM")
    c.setFont("TimesNewRoman-Bold", 10)
    c.drawString(70, height - 85, "Độc lập - Tự do - Hạnh phúc")
    c.setLineWidth(0.8)
    c.setStrokeColor(colors.HexColor("#1B365D"))
    c.line(85, height - 90, 185, height - 90)

    c.setFont("TimesNewRoman-Bold", 15)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawCentredString(width/2, height - 130, "CHỈ DẪN KỸ THUẬT HỆ THỐNG PHÒNG CHÁY CHỮA CHÁY")
    c.setFont("TimesNewRoman-Bold", 13)
    c.drawCentredString(width/2, height - 150, "& VẬT LIỆU NGĂN CHÁY CÁCH NHIỆT CÔNG TRÌNH")

    c.setFont("TimesNewRoman-Italic", 10)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawCentredString(width/2, height - 170, "(Kèm theo Hồ sơ Thiết kế Bản vẽ Thi công — Giai đoạn Đấu thầu xây dựng)")

    # Box Project Info
    c.setLineWidth(1)
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.rect(54, height - 290, width - 108, 105, fill=True, stroke=True)

    c.setFont("TimesNewRoman-Bold", 10)
    c.setFillColor(colors.HexColor("#0F172A"))
    c.drawString(68, height - 205, "Tên dự án:")
    c.drawString(68, height - 225, "Chủ đầu tư:")
    c.drawString(68, height - 245, "Tư vấn thiết kế:")
    c.drawString(68, height - 265, "Quy mô:")
    c.drawString(68, height - 280, "Số hiệu tài liệu:")

    c.setFont("TimesNewRoman", 10)
    c.drawString(160, height - 205, "Tổ hợp Thương mại, Văn phòng & Căn hộ cao cấp GreenTech Tower")
    c.drawString(160, height - 225, "Công ty Cổ phần Đầu tư Phát triển Công nghệ GreenTech")
    c.drawString(160, height - 245, "Công ty Cổ phần Tư vấn Thiết kế Kiến trúc & Xây dựng V-Design")
    c.drawString(160, height - 265, "28 tầng nổi, 03 tầng hầm — Chiều cao PCCC: 98.5 m")
    c.drawString(160, height - 280, "CDKT-PCCC-REV02 (Phát hành ngày 15/05/2026)")

    # Section 1: Tiêu chuẩn áp dụng
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 320, "MỤC 1: TIÊU CHUẨN VÀ QUY CHUẨN KỸ THUẬT PHÁP LÝ ÁP DỤNG")
    
    c.setFont("TimesNewRoman", 10)
    c.setFillColor(colors.black)
    body1 = [
        "1.1. Công trình thuộc nhóm nguy hiểm cháy theo công năng F2.2 kết hợp F4.3, bậc chịu lửa Bậc I.",
        "1.2. Hệ thống PCCC và các giải pháp thoát nạn, ngăn cháy lan phải tuân thủ nghiêm ngặt:",
        "   - QCVN 06:2022/BXD: Quy chuẩn kỹ thuật quốc gia về An toàn cháy cho nhà và công trình.",
        "   - Sửa đổi 1:2023 QCVN 06:2022/BXD ban hành kèm Thông tư số 09/2023/TT-BXD.",
        "   - TCVN 9383:2012: Thử nghiệm khả năng chịu lửa — Cửa đi và cửa ngăn cháy.",
        "   - TCVN 3890:2023: Phòng cháy chữa cháy — Phương tiện PCCC cho nhà và công trình.",
        "1.3. NGUYÊN TẮC PHÁP LÝ ƯU TIÊN:",
        "   Mọi sai khác giữa bản vẽ thiết kế kiến trúc và chỉ dẫn kỹ thuật PCCC thì chỉ dẫn kỹ thuật và",
        "   quy chuẩn an toàn cháy có cấp pháp lý cao hơn bắt buộc phải được tuân thủ tuyệt đối."
    ]
    y_pos = height - 340
    for line in body1:
        if "NGUYÊN TẮC PHÁP LÝ" in line:
            c.setFont("TimesNewRoman-Bold", 10)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 10)
            c.setFillColor(colors.black)
        c.drawString(54, y_pos, line)
        y_pos -= 17

    c.showPage()

    # Trang 2: Điều 5.3 Trọng tâm (Trang 42 trích đoạn)
    draw_header_footer(c, width, height, "DỰ ÁN TỔ HỢP GREENTECH TOWER", "TẬP 03: CHỈ DẪN PCCC", 2, 3)

    c.setFont("TimesNewRoman-Bold", 12)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "MỤC 5: YÊU CẦU ĐỐI VỚI HỆ THỐNG CỬA VÀ BỘ PHẬN NGĂN CHÁY")

    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#C0392B"))
    c.drawString(54, height - 92, "Điều 5.3: Yêu cầu đối với hệ thống cửa và vách buồng thang bộ thoát hiểm (Trang 42)")

    pccc_specs = [
        "1. Phân loại và Giới hạn chịu lửa bắt buộc:",
        "   a) Căn cứ Bảng 4 và Điều 2.4.3 của QCVN 06:2022/BXD đối với nhà có chiều cao trên 50m,",
        "      toàn bộ cửa mở vào buồng thang bộ thoát nạn không nhiễm khói (loại N1 và N2) từ tầng",
        "      hầm B3 đến tầng mái 28 BẮT BUỘC PHẢI LÀ CỬA THÉP CHỐNG CHÁY ĐẠT GIỚI HẠN CHỊU",
        "      LỬA TỐI THIỂU EI 90 (chịu lửa và cách nhiệt trong thời gian 90 phút liên tục).",
        "   b) Tuyệt đối không chấp thuận cửa có giới hạn chịu lửa EI 60 hoặc EI 45 cho các buồng thang",
        "      thoát nạn trục (2-3, C-D) và trục (6-7, A-B). Mọi đề xuất hạ cấp chịu lửa đều bị từ chối.",
        "",
        "2. Cấu tạo và Quy cách vật tư cửa chống cháy EI 90:",
        "   - Thép khung: Thép mạ điện dày 1.5mm, sơn tĩnh điện bột hoàn thiện chống ăn mòn.",
        "   - Thép cánh: Thép tấm mạ kẽm dày 1.2mm mỗi mặt, chiều dày cánh tối thiểu 50mm.",
        "   - Lõi cách nhiệt: Bông khoáng vô cơ Rockwool tỷ trọng tối thiểu 120 kg/m³ kết hợp tấm chống",
        "     cháy Magie Oxit (MgO) dày tối thiểu 5mm mỗi bên để đảm bảo tính cách nhiệt (I >= 90).",
        "   - Gioăng ngăn khói: Bố trí kép gồm gioăng cao su silicone chịu nhiệt và gioăng than chì tự",
        "     giãn nở ở nhiệt độ > 150°C đạt chuẩn BS EN 1634-3.",
        "",
        "3. Phụ kiện cơ điện và kiểm soát an toàn:",
        "   - Bản lề inox SUS 304 chịu tải tối thiểu 120kg/bộ, tối thiểu 04 bản lề/cánh.",
        "   - Tay co thủy lực tự động đóng (Door closer) đạt tiêu chuẩn EN 1154.",
        "   - Thanh thoát hiểm panic bar mở khẩn cấp loại chuyên dụng cho cửa chống cháy.",
        "",
        "4. Hồ sơ nghiệm thu & Chứng chỉ kiểm định bắt buộc trước khi đưa vào công trình:",
        "   - Giấy chứng nhận kiểm định phương tiện PCCC do Cục Cảnh sát PCCC & CNCH cấp phép.",
        "   - Biên bản thử nghiệm mẫu đốt đạt chuẩn EI 90 tại phòng thí nghiệm chuyên ngành (IBST/VILAS).",
        "   - Chứng chỉ xuất xưởng (CO/CQ) của thép tấm và vật liệu lõi cách nhiệt Rockwool."
    ]

    y_pos = height - 114
    for line in pccc_specs:
        if "BẮT BUỘC PHẢI LÀ CỬA THÉP CHỐNG CHÁY" in line or "EI 90" in line:
            c.setFont("TimesNewRoman-Bold", 10)
            c.setFillColor(colors.HexColor("#C0392B"))
        elif line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4."):
            c.setFont("TimesNewRoman-Bold", 10.5)
            c.setFillColor(colors.HexColor("#1B365D"))
        else:
            c.setFont("TimesNewRoman", 9.5)
            c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(54, y_pos, line)
        y_pos -= 15.5

    c.showPage()

    # Trang 3: Quy định bảo hành & nghiệm thu
    draw_header_footer(c, width, height, "DỰ ÁN TỔ HỢP GREENTECH TOWER", "TẬP 03: CHỈ DẪN PCCC", 3, 3)

    c.setFont("TimesNewRoman-Bold", 12)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "MỤC 8: NGHIỆM THU VẬT TƯ ĐẦU VÀO VÀ BÀN GIAO CÔNG TRÌNH")

    body3 = [
        "8.1. Kiểm tra nghiệm thu vật tư đầu vào tại hiện trường:",
        "   - Kỹ sư Giám sát của Chủ đầu tư và Tư vấn Giám sát có quyền yêu cầu Nhà thầu cắt lấy mẫu",
        "     ngẫu nhiên 01 bộ cửa thành phẩm tại công trường để kiểm tra cấu tạo lõi và tỷ trọng bông khoáng.",
        "   - Toàn bộ chi phí thí nghiệm lại do Nhà thầu chịu trách nhiệm chi trả.",
        "",
        "8.2. Nghiệm thu hoàn thành với Cơ quan Cảnh sát PCCC:",
        "   - Nhà thầu chính và nhà thầu phụ cửa chống cháy có trách nhiệm phối hợp với Ban QLDA cung cấp",
        "     toàn bộ hồ sơ kiểm định gốc phục vụ buổi nghiệm thu thực địa của Cục Cảnh sát PCCC & CNCH.",
        "   - Nếu công trình bị đình chỉ hoặc không đạt nghiệm thu do sai khác chỉ tiêu EI của cửa thoát hiểm,",
        "     Nhà thầu phải chịu toàn bộ phí tổn phát sinh và chi phí khắc phục thay thế 100%."
    ]
    y_pos = height - 95
    for line in body3:
        if line.startswith("8.1") or line.startswith("8.2"):
            c.setFont("TimesNewRoman-Bold", 10.5)
            c.setFillColor(colors.HexColor("#1B365D"))
        else:
            c.setFont("TimesNewRoman", 10)
            c.setFillColor(colors.black)
        c.drawString(54, y_pos, line)
        y_pos -= 16

    c.save()
    print("Generated PDF 1:", pdf_path)

# =========================================================================
# FILE 2: THUYẾT MINH BẢN VẼ KIẾN TRÚC KT-102 (GHI CHÚ EI 60 - GÂY MÂU THUẪN)
# =========================================================================
def generate_pdf_kt102():
    pdf_path = os.path.join(TARGET_DIR, "02_Thuyet_Minh_Ban_Ve_KT102.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    draw_header_footer(c, width, height, "DỰ ÁN GREENTECH TOWER", "BẢN VẼ KT-102: THỐNG KÊ CỬA", 1, 2)

    c.setFont("TimesNewRoman-Bold", 14)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "HỒ SƠ THIẾT KẾ BẢN VẼ THI CÔNG — GÓI THẦU KIẾN TRÚC & HOÀN THIỆN")
    c.setFont("TimesNewRoman-Bold", 12)
    c.drawString(54, height - 90, "BẢN VẼ SỐ: KT-102 (PHÁT HÀNH REV.02 — TRANG 15)")

    c.setFont("TimesNewRoman-Italic", 10)
    c.drawString(54, height - 108, "Đơn vị lập: Trung tâm Thiết kế Kiến trúc V-Design — Chủ nhiệm đồ án: KTS. Nguyễn Hoàng Nam")

    # Table Thống kê cửa
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 135, "BẢNG THỐNG KÊ CỬA ĐI TẦNG 1 ĐẾN TẦNG 5 (DOOR SCHEDULE)")

    # Table Header
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.rect(54, height - 170, width - 108, 25, fill=True, stroke=False)
    c.setFont("TimesNewRoman-Bold", 9)
    c.setFillColor(colors.white)
    c.drawString(62, height - 155, "MÃ CỬA")
    c.drawString(115, height - 155, "VỊ TRÍ BỐ TRÍ")
    c.drawString(225, height - 155, "KÍCH THƯỚC")
    c.drawString(290, height - 155, "SỐ LƯỢNG")
    c.drawString(345, height - 155, "GIỚI HẠN CHỊU LỬA")
    c.drawString(455, height - 155, "VẬT LIỆU CHÍNH")

    # Table rows
    doors = [
        ("D-01", "Sảnh chính tầng 1", "2400 x 2800", "02 bộ", "Không yêu cầu", "Khung nhôm kính cường lực 12mm"),
        ("D-05", "Khu vệ sinh nam/nữ", "800 x 2200", "20 bộ", "Không yêu cầu", "Gỗ MDF chống ẩm phủ Melamine"),
        ("D-08", "Cửa thang thoát nạn trục (2-3)", "1200 x 2200", "10 bộ", "EI 60 (60 phút)", "Thép mạ kẽm 1.2mm, Rockwool 100"),
        ("D-12", "Phòng kỹ thuật điện tầng", "900 x 2200", "05 bộ", "EI 45 (45 phút)", "Thép tấm 1.0mm sơn tĩnh điện")
    ]

    y_table = height - 195
    for code, pos, size, qty, ei, mat in doors:
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.line(54, y_table - 6, width - 54, y_table - 6)

        c.setFont("TimesNewRoman-Bold", 9.5)
        if code == "D-08":
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFillColor(colors.HexColor("#0F172A"))
        c.drawString(62, y_table, code)

        c.setFont("TimesNewRoman", 9)
        c.setFillColor(colors.black)
        c.drawString(115, y_table, pos)
        c.drawString(225, y_table, size)
        c.drawString(290, y_table, qty)

        if code == "D-08":
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 9)
            c.setFillColor(colors.black)
        c.drawString(345, y_table, ei)

        c.setFont("TimesNewRoman", 8.5)
        c.setFillColor(colors.black)
        c.drawString(455, y_table, mat)
        y_table -= 25

    # Highlight box for D-08
    c.setLineWidth(1)
    c.setStrokeColor(colors.HexColor("#E11D48"))
    c.setFillColor(colors.HexColor("#FFF1F2"))
    c.rect(54, height - 380, width - 108, 75, fill=True, stroke=True)

    c.setFont("TimesNewRoman-Bold", 10.5)
    c.setFillColor(colors.HexColor("#E11D48"))
    c.drawString(68, height - 325, "GHI CHÚ KỸ THUẬT RIÊNG CHO CỬA D-08 TRÊN BẢN VẼ KT-102 (REV.02):")

    c.setFont("TimesNewRoman", 9.5)
    c.setFillColor(colors.HexColor("#0F172A"))
    c.drawString(68, height - 345, "- Giới hạn chịu lửa quy định: EI 60 (Khả năng ngăn cháy 60 phút theo tiêu chuẩn TCVN 9383:2012).")
    c.drawString(68, height - 362, "- Lõi cửa: Bông khoáng Rockwool tỷ trọng 100 kg/m³, không yêu cầu tấm cách nhiệt MgO bổ sung.")
    c.drawString(68, height - 378, "- Phụ kiện: Thanh panic bar Hafele, 03 bản lề chịu lực SUS 304, tay co thủy lực Hafele.")

    # QS Notes
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 410, "GHI CHÚ CỦA BỘ PHẬN ĐẤU THẦU & DỰ TOÁN (QS NOTE):")
    qs_notes = [
        "1. Đơn giá lập dự toán mời thầu hiện đang tính theo định mức cửa thép EI 60: 2.450.000 VNĐ/m².",
        "2. Toàn bộ 10 bộ cửa D-08 tầng 1 đến tầng 5 có tổng diện tích: 10 x (1.2m x 2.2m) = 26.4 m².",
        "3. Thành tiền dự toán tạm tính: 26.4 m² x 2.450.000 VNĐ = 64.680.000 VNĐ.",
        "4. CẢNH BÁO TIỀM ẨN: Có sự sai lệch giữa tiêu chuẩn thiết kế kiến trúc (EI 60) và tiêu chuẩn",
        "   Chỉ dẫn PCCC tập 3 (yêu cầu EI 90). Nếu chuyển sang EI 90, chi phí sẽ tăng lên 3.850.000 VNĐ/m²."
    ]
    y_qs = height - 430
    for line in qs_notes:
        if "CẢNH BÁO" in line:
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 9.5)
            c.setFillColor(colors.black)
        c.drawString(54, y_qs, line)
        y_qs -= 16

    c.save()
    print("Generated PDF 2:", pdf_path)

# =========================================================================
# FILE 3: CHỈ DẪN KỸ THUẬT BÊ TÔNG VÁCH HẦM (DÙNG TEST TÁI SỬ DỤNG SKILL)
# =========================================================================
def generate_pdf_concrete():
    pdf_path = os.path.join(TARGET_DIR, "03_Chi_Dan_Thi_Cong_Be_Tong_Vach_Ham.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    draw_header_footer(c, width, height, "DỰ ÁN GREENTECH TOWER", "TẬP 02: KẾT CẤU PHẦN NGẦM", 1, 2)

    c.setFont("TimesNewRoman-Bold", 14)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "CHỈ DẪN KỸ THUẬT THI CÔNG VÀ NGHIỆM THU BÊ TÔNG VÁCH HẦM")
    c.setFont("TimesNewRoman-Bold", 11)
    c.drawString(54, height - 90, "MỤC 3.2: BÊ TÔNG CỐT THÉP VÁCH TẦNG HẦM B1, B2, B3 (TRANG 48)")

    c.setFont("TimesNewRoman-Italic", 9.5)
    c.drawString(54, height - 108, "Tiêu chuẩn viện dẫn: TCVN 5574:2018, TCVN 3118:1993, TCVN 4453:1995")

    # Specs table
    c.setLineWidth(1)
    c.setStrokeColor(colors.HexColor("#CBD5E1"))
    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.rect(54, height - 260, width - 108, 140, fill=True, stroke=True)

    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(68, height - 138, "YÊU CẦU CHỈ TIÊU KỸ THUẬT CỐT LÕI:")

    concrete_items = [
        ("Cường độ nén (Mác thiết kế):", "B35 (tương đương Mác 450 daN/cm²), mẫu lập phương 150x150mm."),
        ("Cấp độ chống thấm nước:", "W10 (theo tiêu chuẩn TCVN 3118:1993, thí nghiệm áp lực thủy tĩnh)."),
        ("Độ sụt tại hiện trường:", "16 ± 2 cm (bơm bê tông thương phẩm), duy trì không phân tầng."),
        ("Phụ gia bắt buộc:", "Phụ gia giảm nước kéo dài thời gian ninh kết + Phụ gia bù co ngót trương nở nhẹ."),
        ("Lớp bê tông bảo vệ cốt thép:", "C_min = 40 mm (tiếp xúc trực tiếp môi trường đất ẩm theo TCVN 5574:2018)."),
        ("Tỷ lệ đúc mẫu thí nghiệm:", "01 tổ mẫu (3 viên) cho mỗi 50 m³ bê tông vách, nén thử R7 và R28 ngày.")
    ]

    y_c = height - 160
    for lbl, val in concrete_items:
        c.setFont("TimesNewRoman-Bold", 9.5)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawString(68, y_c, lbl)
        c.setFont("TimesNewRoman", 9.5)
        c.setFillColor(colors.HexColor("#334155"))
        c.drawString(235, y_c, val)
        y_c -= 18

    # Documentation requirement
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 285, "HỒ SƠ NGHIỆM THU ĐẦU VÀO BẮT BUỘC:")

    docs = [
        "1. Chứng chỉ xuất xưởng trạm trộn bê tông thương phẩm cho từng chuyến xe bồn.",
        "2. Kết quả thí nghiệm nén mẫu tuổi 7 ngày và 28 ngày đạt cường độ tối thiểu 100% R28.",
        "3. Phiếu thử nghiệm độ chống thấm W10 do phòng Las-XD hợp chuẩn cấp phép.",
        "4. Biên bản nghiệm thu lắp dựng cốt thép và nghiệm thu cốt pha kín khít trước khi đổ bê tông."
    ]
    y_d = height - 305
    for line in docs:
        c.setFont("TimesNewRoman", 9.5)
        c.drawString(68, y_d, line)
        y_d -= 17

    c.save()
    print("Generated PDF 3:", pdf_path)

if __name__ == "__main__":
    generate_pdf_pccc()
    generate_pdf_kt102()
    generate_pdf_concrete()
    print("ALL 3 PDF DEMO FILES CREATED SUCCESSFULLY!")
