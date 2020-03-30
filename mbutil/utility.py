
def parse_mfrac(mfrac) -> str:
    mns = mfrac.find_all("mn")
    num = mns[0].string
    den = mns[1].string
    return f"{num}/{den}"


def parse_msup(msup) -> str:
    base = msup.mi.string
    exp = msup.mn.string
    return f"{base}**{exp}"


def parse_mo(mo) -> str:
    return mo.string


def parse_graph(math) -> str:
    mrow_childs = math.mrow.findChildren("mrow", recursive=False)
    eq = ""
    for eq_parts in mrow_childs:
        ctr = 0
        extra_part = eq_parts.findChildren("mo", recursive=False)
        if len(extra_part) == 1:
            eq += extra_part[0].string
        for part in eq_parts.findChildren("mrow", recursive=False):
            for part_val in part:
                if part_val.name == "mo":
                    eq += f"{part_val.string}1*"
                elif part_val.name == "mn":
                    eq += part_val.string
                elif part_val.name == "mfrac":
                    if ctr == 0:
                        eq += "+"
                    eq += f"{parse_mfrac(part_val)}"
                elif part_val.name == "msup":
                    if ctr >= 1:
                        eq += "*"
                    eq += f"{parse_msup(part_val)}"
            ctr += 1
    eq = eq.replace("*+", "*").replace("+*", "*")
    return eq


def parse_x0(mrow) -> str:
    c = mrow.find_all("mn")
    print(len(c), c)
    if len(c) == 1:
        return int(c[0].string)
    return f"{c[0].string}/{c[1].string}"
