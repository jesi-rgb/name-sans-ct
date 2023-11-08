import numpy as np
from coldtype import *
from coldtype.warping import warp

font_path = "/Users/jesi/fonts/variable/NameSans.ttf"
font_mono = "/Users/jesi/fonts/variable/NameMono.ttf"
name = Font.Cacheable(font_path)
mono = Font.Cacheable(font_mono)

midi = MidiTimeline("assets/name_sans.mid", track=0, bpm=68, fps=60)
wav = __sibling__("assets/name_sans.wav")

ar = {
    "KD": [10, 20],
    "CW": [15, 75],
    "HT": [2, 2],
    "RS": [5, 5],
    "SD": [3, 90],
    "TM": [5, 10],
}


BG_COLOR = "#16171D"
PRIMARY_COLOR = "#D5D8FB"
SECONDARY_COLOR = "#A3ABFF"
ACCENT_COLOR = "#F35959"


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(100, fps=60))
def name_sans(f):
    return (
        StSt(
            "NAME\nSÄNS\n1234",
            name,
            300,
            opsz=1,
            ital=f.e("qeio"),
            wght=f.e("qeio"),
            leading=60,
            multiline=True,
            features={"onum": True, "titl": True},
        )
        .f(PRIMARY_COLOR)
        .removeOverlap()
        # .outline(offset=3.5)
        .align(f.a.r)
    )


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(500, fps=60))
def wave_bold(f):
    texts = []
    for i in range(12):
        texts.append(
            Glyphwise(
                "NAME SANS VARIABLE",
                lambda g: Style(
                    name,
                    fill=SECONDARY_COLOR if i % 2 == 0 else PRIMARY_COLOR,
                    font_size=110,
                    wght=f.adj(g.i * i).e("qeio", 4),
                    tu=-190,
                ),
            ).align(f.a.r)
        )

    group = PS(*texts).stack(leading=10).align(f.a.r)

    return group


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(500, fps=60))
def chars(f):
    char_code = f.i // 5 + 32
    main = (
        StSt(
            chr(char_code),
            name,
            800,
            opsz=1,
            ital=f.e("qeio", 2),
            wght=f.e("qeio", 3),
            leading=60,
            multiline=True,
            features={"ss15": True, "titl": True},
        )
        .f(PRIMARY_COLOR)
        .removeOverlap()
        # .outline(offset=3.5)
        .align(f.a.r)
        .translate(x=0, y=100)
    )
    code = (
        StSt(
            f"UTF Code \\u{ {char_code} }",
            mono,
            50,
            opsz=0,
            wght=0.3,
            features={"tnum": True},
        )
        .align(f.a.r.inset(30), y="mny")
        .f(SECONDARY_COLOR, 0.7)
    )
    return (main, code)


arrows_length = 600


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(arrows_length, fps=60))
def arrow(f):
    n = 7**2
    arrows = (
        PS(
            [
                StSt(
                    "-->",
                    name,
                    200,
                    opsz=1,
                    # wght=np.cos(100 + (f.i / 100) * (i / 9)),
                    wght=i % n / n,
                    fill=PRIMARY_COLOR,
                ).rotate(45 * np.cos((i / ((n / 2) * 5)) * (f.i / 10)))
                for i in range(n)
            ]
        )
        .grid(every=np.sqrt(n))
        .translate(x=30, transformFrame=False)
    )

    return arrows


length_numbers = 700


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(length_numbers, fps=60))
def numbers(f):
    def map_color(i):
        if i == math.isqrt(i) ** 2:
            return ACCENT_COLOR
        elif i % 2 == 0:
            return PRIMARY_COLOR
        else:
            return SECONDARY_COLOR

    ot_features = f"On  - Tabular Numbers (tnum)\nOn  - Slashed Zero (zero)\nOff - Required Variation Alternates (rvrn)"
    ot_feat_stst = (
        StSt(
            ot_features,
            mono,
            35,
            wght=0.4,
            leading=10,
            features={"tnum": True, "zero": True},
        )
        .align(f.a.r.inset(30), x="mnx", y="mxy")
        .f(SECONDARY_COLOR, 0.6)
    )

    n = 9**2
    numbers = (
        PS(
            [
                StSt(
                    f"{i+1:02d}",
                    name,
                    94,
                    opsz=0.9,
                    # wght=np.cos(i % n * (f.i / 100)),
                    wght=0.5
                    + 0.5 * np.cos(i % n * f.i / length_numbers),  # happy with this one
                    fill=map_color(i + 1),
                    features={"tnum": True, "zero": True, "rvrn": False},
                )
                for i in range(n)
            ]
        )
        .grid(every=np.sqrt(n))
        .lead(30)
        # .align(f.a.r.inset(30), y='mny')
        .translate(x=30, y=30)
    )

    return (numbers, ot_feat_stst)


