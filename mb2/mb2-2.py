from sympy import *

x = Symbol('x')

f = sympify(input("Function f(x): ").replace("^", "**")) #-0.5*x**2+3*x+3
g = sympify(input("Function g(x): ").replace("^", "**")) # x**2-9
gf2 = list(solveset(f-g, x))[1]
g2 = list(solveset(g, x))[1]

res = integrate(f-g, (x, 0, gf2)) - abs(integrate(g, (x, 0, g2)))
print(res)
