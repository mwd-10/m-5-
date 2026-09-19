from flask import Flask, render_template, request, jsonify ,send_file

app = Flask(__name__)


# =========================================================
# 40 MATERIALS
# 20 in A + 20 in B
# Every A material has ONE specific opposite B material.
# =========================================================

MATERIALS = [
    # -------------------------
    # SIDE A - 20 MATERIALS
    # -------------------------

    {
        "id": "hcl",
        "ar": "حمض الهيدروكلوريك",
        "formula": "HCl",
        "color": "#dff7ff",
        "side": "A",
        "pair": 1
    },
    {
        "id": "h2so4",
        "ar": "حمض الكبريتيك",
        "formula": "H₂SO₄",
        "color": "#e8f8ff",
        "side": "A",
        "pair": 2
    },
    {
        "id": "hno3",
        "ar": "حمض النيتريك",
        "formula": "HNO₃",
        "color": "#edfaff",
        "side": "A",
        "pair": 3
    },
    {
        "id": "ch3cooh",
        "ar": "حمض الخليك",
        "formula": "CH₃COOH",
        "color": "#fff8e6",
        "side": "A",
        "pair": 4
    },
    {
        "id": "h3po4",
        "ar": "حمض الفوسفوريك",
        "formula": "H₃PO₄",
        "color": "#eefaff",
        "side": "A",
        "pair": 5
    },
    {
        "id": "cuso4",
        "ar": "كبريتات النحاس",
        "formula": "CuSO₄",
        "color": "#4b8fd8",
        "side": "A",
        "pair": 6
    },
    {
        "id": "cu_no3_2",
        "ar": "نترات النحاس",
        "formula": "Cu(NO₃)₂",
        "color": "#56a6dc",
        "side": "A",
        "pair": 7
    },
    {
        "id": "fecl3",
        "ar": "كلوريد الحديد الثلاثي",
        "formula": "FeCl₃",
        "color": "#d8a13c",
        "side": "A",
        "pair": 8
    },
    {
        "id": "fecl2",
        "ar": "كلوريد الحديد الثنائي",
        "formula": "FeCl₂",
        "color": "#b8d6a0",
        "side": "A",
        "pair": 9
    },
    {
        "id": "znso4",
        "ar": "كبريتات الزنك",
        "formula": "ZnSO₄",
        "color": "#e8f7ff",
        "side": "A",
        "pair": 10
    },
    {
        "id": "mgso4",
        "ar": "كبريتات المغنيسيوم",
        "formula": "MgSO₄",
        "color": "#eefaff",
        "side": "A",
        "pair": 11
    },
    {
        "id": "nacl",
        "ar": "كلوريد الصوديوم",
        "formula": "NaCl",
        "color": "#f7fbff",
        "side": "A",
        "pair": 12
    },
    {
        "id": "kcl",
        "ar": "كلوريد البوتاسيوم",
        "formula": "KCl",
        "color": "#f5fbff",
        "side": "A",
        "pair": 13
    },
    {
        "id": "cacl2",
        "ar": "كلوريد الكالسيوم",
        "formula": "CaCl₂",
        "color": "#f4fbff",
        "side": "A",
        "pair": 14
    },
    {
        "id": "mgcl2",
        "ar": "كلوريد المغنيسيوم",
        "formula": "MgCl₂",
        "color": "#eefaff",
        "side": "A",
        "pair": 15
    },
    {
        "id": "kbr",
        "ar": "بروميد البوتاسيوم",
        "formula": "KBr",
        "color": "#f8fbff",
        "side": "A",
        "pair": 16
    },
    {
        "id": "na2so4",
        "ar": "كبريتات الصوديوم",
        "formula": "Na₂SO₄",
        "color": "#f4fbff",
        "side": "A",
        "pair": 17
    },
    {
        "id": "ca_no3_2",
        "ar": "نترات الكالسيوم",
        "formula": "Ca(NO₃)₂",
        "color": "#f4fbff",
        "side": "A",
        "pair": 18
    },
    {
        "id": "i2",
        "ar": "اليود",
        "formula": "I₂",
        "color": "#9b6a32",
        "side": "A",
        "pair": 19
    },
    {
        "id": "alcl3",
        "ar": "كلوريد الألمنيوم",
        "formula": "AlCl₃",
        "color": "#eefaff",
        "side": "A",
        "pair": 20
    },


    # -------------------------
    # SIDE B - 20 MATERIALS
    # -------------------------

    {
        "id": "naoh",
        "ar": "هيدروكسيد الصوديوم",
        "formula": "NaOH",
        "color": "#f5fbff",
        "side": "B",
        "pair": 1
    },
    {
        "id": "bacl2",
        "ar": "كلوريد الباريوم",
        "formula": "BaCl₂",
        "color": "#f1faff",
        "side": "B",
        "pair": 2
    },
    {
        "id": "nh3",
        "ar": "الأمونيا",
        "formula": "NH₃",
        "color": "#f4fbff",
        "side": "B",
        "pair": 3
    },
    {
        "id": "nahco3",
        "ar": "بيكربونات الصوديوم",
        "formula": "NaHCO₃",
        "color": "#f7fbff",
        "side": "B",
        "pair": 4
    },
    {
        "id": "caoh2",
        "ar": "هيدروكسيد الكالسيوم",
        "formula": "Ca(OH)₂",
        "color": "#f4fbff",
        "side": "B",
        "pair": 5
    },
    {
        "id": "koh",
        "ar": "هيدروكسيد البوتاسيوم",
        "formula": "KOH",
        "color": "#f5fbff",
        "side": "B",
        "pair": 6
    },
    {
        "id": "ki",
        "ar": "يوديد البوتاسيوم",
        "formula": "KI",
        "color": "#f7fbff",
        "side": "B",
        "pair": 7
    },
    {
        "id": "nh4oh",
        "ar": "هيدروكسيد الأمونيوم",
        "formula": "NH₄OH",
        "color": "#f3fbff",
        "side": "B",
        "pair": 8
    },
    {
        "id": "k2co3",
        "ar": "كربونات البوتاسيوم",
        "formula": "K₂CO₃",
        "color": "#f4fbff",
        "side": "B",
        "pair": 9
    },
    {
        "id": "k3po4",
        "ar": "فوسفات البوتاسيوم",
        "formula": "K₃PO₄",
        "color": "#f5fbff",
        "side": "B",
        "pair": 10
    },
    {
        "id": "baoh2",
        "ar": "هيدروكسيد الباريوم",
        "formula": "Ba(OH)₂",
        "color": "#f1faff",
        "side": "B",
        "pair": 11
    },
    {
        "id": "agno3",
        "ar": "نترات الفضة",
        "formula": "AgNO₃",
        "color": "#f6fbff",
        "side": "B",
        "pair": 12
    },
    {
        "id": "pbno3_2",
        "ar": "نترات الرصاص",
        "formula": "Pb(NO₃)₂",
        "color": "#f2faff",
        "side": "B",
        "pair": 13
    },
    {
        "id": "na3po4",
        "ar": "فوسفات الصوديوم",
        "formula": "Na₃PO₄",
        "color": "#f5fbff",
        "side": "B",
        "pair": 14
    },
    {
        "id": "lioh",
        "ar": "هيدروكسيد الليثيوم",
        "formula": "LiOH",
        "color": "#f5fbff",
        "side": "B",
        "pair": 15
    },
    {
        "id": "ag2so4",
        "ar": "كبريتات الفضة",
        "formula": "Ag₂SO₄",
        "color": "#f5fbff",
        "side": "B",
        "pair": 16
    },
    {
        "id": "srcl2",
        "ar": "كلوريد السترونشيوم",
        "formula": "SrCl₂",
        "color": "#f3fbff",
        "side": "B",
        "pair": 17
    },
    {
        "id": "na2hpo4",
        "ar": "فوسفات هيدروجين الصوديوم",
        "formula": "Na₂HPO₄",
        "color": "#f4fbff",
        "side": "B",
        "pair": 18
    },
    {
        "id": "na2s2o3",
        "ar": "ثيوكبريتات الصوديوم",
        "formula": "Na₂S₂O₃",
        "color": "#f5fbff",
        "side": "B",
        "pair": 19
    },
    {
        "id": "na2co3",
        "ar": "كربونات الصوديوم",
        "formula": "Na₂CO₃",
        "color": "#f4fbff",
        "side": "B",
        "pair": 20
    }
]


