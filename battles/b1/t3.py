from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(f, a, b):
        x = Symbol("x")
        area = 0
        nss = solve(f, x)
        points = [a] + [n for n in nss if a < n < b] + [b]
        pl = len(points)
        for i in range(pl):
            if i < pl - 1:
                area += abs(integrate(f, (x, points[i], points[i + 1])))
        return round_res(area)

    @staticmethod
    def cli():
        f = sympify(sanitize_input(input("f(x)=")))
        a = sympify(sanitize_input(input("a=")))
        b = sympify(sanitize_input(input("b=")))
        print(f"Result: {Solver.__solver(f, a, b)}")

    @staticmethod
    def autosolve():
        # Check if script tags contain data
        raise NotImplementedError('Currently working on')