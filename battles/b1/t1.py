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
    async def autosolve():
        mml = MATHML()
        auto_solver = AutoSolver(config.BATTLE_1_EXTENSION, 1)
        while True:
            div = await auto_solver.start()
            math_elements = await div.J('math')
            f = sympify(mml.parse(math_elements[0]))
            g = sympify(mml.parse(math_elements[1]))
            res = Solver.__solver(f, g)
            await (await div.J('input[type=text]')).type(res)
