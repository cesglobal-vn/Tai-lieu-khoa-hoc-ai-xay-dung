# -*- coding: utf-8 -*-
"""Sinh file AutoLISP ve phuong an nha pho lo 7x20m (nha 5x14m, 3 tang + tum).

Chay:  python ve-ban-ve-autocad.py <file.lsp> <TEN-FILE-DWG-VIET-HOA>
Sau do trong AutoCAD (qua MCP execute_lisp):  (load "<file.lsp>")

Goc toa do: goc ngoai, truoc, ben trai cua nha. X theo be ngang 5 m, Y tu mat tien vao sau 14 m.
Don vi mm. Moi so lieu thiet ke nam o phan DU LIEU ben duoi; ban ve va bang thong so sinh tu do.
"""
import pathlib
import sys

OUT_LSP = pathlib.Path(sys.argv[1])
DOC_NAME = sys.argv[2].upper()

# =====================================================================================
# DU LIEU THIET KE (anh duyet ngay 07/10/2026)
# =====================================================================================
LV = {"SAN": -450, "T1": 0, "T2": 3600, "T3": 7000, "ST": 10400, "TUM": 13400}
OFF = {"T1": (0, 0), "T2": (11000, 0), "T3": (22000, 0), "MAI": (40000, 0)}
AX_X = [("1", 100), ("2", 4900)]
AX_Y = [("A", 100), ("B", 1500), ("C", 8100), ("D", 11700), ("E", 13900)]

CUA = {  # ma: (ten, rong, cao, cao be)
    "D1": ("Cửa đi kính khung nhôm 4 cánh", 3600, 2800, 0),
    "D2": ("Cửa đi gỗ 1 cánh", 900, 2200, 0),
    "D3": ("Cửa đi kính lùa 2 cánh", 2400, 2600, 0),
    "D4": ("Cửa đi WC nhôm kính mờ", 800, 2100, 0),
    "S1": ("Cửa sổ kính lớn", 1600, 2200, 400),
    "S2": ("Cửa sổ kính 2 cánh", 1200, 1400, 900),
    "S3": ("Cửa sổ kính đứng cầu thang", 600, 1800, 1200),
    "S4": ("Cửa sổ lật WC", 600, 600, 1500),
    "S5": ("Cửa sổ kính băng", 3600, 1800, 600),
}


def W(x1, y1, x2, y2, *ops):
    return {"r": (x1, y1, x2, y2), "ops": list(ops)}


TRAI_T1 = [("S1", 2600, 4200), ("D2", 6500, 7400), ("S3", 8900, 9500), ("S4", 10700, 11300), ("S2", 12200, 13400)]
TRAI_T23 = [("S1", 2600, 4200), ("S2", 5600, 6800), ("S3", 8900, 9500), ("S4", 10700, 11300), ("S2", 12200, 13400)]
SAU = W(200, 13800, 4800, 14000, ("S2", 1900, 3100))
GIUA_T23 = [W(200, 8050, 4800, 8150, ("D2", 3700, 4600)), W(200, 10250, 3500, 10350),
            W(2400, 10350, 2500, 11650, ("D4", 10600, 11400)), W(200, 11650, 4800, 11750, ("D2", 3700, 4600))]
TUONG = {
    "T1": [W(0, 0, 200, 14000, *TRAI_T1), W(4800, 0, 5000, 14000), W(200, 0, 4800, 200, ("D1", 700, 4300)), SAU,
           W(200, 10250, 3500, 10350), W(2400, 10350, 2500, 11650, ("D4", 10600, 11400)), W(200, 11650, 2500, 11750)],
    "T2": [W(0, 1400, 200, 14000, *TRAI_T23), W(4800, 1400, 5000, 14000), W(200, 1400, 4800, 1600, ("D3", 1300, 3700)),
           SAU] + GIUA_T23,
    "T3": [W(0, 1400, 200, 14000, *TRAI_T23), W(4800, 1400, 5000, 14000), W(200, 1400, 4800, 1600, ("S5", 700, 4300)),
           SAU] + GIUA_T23,
    "MAI": [W(0, 8000, 5000, 8200), W(0, 11600, 5000, 11800, ("D2", 3000, 3900)),
            W(0, 8200, 200, 11600, ("S3", 8900, 9500)), W(4800, 8200, 5000, 11600)],
}
LAN_CAN = {"T2": [(0, 0, 5000, 200), (0, 200, 200, 1400), (4800, 200, 5000, 1400)],
           "MAI": [(0, 11800, 200, 14000), (4800, 11800, 5000, 14000), (200, 13800, 4800, 14000)]}
COT_ALL = [(x, y) for _, x in AX_X for _, y in AX_Y]
COT = {"T1": COT_ALL, "T2": COT_ALL, "T3": [c for c in COT_ALL if c[1] != 100],
       "MAI": [c for c in COT_ALL if c[1] in (8100, 11700)]}
SAN = {"T1": [(0, 0, 5000, 14000)], "T2": [(0, 0, 5000, 14000)], "T3": [(0, 1400, 5000, 14000)],
       "MAI": [(0, 8000, 5000, 14000)]}
LO_THANG = (200, 8150, 3450, 10250)
SAN_LO = {"T2": [LO_THANG], "T3": [LO_THANG], "MAI": [LO_THANG]}
# Thang 2 ve doc theo X: ve 1 (phia truc C) di len ve phia tuong trai, chieu nghi sat tuong trai.
VE1, CHIEU_NGHI, VE2 = (1110, 8200, 3450, 9150), (200, 8200, 1110, 10250), (1110, 9300, 3450, 10250)
MAT_BAC, SO_BAC = 260, 9
MAI = {  # ma: (ten, ap cho, outline, dinh, mep, mat bang ve)
    "M1": ("Mái tôn dốc 1 phía", "Tầng 3", (-150, 800, 5150, 8000), 12800, 10000, "MAI"),
    "M2": ("Mái tôn che ban công", "Tầng 2", (-150, -600, 5150, 1400), 7000, 6200, "MAI"),
    "M3": ("Mái bằng tum BTCT", "Tum", (0, 8000, 5000, 11800), 13400, 13400, "MAI"),
    "M4": ("Mái pergola tấm polycarbonate", "Sân trước", (-100, -4900, 5100, 0), 3200, 3000, "T1"),
}
PHONG = {
    "T1": [("PHÒNG KHÁCH", 3000, 1300), ("BẾP ĂN", 2500, 12500), ("WC", 1900, 10500), ("SẢNH", 3650, 11000)],
    "T2": [("BAN CÔNG", 1100, 1250), ("PHÒNG NGỦ 1", 1700, 2400), ("PHÒNG NGỦ 2", 2300, 12150), ("WC", 1900, 10500)],
    "T3": [("PHÒNG SINH HOẠT", 2000, 2300), ("PHÒNG THỜ", 1700, 12600), ("WC", 1900, 10500)],
    "MAI": [("SÂN THƯỢNG", 2600, 12350), ("MÁI TÔN M1", 2500, 4300),
            ("MÁI M2", 2500, 0)],
}
# San vuon, rao, pergola (chi o mat bang tang 1)
RANH_DAT = (-2000, -5000, 5000, 15000)
SAN_VUON = [(-2000, -5000, 0, 15000), (0, -5000, 5000, 0), (0, 14000, 5000, 15000)]
RAO = [(-2000, -5000, -1100, -4800), (-200, -5000, 300, -4800), (4700, -5000, 5000, -4800)]
CONG = [(-1100, -4950, -200, -4850), (300, -4950, 4700, -4850)]
BAC = [(700, -900, 4300, -600), (700, -600, 4300, -300), (700, -300, 4300, 0)]
PERGOLA_COT = [(0, -4700, 150, -4550), (4850, -4700, 5000, -4550)]
PERGOLA_XA = [(75, -4700, 75, 0), (4925, -4700, 4925, 0), (-100, -4625, 5100, -4625)] + \
             [(-100, y, 5100, y) for y in (-3900, -3200, -2500, -1800, -1100, -400)]