grotesque_length = 400

#
@animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(grotesque_length, fps=60))
def grotesque(f):
    ss19 = True if f.i > grotesque_length // 2 else False
    ss06 = True if f.i > grotesque_length // 2 else False

    style = Style(
        name,
        250,
        opsz=1,
        ital=f.e("qeio", 2),
        wght=f.e("ceio", 4),
        leading=40,
        multiline=True,
        fill=PRIMARY_COLOR,
        features={"ss19": ss19, "ss06": ss06},
    )

    main = (
        P([StSt(t, style) for t in ["GEO", "METRIC", "GROT", "ESQUE"]])
        .reverse()
        .distribute(v=1, tv=True)
        .align(f.a.r)
        .translate(x=0, y=50)
    )
    print(main)
    ot_features = f"Alternate G (ss06) = {'On' if ss06 else 'Off'}\nAlternate R (ss19) = {'On' if ss19 else 'Off'}"
    ot_feat_stst = (
        StSt(
            ot_features,
            mono,
            34,
            wght=0.6,
            leading=20,
            features={"tnum": True, "zero": True},
        )
        .align(f.a.r.inset(30), x="mdx", y="mny")
        .f(SECONDARY_COLOR, 0.6)
    )
    return (*main, ot_feat_stst)


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(grotesque_length, fps=60))
def angle(f):
    angle = f.e("qeio")

    main = (
        StSt("NAME\nSANS", name, 300, opsz=1, ital=angle, wght=0.4, leading=40)
        .f(-1)
        .ro()
        .ssw(PRIMARY_COLOR, f.e("qeio", rng=(0.3, 3)))
        .align(f.a.r.inset(30), x="mnx")
    )

    angle = (
        StSt(
            f"{angle*11.31:05.2f}°",
            name,
            200,
            opsz=1,
            ital=angle,
            features={"tnum": True, "zero": True},
        )
        .f(PRIMARY_COLOR)
        .align(
            f.a.r.inset(30),
            x="mnx",
            y="mny",
        )
    )

    return (main, angle)


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(600, fps=60))
def design_space(f):
    inset = 100

    w, h = 600, 600
    rect = (
        P()
        .roundedRect(Rect(w + 30, h + 30), hr=10)
        .fssw(-1, PRIMARY_COLOR, 6)
        .align(f.a.r.inset(inset), y="mxy")
    )

    w_l = 4
    i_l = 3
    wght_axis = f.e("qeio", w_l)
    ital_axis = f.e("qeio", i_l)

    grid = Grid(
        Rect(w + 30, h + 30).align(f.a.r.inset(inset), y="mxy"),
        "a a a",
        "a a a",
        "1 b c / d e f / g h i",
    )
    squares = [P(grid[c]).fssw(-1, SECONDARY_COLOR, 0.5) for c in "1bcdefghi"]

    dot = (
        P()
        .oval(Rect(30, 30))
        .f(ACCENT_COLOR)
        .align(rect)
        .translate(
            x=f.e("qeio", w_l, rng=(-w / 2, w / 2)),
            y=f.e("qeio", i_l, rng=(-h / 2, h / 2)),
        )
    )

    ital_label = (
        StSt("Italic -->", name, 50, ital=1, wght=0.5, fill=SECONDARY_COLOR)
        .rotate(90)
        .align(rect, x="mnx", y="mny", tx=1, ty=1)
        .translate(x=-50, y=0)
    )
    ital_value = (
        StSt(
            f"{ital_axis:.2f}",
            mono,
            50,
            wght=0.3,
            features={"tnum": True, "zero": True},
        )
        .rotate(90)
        .f(SECONDARY_COLOR, 0.5)
        .align(rect, x="mnx", y="mxy", tx=1, ty=1)
        .translate(x=-50, y=0)
    )
    wght_label = (
        StSt("Weight -->", name, 50, ital=1, wght=0.5, fill=SECONDARY_COLOR)
        .align(rect, x="mnx", y="mny", tx=1, ty=1)
        .translate(x=0, y=-60)
    )
    wght_value = (
        StSt(
            f"{wght_axis*999:06.2f}",
            mono,
            50,
            wght=0.5,
            features={"tnum": True, "zero": True},
        )
        .f(SECONDARY_COLOR, 0.5)
        .align(rect, x="mxx", y="mny", tx=1, ty=1)
        .translate(x=0, y=-50)
    )

    text = StSt(
        "through",
        name,
        130,
        wght=wght_axis,
        ital=ital_axis,
        opsz=1,
        fill=PRIMARY_COLOR,
        features={"ss09": True},
    ).align(f.a.r.inset(inset), y="mny")
    return (rect, text, dot, wght_label, ital_value, wght_value, ital_label, *squares)


