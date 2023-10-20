from defcon import Features
import numpy as np
from coldtype import *

name = Font.Cacheable("~/fonts/variable/NameSans.ttf")

length = 100

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
def eszett(f):
    return (
        StSt(
            "ß",
            name,
            800,
            opsz=1,
            ital=f.e("qeio"),
            wght=f.e("qeio"),
            leading=60,
            multiline=True,
            features={"ss15": True, "titl": True},
        )
        .f(PRIMARY_COLOR)
        .removeOverlap()
        # .outline(offset=3.5)
        .align(f.a.r)
    )


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(length, fps=60))
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
                ).rotate(45 * np.cos((i / (n * 5)) * (f.i / 10)))
                for i in range(n)
            ]
        )
        .grid(every=np.sqrt(n))
        .translate(x=30, transformFrame=False)
    )

    return arrows


@animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(length, fps=60))
def numbers(f):
    def map_color(i):
        if i == math.isqrt(i) ** 2:
            return ACCENT_COLOR
        elif i % 2 == 0:
            return PRIMARY_COLOR
        else:
            return SECONDARY_COLOR

    ot_features = f"Tabular Numbers (tnum) \nSlashed Zero (zero)"
    ot_feat_stst = (
        StSt(
            ot_features,
            name,
            20,
            opsz=0.1,
            wght=0.5,
            leading=10,
            features={"tnum": True, "zero": True},
        )
        .align(f.a.r.inset(30), x="mnx", y="mxy")
        .f(SECONDARY_COLOR, 0.4)
    )

    n = 9**2
    numbers = (
        PS(
            [
                StSt(
                    f"{i+1:02d}",
                    name,
                    94,
                    opsz=0.7,
                    # wght=np.cos(100 + (f.i / 100) * (i / 9)),
                    wght=i / n - f.e("ceio"),
                    fill=map_color(i + 1),
                    features={"tnum": True, "zero": True},
                )
                for i in range(n)
            ]
        )
        .grid(every=np.sqrt(n))
        .lead(30)
        .align(f.a.r.inset(50), x="mdx", y="mny")
    )

    return (numbers, ot_feat_stst)


# @animation(render_bg=1, bg=BG_COLOR, timeline=Timeline(length, fps=60))
def grotesque(f):

    ss19 = True if f.i > length // 2 else False
    ss06 = True if f.i > length // 2 else False
    main = (
        StSt(
            "GRO\nTES\nQUE",
            name,
            300,
            opsz=1,
            ital=f.e("qeio", 2),
            wght=f.e("ceio", 4),
            leading=40,
            multiline=True,
            features={"ss19": ss19, "ss06": ss06},
        )
        .f(PRIMARY_COLOR)
        .removeOverlap()
        # .outline(offset=3.5)
        .align(f.a.r)
    )
    ot_features = f"Alternate G (ss06) = {'On' if ss06 else 'Off'}\nAlternate R (ss19) = {'On' if ss19 else 'Off'}"
    ot_feat_stst = (
        StSt(
            ot_features,
            name,
            30,
            opsz=0.2,
            leading=20,
            features={"tnum": True, "zero": True},
        )
        .align(f.a.r.inset(30), x="mnx", y="mny")
        .f(SECONDARY_COLOR, 0.4)
    )
    return (main, ot_feat_stst)


def release(passes):
    FFMPEGExport(arrow, passes).prores().write()