MAY_LANH = [(-750, 1700, -450, 2500), (-750, 4600, -450, 5400), (-750, 9800, -450, 10600), (-750, 12400, -450, 13200)]
ONG_XOI = [(-60, y) for y in (300, 4400, 8100, 11700, 13700)]
KIM_THU_SET = [(100, 8100), (4900, 8100), (100, 11700), (4900, 11700), (100, 13900), (4900, 13900)]
BON_NUOC = (3500, 9900, 600)
THONG_SO = [  # (ten, gia tri mm) - doc boi script dung 3D
    ("Sàn BTCT dày", 120), ("Mái tôn dày (kể xà gồ)", 120), ("Lan can, tường chắn mái cao", 1000),
    ("Tường chắn mái tum cao", 400), ("Tường rào cao", 1800), ("Cổng cao", 1600),
    ("Bồn nước cao", 1500), ("Chân bồn nước cao", 300), ("Kim thu sét cao", 1500),
    ("Cục nóng máy lạnh cao", 550), ("Ống xối lên tới cao độ", 10400), ("Bậc tam cấp cao", 150),
    ("Chỉ tường đua ra", 50), ("Xà pergola cao", 200),
]
VAT_LIEU = [
    "Tường tầng 1, 2: sơn nước màu kem",
    "Tường tầng 3, tum, lan can, tường chắn mái: ốp tấm gỗ nhựa màu nâu",
    "Cột, chỉ tường ở cốt sàn: sơn màu xám nhạt",
    "Mái M1, M2: tôn sóng màu đỏ nâu",
    "Cửa: khung nhôm xám, kính xanh nhạt",
    "Ống xối: PVC màu xanh lá. Cục nóng máy lạnh: màu trắng",
    "Pergola, tường rào: khung thép sơn nâu đỏ, mái tấm polycarbonate",
    "Sân, lối đi: bê tông xám. Bồn nước: inox",
]
# Noi that: (ten, x1, y1, x2, y2[, vi tri chu]). Ten dung dung bo chu duoi de script 3D nhan ra.
# TỦ BẾP TRÊN ve net dut tren layer NOI-THAT-TREN (treo tuong).
WC_NT = [("LAVABO", 700, 10350, 1200, 10800), ("SEN TẮM", 200, 10850, 1050, 11650),
         ("BỒN CẦU", 1150, 10950, 1550, 11650)]
NOI_THAT = {
    "T1": [("SOFA", 300, 2400, 1200, 4600), ("BÀN TRÀ", 1700, 2950, 2300, 4050), ("KỆ TV", 4350, 2600, 4800, 4400),
           ("THẢM", 1350, 2300, 3600, 4700, (3100, 4450)), ("BÀN ĂN", 2400, 5600, 3300, 7000),
           ("GHẾ", 1950, 5850, 2350, 6250), ("GHẾ", 1950, 6350, 2350, 6750), ("GHẾ", 3350, 5850, 3750, 6250),
           ("GHẾ", 3350, 6350, 3750, 6750), ("TỦ BẾP DƯỚI", 300, 13200, 4700, 13800),
           ("TỦ BẾP TRÊN", 300, 13450, 1800, 13800), ("TỦ BẾP TRÊN", 3200, 13450, 4700, 13800),
           ("TỦ LẠNH", 4100, 11850, 4800, 12550), ("Ô TÔ", 1600, -4650, 3200, -1000),
           ("CHẬU CÂY", -1800, -4700, -1400, -4300), ("CHẬU CÂY", 4350, -1500, 4750, -1100)] + WC_NT,
    "T2": [("GIƯỜNG ĐÔI", 2800, 3200, 4800, 5000), ("TAB", 4350, 2700, 4800, 3150), ("TAB", 4350, 5050, 4800, 5500),
           ("TỦ ÁO", 300, 7450, 2300, 8050), ("BÀN TRANG ĐIỂM", 200, 4500, 650, 5500),
           ("THẢM", 2300, 2900, 4300, 5300, (2550, 3100)),
           ("BÀN NHỎ", 2200, 500, 2800, 1100), ("GHẾ", 1450, 550, 1950, 1050), ("GHẾ", 3050, 550, 3550, 1050),
           ("CHẬU CÂY", 300, 300, 700, 700), ("CHẬU CÂY", 4300, 300, 4700, 700),
           ("GIƯỜNG ĐƠN", 200, 12500, 2200, 13700), ("TỦ ÁO", 4250, 12700, 4800, 13700),
           ("BÀN HỌC", 2300, 13300, 3300, 13800), ("GHẾ", 2600, 12800, 3000, 13200)] + WC_NT,
    "T3": [("SOFA", 3900, 3800, 4800, 6000), ("BÀN TRÀ", 2700, 4350, 3300, 5450), ("KỆ TV", 200, 4300, 650, 5500),
           ("THẢM", 1300, 3600, 3700, 6200, (1600, 3800)), ("BÀN LÀM VIỆC", 300, 7450, 1500, 8050),
           ("GHẾ", 700, 6900, 1100, 7300), ("KỆ SÁCH", 1700, 7650, 3300, 8050),
           ("BÀN THỜ", 3300, 13200, 4700, 13800), ("THẢM", 2400, 12300, 3800, 13100, (2700, 12450))] + WC_NT,
    "MAI": [("MÁY GIẶT", 4100, 10950, 4700, 11550), ("GIÀN PHƠI", 900, 13000, 2700, 13500),
            ("BÀN NHỎ", 3500, 12500, 4100, 13100), ("GHẾ", 2950, 12550, 3400, 13050), ("GHẾ", 4200, 12550, 4650, 13050),
            ("CHẬU CÂY", 300, 11950, 700, 12350), ("CHẬU CÂY", 4300, 13300, 4700, 13700),
            ("CHẬU CÂY", 300, 13300, 700, 13700)],
}

# =====================================================================================
# CONG CU SINH LISP
# =====================================================================================
L = []


def u(s):
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append('\\\\' if ch == '\\' else ('\\"' if ch == '"' else ch))
        else:
            out.append('\\\\U+%04X' % ord(ch))
    return '"' + ''.join(out) + '"'


def f(v):
    return f"{v:.1f}"


def poly(pts, lay, closed=True, hatch=None):
    flat = ' '.join(f"{f(x)} {f(y)}" for x, y in pts)
    L.append(f'(setq e (pl (list {flat}) {"T" if closed else "nil"} "{lay}"))')
    if hatch:
        L.append(f'(ht e "{hatch[0]}" {hatch[1]} "{hatch[2]}")')


def rect(x1, y1, x2, y2, lay, hatch=None):
    poly([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], lay, True, hatch)


