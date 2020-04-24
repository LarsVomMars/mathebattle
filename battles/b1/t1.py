from dotenv import load_dotenv
from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

from mbutil.autosolver import AutoSolver
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
        raise NotImplementedError("Currently working on :)")
        load_dotenv()
        battle_url_extension = "8518"
        task = 1
        auto_solver = AutoSolver(battle_url_extension, task, [0, 1])
        while True:
            # Why the heck are they using different page layouts
            elms = auto_solver.start()
            f = sympify(elms[0])
            g = sympify(elms[1])
            res = Solver.__solver(f, g)
            auto_solver.send(res)
