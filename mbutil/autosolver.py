from time import sleep

from bs4 import BeautifulSoup

from mbutil.mathml import MATHML
from mbutil.util import open_page, select_task, mb_login, open_browser

from selenium.webdriver.common.keys import Keys


class AutoSolver:
    def __init__(self, battle_url_extension: str, task: int):
        self.extension = battle_url_extension
        self.task = task

    async def __login(self):
        self.browser = await open_browser()
        self.page = await mb_login(self.browser)

    async def start(self):
        # Login
        await self.__login()
        # Open battle page
        self.page = await open_page(self.page, self.extension)
        sleep(1)

        # Open task
        return await select_task(self.page, self.task)