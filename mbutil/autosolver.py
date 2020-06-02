from time import sleep

from bs4 import BeautifulSoup

from mbutil.mathml import MATHML
from mbutil.util import get_webdriver, open_page, select_task, mb_login, open_browser

from selenium.webdriver.common.keys import Keys


class AutoSolver:
    def __init__(self, battle_url_extension: str, task: int):
        self.browser = await open_browser()
        self.extension = battle_url_extension
        self.task = task

    def __login(self):
        mb_login(self.browser)

    def start(self) -> BeautifulSoup:
        # Login
        self.__login()
        # Open battle page
        page = open_page(self.browser, self.extension)
        sleep(1)
        # Open task
        
        battle_page = select_task(page, self.task)
        sleep(1)


        soup = BeautifulSoup(div.get_attribute("innerHTML"), "html.parser")
        return soup

