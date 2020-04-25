from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
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
        raise NotImplementedError('Currently working on')
        load_dotenv()
        mml = MATHML()
        task = 2
        auto_solver = AutoSolver(config.BATTLE_1_EXTENSION, task)
        while True:
            div = auto_solver.start()
            math_elements = div.find_all('math')
            f = sympify(mml.parse(math_elements[1]))
            g = sympify(mml.parse(math_elements[3]))
            p = div.find_all('p')[1].text # TODO: I don't want

            res = Solver.__solver(f, g)
            auto_solver.send(res)
