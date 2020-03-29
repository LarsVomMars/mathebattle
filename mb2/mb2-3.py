from sympy import Symbol, integrate, diff, sympify, N
from sympy.solvers import solve

# Simple cli

x = Symbol('x')

f = sympify(input("Function f(x): ").replace("^", "**")) # -1/3*x^2 + 16/3
x0 = sympify(input("Tangent point: "))
fs = diff(f)
T = fs.subs(x, x0) * (x - x0) + f.subs(x, x0)

f1 = list(solve(f, x))[1]
t1 = list(solve(T, x))[0]
ft = list(solve(f-T, x))[0]

TI = integrate(T, (x, ft, t1))
FI = integrate(f, (x, ft, f1))

res = TI - abs(FI)
print(N(res))
print(N(res).round(2))
