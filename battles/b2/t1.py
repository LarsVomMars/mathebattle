from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(rl, ul, function):
        x = Symbol("x")
        point_of_intersection = solve(function - ul, x)
        area = integrate(ul - function, (x, point_of_intersection, rl))
        area_under_curve = rl * ul - area
        return round_res(area_under_curve)

    @staticmethod
    def cli():
        rl = sympify(input("Right limit: "))
        ul = sympify(input("Upper limit: "))
        function = sympify(sanitize_input(input("Function f(x)=")))
        print(f"Result: {Solver.__solver(rl, ul, function)}")

    @staticmethod
    def autosolve():
        print("Cannot use autosolver due to unknown parameters!")
