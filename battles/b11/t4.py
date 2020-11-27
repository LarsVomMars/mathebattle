from mathew.geometry import Vector, Point

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import create_point


class Solver:
    @staticmethod
    def __solver(p1: Point, p2: Point, p3: Point, p4: Point):
        ab = Vector.from_points(p1, p2)
        ac = Vector.from_points(p1, p3)
        az = Vector.from_points(p1, p4)
        G = ab.cross(ac)
        volume = abs(G.dot(az)) / 6
        return volume

    @staticmethod
    def cli():
        A = create_point(input("A[x,y,z]="))
        B = create_point(input("B[x,y,z]="))
        C = create_point(input("C[x,y,z]="))
        S = create_point(input("S[x,y,z]="))
        print(f"Result: {Solver.__solver(A, B, C, S)}")

    @staticmethod
    def autosolve():
        raise NotImplementedError()
