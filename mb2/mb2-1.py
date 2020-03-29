from sympy import Symbol, sympify, integrate
from sympy.solvers import solve

x = Symbol('x')

b = sympify(input("Right limit: ")) # l2
c = sympify(input("Upper limit: ")) # ul
f = sympify(input("Function: ").replace("e", "E").replace("^", "**")) # function

a = solve(f-c,x)[-1]
FI = integrate(c-f, (x, a, b))
res = b*c - FI
print(res)
