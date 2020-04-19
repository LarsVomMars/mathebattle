from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(f, g, a, b):
        x = Symbol("x")
        area = 0
        fg = f - g
        nss = solve(fg, x)
        points = [a] + [n for n in nss if a < n < b] + [b]
        pl = len(points)
        for i in range(pl):
            if i < pl - 1:
                area += abs(integrate(fg, (x, points[i], points[i + 1])))
        return round_res(area)

    @staticmethod
    def cli():
        f = sympify(sanitize_input(input("f(x)=")))
        g = sympify(sanitize_input(input("g(x)=")))
        a = sympify(sanitize_input(input("a=")))
        b = sympify(sanitize_input(input("b=")))
        print(f"Result: {Solver.__solver(f, g, a, b)}")

    @staticmethod
    def autosolve():
        # TODO: Implement
        raise NotImplementedError("TODO")
