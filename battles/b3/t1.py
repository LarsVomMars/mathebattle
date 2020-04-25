from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol, pi

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(f, a, b):
        x = Symbol("x")
        volume = pi * integrate(f ** 2, (x, a, b))
        return round_res(volume)

    @staticmethod
    def cli():
        f = sympify(sanitize_input(input("f(x)=")))
        a = sympify(sanitize_input(input("a=")))
        b = sympify(sanitize_input(input("b=")))
        print(f"Result: {Solver.__solver(f, a, b)}")

    @staticmethod
    def autosolve():
        load_dotenv()
        mml = MATHML()
        task = 1
        auto_solver = AutoSolver(config.BATTLE_3_EXTENSION, task)
        while True:
            div = auto_solver.start()
            math_elements = div.find_all('math')
            f = sympify(mml.parse(math_elements[1]))
            splits = str(div.p).split('[')[-1].split(']')[0].split(',')
            print(splits)
            a, b = [sympify(sanitize_input(i)) for i in splits]
            res = Solver.__solver(f, a, b)
            auto_solver.send(res)
