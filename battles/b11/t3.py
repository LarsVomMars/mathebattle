from mathew.geometry import Vector, Point

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import create_point


class Solver:
    @staticmethod
    def __solver(p1: Point, p2: Point, p4: Point, p5: Point):
        ab = Vector.from_points(p1, p2)
        ad = Vector.from_points(p1, p4)
        az = Vector.from_points(p1, p5)
        G = ab.cross(ad)
        volume = abs(G.dot(az)) / 3
        return volume

    @staticmethod
    def cli():
        A = create_point(input("A[x,y,z]="))
        B = create_point(input("B[x,y,z]="))
        D = create_point(input("D[x,y,z]="))
        S = create_point(input("S[x,y,z]="))
        print(f"Result: {Solver.__solver(A, B, D, S)}")

    @staticmethod
    def autosolve():
        raise NotImplementedError()
