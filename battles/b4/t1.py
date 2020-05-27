from dotenv import load_dotenv
from larsmathlib.geometry import Vector, Point
from math import sqrt

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import round_res, create_vector, create_point


class Solver:
    @staticmethod
    def __solver(p1: Point, p2: Point, p3: Point):
        u = Vector.from_points(p2, p3) # create vector between B and C
        D = p1 + u # Add vector to A -> D
        return D


    @staticmethod
    def cli():
        A = create_point(input("A[x,y,z]="))
        B = create_point(input("B[x,y,z]="))
        C = create_point(input("C[x,y,z]="))
        print(f"Result: {Solver.__solver(A, B, C)}")


    @staticmethod
    def autosolve():
        raise NotImplementedError()