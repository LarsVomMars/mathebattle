from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import sanitize_input, round_res


class Solver:
    @staticmethod
    def __solver(function_f, function_g):
        x = Symbol("x")
        poi2_fg = solve(function_f - function_g, x)[1]
        zero2_g = solve(function_g)[1]
        area_between_curves = integrate(function_f - function_g, (x, 0, poi2_fg)) - abs(
            integrate(function_g, (x, 0, zero2_g)))
        return round_res(area_between_curves)

    @staticmethod
    def cli():
        function_f = sympify(sanitize_input(input("Function f(x)=")))
        function_g = sympify(sanitize_input(input("Function g(x)=")))
        print(f"Result: {Solver.__solver(function_f, function_g)}")

    @staticmethod
    def autosolve():
        load_dotenv()
        mml = MATHML()
        task = 2
        auto_solver = AutoSolver(config.BATTLE_1_EXTENSION, task)
        while True:
            div = auto_solver.start()
            math_elements = div.find_all('math')
            f = sympify(mml.parse(math_elements[1]))
            g = sympify(mml.parse(math_elements[3]))
            res = Solver.__solver(f, g)
            auto_solver.send(res)