def line(x1, y1, x2, y2, lay):
    L.append(f'(ln {f(x1)} {f(y1)} {f(x2)} {f(y2)} "{lay}")')


def arc(cx, cy, r, a0, a1, lay):
    L.append(f'(ar {f(cx)} {f(cy)} {f(r)} {a0} {a1} "{lay}")')


def circle(cx, cy, r, lay):
    L.append(f'(ci {f(cx)} {f(cy)} {f(r)} "{lay}")')


def text(x, y, s, h, lay, mid=True):
    L.append(f'(tx {f(x)} {f(y)} {u(s)} {h} "{lay}" {"T" if mid else "nil"})')


def dim(x1, y1, x2, y2, off, vert):
    """Kich thuoc thang. vert: do theo Y, duong kich thuoc tai x = off; nguoc lai tai y = off."""
    if vert:
        L.append(f'(dm {f(x1)} {f(y1)} {f(x2)} {f(y2)} {f(off)} {f((y1 + y2) / 2)} T)')
    else:
        L.append(f'(dm {f(x1)} {f(y1)} {f(x2)} {f(y2)} {f((x1 + x2) / 2)} {f(off)} nil)')


def chain(vals, fixed, off, vert):
    vals = sorted(set(vals))
    for a, b in zip(vals, vals[1:]):
        if vert:
            dim(fixed, a, fixed, b, off, True)
        else:
            dim(a, fixed, b, fixed, off, False)


ANSI = ("ANSI31", 20, "HATCH")
SOLID_COT = ("SOLID", 1, "COT")
SOLID_CAT = ("SOLID", 1, "MAT-CAT")


def cot_cao(cao_do):
    return f"+{cao_do / 1000:.3f}" if cao_do > 0 else ("±0.000" if cao_do == 0 else f"{cao_do / 1000:.3f}")


# =====================================================================================
# MAT BANG
# =====================================================================================
def tach(r, cuts):
    """Cat hinh chu nhat tuong r theo cac khoang cuts (doc theo truc dai). Tra ve cac doan con lai."""
    x1, y1, x2, y2 = r
    doc_x = (x2 - x1) >= (y2 - y1)
    a0, a1 = (x1, x2) if doc_x else (y1, y2)
    cuts = sorted((max(a, a0), min(b, a1)) for a, b in cuts if b > a0 and a < a1)
    pieces, cur = [], a0
    for a, b in cuts:
        if a > cur:
            pieces.append((cur, a))
        cur = max(cur, b)
    if cur < a1:
        pieces.append((cur, a1))
    return [(a, y1, b, y2) if doc_x else (x1, a, x2, b) for a, b in pieces], doc_x


def cot_trong(r, cols):
    x1, y1, x2, y2 = r
    doc_x = (x2 - x1) >= (y2 - y1)
    out = []
    for cx, cy in cols:
        if cx + 100 > x1 and cx - 100 < x2 and cy + 100 > y1 and cy - 100 < y2:
            out.append((cx - 100, cx + 100) if doc_x else (cy - 100, cy + 100))
    return out


def ve_cua(code, r, doc_x, a, b, ox, oy, lay="CUA"):
    """Ve o cua (khung kin tren layer CUA) + ky hieu + ma cua."""
    x1, y1, x2, y2 = r
    if doc_x:
        gx1, gy1, gx2, gy2 = a, y1, b, y2
    else:
        gx1, gy1, gx2, gy2 = x1, a, x2, b
    rect(gx1 + ox, gy1 + oy, gx2 + ox, gy2 + oy, lay)
    t = (y2 - y1) if doc_x else (x2 - x1)
    cxm, cym = (x1 + x2) / 2, (y1 + y2) / 2
    # huong ra ngoai nha (xa tam nha)
    sgn = (-1 if cym < 7000 else 1) if doc_x else (-1 if cxm < 2500 else 1)
    if code.startswith("S"):
        for k in (1, 2):
            if doc_x:
                yy = y1 + t * k / 3
                line(a + ox, yy + oy, b + ox, yy + oy, lay)
            else:
                xx = x1 + t * k / 3
                line(xx + ox, a + oy, xx + ox, b + oy, lay)
    elif code in ("D2", "D4"):
        w = b - a
        if doc_x:
            ym = y2 if sgn < 0 else y1          # mep tuong phia trong
            dy = w if sgn < 0 else -w
            line(a + ox, ym + oy, a + ox, ym + dy + oy, lay)
            a0, a1 = (0, 90) if dy > 0 else (270, 360)
            arc(a + ox, ym + oy, w, a0, a1, lay)
        else:
            xm = x2 if sgn < 0 else x1
            dx = w if sgn < 0 else -w
            line(xm + ox, a + oy, xm + dx + ox, a + oy, lay)
            a0, a1 = (0, 90) if dx > 0 else (90, 180)
            arc(xm + ox, a + oy, w, a0, a1, lay)
    else:  # D1, D3: cua kinh nhieu canh, ve 2 duong canh
        for k in (1, 2):
            if doc_x:
                yy = y1 + t * k / 3
                line(a + ox, yy + oy, b + ox, yy + oy, lay)
            else:
                xx = x1 + t * k / 3
                line(xx + ox, a + oy, xx + ox, b + oy, lay)
    # ma cua dat phia ngoai, cach mep tuong 450
    m = (a + b) / 2
    if doc_x:
        ty = (y1 - 450) if sgn < 0 else (y2 + 450)
        text(m + ox, ty + oy, code, 250, "KY-HIEU-CUA")
    else:
        tx_ = (x1 - 450) if sgn < 0 else (x2 + 450)
        text(tx_ + ox, m + oy, code, 250, "KY-HIEU-CUA")