# =========================================================
# THE 20 INTENDED PAIRS
# =========================================================

PAIR_LAYOUT = [
    ("hcl", "naoh"),
    ("h2so4", "bacl2"),
    ("hno3", "nh3"),
    ("ch3cooh", "nahco3"),
    ("h3po4", "caoh2"),
    ("cuso4", "koh"),
    ("cu_no3_2", "ki"),
    ("fecl3", "nh4oh"),
    ("fecl2", "k2co3"),
    ("znso4", "k3po4"),
    ("mgso4", "baoh2"),
    ("nacl", "agno3"),
    ("kcl", "pbno3_2"),
    ("cacl2", "na3po4"),
    ("mgcl2", "lioh"),
    ("kbr", "ag2so4"),
    ("na2so4", "srcl2"),
    ("ca_no3_2", "na2hpo4"),
    ("i2", "na2s2o3"),
    ("alcl3", "na2co3")
]


# =========================================================
# REACTION DATA
# =========================================================

REACTIONS = {

    # 1
    ("hcl", "naoh"): {
        "title": "تعادل حمض وقاعدة",
        "equation": "HCl + NaOH → NaCl + H₂O",
        "explanation": "يتفاعل حمض الهيدروكلوريك مع هيدروكسيد الصوديوم في تفاعل تعادل ينتج عنه ملح وماء.",
        "observation": "ستلاحظ أن المحلول يبقى شبه شفاف وعديم اللون، ولا يظهر راسب أو غاز واضح.",
        "color": "#e9f8ff",
        "precipitate": False,
        "gas": False
    },

    # 2
    ("h2so4", "bacl2"): {
        "title": "تكوّن راسب أبيض",
        "equation": "H₂SO₄ + BaCl₂ → BaSO₄↓ + 2HCl",
        "explanation": "تتحد أيونات الباريوم مع أيونات الكبريتات لتكوين كبريتات الباريوم غير الذائبة.",
        "observation": "ستلاحظ تحوّل المحلول إلى عكر وظهور راسب أبيض واضح.",
        "color": "#edf7ff",
        "precipitate": True,
        "gas": False
    },

    # 3
    ("hno3", "nh3"): {
        "title": "تكوّن نترات الأمونيوم",
        "equation": "HNO₃ + NH₃ → NH₄NO₃",
        "explanation": "يتفاعل حمض النيتريك مع الأمونيا لتكوين نترات الأمونيوم.",
        "observation": "يبقى المحلول شبه شفاف، ولا يظهر راسب أو فقاعات غازية واضحة.",
        "color": "#eefaff",
        "precipitate": False,
        "gas": False
    },

    # 4
    ("ch3cooh", "nahco3"): {
        "title": "تفاعل مع انطلاق غاز",
        "equation": "CH₃COOH + NaHCO₃ → CH₃COONa + H₂O + CO₂↑",
        "explanation": "يتفاعل حمض الخليك مع بيكربونات الصوديوم وينتج غاز ثاني أكسيد الكربون.",
        "observation": "ستلاحظ فقاعات واضحة تتصاعد في المحلول، بينما يبقى المحلول قريبًا من اللون الشفاف.",
        "color": "#eefaff",
        "precipitate": False,
        "gas": True
    },

    # 5
    ("h3po4", "caoh2"): {
        "title": "تكوّن فوسفات الكالسيوم",
        "equation": "2H₃PO₄ + 3Ca(OH)₂ → Ca₃(PO₄)₂↓ + 6H₂O",
        "explanation": "يتكوّن فوسفات الكالسيوم، وهو مركب قليل الذوبان يظهر على هيئة راسب.",
        "observation": "ستلاحظ ظهور عكورة وراسب فاتح اللون في المحلول.",
        "color": "#eaf5fa",
        "precipitate": True,
        "gas": False
    },

    # 6
    ("cuso4", "koh"): {
        "title": "تكوّن هيدروكسيد النحاس",
        "equation": "CuSO₄ + 2KOH → Cu(OH)₂↓ + K₂SO₄",
        "explanation": "تتفاعل أيونات النحاس مع أيونات الهيدروكسيد لتكوين هيدروكسيد النحاس غير الذائب.",
        "observation": "ستلاحظ ظهور راسب أزرق فاتح داخل المحلول وتخفّف اللون الأزرق الأصلي.",
        "color": "#72a9d6",
        "precipitate": True,
        "gas": False
    },

    # 7
    ("cu_no3_2", "ki"): {
        "title": "تكوّن راسب وتغيّر في اللون",
        "equation": "2Cu(NO₃)₂ + 4KI → 2CuI↓ + I₂ + 4KNO₃",
        "explanation": "يتكوّن يوديد النحاس مع ظهور اليود في المحلول.",
        "observation": "ستلاحظ ظهور راسب فاتح مع ظهور لون بني/داكن مرتبط بتكوّن اليود.",
        "color": "#9c7951",
        "precipitate": True,
        "gas": False
    },

    # 8
    ("fecl3", "nh4oh"): {
        "title": "تكوّن هيدروكسيد الحديد الثلاثي",
        "equation": "FeCl₃ + 3NH₄OH → Fe(OH)₃↓ + 3NH₄Cl",
        "explanation": "تتفاعل أيونات الحديد الثلاثي مع الهيدروكسيد لتكوين هيدروكسيد الحديد الثلاثي.",
        "observation": "ستلاحظ ظهور راسب بني واضح في المحلول.",
        "color": "#9b6338",
        "precipitate": True,
        "gas": False
    },

    # 9
    ("fecl2", "k2co3"): {
        "title": "تكوّن راسب كربونات الحديد",
        "equation": "FeCl₂ + K₂CO₃ → FeCO₃↓ + 2KCl",
        "explanation": "تتفاعل أيونات الحديد الثنائي مع الكربونات لتكوين كربونات الحديد قليلة الذوبان.",
        "observation": "ستلاحظ ظهور راسب فاتح يميل إلى الأخضر داخل المحلول.",
        "color": "#b3c49b",
        "precipitate": True,
        "gas": False
    },

    # 10
    ("znso4", "k3po4"): {
        "title": "تكوّن فوسفات الزنك",
        "equation": "3ZnSO₄ + 2K₃PO₄ → Zn₃(PO₄)₂↓ + 3K₂SO₄",
        "explanation": "تتفاعل أيونات الزنك والفوسفات لتكوين فوسفات الزنك قليلة الذوبان.",
        "observation": "ستلاحظ ظهور راسب أبيض أو فاتح وعكورة في المحلول.",
        "color": "#eaf5fa",
        "precipitate": True,
        "gas": False
    },

    # 11
    ("mgso4", "baoh2"): {
        "title": "تكوّن راسبين",
        "equation": "MgSO₄ + Ba(OH)₂ → Mg(OH)₂↓ + BaSO₄↓",
        "explanation": "ينتج عن التفاعل مركبان قليلَا الذوبان، هما هيدروكسيد المغنيسيوم وكبريتات الباريوم.",
        "observation": "ستلاحظ عكورة واضحة وظهور مادة راسبة فاتحة في المحلول.",
        "color": "#e9f4f7",
        "precipitate": True,
        "gas": False
    },

    # 12
    ("nacl", "agno3"): {
        "title": "تكوّن كلوريد الفضة",
        "equation": "NaCl + AgNO₃ → AgCl↓ + NaNO₃",
        "explanation": "تتفاعل أيونات الفضة مع أيونات الكلوريد لتكوين كلوريد الفضة غير الذائب.",
        "observation": "ستلاحظ ظهور راسب أبيض واضح في المحلول.",
        "color": "#edf5fa",
        "precipitate": True,
        "gas": False
    },

    # 13
    ("kcl", "pbno3_2"): {
        "title": "تكوّن راسب كلوريد الرصاص",
        "equation": "2KCl + Pb(NO₃)₂ → PbCl₂↓ + 2KNO₃",
        "explanation": "تتحد أيونات الرصاص مع أيونات الكلوريد لتكوين كلوريد الرصاص قليل الذوبان.",
        "observation": "ستلاحظ ظهور راسب أبيض في المحلول.",
        "color": "#edf6fa",
        "precipitate": True,
        "gas": False
    },

    # 14
    ("cacl2", "na3po4"): {
        "title": "تكوّن فوسفات الكالسيوم",
        "equation": "3CaCl₂ + 2Na₃PO₄ → Ca₃(PO₄)₂↓ + 6NaCl",
        "explanation": "تتفاعل أيونات الكالسيوم والفوسفات لتكوين فوسفات الكالسيوم قليلة الذوبان.",
        "observation": "ستلاحظ ظهور عكورة وراسب فاتح اللون.",
        "color": "#eaf5fa",
        "precipitate": True,
        "gas": False
    },

    # 15
    ("mgcl2", "lioh"): {
        "title": "تكوّن هيدروكسيد المغنيسيوم",
        "equation": "MgCl₂ + 2LiOH → Mg(OH)₂↓ + 2LiCl",
        "explanation": "تتفاعل أيونات المغنيسيوم مع الهيدروكسيد لتكوين هيدروكسيد المغنيسيوم غير الذائب.",
        "observation": "ستلاحظ ظهور راسب أبيض وعكورة في المحلول.",
        "color": "#eaf6fa",
        "precipitate": True,
        "gas": False
    },

    # 16
    ("kbr", "ag2so4"): {
        "title": "تكوّن بروميد الفضة",
        "equation": "2KBr + Ag₂SO₄ → 2AgBr↓ + K₂SO₄",
        "explanation": "تتفاعل أيونات الفضة مع أيونات البروميد لتكوين بروميد الفضة قليل الذوبان.",
        "observation": "ستلاحظ ظهور راسب فاتح يميل إلى اللون الكريمي.",
        "color": "#e5ded0",
        "precipitate": True,
        "gas": False
    },

    # 17
    ("na2so4", "srcl2"): {
        "title": "تكوّن كبريتات السترونشيوم",
        "equation": "Na₂SO₄ + SrCl₂ → SrSO₄↓ + 2NaCl",
        "explanation": "تتحد أيونات السترونشيوم مع أيونات الكبريتات لتكوين كبريتات السترونشيوم قليلة الذوبان.",
        "observation": "ستلاحظ ظهور راسب أبيض وعكورة خفيفة في المحلول.",
        "color": "#edf6fa",
        "precipitate": True,
        "gas": False
    },

    # 18
    ("ca_no3_2", "na2hpo4"): {
        "title": "تكوّن فوسفات هيدروجين الكالسيوم",
        "equation": "Ca(NO₃)₂ + Na₂HPO₄ → CaHPO₄↓ + 2NaNO₃",
        "explanation": "تتفاعل أيونات الكالسيوم مع فوسفات الهيدروجين لتكوين مركب قليل الذوبان.",
        "observation": "ستلاحظ ظهور راسب فاتح وعكورة في المحلول.",
        "color": "#edf6fa",
        "precipitate": True,
        "gas": False
    },

    # 19
    ("i2", "na2s2o3"): {
        "title": "اختفاء لون اليود",
        "equation": "I₂ + 2Na₂S₂O₃ → 2NaI + Na₂S₄O₆",
        "explanation": "يتفاعل اليود مع ثيوكبريتات الصوديوم، مما يؤدي إلى استهلاك اليود.",
        "observation": "ستلاحظ اختفاء اللون البني لليود تدريجيًا ليصبح المحلول شبه عديم اللون.",
        "color": "#edfaff",
        "precipitate": False,
        "gas": False
    },

    # 20
    ("alcl3", "na2co3"): {
        "title": "تكوّن راسب مع فقاعات",
        "equation": "2AlCl₃ + 3Na₂CO₃ + 3H₂O → 2Al(OH)₃↓ + 3CO₂↑ + 6NaCl",
        "explanation": "يتكوّن هيدروكسيد الألمنيوم مع انطلاق ثاني أكسيد الكربون في المحاكاة.",
        "observation": "ستلاحظ ظهور راسب أبيض مع فقاعات غازية في المحلول.",
        "color": "#e8f4f8",
        "precipitate": True,
        "gas": True
    }
}


