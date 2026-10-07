# -*- coding: utf-8 -*-
"""Dung mo hinh 3D nha pho lo 7x20m trong Blender tu file mo ta JSON (doc ra tu ban ve DXF).

Chay (khong mo giao dien):
  blender --background --factory-startup --python dung-nha-blender.py -- <mo-ta.json> <thu-muc-ra> [ten-blend] [anh1,anh2,anh3]

Moi kich thuoc lay tu file mo ta. Script chi quy dinh cach the hien: vat lieu, den, camera.
"""
import json
import math
import sys
from pathlib import Path

import bmesh
import bpy

# Hai cach chay:
# 1) Chay nen tu dong lenh: tham so sau dau "--" (xem docstring).
# 2) Chay trong Blender dang mo qua MCP (cong cu chay_python): them mot dong o dau doan code
#    THAM_SO = {"mo_ta": r"...\03_mo-ta-tu-ban-ve.json", "ra": r"...\thu-muc-ra", "render": False}
if "--" in sys.argv:
    args = sys.argv[sys.argv.index("--") + 1:]
    THAM_SO = {"mo_ta": args[0], "ra": args[1], "render": True}
    if len(args) > 2:
        THAM_SO["blend"] = args[2]
    if len(args) > 3:
        THAM_SO["anh"] = args[3].split(",")
MO_TA, RA = Path(THAM_SO["mo_ta"]), Path(THAM_SO["ra"])
CO_RENDER = THAM_SO.get("render", True)
TEN_BLEND = THAM_SO.get("blend", "04_nha-pho-lo-7x20m.blend")
TEN_ANH = THAM_SO.get("anh", ["05_phoi-canh-goc-hong.png", "06_phoi-canh-tren-cao.png", "07_phoi-canh-mat-tien.png"])
D = json.loads(MO_TA.read_text(encoding="utf-8"))
CD, CUA, MAI, TS, MB = D["cao_do"], D["cua"], D["mai"], D["thong_so"], D["mat_bang"]
K = 0.001  # mm -> m

NEN = {"T1": "T1", "T2": "T2", "T3": "T3", "MAI": "ST"}
TREN = {"T1": "T2", "T2": "T3", "T3": "ST", "MAI": "TUM"}
SAN_DAY = TS["Sàn BTCT dày"]
MAI_DAY = TS["Mái tôn dày (kể xà gồ)"]
LAN_CAN_CAO = TS["Lan can, tường chắn mái cao"]
CHI_DUA = TS["Chỉ tường đua ra"]

# ------------------------------------------------------------------ xoa canh mac dinh
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o, do_unlink=True)
for c in list(bpy.data.collections):
    bpy.data.collections.remove(c)
scene = bpy.context.scene
NHOM = {}
# Moi tang mot collection cha; ten nhom con bat dau bang ma tang (T1, T2, T3, MAI), "mai" thuoc Mai - Tum,
# con lai (san vuon, pergola, thiet bi ngoai nha) thuoc San vuon.
TANG = {"T1": "Tang 1", "T2": "Tang 2", "T3": "Tang 3", "MAI": "Mai - Tum"}
THU_TU_TANG = ["San vuon", "Tang 1", "Tang 2", "Tang 3", "Mai - Tum"]


def tang_cua(ten):
    dau = ten.split()[0]
    if dau in TANG:
        return TANG[dau]
    return "Mai - Tum" if dau == "mai" else "San vuon"


def nhom(ten):
    if ten not in NHOM:
        cha_ten = tang_cua(ten)
        if cha_ten not in NHOM:
            cha = bpy.data.collections.new(cha_ten)
            scene.collection.children.link(cha)
            NHOM[cha_ten] = cha
        c = bpy.data.collections.new(ten)
        NHOM[cha_ten].children.link(c)
        NHOM[ten] = c
    return NHOM[ten]


# ------------------------------------------------------------------ vat lieu
def principled(mat):
    return next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")


def vat_lieu(ten, mau, nham=0.8, kim_loai=0.0, alpha=1.0, van=None):
    """van: (truc, chu ky m, do sau) tao ranh/song bang bump theo toa do the gioi."""
    m = bpy.data.materials.new(ten)
    m.use_nodes = True
    p = principled(m)
    p.inputs["Base Color"].default_value = (*mau, 1)
    p.inputs["Roughness"].default_value = nham
    p.inputs["Metallic"].default_value = kim_loai
    if alpha < 1:
        p.inputs["Alpha"].default_value = alpha
    m.diffuse_color = (*mau, alpha)
    if van:
        truc, chu_ky, sau = van
        nt = m.node_tree
        toa_do = nt.nodes.new("ShaderNodeTexCoord")
        tach = nt.nodes.new("ShaderNodeSeparateXYZ")
        nt.links.new(toa_do.outputs["Object"], tach.inputs[0])
        if truc == "xy":
            cong = nt.nodes.new("ShaderNodeMath")
            cong.operation = "ADD"
            nt.links.new(tach.outputs[0], cong.inputs[0])
            nt.links.new(tach.outputs[1], cong.inputs[1])
            nguon = cong.outputs[0]
        else:
            nguon = tach.outputs["XYZ".index(truc.upper())]
        nhan = nt.nodes.new("ShaderNodeMath")
        nhan.operation = "MULTIPLY"
        nhan.inputs[1].default_value = 2 * math.pi / chu_ky
        nt.links.new(nguon, nhan.inputs[0])
        sin = nt.nodes.new("ShaderNodeMath")
        sin.operation = "SINE"
        nt.links.new(nhan.outputs[0], sin.inputs[0])
        bump = nt.nodes.new("ShaderNodeBump")
        bump.inputs["Strength"].default_value = sau
        nt.links.new(sin.outputs[0], bump.inputs["Height"])
        nt.links.new(bump.outputs["Normal"], p.inputs["Normal"])
    return m


