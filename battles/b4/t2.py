from dotenv import load_dotenv
from mathew.geometry import Vector
from math import sqrt

import config
from mbutil.autosolver import AutoSolver
from mbutil.mathml import MATHML
from mbutil.util import round_res, create_vector


class Solver:
    @staticmethod
    def __solver(v1: Vector, v2: Vector):
        res = .5 * (v1+v2)
        return res


    @staticmethod
    def cli():
        a = create_vector(input("A[x,y,z]="))
        c = create_vector(input("C[x,y,z]="))
        print(f"Result: {Solver.__solver(a, c)}")


    @staticmethod
    def autosolve():
        raise NotImplementedError()