def ve_mat_bang(key, tieu_de):
    ox, oy = OFF[key]
    lv = LV["ST"] if key == "MAI" else LV[key]
    cols = COT[key]
    # truc
    y_lo, y_hi = (-6000, 15600) if key == "T1" else (-1200, 15600)
    x_lo, x_hi = (-2600, 6200) if key == "T1" else (-1200, 6200)
    for name, x in AX_X:
        line(x + ox, y_lo + oy, x + ox, y_hi + oy, "TRUC")
        circle(x + ox, y_hi + 400 + oy, 400, "TRUC")
        text(x + ox, y_hi + 400 + oy, name, 350, "TRUC")
    for name, y in AX_Y:
        line(x_lo + ox, y + oy, x_hi + ox, y + oy, "TRUC")
        circle(x_hi + 400 + ox, y + oy, 400, "TRUC")
        text(x_hi + 400 + ox, y + oy, name, 350, "TRUC")
    # san va lo san
    for r in SAN.get(key, []):
        rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "SAN")
    for r in SAN_LO.get(key, []):
        rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "SAN-LO")
        line(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "SAN-LO")
        line(r[0] + ox, r[3] + oy, r[2] + ox, r[1] + oy, "SAN-LO")
    # tuong
    for w in TUONG[key]:
        cuts = [(a, b) for _, a, b in w["ops"]] + cot_trong(w["r"], cols)
        pieces, doc_x = tach(w["r"], cuts)
        for p in pieces:
            rect(p[0] + ox, p[1] + oy, p[2] + ox, p[3] + oy, "TUONG", ANSI)
        for code, a, b in w["ops"]:
            ve_cua(code, w["r"], doc_x, a, b, ox, oy)
    for r in LAN_CAN.get(key, []):
        rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "LAN-CAN", ("ANSI37", 20, "HATCH"))
    for cx, cy in cols:
        rect(cx - 100 + ox, cy - 100 + oy, cx + 100 + ox, cy + 100 + oy, "COT", SOLID_COT)
    # thang (tang 1, 2, 3)
    if key in ("T1", "T2", "T3"):
        for r in (VE1, CHIEU_NGHI, VE2):
            rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "CAU-THANG")
        for k in range(1, SO_BAC):
            x = VE1[2] - k * MAT_BAC
            line(x + ox, VE1[1] + oy, x + ox, VE1[3] + oy, "CAU-THANG")
            x = VE2[0] + k * MAT_BAC
            line(x + ox, VE2[1] + oy, x + ox, VE2[3] + oy, "CAU-THANG")
        ym1, ym2 = (VE1[1] + VE1[3]) / 2, (VE2[1] + VE2[3]) / 2
        poly([(3300 + ox, ym1 + oy), (650 + ox, ym1 + oy), (650 + ox, ym2 + oy), (3100 + ox, ym2 + oy)],
             "CAU-THANG", closed=False)
        poly([(2950 + ox, ym2 + 120 + oy), (3100 + ox, ym2 + oy), (2950 + ox, ym2 - 120 + oy)],
             "CAU-THANG", closed=False)
        text(3200 + ox, ym1 - 300 + oy, "LÊN", 250, "CAU-THANG")
    # mai
    for code, (ten, ap, r, dinh, mep, ve_o) in MAI.items():
        if ve_o != key:
            continue
        rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "MAI")
        cx = (r[0] + r[2]) / 2
        if dinh != mep:  # mui ten doc ve mat tien
            yt, yb = r[3] - 400, r[1] + 400
            line(cx + 900 + ox, yt + oy, cx + 900 + ox, yb + oy, "MAI")
            poly([(cx + 780 + ox, yb + 250 + oy), (cx + 900 + ox, yb + oy), (cx + 1020 + ox, yb + 250 + oy)],
                 "MAI", closed=False)
            i = (dinh - mep) / (r[3] - r[1]) * 100
            text(cx + 1700 + ox, (yt + yb) / 2 + oy, f"i={i:.0f}%", 250, "MAI")
        text(cx - 900 + ox, (r[1] + r[3]) / 2 + 350 + oy, code, 350, "MAI")
    # tang 1: san vuon, rao, pergola, thiet bi ngoai nha
    if key == "T1":
        rect(*[v for v in (RANH_DAT[0] + ox, RANH_DAT[1] + oy, RANH_DAT[2] + ox, RANH_DAT[3] + oy)], lay="RANH-DAT")
        for r in SAN_VUON:
            rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "SAN-VUON")
        for r in RAO:
            rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "RAO", ANSI)
        for r in CONG:
            rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "CONG")
        for r in BAC:
            rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "BAC-THEM")
        for r in PERGOLA_COT:
            rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "PERGOLA", ("SOLID", 1, "PERGOLA"))
        for x1, y1, x2, y2 in PERGOLA_XA:
            line(x1 + ox, y1 + oy, x2 + ox, y2 + oy, "PERGOLA")
        for r in MAY_LANH:
            rect(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "MAY-LANH")
            line(r[0] + ox, r[1] + oy, r[2] + ox, r[3] + oy, "MAY-LANH")
        for x, y in ONG_XOI:
            circle(x + ox, y + oy, 45, "ONG-XOI")
        text(-1000 + ox, 7000 + oy, "LỐI ĐI HÔNG", 250, "CHU")
        text(2500 + ox, -2900 + oy, "SÂN ĐỂ XE", 250, "CHU")
        text(2500 + ox, -3300 + oy, cot_cao(LV["SAN"]), 250, "CHU")
        text(2500 + ox, -4250 + oy, "PERGOLA", 250, "CHU")
        text(-650 + ox, -5300 + oy, "CỔNG PHỤ", 200, "CHU")
        text(2500 + ox, -5300 + oy, "CỔNG CHÍNH", 200, "CHU")
        text(-600 + ox, 3200 + oy, "CỤC NÓNG", 180, "CHU")
    if key == "MAI":
        cx, cy, r = BON_NUOC
        circle(cx + ox, cy + oy, r, "BON-NUOC")
        text(cx + ox, cy + oy, "BỒN NƯỚC", 200, "BON-NUOC")
        for x, y in KIM_THU_SET:
            circle(x + ox, y + oy, 60, "KIM-THU-SET")
        text(2600 + ox, 11980 + oy, cot_cao(LV["ST"]), 250, "CHU")
        text(1700 + ox, 10900 + oy, "MÁI TUM " + cot_cao(LV["TUM"]), 250, "CHU")
    # noi that: hinh chu nhat dung kich thuoc + ten
    for it in NOI_THAT.get(key, []):
        ten, x1, y1, x2, y2 = it[:5]
        lx, ly = it[5] if len(it) > 5 else ((x1 + x2) / 2, (y1 + y2) / 2)
        rect(x1 + ox, y1 + oy, x2 + ox, y2 + oy, "NOI-THAT-TREN" if ten == "TỦ BẾP TRÊN" else "NOI-THAT")
        text(lx + ox, ly + oy, ten, 110, "NOI-THAT-TEN")
    # ten phong + cao do san
    for ten, x, y in PHONG[key]:
        text(x + ox, y + oy, ten, 250, "CHU")
        if key != "MAI":
            text(x + ox, y - 380 + oy, cot_cao(lv if ten != "BAN CÔNG" else lv - 50), 200, "CHU")
    # kich thuoc
    if key == "T1":
        x_d = [-2600, -3300, -4000]
        y_d = [-1500, -5600, -6300]
    else:
        x_d = [-700, -1400, -2100]
        y_d = [-800, -1500, -2200]
    # ben trai: chi tiet tuong trai, truc, tong
    trai = next(w for w in TUONG[key] if w["r"][0] == 0 and w["r"][2] == 200)
    ys = [trai["r"][1], trai["r"][3]] + [v for _, a, b in trai["ops"] for v in (a, b)]
    if key == "T1":
        chain([v + oy for v in ys], ox, x_d[0] + ox, True)
        chain([v + oy for _, v in AX_Y], ox, x_d[1] + ox, True)
        dim(ox, oy, ox, 14000 + oy, x_d[2] + ox, True)
        chain([-5000 + oy, oy, 14000 + oy, 15000 + oy], -2000 + ox, -4700 + ox, True)
    else:
        chain([v + oy for v in ys], ox, x_d[0] + ox, True)
        chain([v + oy for _, v in AX_Y], ox, x_d[1] + ox, True)
        dim(ox, oy, ox, 14000 + oy, x_d[2] + ox, True)
    # phia truoc: chi tiet tuong truoc, truc, tong
    truoc = next(w for w in TUONG[key] if w["r"][2] - w["r"][0] > 4000 and w["r"][1] in (0, 1400, 8000))
    xs = [0, 5000] + [v for _, a, b in truoc["ops"] for v in (a, b)]
    chain([v + ox for v in xs], truoc["r"][1] + oy, y_d[0] + oy, False)
    chain([v + ox for _, v in AX_X] + [ox, 5000 + ox], oy, y_d[1] + oy, False)
    if key == "T1":
        chain([-2000 + ox, ox, 5000 + ox], -5000 + oy, y_d[2] + oy, False)
    else:
        dim(ox, oy, 5000 + ox, oy, y_d[2] + oy, False)
    ty = (-7600 if key == "T1" else -3200) + oy
    text(2500 + ox, ty, tieu_de, 350, "CHU")
    text(2500 + ox, ty - 550, "TỶ LỆ 1/100", 250, "CHU")


