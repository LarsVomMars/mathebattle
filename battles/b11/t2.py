from mathew.geometry import Vector, Point

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import create_point


class Solver:
    @staticmethod
    def __solver(p1: Point, p2: Point, p3: Point):
        ab = Vector.from_points(p1, p2)
        ac = Vector.from_points(p1, p3)
        area = abs(ab.cross(ac)) / 2
        return area

    @staticmethod
    def cli():
        A = create_point(input("A[x,y,z]="))
        B = create_point(input("B[x,y,z]="))
        C = create_point(input("C[x,y,z]="))
        print(f"Result: {Solver.__solver(A, B, C)}")

    @staticmethod
    def autosolve():
        raise NotImplementedError()
