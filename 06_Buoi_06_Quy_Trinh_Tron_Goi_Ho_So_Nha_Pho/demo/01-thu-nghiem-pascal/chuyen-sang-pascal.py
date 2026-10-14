# Chuyen file mo ta ban ve (03_mo-ta-tu-ban-ve.json, mm) sang ke hoach dung cho Pascal (m).
# Pascal can tuong lien roi dat cua theo ty le t (0..1) doc tuong; file mo ta thi tuong da cat san tai lo cua
# va dung tai cot, nen o day noi cac doan tuong, cot, lo cua thang hang thanh mot tuong.
import json, sys
from collections import defaultdict

SRC = sys.argv[1]
OUT = sys.argv[2]
d = json.load(open(SRC, encoding="utf-8"))
CD = d["cao_do"]
TBL = d["cua"]
LEVELS = [("T1", CD["T1"], CD["T2"]), ("T2", CD["T2"], CD["T3"]), ("T3", CD["T3"], CD["ST"]), ("MAI", CD["ST"], CD["TUM"])]


def m(v):
    return round(v / 1000.0, 3)


def runs(pieces):
    """pieces: list of (a, b, kind, extra). Merge touching intervals; keep runs containing a wall piece."""
    pieces = sorted(pieces, key=lambda p: p[0])
    out, cur = [], None
    for p in pieces:
        if cur and p[0] <= cur["b"] + 1:
            cur["b"] = max(cur["b"], p[1]); cur["items"].append(p)
        else:
            if cur: out.append(cur)
            cur = {"a": p[0], "b": p[1], "items": [p]}
    if cur: out.append(cur)
    return [r for r in out if any(i[2] == "wall" for i in r["items"])]


plan = {"don_vi": "m", "truc": "x ban ve -> X Pascal, y ban ve -> Z Pascal", "levels": []}
for key, z0, z1 in LEVELS:
    mb = d["mat_bang"][key]
    walls_h, walls_v = defaultdict(list), defaultdict(list)   # band -> pieces
    def add(rect, kind, extra=None):
        x1, y1, x2, y2 = rect
        if (x2 - x1) >= (y2 - y1):   # nam ngang: day theo y
            walls_h[(y1, y2)].append((x1, x2, kind, extra))
        else:
            walls_v[(x1, x2)].append((y1, y2, kind, extra))
    for r in mb["tuong"]:
        add(r, "wall")
    for c in mb["cua"]:
        # lo cua nam trong tuong: huong theo canh dai cua hinh chu nhat (doc_x = True la chay doc truc x)
        add(c["hcn"], "open", c["ma"])
    # cot: gan vao band nao no nam tron trong do day
    for x1, y1, x2, y2 in mb["cot"]:
        for (b1, b2), ps in walls_h.items():
            if y1 <= b1 and b2 <= y2: ps.append((x1, x2, "col", None))
        for (b1, b2), ps in walls_v.items():
            if x1 <= b1 and b2 <= x2: ps.append((y1, y2, "col", None))
    walls, openings = [], []
    def emit(band, r, horiz):
        b1, b2 = band
        c = (b1 + b2) / 2
        if horiz:
            start, end = [m(r["a"]), m(c)], [m(r["b"]), m(c)]
        else:
            start, end = [m(c), m(r["a"])], [m(c), m(r["b"])]
        wi = len(walls)
        walls.append({"i": wi, "start": start, "end": end, "thickness": m(b2 - b1)})
        L = r["b"] - r["a"]
        for a, b, kind, ma in r["items"]:
            if kind != "open": continue
            t = TBL[ma]
            openings.append({"wall": wi, "ma": ma, "loai": "door" if ma.startswith("D") else "window",
                             "t": round(((a + b) / 2 - r["a"]) / L, 4), "rong": m(t["rong"]),
                             "cao": m(t["cao"]), "bau": m(t["be"]), "ten": t["ten"]})
    for band, ps in walls_h.items():
        for r in runs(ps): emit(band, r, True)
    for band, ps in walls_v.items():
        for r in runs(ps): emit(band, r, False)
    lv = {"key": key, "cao_do_san": m(z0), "cao_tang": m(z1 - z0), "walls": walls, "openings": openings,
          "san": [[[m(x1), m(y1)], [m(x2), m(y1)], [m(x2), m(y2)], [m(x1), m(y2)]] for x1, y1, x2, y2 in mb["san"]],
          "lo_san": [[m(v) for v in r] for r in mb.get("lo_san", [])],
          "lan_can": [{"start": [m(r[0]), m((r[1] + r[3]) / 2)] if (r[2] - r[0]) >= (r[3] - r[1]) else [m((r[0] + r[2]) / 2), m(r[1])],
                       "end": [m(r[2]), m((r[1] + r[3]) / 2)] if (r[2] - r[0]) >= (r[3] - r[1]) else [m((r[0] + r[2]) / 2), m(r[3])],
                       "thickness": m(min(r[2] - r[0], r[3] - r[1])), "height": 1.0} for r in mb.get("lan_can", [])],
          "thang": {k: ([m(v) for v in val] if isinstance(val, list) and k != "so_bac_moi_ve" else val)
                    for k, val in mb["thang"].items()} if isinstance(mb.get("thang"), dict) else None,
          "noi_that": [{"ten": n["ten"], "tam": [m((n["hcn"][0] + n["hcn"][2]) / 2), m((n["hcn"][1] + n["hcn"][3]) / 2)],
                        "kich_thuoc": [m(n["hcn"][2] - n["hcn"][0]), m(n["hcn"][3] - n["hcn"][1])],
                        "treo": n.get("treo"), "lung": n.get("lung")} for n in mb.get("noi_that", [])]}
    plan["levels"].append(lv)

plan["mai"] = {k: {"ten": v["ten"], "ap_cho": v["ap_cho"], "dinh": m(v["dinh"]), "mep": m(v["mep"])} for k, v in d["mai"].items()}
plan["mai_hcn"] = [{"ma": r["ma"], "hcn": [m(v) for v in r["hcn"]]} for r in d["mat_bang"]["MAI"]["mai"]]
json.dump(plan, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for lv in plan["levels"]:
    print(lv["key"], "tuong", len(lv["walls"]), "cua", len(lv["openings"]), "noi that", len(lv["noi_that"]))
print("tong cua", sum(len(l["openings"]) for l in plan["levels"]))
