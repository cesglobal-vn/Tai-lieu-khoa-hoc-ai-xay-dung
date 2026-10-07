# Tach tung tang ra mat dat canh toa nha goc (toa nha goc giu nguyen) roi render nhin tu tren xuong.
# Chay trong Blender dang mo file 04_nha-pho-lo-7x20m.blend (sau dung-nha-blender.py):
#   exec(open(r"...\scripts\tach-tang-mat-bang.py", encoding="utf-8").read())
# Ban sao dung chung mesh voi ban goc (linked duplicate): sua vat lieu ban goc thi ban tach cung doi.
import bpy, math, mathutils
from bpy_extras.object_utils import world_to_camera_view
from pathlib import Path

RA = Path(globals().get("RA_THU") or Path(bpy.data.filepath).parent / "15-render-tach-tang")
CO_RENDER = globals().get("CO_RENDER", True)
CHI_ANH = globals().get("CHI_ANH")        # vd {"01", "05"}: chi render cac anh co so nay (de thu nhanh)
NEN_Z = -0.455            # mat tren nen trung bay: tren mat co (-0.47), duoi mat san vuon (-0.45)
KHOANG = 10.0             # buoc dat cac tang theo truc X
X0 = 12.0                 # tang 1 dat tu x = 12 m (toa nha goc o x = 0..5)

# (ten hien thi, collection goc, collection con bo qua, ten doi tuong bo qua (tien to), them tu San vuon?)
BO_CAT = ("cat mat bang",)
TANG = [
    ("TANG 1 + SAN VUON", "Tang 1", "tang-1-san-vuon"),
    ("TANG 2", "Tang 2", "tang-2"),
    ("TANG 3", "Tang 3", "tang-3"),
    ("TUM + SAN THUONG", "Mai - Tum", "tum-san-thuong"),
]
NHAN = {"Tang 1": "TẦNG 1 + SÂN VƯỜN", "Tang 2": "TẦNG 2", "Tang 3": "TẦNG 3", "Mai - Tum": "TUM + SÂN THƯỢNG"}
# mai doc M1 (tren tang 3), M2 (mai ban cong tang 2), mai tum M3 va do tren mai tum: bo de nhin thay ben trong
BO_TEN = ("mai_M1", "mai_M2", "mai_M3", "bon_", "kim_thu_set_0", "kim_thu_set_1", "kim_thu_set_2",
          "kim_thu_set_3", "ong_xoi", "pergola", "mai_M4")
BO_TEN_DUNG = {"co"}      # mat co cua khu dat

scene = bpy.context.scene


def lay_doi_tuong(ten_col):
    ds = []
    for col in bpy.data.collections[ten_col].children_recursive:
        if col.name.endswith(BO_CAT):
            continue
        ds += [o for o in col.objects if o.type == "MESH" and not o.name.startswith(BO_TEN) and o.name not in BO_TEN_DUNG]
    return ds


def hop_bao(objs):
    mn = mathutils.Vector((1e9,) * 3); mx = mathutils.Vector((-1e9,) * 3)
    for o in objs:
        for c in o.bound_box:
            w = o.matrix_world @ mathutils.Vector(c)
            mn = mathutils.Vector(map(min, mn, w)); mx = mathutils.Vector(map(max, mx, w))
    return mn, mx


def vat_lieu_nen():
    m = bpy.data.materials.get("Nen trung bay") or bpy.data.materials.new("Nen trung bay")
    m.use_nodes = True
    bsdf = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (0.5, 0.5, 0.49, 1)
    bsdf.inputs["Roughness"].default_value = 0.9
    return m


def vat_lieu_chu():
    m = bpy.data.materials.get("Chu nhan tang") or bpy.data.materials.new("Chu nhan tang")
    m.use_nodes = True
    bsdf = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = (0.05, 0.05, 0.06, 1)
    bsdf.inputs["Roughness"].default_value = 0.6
    return m


