from sympy import sympify, integrate, Symbol, diff
from sympy.solvers import solve

from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(function_f, poi_t):
        x = Symbol("x")
        diff_f = diff(function_f)
        tangent = diff_f.subs(x, poi_t) * (x - poi_t) + function_f.subs(x, poi_t)

        zero1_f = solve(function_f, x)[1]
        zero0_t = solve(tangent, x)[0]
        poi_ft = solve(function_f - tangent, x)[0]

        area = integrate(tangent, (x, poi_ft, zero0_t)) - abs(integrate(function_f, (x, poi_ft, zero1_f)))
        return round_res(area)

    @staticmethod
    def cli():
        function_f = sympify(sanitize_input(input("Function f(x)=")))
        poi_t = sympify(input("x0 of tangent: "))
        print(f"Result: {Solver.__solver(function_f, poi_t)}")

    @staticmethod
    def autosolve():
        pass
