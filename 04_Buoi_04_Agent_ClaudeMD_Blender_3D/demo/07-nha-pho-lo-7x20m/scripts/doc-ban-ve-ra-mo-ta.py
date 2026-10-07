# -*- coding: utf-8 -*-
"""Doc ban ve DXF (sinh tu AutoCAD) ra file mo ta JSON de dung 3D.

Chay:  python doc-ban-ve-ra-mo-ta.py <ban-ve.dxf> <mo-ta.json>

Moi so lieu lay tu ban ve:
- Hinh hoc (tuong, cua, cot, san, mai, thang, san vuon...) doc theo layer trong tung vung mat bang.
- Chieu cao (cao do, cua, mai, thong so dung hinh) doc tu 4 bang dat trong Model.
Chi co bang VUNG duoi day la khai bao tay: vi tri moi mat bang tren ban ve va goc toa do cua no.
"""
import json
import math
import re
import sys
from collections import defaultdict

import ezdxf

DXF, OUT = sys.argv[1], sys.argv[2]

# vung (x1, y1, x2, y2) va goc toa do cua tung mat bang tren ban ve, don vi mm
VUNG = {
    "T1": ((-6000, -9000, 8000, 17500), (0, 0)),
    "T2": ((8000, -4000, 19000, 17500), (11000, 0)),
    "T3": ((19000, -4000, 30000, 17500), (22000, 0)),
    "MAI": ((36000, -4000, 48000, 17500), (40000, 0)),
}
VUNG_BANG = (49000, -8000, 80000, 17000)

doc = ezdxf.readfile(DXF)
msp = doc.modelspace()


def giai_ma(s):
    s = re.sub(r"\\U\+([0-9A-Fa-f]{4})", lambda m: chr(int(m.group(1), 16)), s)
    return s.strip()


def trong(p, v):
    return v[0] <= p[0] <= v[2] and v[1] <= p[1] <= v[3]


# ---------------------------------------------------------------- thu thap doi tuong
chu = []          # (layer, x, y, text)
hinh_kin = []     # (layer, [(x, y)...])
duong = []        # (layer, x1, y1, x2, y2)
tron = []         # (layer, x, y, r)
for e in msp:
    t = e.dxftype()
    lay = e.dxf.layer
    if t == "TEXT":
        p = e.dxf.insert
        chu.append((lay, p.x, p.y, giai_ma(e.dxf.text)))
    elif t == "MTEXT":
        p = e.dxf.insert
        chu.append((lay, p.x, p.y, giai_ma(e.plain_text())))
    elif t == "LWPOLYLINE":
        pts = [(round(x, 1), round(y, 1)) for x, y in e.get_points("xy")]
        if e.closed:
            hinh_kin.append((lay, pts))
        else:
            for a, b in zip(pts, pts[1:]):
                duong.append((lay, a[0], a[1], b[0], b[1]))
    elif t == "LINE":
        duong.append((lay, e.dxf.start.x, e.dxf.start.y, e.dxf.end.x, e.dxf.end.y))
    elif t == "CIRCLE":
        tron.append((lay, e.dxf.center.x, e.dxf.center.y, e.dxf.radius))


def hcn(pts):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return [min(xs), min(ys), max(xs), max(ys)]


# ---------------------------------------------------------------- doc bang
def doc_bang(layer):
    hang = defaultdict(list)
    for lay, x, y, s in chu:
        if lay == layer and trong((x, y), VUNG_BANG):
            hang[round(y / 100)].append((x, s))
    return [[s for _, s in sorted(v)] for _, v in sorted(hang.items(), reverse=True)]


def so_cao_do(s):
    s = s.replace("±", "").replace("+", "").strip()
    return round(float(s) * 1000)


TEN_MOC = {"Sân": "SAN", "Tầng 1": "T1", "Tầng 2": "T2", "Tầng 3": "T3", "Sân thượng": "ST", "Mái tum": "TUM"}
cao_do = {TEN_MOC[r[0]]: so_cao_do(r[1]) for r in doc_bang("BANG-CAO-DO")}
cua = {r[0]: {"ten": r[1], "rong": int(r[2]), "cao": int(r[3]), "be": int(r[4]), "so_luong": int(r[5])}
       for r in doc_bang("BANG-CUA")}
AP_CHO = {"Tầng 3": "T3", "Tầng 2": "T2", "Tum": "MAI", "Sân trước": "SAN"}
mai = {r[0]: {"ten": r[1], "ap_cho": AP_CHO[r[2]], "dinh": so_cao_do(r[3]), "mep": so_cao_do(r[4])}
       for r in doc_bang("BANG-MAI")}