VL = {
    "son_kem": vat_lieu("Son kem", (0.86, 0.72, 0.52), 0.9),
    "go_nau": vat_lieu("Op go nau", (0.40, 0.20, 0.09), 0.6, van=("xy", 0.15, 0.35)),
    "xam_nhat": vat_lieu("Son xam nhat", (0.72, 0.72, 0.70), 0.85),
    "tuong_trong": vat_lieu("Tuong trong", (0.90, 0.89, 0.86), 0.9),
    "ton_do": vat_lieu("Ton song do nau", (0.50, 0.15, 0.07), 0.45, 0.3, van=("x", 0.2, 0.5)),
    "be_tong": vat_lieu("Be tong", (0.55, 0.55, 0.53), 0.9),
    "kinh": vat_lieu("Kinh xanh nhat", (0.50, 0.68, 0.78), 0.05, 0.2),
    "kinh_mo": vat_lieu("Kinh mo", (0.80, 0.84, 0.86), 0.4),
    "khung": vat_lieu("Khung nhom xam", (0.22, 0.23, 0.24), 0.35, 0.7),
    "cua_go": vat_lieu("Cua go", (0.36, 0.20, 0.10), 0.5, van=("z", 0.25, 0.1)),
    "ong_xoi": vat_lieu("Ong xoi xanh la", (0.08, 0.38, 0.12), 0.4),
    "trang": vat_lieu("Cuc nong trang", (0.92, 0.92, 0.91), 0.5),
    "den": vat_lieu("Den", (0.03, 0.03, 0.03), 0.4, 0.5),
    "thep_nau_do": vat_lieu("Thep son nau do", (0.45, 0.14, 0.07), 0.5, 0.3),
    "polycarbonate": vat_lieu("Tam polycarbonate", (0.70, 0.80, 0.86), 0.15, 0.0, alpha=0.45),
    "co": vat_lieu("Co", (0.20, 0.38, 0.12), 1.0),
    "inox": vat_lieu("Inox", (0.86, 0.86, 0.88), 0.45, 0.5),
    # noi that
    "vai": vat_lieu("Vai sofa xam xanh", (0.30, 0.36, 0.44), 0.95),
    "vai_kem": vat_lieu("Vai goi kem", (0.85, 0.80, 0.70), 0.95),
    "go_sang": vat_lieu("Go soi sang", (0.62, 0.45, 0.28), 0.55, van=("xy", 0.08, 0.05)),
    "go_toi": vat_lieu("Go oc cho", (0.24, 0.14, 0.07), 0.5),
    "go_tho": vat_lieu("Go do ban tho", (0.36, 0.07, 0.04), 0.35),
    "san_go": vat_lieu("San go", (0.55, 0.38, 0.22), 0.5, van=("x", 0.18, 0.08)),
    "gach_xam": vat_lieu("Gach xam san thuong", (0.62, 0.62, 0.60), 0.7),
    "su_trang": vat_lieu("Su trang", (0.95, 0.95, 0.95), 0.15),
    "da_bep": vat_lieu("Da mat bep", (0.12, 0.12, 0.13), 0.25),
    "tham": vat_lieu("Tham", (0.72, 0.64, 0.52), 1.0),
    "chan": vat_lieu("Chan ga", (0.25, 0.45, 0.55), 0.9),
    "dong": vat_lieu("Dong thau", (0.80, 0.60, 0.25), 0.3, 1.0),
    "la_cay": vat_lieu("La cay", (0.12, 0.38, 0.10), 0.8),
    "dat_nung": vat_lieu("Chau dat nung", (0.60, 0.30, 0.18), 0.8),
    "son_xe": vat_lieu("Son xe do", (0.70, 0.06, 0.06), 0.25, 0.4),
    "lop_xe": vat_lieu("Lop xe", (0.03, 0.03, 0.03), 0.8),
    "kinh_toi": vat_lieu("Kinh toi", (0.04, 0.06, 0.08), 0.08, 0.3),
    "kinh_sen": vat_lieu("Kinh vach tam", (0.80, 0.90, 0.92), 0.05, 0.0, alpha=0.25),
    "sach_1": vat_lieu("Bia sach 1", (0.55, 0.15, 0.12), 0.7),
    "sach_2": vat_lieu("Bia sach 2", (0.15, 0.30, 0.50), 0.7),
    "sach_3": vat_lieu("Bia sach 3", (0.80, 0.70, 0.30), 0.7),
    "poche": vat_lieu("Mat cat tuong", (0.10, 0.10, 0.11), 0.9),
}
CAT = 1400   # cao do mat cat ngang cho anh mat bang tung tang, mm tren mat san
for _m in ("kinh_sen",):
    try:
        VL[_m].surface_render_method = "BLENDED"
    except AttributeError:
        VL[_m].blend_method = "BLEND"
try:
    VL["polycarbonate"].surface_render_method = "BLENDED"
except AttributeError:
    VL["polycarbonate"].blend_method = "BLEND"


# ------------------------------------------------------------------ hinh hoc co ban (dau vao mm)
def luoi(ten, verts, faces, mat, nhom_ten, vat=True):
    me = bpy.data.meshes.new(ten)
    me.from_pydata([(x * K, y * K, z * K) for x, y, z in verts], [], faces)
    me.update()
    o = bpy.data.objects.new(ten, me)
    nhom(nhom_ten).objects.link(o)
    o.data.materials.append(VL[mat])
    if vat:
        m = o.modifiers.new("vat canh", "BEVEL")
        m.width = 0.006
        m.segments = 1
        m.limit_method = "ANGLE"
    return o


def khoi(ten, x1, y1, x2, y2, z1, z2, mat, nhom_ten, z_tren=None, vat=True):
    """Hop chu nhat. z_tren: (z tai y1, z tai y2) neu mat tren nghieng theo Y."""
    if z2 - z1 <= 0.5 and z_tren is None:
        return None
    a, b = z_tren if z_tren else (z2, z2)
    v = [(x1, y1, z1), (x2, y1, z1), (x2, y2, z1), (x1, y2, z1), (x1, y1, a), (x2, y1, a), (x2, y2, b), (x1, y2, b)]
    f = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    return luoi(ten, v, f, mat, nhom_ten, vat)


def tru(ten, x, y, r, z1, z2, mat, nhom_ten, truc="z", doan=24):
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=doan, radius1=r * K, radius2=r * K, depth=(z2 - z1) * K)
    me = bpy.data.meshes.new(ten)
    bm.to_mesh(me)
    bm.free()
    o = bpy.data.objects.new(ten, me)
    nhom(nhom_ten).objects.link(o)
    o.data.materials.append(VL[mat])
    if truc == "z":
        o.location = (x * K, y * K, (z1 + z2) / 2 * K)
    elif truc == "x":  # (z1, z2) la khoang theo X, tam tai (y, z) = (x, y)
        o.rotation_euler = (0, math.pi / 2, 0)
        o.location = ((z1 + z2) / 2 * K, x * K, y * K)
    else:              # truc y: (z1, z2) la khoang theo Y, tam tai (x, z) = (x, y)
        o.rotation_euler = (math.pi / 2, 0, 0)
        o.location = (x * K, (z1 + z2) / 2 * K, y * K)
    for p in me.polygons:
        p.use_smooth = True
    return o


def hop_doc_x(ten, x1, x2, y1, y2, zd1, zd2, zt1, zt2, mat, nhom_ten):
    """Hop nghieng theo X: day tai (x1, x2) = (zd1, zd2), dinh tai (x1, x2) = (zt1, zt2)."""
    v = [(x1, y1, zd1), (x2, y1, zd2), (x2, y2, zd2), (x1, y2, zd1),
         (x1, y1, zt1), (x2, y1, zt2), (x2, y2, zt2), (x1, y2, zt1)]
    f = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    return luoi(ten, v, f, mat, nhom_ten, vat=False)


# ------------------------------------------------------------------ cao do tuong theo mai doc
def ham_mai(m, r):
    y1, y2 = r[1], r[3]
    return lambda y: m["mep"] + (y - y1) / (y2 - y1) * (m["dinh"] - m["mep"])


MAI_DOC = {}   # tang -> [(hcn, ham z mat tren)]
for key, mb in MB.items():
    for mm in mb["mai"]:
        m = MAI[mm["ma"]]
        if m["dinh"] != m["mep"]:
            MAI_DOC.setdefault(m["ap_cho"], []).append((mm["hcn"], ham_mai(m, mm["hcn"])))


def dinh_tuong(key, r):
    """Tra ve (z tai y1, z tai y2) cua mat tren tuong/cot dat tai hcn r tren tang key."""
    cx, cy = (r[0] + r[2]) / 2, (r[1] + r[3]) / 2
    for hr, f in MAI_DOC.get(key, []):
        if hr[0] <= cx <= hr[2] and hr[1] <= cy <= hr[3]:
            doc_x = (r[2] - r[0]) >= (r[3] - r[1])
            if doc_x:   # tuong chay theo X: lay cao do thap hon (mep y1)
                z = f(r[1]) - MAI_DAY
                return z, z
            return f(r[1]) - MAI_DAY, f(r[3]) - MAI_DAY
    z = CD[TREN[key]]
    return z, z