# ---- don ban cu (neu chay lai): chi xoa doi tuong do chinh script nay tao, nam trong collection rieng
GOC = bpy.data.collections.get("Tach tang mat bang")
if GOC:
    for o in list(GOC.all_objects):
        bpy.data.objects.remove(o, do_unlink=True)
    for c in list(GOC.children_recursive):
        bpy.data.collections.remove(c)
    for kho in (bpy.data.curves, bpy.data.meshes, bpy.data.lights):   # du lieu rieng cua nhan, nen, den; khong con ai dung
        for d in [d for d in kho if d.users == 0 and d.name.startswith(("Nhan ", "TT_"))]:
            kho.remove(d)
else:
    GOC = bpy.data.collections.new("Tach tang mat bang")
    scene.collection.children.link(GOC)

font = None
for duong_dan in (r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf"):
    if Path(duong_dan).exists():
        font = bpy.data.fonts.load(duong_dan, check_existing=True)
        break

KHOI = {}   # ten collection goc -> (collection moi, hop bao min, max)
for i, (_, ten_col, _) in enumerate(TANG):
    objs = lay_doi_tuong(ten_col)
    if ten_col == "Tang 1":
        objs += lay_doi_tuong("San vuon")
    # ha tang xuong: day san (diem thap nhat cua collection san) dat len nen trung bay
    san = [o for o in objs if o.users_collection[0].name.endswith(" san")]
    z_day = hop_bao(san)[0].z if ten_col != "Tang 1" else 0.0
    dz = 0.0 if ten_col == "Tang 1" else (NEN_Z - z_day)
    dx = X0 + i * KHOANG
    col = bpy.data.collections.new(f"Tach {ten_col}")
    GOC.children.link(col)
    T = mathutils.Matrix.Translation((dx, 0.0, dz))
    moi = []
    for o in objs:
        b = o.copy()                       # dung chung mesh
        b.parent = None
        b.animation_data_clear()
        b.matrix_world = T @ o.matrix_world
        b.name = "TT_" + o.name
        b.hide_render = o.hide_render
        col.objects.link(b)
        moi.append(b)
    mn, mx = hop_bao(moi)
    KHOI[ten_col] = (col, mn, mx)
    # nhan ten tang nam tren nen, phia truoc (y nho) cua tang
    cu = bpy.data.curves.new(f"Nhan {ten_col}", "FONT")
    cu.body = NHAN[ten_col]
    if font:
        cu.font = font
    cu.size = 0.9
    cu.align_x = "CENTER"
    cu.extrude = 0.01
    t = bpy.data.objects.new(f"TT_nhan_{ten_col}", cu)
    t.data.materials.append(vat_lieu_chu())
    t.location = ((mn.x + mx.x) / 2, mn.y - 1.6, NEN_Z + 0.005)
    col.objects.link(t)
    print(ten_col, "->", len(moi), "doi tuong, dx", dx, "dz", round(dz, 3), "hop", [round(v, 2) for v in mn], [round(v, 2) for v in mx])

# nen trung bay chung cho cac tang tach
# phu tu mep lo dat goc ra rat xa sau day tang tach de anh goc 3/4 khong lo mep nen
x_min = 5.2               # sat mep phai lo dat goc (x = 5), anh tren xuong tang 1 khong lo nen troi
x_max = max(k[2].x for k in KHOI.values()) + 60
y_min, y_max = -80.0, 100.0
me = bpy.data.meshes.new("TT_nen_trung_bay")
me.from_pydata([(x_min, y_min, NEN_Z), (x_max, y_min, NEN_Z), (x_max, y_max, NEN_Z), (x_min, y_max, NEN_Z)], [], [(0, 1, 2, 3)])
nen = bpy.data.objects.new("TT_nen_trung_bay", me)
nen.data.materials.append(vat_lieu_nen())
GOC.objects.link(nen)
bpy.context.view_layer.update()   # cap nhat matrix_world cua nhan chu vua dat location (de tinh khung camera)


def dat_nen(x_trai):
    """Keo mep trai nen: luc render rieng tung tang (toa nha goc an) thi keo rong de khong lo troi."""
    for i in (0, 3):
        me.vertices[i].co.x = x_trai
    me.update()

# ---- camera + render
r = scene.render
cam_cu, res_cu = scene.camera, (r.resolution_x, r.resolution_y)


def camera(ten, vi_tri, nhin_toi, ortho=None, lens=32):
    cd = bpy.data.cameras.get(ten) or bpy.data.cameras.new(ten)
    cam = bpy.data.objects.get(ten) or bpy.data.objects.new(ten, cd)
    if cam.name not in GOC.objects:
        GOC.objects.link(cam)
    cam.location = vi_tri
    if ortho:
        cd.type = "ORTHO"; cd.ortho_scale = ortho
        cam.rotation_euler = (0, 0, 0)   # anh dung: mat tien o duoi anh
    else:
        cd.type = "PERSP"; cd.lens = lens
        huong = mathutils.Vector(nhin_toi) - mathutils.Vector(vi_tri)
        cam.rotation_euler = huong.to_track_quat("-Z", "Y").to_euler()
    cd.clip_start, cd.clip_end = 0.1, 500
    return cam


def chi_hien(giu):
    """Tat render moi collection cap 1 tru cac tang tach trong 'giu'; tra lai trang thai cu."""
    cu = {c.name: c.hide_render for c in bpy.data.collections}
    for c in scene.collection.children:
        c.hide_render = c is not GOC
    for ten_col, (col, _, _) in KHOI.items():
        col.hide_render = ten_col not in giu
    return cu


def tra_lai(cu):
    for c in bpy.data.collections:
        if c.name in cu:
            c.hide_render = cu[c.name]


def chup(cam, ten):
    scene.camera = cam
    if not CO_RENDER or (CHI_ANH and ten[:2] not in CHI_ANH):
        return
    r.filepath = str(RA / ten)
    bpy.ops.render.render(write_still=True)
    print("Da render", ten)



RA.mkdir(parents=True, exist_ok=True)
nen.hide_render = False
rt_cu = scene.eevee.use_raytracing
scene.eevee.use_raytracing = True              # bong tiep xuc o chan tuong, goc phong ro hon
# anh tung tang: mat troi rieng gan thang dung + troi trung tinh (troi xanh lam bong bi am mau lam)
mat_troi = bpy.data.objects.get("Mat troi")
sd = bpy.data.lights.get("TT_mat_troi_rieng") or bpy.data.lights.new("TT_mat_troi_rieng", "SUN")
sd.energy, sd.angle = 4.5, math.radians(8)
den_rieng = bpy.data.objects.new("TT_mat_troi_rieng", sd)
GOC.objects.link(den_rieng)
nen_troi = next((n for n in scene.world.node_tree.nodes if n.type == "BACKGROUND"), None) if scene.world else None
troi_cu = (tuple(nen_troi.inputs["Color"].default_value), nen_troi.inputs["Strength"].default_value) if nen_troi else None


def anh_sang_rieng(bat):
    den_rieng.hide_render = not bat
    if mat_troi:
        mat_troi.hide_render = bat
    if nen_troi:
        if bat:
            nen_troi.inputs["Color"].default_value = (0.85, 0.87, 0.9, 1)
            nen_troi.inputs["Strength"].default_value = 0.7
        else:
            nen_troi.inputs["Color"].default_value, nen_troi.inputs["Strength"].default_value = troi_cu


def vua_khung(cam, dich, huong, diem, le=0.05):
    """Lui camera theo huong co dinh toi khi hinh vua khung (cach mep 'le'), roi dich khung (shift) cho can giua."""
    cam.data.shift_x = cam.data.shift_y = 0.0
    ty_le = r.resolution_y / r.resolution_x
    D = 4.0
    for _ in range(150):
        cam.location = dich + huong * D
        bpy.context.view_layer.update()
        ps = [world_to_camera_view(scene, cam, v) for v in diem]
        xs, ys = [p.x for p in ps], [p.y for p in ps]
        if all(p.z > 0 for p in ps) and max(xs) - min(xs) <= 1 - 2 * le and max(ys) - min(ys) <= 1 - 2 * le:
            cam.data.shift_x = (max(xs) + min(xs)) / 2 - 0.5          # don vi shift = canh dai cua anh
            cam.data.shift_y = ((max(ys) + min(ys)) / 2 - 0.5) * ty_le
            return D
        D *= 1.03
    return D


anh_sang_rieng(True)
dat_nen(-40.0)
so = 1
# 1) nhin thang tu tren xuong (camera truc giao), anh dung, mat tien o duoi anh
r.resolution_x, r.resolution_y = 1500, 2100
den_rieng.rotation_euler = (math.radians(12), 0, math.radians(-35))   # bong tuong ngan, khong phu kin phong
for ten_hien, ten_col, ten_file in TANG:
    col, mn, mx = KHOI[ten_col]
    y_duoi, y_tren = mn.y - 2.4, mx.y + 0.8               # chua ca nhan ten tang o phia truoc
    dai, rong = y_tren - y_duoi, mx.x - mn.x + 3          # truc Y theo chieu doc anh
    khung = max(dai, rong * r.resolution_y / r.resolution_x)
    cu = chi_hien([ten_col])
    cam = camera(f"Cam tach {ten_col} tren xuong", ((mn.x + mx.x) / 2, (y_duoi + y_tren) / 2, 60.0), None, ortho=khung)
    chup(cam, f"{so:02d}_{ten_file}-tren-xuong.png"); so += 1
    tra_lai(cu)
# 2) goc 3/4 tu tren cao phia truoc ben trai: thay chieu cao tuong, cua, noi that
r.resolution_x, r.resolution_y = 2000, 1250
den_rieng.rotation_euler = (math.radians(30), 0, math.radians(-35))
goc_cao = math.radians(58)                               # nhin xuong 58 do
# goc lech so voi huong nhin thang mat tien (0 = dung truoc nha, 90 = dung ben trai nha, 180 = phia sau)
GOC_LECH = {"Mai - Tum": 140}                             # tum che san thuong phia sau: nhin tu sau ben trai
for ten_hien, ten_col, ten_file in TANG:
    col, mn, mx = KHOI[ten_col]
    a = math.radians(GOC_LECH.get(ten_col, 50))
    huong = mathutils.Vector((-math.cos(goc_cao) * math.sin(a), -math.cos(goc_cao) * math.cos(a), math.sin(goc_cao)))
    nhan = col.objects.get(f"TT_nhan_{ten_col}")
    an_nhan = math.degrees(a) > 90                         # nhin tu phia sau thi chu bi nguoc: an nhan
    lo = mathutils.Vector((mn.x, mn.y - (0 if an_nhan else 2.3), NEN_Z))
    # goc hop bao cua tung doi tuong (sat hinh hon mot hop bao chung), ca nhan ten tang neu hien
    diem = [o.matrix_world @ mathutils.Vector(c) for o in col.objects
            if o.type in ("MESH", "FONT") and not (o is nhan and an_nhan) for c in o.bound_box]
    dich = (lo + mx) / 2
    dich.z = NEN_Z + 0.3 * (mx.z - NEN_Z)
    cu = chi_hien([ten_col])
    if nhan:
        nhan.hide_render = an_nhan
    cam = camera(f"Cam tach {ten_col} 3-4", dich + huong * 30, dich, lens=30)
    print("Goc 3/4", ten_col, "camera cach", round(vua_khung(cam, dich, huong, diem), 1), "m")
    chup(cam, f"{so:02d}_{ten_file}-goc-3-4.png"); so += 1
    if nhan:
        nhan.hide_render = False
    tra_lai(cu)
# 3) tong the: toa nha goc va 4 tang tach, anh sang goc cua file
anh_sang_rieng(False)
dat_nen(5.2)
x_giua = (0 + max(k[2].x for k in KHOI.values())) / 2
cam = camera("Cam tach tang tong the", (x_giua - 6, -38.0, 32.0), (x_giua, 5.0, 0.0), lens=30)
chup(cam, f"{so:02d}_tong-the-toa-nha-va-cac-tang-tach.png")

den_rieng.hide_render = True
r.resolution_x, r.resolution_y = res_cu
scene.camera = cam_cu
scene.eevee.use_raytracing = rt_cu
print("Xong. Anh luu tai", RA)