thong_so = {r[0]: int(r[1]) for r in doc_bang("BANG-THONG-SO")}
vat_lieu = [s for lay, x, y, s in chu if lay == "GHI-CHU-VAT-LIEU"]

# ---------------------------------------------------------------- doc mat bang
mat_bang = {}
canh_bao = []
for key, (v, (gx, gy)) in VUNG.items():
    def L(pts):
        return [[round(p[0] - gx), round(p[1] - gy)] for p in pts]

    def rect_layer(layer):
        out = []
        for lay, pts in hinh_kin:
            if lay == layer and all(trong(p, v) for p in pts):
                r = hcn(pts)
                out.append([round(r[0] - gx), round(r[1] - gy), round(r[2] - gx), round(r[3] - gy)])
        return out

    def chu_layer(layer):
        return [(x - gx, y - gy, s) for lay, x, y, s in chu if lay == layer and trong((x, y), v)]

    mb = {"tuong": rect_layer("TUONG"), "cot": rect_layer("COT"), "lan_can": rect_layer("LAN-CAN"),
          "san": rect_layer("SAN"), "lo_san": rect_layer("SAN-LO")}
    # cua: o cua kin tren layer CUA, ma cua la chu gan nhat tren layer KY-HIEU-CUA
    ma_cua = chu_layer("KY-HIEU-CUA")
    mb["cua"] = []
    for r in rect_layer("CUA"):
        cx, cy = (r[0] + r[2]) / 2, (r[1] + r[3]) / 2
        gan = min(ma_cua, key=lambda t: math.hypot(t[0] - cx, t[1] - cy))
        if math.hypot(gan[0] - cx, gan[1] - cy) > 900:
            canh_bao.append(f"{key}: o cua tai ({cx:.0f},{cy:.0f}) khong co ma cua gan")
        mb["cua"].append({"ma": gan[2], "hcn": r, "doc_x": (r[2] - r[0]) > (r[3] - r[1])})
    # mai ve tren mat bang nay: nhan Mx nam trong hinh
    nhan_mai = chu_layer("MAI")
    mb["mai"] = []
    for r in rect_layer("MAI"):
        for x, y, s in nhan_mai:
            if re.fullmatch(r"M\d", s) and r[0] <= x <= r[2] and r[1] <= y <= r[3]:
                mb["mai"].append({"ma": s, "hcn": r})
    # thang: 3 hinh kin (2 ve + chieu nghi), dem duong bac trong moi ve, chu LEN danh dau ve 1
    hinh_thang = rect_layer("CAU-THANG")
    if hinh_thang:
        nghi = max(hinh_thang, key=lambda r: (r[3] - r[1]) / max(r[2] - r[0], 1))
        ve = [r for r in hinh_thang if r is not nghi]
        len_ = [(x, y) for x, y, s in chu_layer("CAU-THANG") if s.upper() == "LÊN"]
        lx, ly = len_[0]
        ve.sort(key=lambda r: math.hypot((r[0] + r[2]) / 2 - lx, (r[1] + r[3]) / 2 - ly))
        bac = []
        for r in ve:
            n = 0
            for lay, x1, y1, x2, y2 in duong:
                if lay != "CAU-THANG":
                    continue
                x1, y1, x2, y2 = x1 - gx, y1 - gy, x2 - gx, y2 - gy
                if abs(x1 - x2) < 1 and r[0] + 1 < x1 < r[2] - 1 and min(y1, y2) >= r[1] - 1 and max(y1, y2) <= r[3] + 1:
                    n += 1
            bac.append(n + 1)
        # ve 1 bat dau o dau xa chieu nghi
        mb["thang"] = {"ve1": ve[0], "ve2": ve[1], "chieu_nghi": nghi, "so_bac_moi_ve": bac}
    # noi that: moi hinh chu nhat nhan ten nam trong no (chon hinh nho nhat chua chu);
    # mat lung = canh sat tuong, cot hoac lan can nhat (cach toi da 400 mm)
    hinh_nt = [(r, False) for r in rect_layer("NOI-THAT")] + [(r, True) for r in rect_layer("NOI-THAT-TREN")]
    ten_nt = {}
    for x, y, s in chu_layer("NOI-THAT-TEN"):
        chua = [i for i, (r, _) in enumerate(hinh_nt) if r[0] <= x <= r[2] and r[1] <= y <= r[3]]
        if not chua:
            canh_bao.append(f"{key}: ten noi that '{s}' khong nam trong hinh nao")
            continue
        i = min(chua, key=lambda i: (hinh_nt[i][0][2] - hinh_nt[i][0][0]) * (hinh_nt[i][0][3] - hinh_nt[i][0][1]))
        ten_nt[i] = s
    vat_can = mb["tuong"] + mb["cot"] + mb["lan_can"]

    def mat_lung(r):
        tot = (401, None)
        for w in vat_can:
            chong_y = w[1] < r[3] and w[3] > r[1]
            chong_x = w[0] < r[2] and w[2] > r[0]
            for canh, ok, d in (("T", chong_y and w[2] <= r[0] + 1, r[0] - w[2]),
                                ("P", chong_y and w[0] >= r[2] - 1, w[0] - r[2]),
                                ("D", chong_x and w[3] <= r[1] + 1, r[1] - w[3]),
                                ("S", chong_x and w[1] >= r[3] - 1, w[1] - r[3])):
                if ok and d < tot[0]:
                    tot = (d, canh)
        return tot[1]

    mb["noi_that"] = []
    for i, (r, tren) in enumerate(hinh_nt):
        if i not in ten_nt:
            canh_bao.append(f"{key}: hinh noi that tai {r} chua co ten")
            continue
        mb["noi_that"].append({"ten": ten_nt[i], "hcn": r, "treo": tren, "lung": mat_lung(r)})
    if key == "T1":
        for ten, layer in (("ranh_dat", "RANH-DAT"), ("san_vuon", "SAN-VUON"), ("rao", "RAO"), ("cong", "CONG"),
                           ("bac", "BAC-THEM"), ("pergola_cot", "PERGOLA"), ("may_lanh", "MAY-LANH")):
            mb[ten] = rect_layer(layer)
        mb["pergola_xa"] = [[round(x1 - gx), round(y1 - gy), round(x2 - gx), round(y2 - gy)]
                            for lay, x1, y1, x2, y2 in duong
                            if lay == "PERGOLA" and trong((x1, y1), v) and trong((x2, y2), v)]
        mb["ong_xoi"] = [[round(x - gx), round(y - gy), round(r)] for lay, x, y, r in tron
                         if lay == "ONG-XOI" and trong((x, y), v)]
    if key == "MAI":
        mb["bon_nuoc"] = [[round(x - gx), round(y - gy), round(r)] for lay, x, y, r in tron
                          if lay == "BON-NUOC" and trong((x, y), v)]
        mb["kim_thu_set"] = [[round(x - gx), round(y - gy)] for lay, x, y, r in tron
                             if lay == "KIM-THU-SET" and trong((x, y), v)]
    mat_bang[key] = mb