def la_tuong_ngoai(r):
    return min(r[2] - r[0], r[3] - r[1]) >= 190


def vl_tuong(key, r):
    if not la_tuong_ngoai(r):
        return "tuong_trong"
    return "son_kem" if key in ("T1", "T2") else "go_nau"


# ------------------------------------------------------------------ dung tung tang
dem = {"tuong": 0, "lo_cua": 0, "cot": 0}
for key, mb in MB.items():
    nen = CD[NEN[key]]
    for i, r in enumerate(mb["tuong"]):
        za, zb = dinh_tuong(key, r)
        khoi(f"{key}_tuong_{i}", *r, nen, za, vl_tuong(key, r), f"{key} tuong", z_tren=(za, zb))
        dem["tuong"] += 1
    for i, r in enumerate(mb["cot"]):
        za, zb = dinh_tuong(key, r)
        mat = "xam_nhat" if key in ("T1", "T2") else "go_nau"
        khoi(f"{key}_cot_{i}", *r, nen, min(za, zb), mat, f"{key} cot")
        dem["cot"] += 1
    for i, r in enumerate(mb["lan_can"]):
        khoi(f"{key}_lan_can_{i}", *r, nen, nen + LAN_CAN_CAO, "go_nau", f"{key} lan can")
        khoi(f"{key}_lan_can_mu_{i}", r[0] - 20, r[1] - 20, r[2] + 20, r[3] + 20, nen + LAN_CAN_CAO,
             nen + LAN_CAN_CAO + 40, "xam_nhat", f"{key} lan can")
    # mat cat to dam o cao do san + 1.4 m (chi bat khi render anh mat bang tung tang)
    if key != "MAI":
        for i, rr in enumerate(mb["tuong"] + mb["cot"] +
                               [c["hcn"] for c in mb["cua"] if CUA[c["ma"]]["be"] >= CAT]):
            khoi(f"{key}_cat_{i}", *rr, nen + CAT - 25, nen + CAT - 5, "poche", f"{key} cat mat bang", vat=False)
        NHOM[f"{key} cat mat bang"].hide_render = True
        NHOM[f"{key} cat mat bang"].hide_viewport = True
    # o cua: phan tuong duoi be, tren dau cua, khung va kinh
    for i, c in enumerate(mb["cua"]):
        r, ma, doc_x = c["hcn"], c["ma"], c["doc_x"]
        tt = CUA[ma]
        z0, z1 = nen + tt["be"], nen + tt["be"] + tt["cao"]
        za, zb = dinh_tuong(key, r)
        mat = vl_tuong(key, r)
        if tt["be"] > 0:
            khoi(f"{key}_{ma}_be_{i}", *r, nen, z0, mat, f"{key} tuong")
        if min(za, zb) > z1 + 1:
            khoi(f"{key}_{ma}_dau_{i}", *r, z1, za, mat, f"{key} tuong", z_tren=(za, zb))
        dem["lo_cua"] += 1
        # khung + kinh dat giua be day tuong
        a0, a1 = (r[0], r[2]) if doc_x else (r[1], r[3])
        bc = (r[1] + r[3]) / 2 if doc_x else (r[0] + r[2]) / 2

        def hop(ten, aa, ab, ba, bb, za_, zb_, m):
            if doc_x:
                khoi(ten, aa, ba, ab, bb, za_, zb_, m, f"{key} cua", vat=False)
            else:
                khoi(ten, ba, aa, bb, ab, za_, zb_, m, f"{key} cua", vat=False)

        n = {"D1": 4, "S5": 4, "D3": 2, "S1": 2, "S2": 2}.get(ma, 1)
        kh = 50
        hop(f"{key}_{ma}_khung_t_{i}", a0, a0 + kh, bc - 35, bc + 35, z0, z1, "khung")
        hop(f"{key}_{ma}_khung_p_{i}", a1 - kh, a1, bc - 35, bc + 35, z0, z1, "khung")
        hop(f"{key}_{ma}_khung_d_{i}", a0, a1, bc - 35, bc + 35, z1 - kh, z1, "khung")
        if tt["be"] > 0:
            hop(f"{key}_{ma}_khung_b_{i}", a0, a1, bc - 35, bc + 35, z0, z0 + kh, "khung")
            khoi(f"{key}_{ma}_bau_cua_{i}", *(r if doc_x else r), z0 - 30, z0, "xam_nhat", f"{key} cua", vat=False)
        for k in range(1, n):
            a = a0 + (a1 - a0) * k / n
            hop(f"{key}_{ma}_dong_{i}_{k}", a - 20, a + 20, bc - 30, bc + 30, z0, z1, "khung")
        kinh = "cua_go" if ma == "D2" else ("kinh_mo" if ma == "D4" else "kinh")
        day = 20 if ma == "D2" else 6
        hop(f"{key}_{ma}_kinh_{i}", a0 + kh, a1 - kh, bc - day, bc + day, z0 + (kh if tt["be"] > 0 else 0),
            z1 - kh, kinh)

    # san (tru lo thang), mo rong ra ngoai thanh chi tuong
    for j, r in enumerate(mb["san"]):
        if key == "T1":
            khoi("T1_nen", *r, CD["SAN"], 0, "xam_nhat", "T1 san")
            khoi("T1_lat_san", r[0] + 200, r[1] + 200, r[2] - 200, r[3] - 200, 0, 10, "tuong_trong", "T1 san",
                 vat=False)
            continue
        lv = CD[NEN[key]]
        x1, y1, x2, y2 = r[0] - CHI_DUA, r[1] - CHI_DUA, r[2] + CHI_DUA, r[3] + CHI_DUA
        manh = [(x1, y1, x2, y2)]
        for h in mb["lo_san"]:
            moi = []
            for (a, b, c, d) in manh:
                if h[2] <= a or h[0] >= c or h[3] <= b or h[1] >= d:
                    moi.append((a, b, c, d))
                    continue
                if h[1] > b:
                    moi.append((a, b, c, h[1]))
                if h[3] < d:
                    moi.append((a, h[3], c, d))
                if h[0] > a:
                    moi.append((a, max(b, h[1]), h[0], min(d, h[3])))
                if h[2] < c:
                    moi.append((h[2], max(b, h[1]), c, min(d, h[3])))
            manh = moi
        for k, m in enumerate(manh):
            khoi(f"{key}_san_{j}_{k}", *m, lv - SAN_DAY - 30, lv, "xam_nhat", f"{key} san")
            # lop hoan thien san: go cho tang 2, 3; gach xam cho tum, san thuong
            a, b = max(m[0], r[0] + 200), max(m[1], r[1] + 200)
            c, d = min(m[2], r[2] - 200), min(m[3], r[3] - 200)
            if c - a > 50 and d - b > 50:
                khoi(f"{key}_lat_san_{j}_{k}", a, b, c, d, lv, lv + 10,
                     "gach_xam" if key == "MAI" else "san_go", f"{key} san", vat=False)

    # thang: 2 ve + chieu nghi
    if mb.get("thang"):
        t = mb["thang"]
        nen_t, tren_t = CD[NEN[key]], CD[TREN[key]]
        n1, n2 = t["so_bac_moi_ve"]
        ch = (tren_t - nen_t) / (n1 + n2 + 2)
        nghi = t["chieu_nghi"]
        z = nen_t
        for so, (ve, n) in enumerate(((t["ve1"], n1), (t["ve2"], n2))):
            dai = (ve[2] - ve[0]) / n
            gan_nghi_ben_trai = abs(ve[0] - nghi[2]) < abs(ve[2] - nghi[0])
            # ve 1 di ve phia chieu nghi, ve 2 di ra xa chieu nghi
            ve_tien_ve_nghi = so == 0
            huong_am = gan_nghi_ben_trai == ve_tien_ve_nghi
            khac = t["ve2"] if so == 0 else t["ve1"]
            yv = (ve[3] - 60, ve[3] - 20) if ve[1] < khac[1] else (ve[1] + 20, ve[1] + 60)   # mep phia gieng thang
            z_dau = z + ch
            for b in range(1, n + 1):
                z += ch
                if huong_am:
                    xa, xb = ve[2] - b * dai, ve[2] - (b - 1) * dai
                else:
                    xa, xb = ve[0] + (b - 1) * dai, ve[0] + b * dai
                khoi(f"{key}_thang_{so}_{b}", xa, ve[1], xb, ve[3], z - ch - 150, z, "be_tong", f"{key} thang")
                xm = (xa + xb) / 2   # con tien
                khoi(f"{key}_con_tien_{so}_{b}", xm - 10, yv[0] + 10, xm + 10, yv[1] - 10, z, z + 900, "khung",
                     f"{key} thang", vat=False)
            # tay vin go nghieng theo ve
            xs, xe = (ve[2], ve[0]) if huong_am else (ve[0], ve[2])
            x_lo, x_hi = min(xs, xe), max(xs, xe)
            z_lo, z_hi = (z_dau, z) if x_lo == xs else (z, z_dau)
            hop_doc_x(f"{key}_tay_vin_{so}", x_lo, x_hi, yv[0], yv[1], z_lo + 900, z_hi + 900,
                      z_lo + 950, z_hi + 950, "go_toi", f"{key} thang")
            if so == 0:
                z += ch
                khoi(f"{key}_chieu_nghi", *nghi, z - 150, z, "be_tong", f"{key} thang")