# =====================================================================================
# MAT DUNG, MAT CAT (sinh tu cung du lieu)
# =====================================================================================
ZB = -25000  # cao do 0 cua hang mat dung nam o y = -25000


def z(v):
    return ZB + v


def mai_z(code, y):
    _, _, r, dinh, mep, _ = MAI[code]
    return mep + (y - r[1]) / (r[3] - r[1]) * (dinh - mep)


def moc_cao_do(x, zs, lay="MAT-DUNG", trai=False):
    for v in zs:
        line(x - 300, z(v), x + 300, z(v), lay)
        poly([(x - 150, z(v) + 250), (x, z(v)), (x + 150, z(v) + 250)], lay, closed=True)
        text(x + (-1100 if trai else 1100), z(v) + 150, cot_cao(v), 250, "CHU")


def o_cua_mat_dung(u1, u2, base, code, lay="MAT-DUNG"):
    _, w, h, be = CUA[code]
    rect(u1, z(base + be), u2, z(base + be + h), lay)
    rect(u1 + 50, z(base + be) + 50, u2 - 50, z(base + be + h) - 50, lay)
    n = 4 if code in ("D1", "S5") else (2 if code in ("D3", "S1", "S2") else 1)
    for k in range(1, n):
        x = u1 + (u2 - u1) * k / n
        line(x, z(base + be) + 50, x, z(base + be + h) - 50, lay)


def mat_dung_chinh():
    ox = 0
    line(-2500, z(LV["SAN"]), 5500, z(LV["SAN"]), "MAT-DUNG")
    rect(0, z(0), 5000, z(LV["T2"]), "MAT-DUNG")
    o_cua_mat_dung(700, 4300, 0, "D1")
    for r in BAC:
        pass
    for k, (a, b) in enumerate([(-450, -300), (-300, -150), (-150, 0)]):
        rect(700 - 0, z(a), 4300, z(b), "MAT-DUNG")
    rect(0, z(LV["T2"] - 120), 5000, z(LV["T2"]), "MAT-DUNG")
    rect(0, z(LV["T2"]), 5000, z(LV["T2"] + 1000), "MAT-DUNG")        # lan can ban cong
    o_cua_mat_dung(1300, 3700, LV["T2"], "D3")
    for x in (0, 4800):
        rect(x, z(LV["T2"] + 1000), x + 200, z(mai_z("M2", 100) - 120), "MAT-DUNG")
    rect(-150, z(MAI["M2"][4]), 5150, z(MAI["M2"][3]), "MAT-DUNG")       # mai M2 nhin tu truoc
    rect(0, z(LV["T3"]), 5000, z(mai_z("M1", 1400)), "MAT-DUNG")
    o_cua_mat_dung(700, 4300, LV["T3"], "S5")
    rect(-150, z(MAI["M1"][4]), 5150, z(MAI["M1"][3]), "MAT-DUNG")       # mai M1
    for k in range(1, 12):
        line(-150 + k * 5300 / 12, z(MAI["M1"][4]), -150 + k * 5300 / 12, z(MAI["M1"][3]), "MAT-DUNG")
    rect(0, z(MAI["M1"][3]), 5000, z(LV["TUM"] + 400), "MAT-DUNG")       # tum nhin phia sau mai
    cx, cy, rb = BON_NUOC
    rect(cx - rb, z(LV["TUM"] + 400), cx + rb, z(LV["TUM"] + 400 + 1800), "MAT-DUNG")
    for x1, _, x2, _ in RAO:
        rect(x1, z(LV["SAN"]), x2, z(LV["SAN"] + 1800), "MAT-DUNG")
    for x1, _, x2, _ in CONG:
        rect(x1, z(LV["SAN"]), x2, z(LV["SAN"] + 1600), "MAT-DUNG")
        n = int((x2 - x1) / 150)
        for k in range(1, n):
            line(x1 + k * (x2 - x1) / n, z(LV["SAN"]), x1 + k * (x2 - x1) / n, z(LV["SAN"] + 1600), "MAT-DUNG")
    for x1, _, x2, _ in PERGOLA_COT:
        rect(x1, z(LV["SAN"] + 1800), x2, z(MAI["M4"][4] - 200), "MAT-DUNG")
    rect(-100, z(MAI["M4"][4] - 200), 5100, z(MAI["M4"][4]), "MAT-DUNG")
    moc_cao_do(6300, [LV["SAN"], 0, LV["T2"], LV["T3"], MAI["M1"][4], MAI["M1"][3], LV["TUM"]])
    chain([z(v) for v in (LV["SAN"], 0, LV["T2"], LV["T3"], LV["ST"], LV["TUM"])], -2000, -3000, True)
    text(2500, z(-2600), "MẶT ĐỨNG CHÍNH (TRỤC 1-2)", 350, "CHU")
    text(2500, z(-3150), "TỶ LỆ 1/100", 250, "CHU")


def mat_dung_ben():
    """Nhin tu loi di hong (tu -X), mat tien nam ben phai: u = 26000 - Y."""
    U = lambda y: 26000 - y
    line(U(15500), z(LV["SAN"]), U(-5500), z(LV["SAN"]), "MAT-DUNG")
    rect(U(14000), z(0), U(0), z(LV["T2"]), "MAT-DUNG")
    rect(U(14000), z(LV["T2"]), U(1400), z(LV["T3"]), "MAT-DUNG")
    rect(U(1400), z(LV["T2"]), U(0), z(LV["T2"] + 1000), "MAT-DUNG")          # lan can ban cong
    poly([(U(8000), z(LV["T3"])), (U(1400), z(LV["T3"])), (U(1400), z(mai_z("M1", 1400) - 120)),
          (U(8000), z(MAI["M1"][3] - 120))], "MAT-DUNG")                         # hoi tuong tang 3
    rect(U(14000), z(LV["T3"]), U(8000), z(LV["ST"]), "MAT-DUNG")
    rect(U(11800), z(LV["ST"]), U(8000), z(LV["TUM"] + 400), "MAT-DUNG")       # tum
    rect(U(14000), z(LV["ST"]), U(11800), z(LV["ST"] + 1000), "MAT-DUNG")      # tuong chan mai
    for code in ("M1", "M2"):
        _, _, r, dinh, mep, _ = MAI[code]
        poly([(U(r[1]), z(mep - 120)), (U(r[1]), z(mep)), (U(r[3]), z(dinh)), (U(r[3]), z(dinh - 120))],
             "MAT-DUNG")
    _, _, r, dinh, mep, _ = MAI["M4"]
    poly([(U(r[1]), z(mep - 200)), (U(r[1]), z(mep)), (U(r[3]), z(dinh)), (U(r[3]), z(dinh - 200))], "MAT-DUNG")
    for _, y1, _, y2 in PERGOLA_COT:
        rect(U(y2), z(LV["SAN"]), U(y1), z(MAI["M4"][4] - 200), "MAT-DUNG")
    rect(U(-4800), z(LV["SAN"]), U(-5000), z(LV["SAN"] + 1800), "MAT-DUNG")
    cx, cy, rb = BON_NUOC
    rect(U(cy + rb), z(LV["TUM"] + 400 + 300), U(cy - rb), z(LV["TUM"] + 400 + 1800), "MAT-DUNG")
    for v in (LV["T2"], LV["T3"]):
        line(U(14000), z(v - 150), U(0 if v == LV["T2"] else 1400), z(v - 150), "MAT-DUNG")
    tuong_trai = {k: next(w for w in TUONG[k] if w["r"][0] == 0 and w["r"][2] == 200) for k in ("T1", "T2", "T3", "MAI")}
    for k, base in (("T1", 0), ("T2", LV["T2"]), ("T3", LV["T3"]), ("MAI", LV["ST"])):
        for code, a, b in tuong_trai[k]["ops"]:
            o_cua_mat_dung(U(b), U(a), base, code)
    for _, y1, _, y2 in MAY_LANH:
        rect(U(y2), z(LV["SAN"]), U(y1), z(LV["SAN"] + 550), "MAT-DUNG")
    for _, y in ONG_XOI:
        rect(U(y) - 45, z(LV["SAN"]), U(y) + 45, z(10400), "ONG-XOI")
    moc_cao_do(U(15500) - 400, [LV["SAN"], 0, LV["T2"], LV["T3"], LV["ST"], MAI["M1"][3], LV["TUM"]], trai=True)
    for i, s in enumerate(VAT_LIEU[:4]):
        text(U(9000), z(-3900 - i * 380), s, 200, "CHU", mid=False)
    text(U(5000), z(-2600), "MẶT ĐỨNG BÊN (NHÌN TỪ LỐI ĐI HÔNG)", 350, "CHU")
    text(U(5000), z(-3150), "TỶ LỆ 1/100", 250, "CHU")