# @animation(render_bg=1, bg=BG_COLOR, timeline=midi, audio=wav)
def on_beat(f):
    drums = f.t

    snare = drums.ki(37)
    snare_v, si = snare.adsr(ar["SD"], find=1)

    kick = drums.ki(36)

    perc_1 = drums.ki(46)
    perc_2 = drums.ki(49)
    perc_3 = drums.ki(52)
    perc_4 = drums.ki(58)
    perc_5 = drums.ki(57)
    hh = drums.ki(42)

    string = "Variable"
    if si % 4 == 0:
        string = "Weight"
    elif si % 4 == 1:
        string = "Italic"
    elif si % 4 == 2:
        string = "OPSZ"
    else:
        string = "Variable"

    subdivisions = 10
    subdv_string = (
        "a " * subdivisions
    )  # a is automatic, we create {subdivisions} slots of automatic width and height
    names = [
        str(c) for c in range(subdivisions**2)
    ]  # give each slot a name, programatically
    names_breakdown = " / ".join(
        [
            " ".join(names[i * subdivisions : i * subdivisions + subdivisions])
            for i in range(subdivisions)
        ]
    )  # the result for this operation is a string in the form "1 2 3 / 4 5 6 / 7 8 9" with the rows in between the slashes having exactly {subdivisions} numbers
    # for subdivisions = 3, this would be "1 2 3 / 4 5 6 / 7 8 9"
    # for subdivisions = 4, this would be "1 2 3 4 / 5 6 7 8 / 9 10 11 12 / 13 14 15 16"
    # technically it starts at zero, so everything offset by -1. but you get the point

    grid = Grid(
        Rect(f.a.r).align(f.a.r, y="mxy"), subdv_string, subdv_string, names_breakdown
    )
    squares = [P(grid[(str(c))]).fssw(-1, SECONDARY_COLOR, 0.0) for c in names]

    squares[9].f(PRIMARY_COLOR, perc_3.adsr(ar["HT"]))
    squares[15].f(PRIMARY_COLOR, perc_2.adsr(ar["KD"]))
    squares[40].f(PRIMARY_COLOR, perc_1.adsr(ar["KD"]))
    squares[79].f(PRIMARY_COLOR, perc_4.adsr(ar["KD"]))
    squares[32].f(PRIMARY_COLOR, perc_5.adsr(ar["KD"]))
    squares[np.random.randint(0, subdivisions**2)].f(
        SECONDARY_COLOR, hh.adsr(ar["HT"])
    )

    main = (
        StSt(
            string,
            name,
            300,
            opsz=1,
            wght=kick.adsr(ar["KD"], rng=(0.1, 0.9)) + snare_v,
            ital=snare_v,
            features={"ss10": True},
            ro=1,
            tu=-70,
        )
        .align(f.a.r)
        .f(ACCENT_COLOR, snare.adsr(ar["SD"]))
        .ssw(PRIMARY_COLOR, kick.adsr(ar["SD"], rng=(1, 3)))
    )

    return (*squares, main)


def release(passes):
    FFMPEGExport(design_space, passes).prores().write().open()