# ------------------------------------------------------------------ mai
for key, mb in MB.items():
    for mm in mb["mai"]:
        m, r = MAI[mm["ma"]], mm["hcn"]
        if mm["ma"] == "M4":
            continue
        if m["dinh"] != m["mep"]:
            f = ham_mai(m, r)
            khoi(f"mai_{mm['ma']}", *r, 0, 0, "ton_do", "mai",
                 z_tren=(f(r[1]), f(r[3])))
            # mat duoi: dung khoi thu hai mong de co do day
            o = bpy.data.objects[f"mai_{mm['ma']}"]
            me = o.data
            for v in me.vertices[:4]:
                yy = v.co.y / K
                v.co.z = (f(yy) - MAI_DAY) * K
            # diem bien diem mep (mang xoi) mau xam
            khoi(f"mai_{mm['ma']}_mang", r[0], r[1] - 60, r[2], r[1], f(r[1]) - MAI_DAY - 60, f(r[1]) + 20,
                 "xam_nhat", "mai")
        else:
            khoi(f"mai_{mm['ma']}", *r, m["dinh"] - SAN_DAY, m["dinh"], "xam_nhat", "mai")
            cao = TS["Tường chắn mái tum cao"]
            z0 = m["dinh"]
            for i, rr in enumerate([(r[0], r[1], r[2], r[1] + 200), (r[0], r[3] - 200, r[2], r[3]),
                                    (r[0], r[1] + 200, r[0] + 200, r[3] - 200),
                                    (r[2] - 200, r[1] + 200, r[2], r[3] - 200)]):
                khoi(f"mai_{mm['ma']}_chan_{i}", *rr, z0, z0 + cao, "go_nau", "mai")

# ------------------------------------------------------------------ san vuon, rao, pergola, thiet bi ngoai nha
t1 = MB["T1"]
SAN = CD["SAN"]
khoi("co", -30000, -30000, 30000, 40000, SAN - 60, SAN - 20, "co", "san vuon", vat=False)
for i, r in enumerate(t1["san_vuon"]):
    khoi(f"san_vuon_{i}", *r, SAN - 50, SAN, "be_tong", "san vuon", vat=False)
for i, r in enumerate(t1["rao"]):
    khoi(f"rao_{i}", *r, SAN, SAN + TS["Tường rào cao"], "thep_nau_do", "san vuon")
for i, r in enumerate(t1["cong"]):
    cao = TS["Cổng cao"]
    khoi(f"cong_{i}_ray_duoi", *r, SAN + 50, SAN + 110, "den", "san vuon", vat=False)
    khoi(f"cong_{i}_ray_tren", *r, SAN + cao - 60, SAN + cao, "den", "san vuon", vat=False)
    n = max(2, int((r[2] - r[0]) / 120))
    for k in range(n + 1):
        x = r[0] + (r[2] - r[0]) * k / n
        khoi(f"cong_{i}_nan_{k}", x - 15, r[1], x + 15, r[3], SAN + 50, SAN + cao, "den", "san vuon", vat=False)
for i, r in enumerate(sorted(t1["bac"], key=lambda r: r[1])):
    khoi(f"bac_{i}", *r, SAN, SAN + TS["Bậc tam cấp cao"] * (i + 1), "xam_nhat", "san vuon")
m4 = next(mm for mm in t1["mai"] if mm["ma"] == "M4")
f4 = ham_mai(MAI["M4"], m4["hcn"])
r4 = m4["hcn"]
khoi("mai_M4", *r4, 0, 0, "polycarbonate", "pergola", z_tren=(f4(r4[1]), f4(r4[3])), vat=False)
o = bpy.data.objects["mai_M4"]
for v in o.data.vertices[:4]:
    v.co.z = (f4(v.co.y / K) - 15) * K
xa_cao = TS["Xà pergola cao"]
for i, (x1, y1, x2, y2) in enumerate(t1["pergola_xa"]):
    if abs(x1 - x2) < 1:   # xa chinh theo Y, doc theo mai
        ya, yb = min(y1, y2), max(y1, y2)
        za, zb = f4(ya) - 15, f4(yb) - 15
        o = khoi(f"pergola_xa_{i}", x1 - 50, ya, x1 + 50, yb, 0, 0, "thep_nau_do", "pergola", z_tren=(za, zb))
        for v in o.data.vertices[:4]:
            v.co.z = (f4(v.co.y / K) - 15 - xa_cao) * K
    else:                   # xa phu theo X
        z = f4(y1) - 15
        khoi(f"pergola_xa_{i}", min(x1, x2), y1 - 40, max(x1, x2), y1 + 40, z - 100, z, "thep_nau_do", "pergola")
for i, r in enumerate(t1["pergola_cot"]):
    cy = (r[1] + r[3]) / 2
    khoi(f"pergola_cot_{i}", *r, SAN, f4(cy) - 15 - xa_cao, "thep_nau_do", "pergola")
for i, r in enumerate(t1["may_lanh"]):
    cao = TS["Cục nóng máy lạnh cao"]
    khoi(f"cuc_nong_{i}", *r, SAN + 20, SAN + 20 + cao, "trang", "thiet bi")
    tru(f"cuc_nong_quat_{i}", (r[1] + r[3]) / 2 - 120, SAN + 20 + cao / 2, 190, r[0] - 8, r[0] + 2, "den",
        "thiet bi", truc="x")