def mat_cat():
    """Mat cat 1-1 tai X = 2700, nhin ve phia tuong trai; mat tien ben trai: u = 45000 + Y."""
    U = lambda y: 45000 + y
    sd = 120
    line(U(-5500), z(LV["SAN"]), U(15500), z(LV["SAN"]), "MAT-CAT")
    # san cat
    for k, (y1, y2) in (("T1", (0, 14000)), ("T2", (0, 14000)), ("T3", (1400, 14000)), ("ST", (8000, 14000))):
        lv = LV[k]
        segs = [(y1, y2)]
        if k in ("T2", "T3", "ST"):
            segs = [(y1, LO_THANG[1]), (LO_THANG[3], y2)]
        for a, b in segs:
            rect(U(a), z(lv - sd), U(b), z(lv), "MAT-CAT", SOLID_CAT)
    rect(U(8000), z(LV["TUM"] - sd), U(11800), z(LV["TUM"]), "MAT-CAT", SOLID_CAT)
    # tuong cat (tuong chay theo X, cat qua X = 2700)
    cat = [("T1", 0, 200, 0, LV["T2"], "D1"), ("T1", 10250, 10350, 0, LV["T2"], None),
           ("T1", 13800, 14000, 0, LV["T2"], "S2")]
    for k in ("T2", "T3"):
        top = LV["T3"] if k == "T2" else None
        cat += [(k, 1400, 1600, LV[k], top or mai_z("M1", 1400) - 120, "D3" if k == "T2" else "S5"),
                (k, 8050, 8150, LV[k], top or LV["ST"], None), (k, 10250, 10350, LV[k], top or LV["ST"], None),
                (k, 11650, 11750, LV[k], top or LV["ST"], None),
                (k, 13800, 14000, LV[k], top or LV["ST"], "S2")]
    cat += [("MAI", 8000, 8200, LV["ST"], LV["TUM"], None), ("MAI", 11600, 11800, LV["ST"], LV["TUM"], None)]
    for _, a, b, z0, z1, code in cat:
        if code:
            _, w, h, be = CUA[code]
            if be > 0:
                rect(U(a), z(z0), U(b), z(z0 + be), "MAT-CAT", SOLID_CAT)
            rect(U(a), z(z0 + be + h), U(b), z(z1), "MAT-CAT", SOLID_CAT)
            line(U((a + b) / 2), z(z0 + be), U((a + b) / 2), z(z0 + be + h), "MAT-CAT")
        else:
            rect(U(a), z(z0), U(b), z(z1), "MAT-CAT", SOLID_CAT)
    rect(U(0), z(LV["T2"]), U(200), z(LV["T2"] + 1000), "MAT-CAT", SOLID_CAT)
    rect(U(11800), z(LV["ST"]), U(14000), z(LV["ST"]), "MAT-CAT")
    rect(U(13800), z(LV["ST"]), U(14000), z(LV["ST"] + 1000), "MAT-CAT", SOLID_CAT)
    rect(U(8000), z(LV["TUM"]), U(8200), z(LV["TUM"] + 400), "MAT-CAT", SOLID_CAT)
    rect(U(11600), z(LV["TUM"]), U(11800), z(LV["TUM"] + 400), "MAT-CAT", SOLID_CAT)
    for code in ("M1", "M2"):
        _, _, r, dinh, mep, _ = MAI[code]
        poly([(U(r[1]), z(mep - 120)), (U(r[1]), z(mep)), (U(r[3]), z(dinh)), (U(r[3]), z(dinh - 120))],
             "MAT-CAT", hatch=SOLID_CAT)
    # thang nhin thay (bac cat va chieu nghi phia sau)
    for k in ("T1", "T2", "T3"):
        lv0 = LV[k]
        lv1 = LV["T2"] if k == "T1" else (LV["T3"] if k == "T2" else LV["ST"])
        cb = (lv1 - lv0) / 20
        n1 = int((VE1[2] - 2700) / MAT_BAC) + 1          # bac cua ve 1 bi cat tai X = 2700
        n2 = int((2700 - VE2[0]) / MAT_BAC) + 1 + 10
        for n, (ya, yb) in ((n1, (VE1[1], VE1[3])), (n2, (VE2[1], VE2[3]))):
            rect(U(ya), z(lv0 + (n - 1) * cb - 150), U(yb), z(lv0 + n * cb), "MAT-CAT", SOLID_CAT)
        rect(U(CHIEU_NGHI[1]), z(lv0 + 10 * cb - 120), U(CHIEU_NGHI[3]), z(lv0 + 10 * cb), "MAT-DUNG")
    moc_cao_do(U(-5500) - 400, [LV["SAN"], 0, LV["T2"], LV["T3"], LV["ST"], MAI["M1"][3], LV["TUM"]], trai=True)
    chain([z(v) for v in (LV["SAN"], 0, LV["T2"], LV["T3"], LV["ST"], LV["TUM"])], U(16000), U(16700), True)
    for ten, y, v in (("PHÒNG KHÁCH", 4000, 0), ("BẾP ĂN", 12800, 0), ("PHÒNG NGỦ 1", 4800, LV["T2"]),
                      ("PHÒNG NGỦ 2", 13000, LV["T2"]), ("PHÒNG SINH HOẠT", 4800, LV["T3"]),
                      ("PHÒNG THỜ", 13000, LV["T3"]), ("TUM", 9900, LV["ST"]), ("SÂN THƯỢNG", 13100, LV["ST"])):
        text(U(y), z(v + 1200), ten, 250, "CHU")
    text(U(5000), z(-2600), "MẶT CẮT 1-1 (CẮT TẠI X = 2700)", 350, "CHU")
    text(U(5000), z(-3150), "TỶ LỆ 1/100", 250, "CHU")


