from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol, pi
from sympy.solvers import solve

from mbutil.autosolver import AutoSolver
from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(f, a, b):
        x = Symbol("x")
        volume = pi * integrate(f**2, (x, a, b))
        return round_res(volume)

    @staticmethod
    def cli():
        f = sympify(sanitize_input(input("f(x)=")))
        a = sympify(sanitize_input(input("a=")))
        b = sympify(sanitize_input(input("b=")))
        print(f"Result: {Solver.__solver(f, a, b)}")

    @staticmethod
    def autosolve():
        raise NotImplementedError("Not implemented yet")