for i, (x, y, r) in enumerate(t1["ong_xoi"]):
    # ong dung duoi mat duoi mai doc neu nam duoi mai
    z_tren = TS["Ống xối lên tới cao độ"]
    for ds in MAI_DOC.values():
        for hr, f in ds:
            if hr[0] <= x <= hr[2] and hr[1] <= y <= hr[3]:
                z_tren = min(z_tren, f(y) - MAI_DAY)
    tru(f"ong_xoi_{i}", x, y, r, SAN, z_tren, "ong_xoi", "thiet bi", doan=16)

mai_mb = MB["MAI"]
m3 = next(mm for mm in mai_mb["mai"] if mm["ma"] == "M3")
for i, (x, y, r) in enumerate(mai_mb["bon_nuoc"]):
    z0 = MAI["M3"]["dinh"]
    chan = TS["Chân bồn nước cao"]
    for k, (dx, dy) in enumerate(((-1, -1), (1, -1), (1, 1), (-1, 1))):
        cx, cy = x + dx * r * 0.6, y + dy * r * 0.6
        khoi(f"bon_chan_{i}_{k}", cx - 30, cy - 30, cx + 30, cy + 30, z0, z0 + chan, "inox", "MAI thiet bi", vat=False)
    tru(f"bon_nuoc_{i}", x, y, r, z0 + chan, z0 + chan + TS["Bồn nước cao"], "inox", "MAI thiet bi", doan=40)
lc = mai_mb["lan_can"]
xs_lc = [v for r in lc for v in (r[0], r[2])]
ys_lc = [v for r in lc for v in (r[1], r[3])]
for i, (x, y) in enumerate(mai_mb["kim_thu_set"]):
    r3 = m3["hcn"]
    if r3[0] <= x <= r3[2] and r3[1] <= y <= r3[3]:
        z0 = MAI["M3"]["dinh"] + TS["Tường chắn mái tum cao"]
    elif min(xs_lc) <= x <= max(xs_lc) and min(ys_lc) <= y <= max(ys_lc):
        z0 = CD["ST"] + LAN_CAN_CAO
    else:
        z0 = CD["ST"]
    tru(f"kim_thu_set_{i}", x, y, 12, z0, z0 + TS["Kim thu sét cao"], "den", "MAI thiet bi", doan=8)

# ------------------------------------------------------------------ noi that (doc tu layer NOI-THAT cua ban ve)
def cau(ten, x, y, z, r, mat, nhom_ten):
    bm = bmesh.new()
    bmesh.ops.create_icosphere(bm, subdivisions=2, radius=r * K)
    me = bpy.data.meshes.new(ten)
    bm.to_mesh(me)
    bm.free()
    o = bpy.data.objects.new(ten, me)
    nhom(nhom_ten).objects.link(o)
    o.data.materials.append(VL[mat])
    o.location = (x * K, y * K, z * K)
    for p in me.polygons:
        p.use_smooth = True
    return o


def sat_tuong(key, r, canh, nguong=60):
    """Canh 'canh' (T/P/D/S) cua hcn r co sat tuong hoac cot khong."""
    mb = MB[key]
    for w in mb["tuong"] + mb["cot"]:
        chong_y = w[1] < r[3] and w[3] > r[1]
        chong_x = w[0] < r[2] and w[2] > r[0]
        if canh == "T" and chong_y and 0 <= r[0] - w[2] <= nguong:
            return True
        if canh == "P" and chong_y and 0 <= w[0] - r[2] <= nguong:
            return True
        if canh == "D" and chong_x and 0 <= r[1] - w[3] <= nguong:
            return True
        if canh == "S" and chong_x and 0 <= w[1] - r[3] <= nguong:
            return True
    return False


def huong_ghe(r, ds):
    """Ghe quay mat ve ban gan nhat; tra ve mat lung."""
    cx, cy = (r[0] + r[2]) / 2, (r[1] + r[3]) / 2
    ban = [n["hcn"] for n in ds if n["ten"].startswith("BÀN")]
    if not ban:
        return "D"
    b = min(ban, key=lambda b: math.hypot((b[0] + b[2]) / 2 - cx, (b[1] + b[3]) / 2 - cy))
    dx, dy = (b[0] + b[2]) / 2 - cx, (b[1] + b[3]) / 2 - cy
    if abs(dx) > abs(dy):
        return "T" if dx > 0 else "P"
    return "D" if dy > 0 else "S"


def khung(r, lung):
    """Doi toa do cuc bo (d: tu mat lung ra truoc, w: doc theo be rong) sang toa do mat bang."""
    x1, y1, x2, y2 = r
    if lung == "T":
        return x2 - x1, y2 - y1, (lambda d, w: (x1 + d, y1 + w)), "x"
    if lung == "P":
        return x2 - x1, y2 - y1, (lambda d, w: (x2 - d, y1 + w)), "x"
    if lung == "S":
        return y2 - y1, x2 - x1, (lambda d, w: (x1 + w, y2 - d)), "y"
    return y2 - y1, x2 - x1, (lambda d, w: (x1 + w, y1 + d)), "y"


