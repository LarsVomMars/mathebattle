from sympy import N


def sanitize_input(eq: str):
    return eq.replace("^", "**").replace("e", "E")


def round_res(res):
    return N(res).round(2)