# =========================================================
# Create lookup dictionaries
# =========================================================

MATERIAL_BY_ID = {
    material["id"]: material
    for material in MATERIALS
}

PAIR_BY_MATERIAL = {}

for pair_number, (a_id, b_id) in enumerate(PAIR_LAYOUT, start=1):
    PAIR_BY_MATERIAL[a_id] = {
        "pair": pair_number,
        "a": a_id,
        "b": b_id
    }

    PAIR_BY_MATERIAL[b_id] = {
        "pair": pair_number,
        "a": a_id,
        "b": b_id
    }


# Make sure the reaction keys are independent from A/B order.
REACTION_MAP = {}

for (a_id, b_id), reaction in REACTIONS.items():
    REACTION_MAP[tuple(sorted((a_id, b_id)))] = reaction


# =========================================================
# Validation
# =========================================================

assert len(MATERIALS) == 40
assert len([m for m in MATERIALS if m["side"] == "A"]) == 20
assert len([m for m in MATERIALS if m["side"] == "B"]) == 20
assert len(PAIR_LAYOUT) == 20

for pair_number, (a_id, b_id) in enumerate(PAIR_LAYOUT, start=1):
    assert MATERIAL_BY_ID[a_id]["side"] == "A"
    assert MATERIAL_BY_ID[b_id]["side"] == "B"
    assert MATERIAL_BY_ID[a_id]["pair"] == pair_number
    assert MATERIAL_BY_ID[b_id]["pair"] == pair_number


