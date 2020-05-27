from dotenv import load_dotenv
from larsmathlib.geometry import Point
from math import sqrt

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import round_res, create_point


class Solver:
    @staticmethod
    def __solver(p1 :Point, p2 :Point, p3 :Point):
        def calculate(sl: float, base: float) -> float:
            # a2 + b2 = c2 -> c2 - a2 = b2
            height = sqrt(sl ** 2 - (.5 * base) ** 2)
            return .5 * height * base

        
        a = p1.distance(p2)
        b = p2.distance(p3)
        c = p3.distance(p1)

        # Check which sides have the same length
        if a == b:
            res = calculate(a, c)
        elif b == c:
            res = calculate(b, a)
        elif c == a:
            res = calculate(c, b)
        else:
            return "Cannot calulate .. :)"
        
        return round_res(res)


    @staticmethod
    def cli():
        A = create_point(input("A[x,y,z]="))
        B = create_point(input("B[x,y,z]="))
        C = create_point(input("C[x,y,z]="))
        print(f"Result: {Solver.__solver(A, B, C)}")


    @staticmethod
    def autosolve():
        raise NotImplementedError()