# =====================================================================================
# BANG THONG SO (dat trong Model de may doc duoc)
# =====================================================================================
def bang(x0, y0, tieu_de, cot, hang, lay):
    """cot: [(tieu de, rong)], hang: [[o, ...]]. Moi o la mot TEXT can trai."""
    rh = 600
    tong = sum(w for _, w in cot)
    text(x0 + tong / 2, y0 + 450, tieu_de, 350, "CHU")
    rows = [[c for c, _ in cot]] + hang
    for i in range(len(rows) + 1):
        line(x0, y0 - i * rh, x0 + tong, y0 - i * rh, "BANG")
    x = x0
    for _, w in cot:
        line(x, y0, x, y0 - len(rows) * rh, "BANG")
        x += w
    line(x, y0, x, y0 - len(rows) * rh, "BANG")
    for i, row in enumerate(rows):
        x = x0
        for (_, w), val in zip(cot, row):
            text(x + 150, y0 - i * rh - 400, str(val), 220, "BANG" if i == 0 else lay, mid=False)
            x += w
    return y0 - len(rows) * rh


def dem_cua():
    n = {k: 0 for k in CUA}
    for key, ws in TUONG.items():
        for w in ws:
            for code, _, _ in w["ops"]:
                n[code] += 1
    return n


def ve_bang():
    x0 = 50000
    n = dem_cua()
    y = bang(x0, 15000, "BẢNG THỐNG KÊ CỬA", [("MÃ", 1200), ("TÊN CỬA", 7000), ("RỘNG", 1500), ("CAO", 1500),
                                              ("CAO BỆ", 1500), ("SỐ LƯỢNG", 1800)],
             [[k, v[0], v[1], v[2], v[3], n[k]] for k, v in CUA.items()], "BANG-CUA")
    bang(x0, 7500, "BẢNG CAO ĐỘ", [("MỐC", 3500), ("CAO ĐỘ (m)", 2500)],
         [["Sân", cot_cao(LV["SAN"])], ["Tầng 1", cot_cao(0)], ["Tầng 2", cot_cao(LV["T2"])],
          ["Tầng 3", cot_cao(LV["T3"])], ["Sân thượng", cot_cao(LV["ST"])], ["Mái tum", cot_cao(LV["TUM"])]],
         "BANG-CAO-DO")
    bang(x0 + 7000, 7500, "BẢNG MÁI (DỐC VỀ PHÍA MẶT TIỀN)",
         [("MÃ", 1000), ("TÊN MÁI", 5800), ("ÁP CHO", 1800), ("ĐỈNH (m)", 1700), ("MÉP (m)", 1700)],
         [[k, v[0], v[1], cot_cao(v[3]), cot_cao(v[4])] for k, v in MAI.items()], "BANG-MAI")
    bang(x0, 2500, "BẢNG THÔNG SỐ DỰNG HÌNH", [("THÔNG SỐ", 5500), ("GIÁ TRỊ (mm)", 2500)],
         [[a, b] for a, b in THONG_SO], "BANG-THONG-SO")
    text(x0 + 13000, 2950, "GHI CHÚ VẬT LIỆU HOÀN THIỆN", 350, "CHU")
    for i, s in enumerate(VAT_LIEU):
        text(x0 + 9500, 2200 - i * 550, f"{i + 1}. {s}", 230, "GHI-CHU-VAT-LIEU", mid=False)
    text(x0 + 9500, 2200 - len(VAT_LIEU) * 550 - 300,
         "Phương án kiến trúc mẫu để dựng 3D; kết cấu chưa tính toán, cần kỹ sư duyệt.", 230, "CHU", mid=False)


# =====================================================================================
# LAYOUT A3
# =====================================================================================
TO = [  # (ma, ten to, tam vung Model)
    ("KT-01", "MẶT BẰNG TẦNG 1, TẦNG 2, TẦNG 3", (12000, 4150)),
    ("KT-02", "MẶT BẰNG MÁI, BẢNG THỐNG KÊ", (56000, 5500)),
    ("KT-03", "MẶT ĐỨNG CHÍNH, MẶT ĐỨNG BÊN", (14150, -20800)),
    ("KT-04", "MẶT CẮT 1-1", (50100, -20800)),
]


def ve_layouts():
    for ma, ten, (cx, cy) in TO:
        L.append(f'(mk-layout "{ma}" {u(ten)} {f(cx)} {f(cy)})')


# =====================================================================================
ve_mat_bang("T1", "MẶT BẰNG TẦNG 1 VÀ SÂN")
ve_mat_bang("T2", "MẶT BẰNG TẦNG 2")
ve_mat_bang("T3", "MẶT BẰNG TẦNG 3")
ve_mat_bang("MAI", "MẶT BẰNG MÁI, TUM")
mat_dung_chinh()
mat_dung_ben()
mat_cat()
ve_bang()
N_MODEL = len(L)
ve_layouts()

