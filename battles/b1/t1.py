from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(f, g):
        x = Symbol("x")
        x1, x2 = solve(f - g, x)
        area = integrate(f - g, (x, x1, x2))
        return round_res(area)

    @staticmethod
    def cli():
        f = sympify(sanitize_input(input("f(x)=")))
        g = sympify(sanitize_input(input("g(x)=")))
        print(f"Result: {Solver.__solver(f, g)}")

    @staticmethod
    def autosolve():
        # TODO: Implement
        raise NotImplementedError("TODO")