def mot_mon(key, idx, n, ds):
    ten, r = n["ten"], n["hcn"]
    ngoai_nha = key == "T1" and (r[3] <= 0 or r[2] <= 0)
    nen = CD["SAN"] if ngoai_nha else CD[NEN[key]] + (10 if key != "T1" else 10)
    g = "san vuon noi that" if ngoai_nha else f"{key} noi that"
    lung = n["lung"]
    if ten == "GHẾ":
        lung = huong_ghe(r, ds)
    if ten == "Ô TÔ":
        lung = "S"
    D, W, f, truc = khung(r, lung)
    goc = f"{key}_{idx}_{ten.replace(' ', '_')}"

    def hop(phan, d0, d1, w0, w1, z0, z1, mat, vat=True):
        a, b = f(d0, w0), f(d1, w1)
        khoi(f"{goc}_{phan}", min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1]),
             nen + z0, nen + z1, mat, g, vat=vat)

    def tru_dung(phan, d, w, rr, z0, z1, mat, doan=24):
        x, y = f(d, w)
        tru(f"{goc}_{phan}", x, y, rr, nen + z0, nen + z1, mat, g, doan=doan)

    if ten == "SOFA":
        hop("chan", 30, D - 30, 30, W - 30, 0, 80, "go_toi")
        hop("de", 0, D, 0, W, 80, 400, "vai")
        hop("tua", 0, 220, 0, W, 400, 820, "vai")
        hop("tay_t", 0, D, 0, 160, 400, 620, "vai")
        hop("tay_p", 0, D, W - 160, W, 400, 620, "vai")
        for i in range(3):
            w0 = 160 + i * (W - 320) / 3 + 8
            w1 = 160 + (i + 1) * (W - 320) / 3 - 8
            hop(f"dem_{i}", 220, D - 20, w0, w1, 400, 520, "vai")
            hop(f"goi_tua_{i}", 220, 360, w0, w1, 520, 780, "vai")
        hop("goi_1", 240, 360, 190, 560, 520, 800, "vai_kem")
        hop("goi_2", 240, 360, W - 560, W - 190, 520, 800, "vai_kem")
    elif ten == "BÀN TRÀ":
        hop("than", 60, D - 60, 60, W - 60, 0, 360, "go_toi")
        hop("mat", 0, D, 0, W, 360, 410, "go_sang")
        tru_dung("lo_hoa", D / 2, W / 2, 60, 410, 620, "su_trang")
        x, y = f(D / 2, W / 2)
        cau(f"{goc}_hoa", x, y, nen + 680, 90, "la_cay", g)
    elif ten == "KỆ TV":
        hop("op_tuong", 0, 20, 0, W, 450, 2500, "go_toi", vat=False)
        hop("ke", 0, D, 0, W, 0, 450, "go_sang")
        tvw = min(W * 0.75, 1500)
        w0 = (W - tvw) / 2
        hop("tv", 30, 70, w0, w0 + tvw, 850, 850 + tvw * 0.56, "den")
        hop("man_hinh", 70, 74, w0 + 15, w0 + tvw - 15, 865, 850 + tvw * 0.56 - 15, "kinh_toi", vat=False)
        hop("loa", 120, D - 60, W / 2 - 300, W / 2 + 300, 450, 520, "den")
    elif ten == "THẢM":
        hop("tham", 0, D, 0, W, 0, 12, "tham", vat=False)
    elif ten in ("BÀN ĂN",):
        hop("mat", 0, D, 0, W, 720, 760, "go_sang")
        for i, (dd, ww) in enumerate(((60, 60), (60, W - 60), (D - 60, 60), (D - 60, W - 60))):
            hop(f"chan_{i}", dd - 30, dd + 30, ww - 30, ww + 30, 0, 720, "go_toi")
        tru_dung("binh", D / 2, W / 2, 70, 760, 950, "su_trang")
        x, y = f(D / 2, W / 2)
        cau(f"{goc}_hoa", x, y, nen + 1010, 110, "la_cay", g)
    elif ten == "GHẾ":
        hop("ngoi", 0, D, 0, W, 420, 460, "go_sang")
        for i, (dd, ww) in enumerate(((25, 25), (25, W - 25), (D - 25, 25), (D - 25, W - 25))):
            hop(f"chan_{i}", dd - 18, dd + 18, ww - 18, ww + 18, 0, 420, "go_toi", vat=False)
        hop("tua", 0, 40, 0, W, 460, 900, "go_sang")
    elif ten == "TỦ BẾP DƯỚI":
        hop("chan", 60, D, 0, W, 0, 100, "go_toi")
        hop("than", 0, D, 0, W, 100, 820, "su_trang")
        hop("mat_da", 0, D + 20, 0, W, 820, 860, "da_bep")
        hop("chau_rua", 120, D - 150, W / 2 - 380, W / 2 + 380, 848, 862, "inox", vat=False)
        hop("voi", 40, 80, W / 2 - 15, W / 2 + 15, 860, 1150, "inox", vat=False)
        hop("bep", 100, D - 120, W * 0.72, W * 0.72 + 600, 860, 872, "den")
        w = 600
        while w < W:
            hop(f"khe_{w}", D - 2, D + 2, w - 3, w + 3, 120, 800, "den", vat=False)
            w += 600
    elif ten == "TỦ BẾP TRÊN":
        hop("than", 0, D, 0, W, 1500, 2200, "go_sang")
        w = 500
        while w < W:
            hop(f"khe_{w}", D - 2, D + 2, w - 3, w + 3, 1520, 2180, "den", vat=False)
            w += 500
    elif ten == "TỦ LẠNH":
        hop("than", 0, D, 0, W, 0, 1800, "inox")
        hop("khe", D - 2, D + 2, 0, W, 1150, 1160, "den", vat=False)
        hop("tay_nam", D, D + 30, W - 90, W - 60, 1250, 1600, "den", vat=False)
    elif ten == "LAVABO":
        hop("tu", 0, D, 0, W, 150, 800, "go_sang")
        hop("chau", 0, D, 0, W, 800, 880, "su_trang")
        hop("voi", 40, 90, W / 2 - 15, W / 2 + 15, 880, 1050, "inox", vat=False)
        hop("guong", 0, 15, W * 0.1, W * 0.9, 1150, 1800, "kinh", vat=False)
    elif ten == "BỒN CẦU":
        hop("ket", 0, 170, 0, W, 0, 800, "su_trang")
        hop("bet", 120, D - 20, 40, W - 40, 0, 400, "su_trang")
        hop("nap", 120, D - 10, 30, W - 30, 400, 440, "su_trang")
    elif ten == "SEN TẮM":
        hop("khay", 0, D, 0, W, 0, 40, "su_trang")
        hop("ong", 0, 30, W / 2 - 12, W / 2 + 12, 900, 2000, "inox", vat=False)
        hop("voi_sen", 20, 220, W / 2 - 60, W / 2 + 60, 1950, 1990, "inox", vat=False)
        x1, y1, x2, y2 = r
        for canh, (a, b, c, d) in (("T", (x1, y1, x1 + 10, y2)), ("P", (x2 - 10, y1, x2, y2)),
                                   ("D", (x1, y1, x2, y1 + 10)), ("S", (x1, y2 - 10, x2, y2))):
            if not sat_tuong(key, r, canh):
                khoi(f"{goc}_kinh_{canh}", a, b, c, d, nen + 40, nen + 2000, "kinh_sen", g, vat=False)
    elif ten in ("GIƯỜNG ĐÔI", "GIƯỜNG ĐƠN"):
        hop("khung", 0, D, 0, W, 0, 300, "go_toi")
        hop("nem", 80, D - 30, 30, W - 30, 300, 520, "trang")
        hop("chan", D * 0.42, D - 15, 15, W - 15, 300, 545, "chan")
        hop("dau_giuong", 0, 80, 0, W, 0, 1050, "go_toi")
        so_goi = 2 if ten == "GIƯỜNG ĐÔI" else 1
        for i in range(so_goi):
            w0 = 100 + i * (W - 200) / so_goi + 20
            w1 = 100 + (i + 1) * (W - 200) / so_goi - 20
            hop(f"goi_{i}", 130, 500, w0, w1, 520, 640, "vai_kem")
    elif ten == "TAB":
        hop("than", 0, D, 0, W, 0, 500, "go_sang")
        tru_dung("den_chan", D / 2, W / 2, 50, 500, 800, "dong")
        tru_dung("den_chao", D / 2, W / 2, 150, 800, 1000, "vai_kem")
    elif ten == "TỦ ÁO":
        hop("than", 0, D, 0, W, 0, 2200, "go_sang")
        w = 500
        while w < W - 100:
            hop(f"khe_{w}", D - 2, D + 2, w - 3, w + 3, 50, 2150, "den", vat=False)
            hop(f"nam_{w}", D, D + 20, w - 60, w - 40, 950, 1250, "den", vat=False)
            w += 500
    elif ten == "BÀN TRANG ĐIỂM":
        hop("hoc", 0, D, 0, W, 550, 720, "go_sang")
        hop("mat", 0, D, 0, W, 720, 750, "go_sang")
        for i, ww in enumerate((20, W - 60)):
            hop(f"chan_{i}", D - 60, D - 20, ww, ww + 40, 0, 550, "go_toi", vat=False)
            hop(f"chan_s_{i}", 20, 60, ww, ww + 40, 0, 550, "go_toi", vat=False)
        hop("guong", 0, 15, W * 0.2, W * 0.8, 900, 1600, "kinh", vat=False)
    elif ten in ("BÀN LÀM VIỆC", "BÀN HỌC"):
        hop("mat", 0, D, 0, W, 720, 750, "go_sang")
        hop("hong_t", 0, D, 0, 40, 0, 720, "go_toi")
        hop("hong_p", 0, D, W - 40, W, 0, 720, "go_toi")
        hop("man_hinh", 60, 90, W / 2 - 280, W / 2 + 280, 900, 1230, "den")
        hop("chan_man", 70, 90, W / 2 - 30, W / 2 + 30, 750, 900, "den", vat=False)
        hop("ban_phim", 250, 400, W / 2 - 220, W / 2 + 220, 750, 765, "den", vat=False)
    elif ten == "KỆ SÁCH":
        hop("hong_t", 0, D, 0, 30, 0, 1800, "go_toi")
        hop("hong_p", 0, D, W - 30, W, 0, 1800, "go_toi")
        hop("lung", 0, 15, 0, W, 0, 1800, "go_toi", vat=False)
        mau = ["sach_1", "sach_2", "sach_3", "sach_2", "sach_1"]
        rong = [40, 30, 55, 35, 45, 28, 50]
        cao = [250, 220, 280, 240, 260]
        for k in range(6):
            z = k * 355
            hop(f"tang_{k}", 0, D, 0, W, z, z + 25, "go_sang")
            if k == 5:
                break
            w, j = 40, 0
            while w < W - 90:
                bw = rong[(j + k) % len(rong)]
                if (j + k) % 9 != 8:
                    hop(f"sach_{k}_{j}", 25, D - 25, w, w + bw - 4, z + 25, z + 25 + cao[(j + 2 * k) % len(cao)],
                        mau[(j + k) % len(mau)], vat=False)
                w += bw
                j += 1
    elif ten == "BÀN THỜ":
        hop("than", 0, D, 0, W, 0, 900, "go_tho")
        hop("mat", 0, D + 30, -20, W + 20, 900, 940, "go_tho")
        hop("tang_tren", 0, D * 0.45, W * 0.1, W * 0.9, 940, 1150, "go_tho")
        tru_dung("bat_huong", D * 0.7, W / 2, 75, 940, 1050, "dong")
        tru_dung("lo_1", D * 0.6, W * 0.2, 50, 940, 1220, "su_trang")
        tru_dung("lo_2", D * 0.6, W * 0.8, 50, 940, 1220, "su_trang")
        hop("khung_anh", 0, 15, W * 0.3, W * 0.7, 1300, 1750, "go_toi", vat=False)
        hop("anh", 15, 18, W * 0.33, W * 0.67, 1330, 1720, "vai_kem", vat=False)
    elif ten == "MÁY GIẶT":
        hop("than", 0, D, 0, W, 0, 850, "trang")
        hop("bang_dk", D - 2, D + 3, 30, W - 30, 760, 830, "den", vat=False)
        x, y = f(D, W / 2)
        a0, a1 = (x - 25, x + 25) if truc == "x" else (y - 25, y + 25)
        if truc == "x":
            tru(f"{goc}_cua", y, nen + 450, 190, a0, a1, "kinh_toi", g, truc="x")
        else:
            tru(f"{goc}_cua", x, nen + 450, 190, a0, a1, "kinh_toi", g, truc="y")
    elif ten == "GIÀN PHƠI":
        for i, ww in enumerate((20, W - 60)):
            hop(f"cot_{i}", D / 2 - 20, D / 2 + 20, ww, ww + 40, 0, 1600, "inox", vat=False)
            hop(f"de_{i}", 0, D, ww, ww + 40, 0, 30, "inox", vat=False)
        for i, dd in enumerate((D * 0.2, D * 0.5, D * 0.8)):
            hop(f"thanh_{i}", dd - 10, dd + 10, 0, W, 1580, 1600, "inox", vat=False)
        mau = ["sach_2", "vai_kem", "chan", "sach_1", "trang"]
        for i in range(5):
            w0 = 120 + i * (W - 240) / 5
            dd = (D * 0.2, D * 0.5, D * 0.8)[i % 3]
            hop(f"ao_{i}", dd - 4, dd + 4, w0, w0 + 260, 950 + 80 * (i % 2), 1580, mau[i], vat=False)
    elif ten == "BÀN NHỎ":
        hop("de", D / 2 - 180, D / 2 + 180, W / 2 - 180, W / 2 + 180, 0, 20, "go_toi")
        hop("than", D / 2 - 40, D / 2 + 40, W / 2 - 40, W / 2 + 40, 0, 430, "go_toi")
        hop("mat", 0, D, 0, W, 430, 460, "go_sang")
    elif ten == "CHẬU CÂY":
        rr = min(D, W) / 2 * 0.85
        tru_dung("chau", D / 2, W / 2, rr, 0, 450, "dat_nung")
        x, y = f(D / 2, W / 2)
        cau(f"{goc}_tan_1", x, y, nen + 450 + rr * 1.5, rr * 1.5, "la_cay", g)
        cau(f"{goc}_tan_2", x + rr * 0.6, y - rr * 0.4, nen + 450 + rr * 2.6, rr * 1.0, "la_cay", g)
    elif ten == "Ô TÔ":
        hop("than", 0, D, 0, W, 250, 800, "son_xe")
        hop("cabin", D * 0.25, D * 0.78, 110, W - 110, 800, 1330, "kinh_toi")
        hop("noc", D * 0.28, D * 0.74, 140, W - 140, 1330, 1390, "son_xe")
        hop("den_1", D - 20, D + 5, 120, 420, 600, 700, "trang", vat=False)
        hop("den_2", D - 20, D + 5, W - 420, W - 120, 600, 700, "trang", vat=False)
        x1, y1, x2, y2 = r
        for i, dd in enumerate((D * 0.18, D * 0.82)):
            _, yy = f(dd, 0)
            tru(f"{goc}_banh_t_{i}", yy, nen + 300, 300, x1 - 10, x1 + 190, "lop_xe", g, truc="x")
            tru(f"{goc}_banh_p_{i}", yy, nen + 300, 300, x2 - 190, x2 + 10, "lop_xe", g, truc="x")
    else:
        print("Chua co mau 3D cho:", ten)
        hop("khoi", 0, D, 0, W, 0, 800, "go_sang")
        return
    # do cao hon mat cat 1.4 m: them mat cat dac de anh mat bang khong bi rong ruot
    mau_cat = {"TỦ ÁO": "go_sang", "TỦ LẠNH": "inox", "KỆ SÁCH": "go_toi"}
    if ten in mau_cat and key != "MAI":
        x1, y1, x2, y2 = r
        khoi(f"{goc}_cat", x1, y1, x2, y2, nen + CAT - 25, nen + CAT - 5, mau_cat[ten], f"{key} cat mat bang",
             vat=False)
    NOI_THAT_DEM[ten] = NOI_THAT_DEM.get(ten, 0) + 1


