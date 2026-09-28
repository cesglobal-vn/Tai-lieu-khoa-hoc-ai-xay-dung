# -*- coding: utf-8 -*-
"""
Script tạo thêm các file PDF demo thực tế cho Buổi 02:
1. 04_Thuyet_Minh_Ban_Ve_Vach_Ham_KC02.pdf (Thuyết minh & bản vẽ kết cấu vách hầm - đối chiếu với File 03)
2. 05_Chi_Dan_Ky_Thuat_Son_Chong_Chay_Ket_Cau_Thep.pdf (Chỉ dẫn kỹ thuật sơn chống cháy - Yêu cầu R120)
3. 06_Thuyet_Minh_Ban_Ve_Ket_Cau_Thep_KC105.pdf (Thuyết minh bản vẽ kết cấu thép - Ghi chú R60)

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
# FILE 04: THUYẾT MINH & BẢN VẼ KẾT CẤU VÁCH HẦM KC-02 (ĐỐI CHIẾU VỚI FILE 03)
# =========================================================================
def generate_pdf_kc02_vach_ham():
    pdf_path = os.path.join(TARGET_DIR, "04_Thuyet_Minh_Ban_Ve_Vach_Ham_KC02.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4 # 595.28 x 841.89 pt

    draw_header_footer(c, width, height, "DỰ ÁN GREENTECH TOWER", "BẢN VẼ KC-02: VÁCH HẦM", 1, 2)

    c.setFont("TimesNewRoman-Bold", 13)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "HỒ SƠ THIẾT KẾ BẢN VẼ THI CÔNG — GÓI THẦU KẾT CẤU PHẦN NGẦM")
    c.setFont("TimesNewRoman-Bold", 12)
    c.drawString(54, height - 90, "BẢN VẼ SỐ: KC-02 (MẶT BẰNG & CHI TIẾT VÁCH HẦM B1-B3 — REV.02 — TRANG 22)")

    c.setFont("TimesNewRoman-Italic", 9.5)
    c.drawString(54, height - 108, "Đơn vị tư vấn thiết kế kết cấu: V-Design Structural — Chủ trì kết cấu: ThS. KS. Phạm Văn Hùng")

    # Table Thống kê vách hầm
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 132, "BẢNG THỐNG KÊ CẤU KIỆN VÁCH TẦNG HẦM (BASEMENT RETAINING WALL SCHEDULE)")

    # Table Header
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.rect(54, height - 165, width - 108, 24, fill=True, stroke=False)
    c.setFont("TimesNewRoman-Bold", 9)
    c.setFillColor(colors.white)
    c.drawString(62, height - 151, "MÃ CẤU KIỆN")
    c.drawString(135, height - 151, "VỊ TRÍ TRỤC")
    c.drawString(225, height - 151, "CHIỀU DÀY (mm)")
    c.drawString(320, height - 151, "MÁC BÊ TÔNG GHI BẢN VẼ")
    c.drawString(455, height - 151, "CHỐNG THẤM GHI CHÚ")

    # Table rows
    walls = [
        ("SW-01", "Vách ngoài trục A, D (Tầng B1)", "350 mm", "B30 (Mác 400 daN/cm²)", "W8 (TCVN 3118)"),
        ("SW-02", "Vách ngoài trục 1, 8 (Tầng B2)", "400 mm", "B30 (Mác 400 daN/cm²)", "W8 (TCVN 3118)"),
        ("SW-03", "Vách hầm B3 tiếp xúc đài cọc", "450 mm", "B30 (Mác 400 daN/cm²)", "W8 (TCVN 3118)"),
        ("IW-01", "Vách lõi thang máy trong nhà", "300 mm", "B35 (Mác 450 daN/cm²)", "Không yêu cầu")
    ]

    y_table = height - 188
    for code, pos, thick, f_mark, wp in walls:
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.line(54, y_table - 6, width - 54, y_table - 6)

        c.setFont("TimesNewRoman-Bold", 9.5)
        if code.startswith("SW"):
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFillColor(colors.HexColor("#0F172A"))
        c.drawString(62, y_table, code)

        c.setFont("TimesNewRoman", 9)
        c.setFillColor(colors.black)
        c.drawString(135, y_table, pos)
        c.drawString(225, y_table, thick)

        if code.startswith("SW"):
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 9)
            c.setFillColor(colors.black)
        c.drawString(320, y_table, f_mark)

        if "W8" in wp:
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 9)
            c.setFillColor(colors.black)
        c.drawString(455, y_table, wp)
        y_table -= 24

    # Highlight box for Conflict
    c.setLineWidth(1)
    c.setStrokeColor(colors.HexColor("#E11D48"))
    c.setFillColor(colors.HexColor("#FFF1F2"))
    c.rect(54, height - 380, width - 108, 90, fill=True, stroke=True)

    c.setFont("TimesNewRoman-Bold", 10.5)
    c.setFillColor(colors.HexColor("#E11D48"))
    c.drawString(68, height - 310, "GHI CHÚ KỸ THUẬT QUAN TRỌNG TRÊN BẢN VẼ KC-02 (REV.02):")

    c.setFont("TimesNewRoman", 9.5)
    c.setFillColor(colors.HexColor("#0F172A"))
    c.drawString(68, height - 328, "1. Bê tông vách ngoài tầng hầm B1, B2, B3 sử dụng mác B30, cấp chống thấm nước W8.")
    c.drawString(68, height - 344, "2. Chiều dày lớp bê tông bảo vệ cốt thép vách hầm: C = 25 mm (cho cả mặt trong và mặt ngoài).")
    c.drawString(68, height - 360, "3. Thép chịu lực chính: Thép thanh vằn CB400-V, bước thép d16 a150.")

    # QS Notes
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 405, "CẢNH BÁO ĐỐI SOÁT HỒ SƠ & DỰ TOÁN (QS & QA/QC AUDIT):")
    qs_notes = [
        "1. XUNG ĐỘT TIÊU CHUẨN KỸ THUẬT: Chỉ dẫn kỹ thuật Tập 02 (Trang 48) BẮT BUỘC vách hầm đạt",
        "   cường độ B35 và cấp chống thấm W10, lớp bảo vệ C_min = 40 mm (theo TCVN 5574:2018).",
        "2. SAI LỆCH TRÊN BẢN VẼ: Bản vẽ KC-02 chỉ ghi B30, W8 và lớp bảo vệ C = 25 mm.",
        "3. ĐÁNH GIÁ RỦI RO: Nếu đổ bê tông theo bản vẽ (C=25mm, W8), vách hầm chịu áp lực nước ngầm",
        "   lớn sẽ có nguy cơ thấm dột và rỉ sét cốt thép nghiêm trọng sau 2-3 năm vận hành!",
        "4. TÁC ĐỘNG CHI PHÍ: Chênh lệch đơn giá giữa Bê tông B30-W8 và B35-W10 là khoảng 110.000 VNĐ/m³.",
        "   Với khối lượng 1.850 m³ vách hầm, chi phí phát sinh vật tư là: 203.500.000 VNĐ."
    ]
    y_qs = height - 425
    for line in qs_notes:
        if "XUNG ĐỘT" in line or "SAI LỆCH" in line or "RỦI RO" in line:
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 9.5)
            c.setFillColor(colors.black)
        c.drawString(54, y_qs, line)
        y_qs -= 16

    c.save()
    print("Generated PDF 04:", pdf_path)

# =========================================================================
# FILE 05: CHỈ DẪN KỸ THUẬT SƠN CHỐNG CHÁY KẾT CẤU THÉP (R120)
# =========================================================================
def generate_pdf_spec_son_chong_chay():
    pdf_path = os.path.join(TARGET_DIR, "05_Chi_Dan_Ky_Thuat_Son_Chong_Chay_Ket_Cau_Thep.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    draw_header_footer(c, width, height, "DỰ ÁN TỔ HỢP GREENTECH TOWER", "TẬP 04: KẾT CẤU THÉP & PCCC", 1, 2)

    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM")
    c.setFont("TimesNewRoman-Bold", 10)
    c.drawString(70, height - 85, "Độc lập - Tự do - Hạnh phúc")
    c.setLineWidth(0.8)
    c.setStrokeColor(colors.HexColor("#1B365D"))
    c.line(85, height - 90, 185, height - 90)

    c.setFont("TimesNewRoman-Bold", 14)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawCentredString(width/2, height - 128, "CHỈ DẪN KỸ THUẬT BẢO VỆ CHỐNG CHÁY KẾT CẤU THÉP")
    c.setFont("TimesNewRoman-Bold", 12)
    c.drawCentredString(width/2, height - 146, "HỆ SƠN PHỒNG NỞ CHỐNG CHÁY CHO HỆ KHUNG THÉP CHỊU LỰC")

    c.setFont("TimesNewRoman-Italic", 9.5)
    c.setFillColor(colors.HexColor("#333333"))
    c.drawCentredString(width/2, height - 164, "(Tập 04 — Kèm theo Hồ sơ Thiết kế Bản vẽ Thi công — Trang 56)")

    # Section 3.1
    c.setFont("TimesNewRoman-Bold", 11.5)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 195, "MỤC 3: YÊU CẦU GIỚI HẠN CHỊU LỬA ĐỐI VỚI HỆ KẾT CẤU THÉP")

    c.setFont("TimesNewRoman-Bold", 10.5)
    c.setFillColor(colors.HexColor("#C0392B"))
    c.drawString(54, height - 215, "Điều 3.1: Giới hạn chịu lửa của hệ cột, dầm thép sảnh chính và vì kèo mái (Trang 56)")

    spec_lines = [
        "1. Tiêu chuẩn và Căn cứ pháp lý áp dụng:",
        "   - Căn cứ Bảng 4 của QCVN 06:2022/BXD và Sửa đổi 1:2023/BXD đối với nhà có bậc chịu lửa Bậc I:",
        "     Toàn bộ các cấu kiện thép chịu lực chính của công trình (bao gồm hệ cột thép sảnh đón đón tầng 1,",
        "     dầm thép chuyển sảnh thông tầng và hệ vì kèo thép đỡ mái kính) BẮT BUỘC PHẢI ĐƯỢC BẢO VỆ",
        "     CHỐNG CHÁY ĐẠT GIỚI HẠN CHỊU LỬA TỐI THIỂU R 120 (chịu lực trong 120 phút dưới tác động nhiệt).",
        "   - Các cấu kiện xà gồ phụ và giằng mái thép phải đạt giới hạn chịu lửa tối thiểu R 60 hoặc R 45.",
        "",
        "2. Giải pháp kỹ thuật bảo vệ chống cháy:",
        "   - Nhà thầu được phép sử dụng giải pháp: Sơn chống cháy hệ phồng nở (Intumescent coating) gốc nước",
        "     hoặc gốc dung môi chuyên dụng đã được kiểm định thử nghiệm đốt mẫu thành công.",
        "   - Chiều dày màng sơn khô (DFT - Dry Film Thickness) phải tuân thủ nghiêm ngặt theo kết quả đốt mẫu",
        "     thực tế của phòng thí nghiệm chuyên ngành, thông thường dao động từ 3.2 mm đến 3.8 mm để đạt R 120.",
        "   - Bề mặt thép phải được làm sạch bằng phương pháp phun cát đạt tiêu chuẩn Sa 2.5 trước khi sơn lót.",
        "",
        "3. Hồ sơ nghiệm thu và Thủ tục kiểm định bắt buộc:",
        "   - BẮT BUỘC PHẢI CÓ Giấy chứng nhận kiểm định phương tiện PCCC do Cục Cảnh sát PCCC & CNCH cấp.",
        "   - BẮT BUỘC PHẢI CÓ Báo cáo kết quả thử nghiệm chịu lửa mẫu đốt đạt chuẩn R 120 (TCVN 9383 / ISO 834).",
        "   - Đo kiểm tra chiều dày màng sơn tại hiện trường bằng máy đo độ dày siêu âm có hiệu chuẩn định kỳ.",
        "   - Mọi đề xuất giảm chiều dày màng sơn hoặc hạ cấp chịu lửa xuống R 60 đều bị TỪ CHỐI NGHIỆM THU."
    ]

    y_pos = height - 235
    for line in spec_lines:
        if "R 120" in line or "BẮT BUỘC" in line or "TỪ CHỐI NGHIỆM THU" in line:
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        elif line.startswith("1.") or line.startswith("2.") or line.startswith("3."):
            c.setFont("TimesNewRoman-Bold", 10)
            c.setFillColor(colors.HexColor("#1B365D"))
        else:
            c.setFont("TimesNewRoman", 9)
            c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(54, y_pos, line)
        y_pos -= 15.5

    c.save()
    print("Generated PDF 05:", pdf_path)

# =========================================================================
# FILE 06: THUYẾT MINH BẢN VẼ KẾT CẤU THÉP KC-105 (GHI CHÚ R60 - GÂY MÂU THUẪN)
# =========================================================================
def generate_pdf_kc105_thep():
    pdf_path = os.path.join(TARGET_DIR, "06_Thuyet_Minh_Ban_Ve_Ket_Cau_Thep_KC105.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    draw_header_footer(c, width, height, "DỰ ÁN GREENTECH TOWER", "BẢN VẼ KC-105: KẾT CẤU THÉP", 1, 2)

    c.setFont("TimesNewRoman-Bold", 13)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 70, "HỒ SƠ THIẾT KẾ BẢN VẼ THI CÔNG — GÓI THẦU KẾT CẤU THÉP")
    c.setFont("TimesNewRoman-Bold", 12)
    c.drawString(54, height - 90, "BẢN VẼ SỐ: KC-105 (CHI TIẾT KẾT CẤU THÉP SẢNH CHÍNH TẦNG 1 — TRANG 18)")

    c.setFont("TimesNewRoman-Italic", 9.5)
    c.drawString(54, height - 108, "Đơn vị thiết kế: V-Design Steel Engineering — Kỹ sư lập: KS. Trần Quốc Tuấn")

    # Table Thống kê thép hình
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 132, "BẢNG THỐNG KÊ CẤU KIỆN THÉP HÌNH & GHI CHÚ BẢO VỆ CHỐNG CHÁY")

    # Table Header
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.rect(54, height - 165, width - 108, 24, fill=True, stroke=False)
    c.setFont("TimesNewRoman-Bold", 9)
    c.setFillColor(colors.white)
    c.drawString(62, height - 151, "MÃ CẤU KIỆN")
    c.drawString(135, height - 151, "TIẾT DIỆN CẤU TẠO")
    c.drawString(245, height - 151, "KHỐI LƯỢNG (Tấn)")
    c.drawString(340, height - 151, "YÊU CẦU SƠN CHỐNG CHÁY")
    c.drawString(465, height - 151, "CHIỀU DÀY SƠN (mm)")

    steel_items = [
        ("COL-01", "Cột thép tròn D406 x 16mm", "18.5 Tấn", "R 60 (Ghi chú bản vẽ)", "1.2 mm"),
        ("COL-02", "Cột thép hộp 300x300x12mm", "12.2 Tấn", "R 60 (Ghi chú bản vẽ)", "1.2 mm"),
        ("BM-01", "Dầm chính I 500x200x10x16mm", "24.8 Tấn", "R 60 (Ghi chú bản vẽ)", "1.2 mm"),
        ("BM-02", "Dầm phụ I 300x150x6.5x9mm", "14.5 Tấn", "R 45 (Ghi chú bản vẽ)", "0.8 mm")
    ]

    y_table = height - 188
    for code, sec, weight, fr, thk in steel_items:
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor("#E2E8F0"))
        c.line(54, y_table - 6, width - 54, y_table - 6)

        c.setFont("TimesNewRoman-Bold", 9.5)
        if "COL" in code or "BM-01" in code:
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFillColor(colors.HexColor("#0F172A"))
        c.drawString(62, y_table, code)

        c.setFont("TimesNewRoman", 9)
        c.setFillColor(colors.black)
        c.drawString(135, y_table, sec)
        c.drawString(245, y_table, weight)

        if "R 60" in fr:
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 9)
            c.setFillColor(colors.black)
        c.drawString(340, y_table, fr)

        c.drawString(465, y_table, thk)
        y_table -= 24

    # Highlight box for Conflict
    c.setLineWidth(1)
    c.setStrokeColor(colors.HexColor("#E11D48"))
    c.setFillColor(colors.HexColor("#FFF1F2"))
    c.rect(54, height - 380, width - 108, 90, fill=True, stroke=True)

    c.setFont("TimesNewRoman-Bold", 10.5)
    c.setFillColor(colors.HexColor("#E11D48"))
    c.drawString(68, height - 310, "GHI CHÚ SƠN BẢO VỆ KẾT CẤU THÉP TRÊN BẢN VẼ KC-105 (REV.01):")

    c.setFont("TimesNewRoman", 9.5)
    c.setFillColor(colors.HexColor("#0F172A"))
    c.drawString(68, height - 328, "1. Toàn bộ hệ cột thép sảnh COL-01, COL-02 và dầm BM-01 được sơn chống cháy đạt giới hạn R 60.")
    c.drawString(68, height - 344, "2. Chiều dày màng sơn khô (DFT) yêu cầu: 1.2 mm. Sơn lót epoxy 2 thành phần 60 micron.")
    c.drawString(68, height - 360, "3. Đơn giá dự toán mời thầu đang lập theo định mức sơn R 60: 480.000 VNĐ/m².")

    # QS Notes
    c.setFont("TimesNewRoman-Bold", 11)
    c.setFillColor(colors.HexColor("#1B365D"))
    c.drawString(54, height - 405, "CẢNH BÁO RỦI RO NGHIỆM THU & PHÁT SINH NGÂN SÁCH (QS AUDIT):")
    qs_notes = [
        "1. XUNG ĐỘT PHÁP LÝ NGHIÊM TRỌNG: Chỉ dẫn kỹ thuật Tập 04 (Trang 56) và QCVN 06:2022/BXD",
        "   bắt buộc kết cấu thép chịu lực chính của nhà bậc I phải đạt R 120 (chống cháy 120 phút).",
        "2. SAI LỆCH TRÊN BẢN VẼ: Bản vẽ KC-105 lại chỉ thiết kế sơn chống cháy màng mỏng R 60 (1.2mm).",
        "3. HẬU QUẢ NGHIỆM THU: Cảnh sát PCCC chắc chắn sẽ TỪ CHỐI NGHIỆM THU BÀN GIAO công trình nếu",
        "   cột thép sảnh chính chỉ đạt R 60, vì nguy cơ sụp đổ kết cấu khi xảy ra sự cố cháy!",
        "4. TÁC ĐỘNG CHI PHÍ: Đơn giá sơn chống cháy R 120 (dày ~3.5mm) thực tế khoảng 1.250.000 VNĐ/m².",
        "   Với diện tích bề mặt thép sảnh chính 1.450 m², chi phí phát sinh là: 1.116.500.000 VNĐ!"
    ]
    y_qs = height - 425
    for line in qs_notes:
        if "XUNG ĐỘT" in line or "SAI LỆCH" in line or "TỪ CHỐI" in line:
            c.setFont("TimesNewRoman-Bold", 9.5)
            c.setFillColor(colors.HexColor("#C0392B"))
        else:
            c.setFont("TimesNewRoman", 9.5)
            c.setFillColor(colors.black)
        c.drawString(54, y_qs, line)
        y_qs -= 16

    c.save()
    print("Generated PDF 06:", pdf_path)

if __name__ == "__main__":
    generate_pdf_kc02_vach_ham()
    generate_pdf_spec_son_chong_chay()
    generate_pdf_kc105_thep()
    print("ALL ADDITIONAL PDF DEMO FILES CREATED SUCCESSFULLY!")
