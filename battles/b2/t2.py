import time

from bs4 import BeautifulSoup
from sympy import sympify, integrate, Symbol
from sympy.solvers import solve

from mbutil.mathml import MATHML
from mbutil.util import sanitize_input, round_res, get_webdriver, open_page, select_task

from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv
load_dotenv()


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
        mml = MATHML()
        driver = get_webdriver()
        open_page(driver)
        battle_url_extension = "9718"
        while True:
            open_page(driver, battle_url_extension)
            time.sleep(1)
            select_task(driver, 2)
            time.sleep(1)

            div = driver.find_element_by_class_name("exercise_question")
            soup = BeautifulSoup(div.get_attribute("innerHTML"), "html.parser")

            p = soup.p

            math_elems = p.find_all("math")
            f = sympify(mml.parse(math_elems[1]))
            g = sympify(mml.parse(math_elems[3]))

            solution = Solver.__solver(f, g)

            inp = driver.find_element_by_class_name("value_form").find_element_by_tag_name("input")
            inp.send_keys(solution)
            inp.send_keys(Keys.RETURN)
            time.sleep(1)