HEADER = r'''
(vl-load-com)
(setq acad (vlax-get-acad-object))
(setq doc (vla-get-activedocument acad))
(if (not (wcmatch (strcase (vla-get-name doc)) "%DOC%*")) (exit))
(vla-put-activespace doc 1)
(setq ms (vla-get-modelspace doc) old nil)
(vlax-for o ms (setq old (cons o old)))
(foreach o old (vla-delete o))
(vla-setvariable doc "INSUNITS" 4)
(vla-setvariable doc "LTSCALE" 50.0)
(vla-setvariable doc "PSLTSCALE" 0)
(defun sp (o p v) (vl-catch-all-apply 'vlax-put-property (list o p v)))
(vl-catch-all-apply 'vla-load (list (vla-get-linetypes doc) "CENTER" "acadiso.lin"))
(vl-catch-all-apply 'vla-load (list (vla-get-linetypes doc) "DASHED" "acadiso.lin"))
(foreach l '(("TRUC" 1 13 "CENTER") ("TUONG" 7 50 nil) ("HATCH" 8 13 nil) ("COT" 7 50 nil) ("CUA" 4 18 nil)
             ("KY-HIEU-CUA" 4 18 nil) ("CAU-THANG" 2 18 nil) ("LAN-CAN" 30 35 nil) ("SAN" 8 13 nil)
             ("SAN-LO" 8 13 "DASHED") ("MAI" 1 25 "DASHED") ("KICH-THUOC" 3 13 nil) ("CHU" 7 18 nil)
             ("RANH-DAT" 6 25 "DASHED") ("SAN-VUON" 8 13 nil) ("RAO" 30 35 nil) ("CONG" 30 18 nil)
             ("BAC-THEM" 8 18 nil) ("PERGOLA" 30 25 nil) ("MAY-LANH" 9 18 nil) ("ONG-XOI" 3 18 nil)
             ("KIM-THU-SET" 1 18 nil) ("BON-NUOC" 5 18 nil) ("MAT-DUNG" 7 25 nil) ("MAT-CAT" 7 50 nil)
             ("BANG" 7 18 nil) ("BANG-CUA" 7 13 nil) ("BANG-CAO-DO" 7 13 nil) ("BANG-MAI" 7 13 nil)
             ("BANG-THONG-SO" 7 13 nil) ("GHI-CHU-VAT-LIEU" 7 13 nil) ("KHUNG" 7 50 nil)
             ("NOI-THAT" 8 13 nil) ("NOI-THAT-TREN" 8 13 "DASHED") ("NOI-THAT-TEN" 8 9 nil))
  (setq lo (vla-add (vla-get-layers doc) (car l)))
  (vla-put-color lo (cadr l)) (sp lo 'Lineweight (caddr l))
  (if (cadddr l) (sp lo 'Linetype (cadddr l))))
(setq ts (vla-add (vla-get-textstyles doc) "ARIAL"))
(vla-setfont ts "Arial" :vlax-false :vlax-false 0 34)
(defun p3 (x y) (vlax-3d-point (list (float x) (float y) 0.0)))
(defun pl (c cl lay / a o)
  (setq a (vlax-make-safearray vlax-vbDouble (cons 0 (1- (length c)))))
  (vlax-safearray-fill a (mapcar 'float c))
  (setq o (vla-addlightweightpolyline ms a))
  (if cl (vla-put-closed o :vlax-true)) (vla-put-layer o lay) o)
(defun ht (o pat scl lay / h a)
  (setq h (vla-addhatch ms 1 pat :vlax-false))
  (vla-put-layer h lay)
  (if (/= pat "SOLID") (vla-put-patternscale h (float scl)))
  (setq a (vlax-make-safearray vlax-vbObject '(0 . 0)))
  (vlax-safearray-put-element a 0 o)
  (vla-appendouterloop h a) (vla-evaluate h) h)
(defun ln (x1 y1 x2 y2 lay) (vla-put-layer (vla-addline ms (p3 x1 y1) (p3 x2 y2)) lay))
(defun ci (x y r lay) (vla-put-layer (vla-addcircle ms (p3 x y) (float r)) lay))
(defun ar (x y r a0 a1 lay)
  (vla-put-layer (vla-addarc ms (p3 x y) (float r) (* pi (/ a0 180.0)) (* pi (/ a1 180.0))) lay))
(defun tx (x y s h lay mid / t1)
  (if mid
    (progn (setq t1 (vla-addmtext ms (p3 x y) 0.0 s))
           (vla-put-attachmentpoint t1 5) (vla-put-insertionpoint t1 (p3 x y)))
    (setq t1 (vla-addtext ms s (p3 x y) (float h))))
  (vla-put-stylename t1 "ARIAL") (vla-put-height t1 (float h)) (vla-put-layer t1 lay) t1)
(defun dm (x1 y1 x2 y2 dx dy vert / d)
  (setq d (vla-adddimrotated ms (p3 x1 y1) (p3 x2 y2) (p3 dx dy) (if vert (/ pi 2) 0.0)))
  (vla-put-layer d "KICH-THUOC")
  (foreach pv (list (cons 'TextStyle "ARIAL") (cons 'TextHeight 250.0) (cons 'Arrowhead1Type 4)
                    (cons 'Arrowhead2Type 4) (cons 'ArrowheadSize 120.0) (cons 'ExtensionLineExtend 100.0)
                    (cons 'ExtensionLineOffset 100.0) (cons 'TextGap 60.0) (cons 'PrimaryUnitsPrecision 0)
                    (cons 'VerticalTextPosition 1) (cons 'TextInsideAlign :vlax-false)
                    (cons 'TextOutsideAlign :vlax-false) (cons 'DimensionLineExtend 100.0))
    (sp d (car pv) (cdr pv)))
  d)
'''.replace("%DOC%", DOC_NAME)

LAYOUT_FN = r'''
(defun ps-ln (blk x1 y1 x2 y2) (vla-put-layer (vla-addline blk (p3 x1 y1) (p3 x2 y2)) "KHUNG"))
(defun ps-tx (blk x y s h / t1)
  (setq t1 (vla-addtext blk s (p3 x y) (float h)))
  (vla-put-stylename t1 "ARIAL") (vla-put-layer t1 "KHUNG") t1)
(defun ps-rect (blk x1 y1 x2 y2) (ps-ln blk x1 y1 x2 y1) (ps-ln blk x2 y1 x2 y2) (ps-ln blk x2 y2 x1 y2) (ps-ln blk x1 y2 x1 y1))
(defun mk-layout (ma ten cx cy / lays lay blk vp r)
  (setq lays (vla-get-layouts doc))
  (setq r (vl-catch-all-apply 'vla-item (list lays ma)))
  (if (not (vl-catch-all-error-p r)) (vla-delete r))
  (setq lay (vla-add lays ma))
  (sp lay 'ConfigName "DWG To PDF.pc3")
  (sp lay 'CanonicalMediaName "ISO_full_bleed_A3_(420.00_x_297.00_MM)")
  (sp lay 'PaperUnits 1)
  (sp lay 'PlotRotation 0)
  (vla-put-activelayout doc lay)
  (setq blk (vla-get-block lay))
  (setq old nil)
  (vlax-for o blk (setq old (cons o old)))
  (foreach o old (vl-catch-all-apply 'vla-delete (list o)))
  (ps-rect blk 20 10 410 287)
  (ps-ln blk 20 32 410 32)
  (foreach x '(110 230 330 370) (ps-ln blk x 10 x 32))
  (ps-tx blk 24 24 "C\\U+00D4NG TY CES AI" 3.5)
  (ps-tx blk 24 15 "PH\\U+01AF\\U+01A0NG \\U+00C1N M\\U+1EAAU" 2.5)
  (ps-tx blk 114 24 "NH\\U+00C0 PH\\U+1ED0 M\\U+1EAAU L\\U+00D4 7x20M" 3.5)
  (ps-tx blk 114 15 ten 2.5)
  (ps-tx blk 234 24 "T\\U+1EF6 L\\U+1EC6 1/100" 2.5)
  (ps-tx blk 234 15 "NG\\U+00C0Y 07/10/2026" 2.5)
  (ps-tx blk 334 22 "M\\U+00C3 T\\U+1EDC" 2.5)
  (ps-tx blk 374 20 ma 5.0)
  (setq vp (vla-addpviewport blk (p3 215 159.5) 386.0 251.0))
  (vla-put-layer vp "KHUNG")
  (vla-display vp :vlax-true)
  (setvar "CMDECHO" 0)
  (command "_.MSPACE")
  (command "_.ZOOM" "_C" (list (float cx) (float cy) 0.0) "0.01xp")
  (command "_.PSPACE")
  (sp vp 'DisplayLocked :vlax-true)
  ma)
'''

FOOTER = r'''
(vla-put-activelayout doc (vla-item (vla-get-layouts doc) "Model"))
(vla-zoomextents acad)
(setq n 0)
(vlax-for o ms (setq n (1+ n)))
(setq sv (vl-catch-all-apply 'vla-save (list doc)))
(strcat "ENT=" (itoa n) " | LAYOUT=" (itoa (vla-get-count (vla-get-layouts doc)))
        " | SAVE=" (if (vl-catch-all-error-p sv) (vl-catch-all-error-message sv) "ok")
        " | TEN=" (vla-get-fullname doc))
'''

OUT_LSP.write_text(HEADER + LAYOUT_FN + "\n".join(L) + "\n" + FOOTER, encoding="ascii")
print("OK", N_MODEL, "lenh Model,", len(L) - N_MODEL, "layout")
