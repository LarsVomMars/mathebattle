from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
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
        load_dotenv()
        mml = MATHML()
        task = 1
        auto_solver = AutoSolver(config.BATTLE_1_EXTENSION, task)
        while True:
            div = auto_solver.start()
            math_elements = div.find_all('math')
            f = sympify(mml.parse(math_elements[0]))
            g = sympify(mml.parse(math_elements[1]))
            res = Solver.__solver(f, g)
            auto_solver.send(res)
