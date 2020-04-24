from time import sleep

from bs4 import BeautifulSoup

from mbutil.mathml import MATHML
from mbutil.util import get_webdriver, open_page, select_task

from selenium.webdriver.common.keys import Keys


class AutoSolver:
    def __init__(self, battle_url_extension: str, task: int, element_nums: list):
        self.__mml = MATHML()
        self.__driver = get_webdriver()
        self.__bue = battle_url_extension
        self.__task = task
        self.__element_nums = element_nums
        self.__login()

    def __login(self):
        open_page(self.__driver)  # Login

    def start(self):
        open_page(self.__driver, self.__bue)  # Open battle
        sleep(1)
        select_task(self.__driver, self.__task)  # Select task
        sleep(1)

        div = self.__driver.find_element_by_class_name("exercise_question")
        soup = BeautifulSoup(div.get_attribute("innerHTML"), "html.parser")
        math_elements = soup.find_all("math")

        return [self.__mml.parse(math_elements[i]) for i in self.__element_nums]

    def send(self, result):
        inp = self.__driver.find_element_by_class_name("value_form").find_element_by_tag_name("input")
        inp.send_keys(result)
        inp.send_keys(Keys.RETURN)
        sleep(1)