def dung_noi_that():
    for key, mb in MB.items():
        ds = mb.get("noi_that", [])
        for i, n in enumerate(ds):
            mot_mon(key, i, n, ds)


# ------------------------------------------------------------------ anh sang, camera, render
mt = bpy.data.worlds.new("Troi")
scene.world = mt
mt.use_nodes = True
bg = next(n for n in mt.node_tree.nodes if n.type == "BACKGROUND")
NOI_THAT_DEM = {}
dung_noi_that()
bg.inputs["Color"].default_value = (0.32, 0.52, 0.95, 1)
bg.inputs["Strength"].default_value = 0.8

sun_d = bpy.data.lights.new("Mat troi", "SUN")
sun_d.energy = 5.0
sun_d.angle = math.radians(2)
sun = bpy.data.objects.new("Mat troi", sun_d)
scene.collection.objects.link(sun)
sun.rotation_euler = (math.radians(48), 0, math.radians(-38))

TAM = (2.5, 6.0)


def camera(ten, vt, nhin, tieu_cu=30):
    cd = bpy.data.cameras.new(ten)
    cd.lens = tieu_cu
    cd.clip_end = 500
    o = bpy.data.objects.new(ten, cd)
    scene.collection.objects.link(o)
    o.location = vt
    huong = (nhin[0] - vt[0], nhin[1] - vt[1], nhin[2] - vt[2])
    import mathutils
    o.rotation_euler = mathutils.Vector(huong).to_track_quat("-Z", "Y").to_euler()
    return o