# ---------------------------------------------------------------- soat: so cua dem duoc so voi bang
dem = defaultdict(int)
for mb in mat_bang.values():
    for c in mb["cua"]:
        dem[c["ma"]] += 1
for ma, c in cua.items():
    if dem[ma] != c["so_luong"]:
        canh_bao.append(f"Cua {ma}: dem tren mat bang {dem[ma]}, bang thong ke ghi {c['so_luong']}")
for ma in dem:
    if ma not in cua:
        canh_bao.append(f"Ma cua {ma} co tren mat bang nhung khong co trong bang thong ke")

mo_ta = {"nguon": DXF, "don_vi": "mm", "cao_do": cao_do, "cua": cua, "mai": mai, "thong_so": thong_so,
         "vat_lieu": vat_lieu, "mat_bang": mat_bang, "canh_bao": canh_bao}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(mo_ta, f, ensure_ascii=False, indent=1)

print("Cao do:", cao_do)
print("Mai:", {k: (m["ap_cho"], m["dinh"], m["mep"]) for k, m in mai.items()})
print("Thong so:", len(thong_so), "dong")
for k, mb in mat_bang.items():
    print(f"{k}: tuong {len(mb['tuong'])}, cua {len(mb['cua'])}, cot {len(mb['cot'])}, lan can {len(mb['lan_can'])},"
          f" san {len(mb['san'])}, lo san {len(mb['lo_san'])}, mai {[m['ma'] for m in mb['mai']]},"
          f" thang {mb.get('thang', {}).get('so_bac_moi_ve')}, noi that {len(mb['noi_that'])}")
    print("   ", ", ".join(f"{n['ten']}({n['lung']})" for n in mb["noi_that"]))
print("So cua theo ma:", dict(dem))
print("Canh bao:", canh_bao or "khong co")