# =========================================================
# Routes
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/materials")
def get_materials():
    side_a = sorted(
        [m for m in MATERIALS if m["side"] == "A"],
        key=lambda x: x["pair"]
    )

    side_b = sorted(
        [m for m in MATERIALS if m["side"] == "B"],
        key=lambda x: x["pair"]
    )

    return jsonify({
        "A": side_a,
        "B": side_b,
        "count": len(MATERIALS)
    })


@app.route("/api/pairs")
def get_pairs():
    pairs = []

    for number, (a_id, b_id) in enumerate(PAIR_LAYOUT, start=1):
        pairs.append({
            "number": number,
            "a": MATERIAL_BY_ID[a_id],
            "b": MATERIAL_BY_ID[b_id]
        })

    return jsonify({
        "hint": (
            "المواد موزعة إلى 20 مادة في الخانة A و20 مادة في الخانة B. "
            "كل مادة في A لها مادة مقابلة محددة في B مصممة لتكوين تفاعل. "
            "يمكنك تجربة أي تركيبة أخرى أيضًا."
        ),
        "pairs": pairs
    })


@app.route("/api/mix", methods=["POST"])
def mix():
    data = request.get_json(silent=True) or {}

    a_id = data.get("a")
    b_id = data.get("b")

    if not a_id or not b_id:
        return jsonify({
            "success": False,
            "message": "يرجى اختيار مادة من كل خانة."
        }), 400

    if a_id not in MATERIAL_BY_ID or b_id not in MATERIAL_BY_ID:
        return jsonify({
            "success": False,
            "message": "المادة غير موجودة."
        }), 400

    material_a = MATERIAL_BY_ID[a_id]
    material_b = MATERIAL_BY_ID[b_id]

    # Must actually be one from A and one from B.
    if material_a["side"] != "A" or material_b["side"] != "B":
        return jsonify({
            "success": False,
            "message": "يجب اختيار مادة من A ومادة من B."
        }), 400

    # IMPORTANT:
    # The only intended reaction is between the specific
    # opposite pair.
    is_opposite_pair = (
        material_a["pair"] == material_b["pair"]
    )

    reaction = REACTION_MAP.get(
        tuple(sorted((a_id, b_id)))
    ) if is_opposite_pair else None

    if reaction:
        return jsonify({
            "success": True,
            "reacts": True,
            "title": reaction["title"],
            "equation": reaction["equation"],
            "explanation": reaction["explanation"],
            "observation": reaction["observation"],
            "color": reaction["color"],
            "precipitate": reaction["precipitate"],
            "gas": reaction["gas"]
        })

    # Any non-opposite combination
    return jsonify({
        "success": True,
        "reacts": False,
        "title": "لا يوجد تفاعل مرئي مسجل",
        "equation": "لا يوجد تفاعل مسجل لهذه التركيبة.",
        "explanation": (
            "هذه المادتان ليستا زوجًا متقابلًا من الأزواج المصممة "
            "في اللعبة."
        ),
        "observation": (
            "لن يظهر في المحاكاة تغيّر مرئي واضح: "
            "لا راسب ولا غاز ولا تغيّر لون مسجل لهذه التركيبة."
        ),
        "color": "#eef8fb",
        "precipitate": False,
        "gas": False
    })


if __name__ == "__main__":
    app.run(debug=True  
           
    )
 
