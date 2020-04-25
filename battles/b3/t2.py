from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol, pi
from sympy.solvers import solve

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(f, a, b):
        x = Symbol("x")
        volume = (1/(b-a)) * integrate(f, (x, a, b))
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
        load_dotenv()
        mml = MATHML()
        task = 2
        auto_solver = AutoSolver(config.BATTLE_3_EXTENSION, task)
        while True:
            div = auto_solver.start()
            math_elements = div.find_all('math')
            f = sympify(mml.parse(math_elements[1]))
            a, b = [sympify(sanitize_input(i)) for i in div.p.split('[')[-1].split(']')[0].split(',')]
            res = Solver.__solver(f, a, b)
            auto_solver.send(res)