CAM = [
    camera("Cam goc hong", (-16.5, -4.5, 6.5), (2.5, 6.5, 5.6), 24),
    camera("Cam tren cao", (-17.0, -9.0, 19.0), (2.5, 5.5, 4.0), 28),
    camera("Cam mat tien", (-7.5, -17.0, 4.5), (2.5, 3.0, 5.5), 26),
]

r = scene.render
for eng in ("BLENDER_EEVEE", "BLENDER_EEVEE_NEXT"):
    try:
        r.engine = eng
        break
    except TypeError:
        pass
r.resolution_x, r.resolution_y = 1600, 1000
r.film_transparent = False
try:
    scene.eevee.taa_render_samples = 64
    scene.eevee.use_raytracing = True
except AttributeError:
    pass
scene.view_settings.view_transform = "AgX"
try:
    scene.view_settings.look = "AgX - Medium High Contrast"
except TypeError:
    pass

# ------------------------------------------------------------------ tach tang
# Moi tang gan vao mot Empty "TANG ..."; Empty "DIEU KHIEN TACH TANG" co thuoc tinh tach_m (met).
# Keo tach_m (bang N > Item > Custom Properties) la cac tang bung len theo truc Z.
dk = bpy.data.objects.new("DIEU KHIEN TACH TANG", None)
scene.collection.objects.link(dk)
dk.empty_display_type = "ARROWS"
dk.empty_display_size = 1.5
dk.location = (-3.0, -6.0, 0)
dk["tach_m"] = 0.0
dk.id_properties_ui("tach_m").update(min=0.0, max=10.0, soft_min=0.0, soft_max=8.0, step=10,
                                     description="Khoang tach giua cac tang, met")
TANG_EMPTY = {}
for k, ten_tang in enumerate(THU_TU_TANG):
    c = NHOM.get(ten_tang)
    if not c:
        continue
    e = bpy.data.objects.new(f"TANG {ten_tang}", None)
    c.objects.link(e)
    e.empty_display_size = 0.5
    TANG_EMPTY[ten_tang] = e
    for o in c.all_objects:
        if o is not e and o.parent is None:
            o.parent = e
    he_so = max(0, k - 1)   # san vuon va tang 1 dung yen
    if he_so:
        fc = e.driver_add("location", 2)
        dv = fc.driver
        dv.type = "SCRIPTED"
        v = dv.variables.new()
        v.name = "tach"
        v.type = "SINGLE_PROP"
        v.targets[0].id = dk
        v.targets[0].data_path = '["tach_m"]'
        dv.expression = f"tach * {he_so}"

RA.mkdir(parents=True, exist_ok=True)


def chup(cam, ten):
    scene.camera = cam
    if not CO_RENDER:   # chay qua MCP: bo qua render cho nhanh, van tao camera
        return
    r.filepath = str(RA / ten)
    bpy.ops.render.render(write_still=True)
    print("Da render", ten)


for cam, ten in zip(CAM, TEN_ANH):
    chup(cam, ten)

# anh tung tang: camera nhin thang xuong, cat ngang o cao do san + 1.4 m (clip_start) nhu mat bang 3D
ong_xoi = [o for o in bpy.data.objects if o.name.startswith("ong_xoi")]
TANG_ANH = [("Tang 1", 0, "09_tang-1-noi-that.png", 21.0), ("Tang 2", CD["T2"], "10_tang-2-noi-that.png", 16.5),
            ("Tang 3", CD["T3"], "11_tang-3-noi-that.png", 16.5)]
for o in ong_xoi:
    o.hide_render = True
mai_pergola = [o for o in bpy.data.objects if o.name.startswith(("mai_M4", "pergola_xa"))]
# den chieu thang xuong cho anh mat bang (tat khi render phoi canh)
sd = bpy.data.lights.new("Den mat bang", "SUN")
sd.energy = 2.5
sd.angle = math.radians(15)
den_mb = bpy.data.objects.new("Den mat bang", sd)
scene.collection.objects.link(den_mb)
for i, (ten_tang, lv, ten_anh, khung_m) in enumerate(TANG_ANH):
    # an han cac tang phia tren (neu chi cat bang clip thi chung van do bong xuong)
    tren = THU_TU_TANG[THU_TU_TANG.index(ten_tang) + 1:]
    for t in THU_TU_TANG:
        if t in NHOM:
            NHOM[t].hide_render = t in tren
    for o in mai_pergola:
        o.hide_render = ten_tang == "Tang 1"
    for kk in ("T1", "T2", "T3"):
        NHOM[f"{kk} cat mat bang"].hide_render = TANG[kk] != ten_tang
    H = 30.0
    cd_ = bpy.data.cameras.new(f"Cam mat bang {ten_tang}")
    cd_.type = "ORTHO"
    cd_.ortho_scale = khung_m
    cd_.clip_start = H - CAT * K
    cd_.clip_end = H + 5
    cam = bpy.data.objects.new(cd_.name, cd_)
    scene.collection.objects.link(cam)
    tam_y = 5.0 if ten_tang == "Tang 1" else 7.0
    cam.location = (2.5, tam_y, lv * K + H)
    cam.rotation_euler = (0, 0, math.pi / 2)   # mat tien ben trai anh
    chup(cam, ten_anh)
for t in THU_TU_TANG:
    if t in NHOM:
        NHOM[t].hide_render = False
for o in mai_pergola:
    o.hide_render = False
for kk in ("T1", "T2", "T3"):
    NHOM[f"{kk} cat mat bang"].hide_render = True
den_mb.hide_render = True
den_mb.hide_viewport = True

# tum, san thuong: goc 3/4, an mai tum de thay ben trong
an_tum = [o for o in bpy.data.objects if o.name.startswith(("mai_M3", "bon_"))]
for o in an_tum:
    o.hide_render = True
cam = camera("Cam tum san thuong", (-5.0, 19.5, CD["ST"] * K + 9.5), (2.5, 11.0, CD["ST"] * K), 26)
chup(cam, "12_tum-san-thuong.png")
for o in an_tum:
    o.hide_render = False

# anh bung tang (khung doc)
dk["tach_m"] = 3.0
bpy.context.view_layer.update()
r.resolution_x, r.resolution_y = 1200, 1500
cam_bung = camera("Cam bung tang", (-25.0, -21.0, 21.0), (2.5, 6.5, 11.0), 30)
chup(cam_bung, "13_bung-tang.png")
r.resolution_x, r.resolution_y = 1600, 1000
dk["tach_m"] = 0.0
bpy.context.view_layer.update()
for o in ong_xoi:
    o.hide_render = False

scene.camera = CAM[0]
print("Noi that:", NOI_THAT_DEM, "| tong", sum(NOI_THAT_DEM.values()))
if "--" in sys.argv:   # chi khi chay nen: khong de lai file .blend1 (khong dong vao cai dat cua Blender dang mo)
    bpy.context.preferences.filepaths.save_version = 0
bpy.ops.wm.save_as_mainfile(filepath=str(RA / TEN_BLEND))
print("Dem:", dem, "| doi tuong:", len(bpy.data.objects))
