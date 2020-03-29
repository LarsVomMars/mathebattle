from sympy import Symbol, integrate, diff, sympify, N
from sympy.solvers import solve

# function for autosaver
def mb3(fp, x0p):
    x = Symbol('x')

    f = sympify(fp) # -1/3*x^2 + 16/3
    x0 = sympify(x0p)
    fs = diff(f)
    T = fs.subs(x, x0) * (x - x0) + f.subs(x, x0)

    f1 = list(solve(f, x))[1]
    t1 = list(solve(T, x))[0]
    ft = list(solve(f-T, x))[0]

    TI = integrate(T, (x, ft, t1))
    FI = integrate(f, (x, ft, f1))

    res = TI - abs(FI)
    return N(res).round(2)
