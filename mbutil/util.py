import re
import time

from os import getenv as ge

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from sympy import N


def sanitize_input(eq: str):
    return eq.replace("^", "**").replace("e", "E")


def round_res(res) -> str:
    return str(N(res).round(2))


def open_page(driver, url_ext: str = None):
    if url_ext is None:
        driver.get("https://mathebattle.de/users/login")
        time.sleep(.5)
        login(driver)
        while re.match("http[s]://mathebattle.de/users/login", driver.current_url) is not None:
            time.sleep(1)
    else:
        driver.get(f"https://mathebattle.de/edu_battles/start/{url_ext}")
    time.sleep(1)


def get_webdriver():
    # TODO: Driver for other browsers …
    # TODO: None Linux compatibility
    binary = FirefoxBinary("/usr/bin/firefox")
    driver = webdriver.Firefox(firefox_binary=binary)
    return driver


def select_task(driver, num: int):
    form = driver.find_element_by_id("EduBattleStartForm")
    sel = form.find_elements_by_tag_name("input")
    sel[1 + num].click()
    sel[5].click()


def login(driver):
    driver.find_element_by_id("UserUsername").send_keys(ge("MB_USERNAME"))
    driver.find_element_by_id("UserPassword").send_keys(ge("MB_PASSWORD"))
    driver.find_element_by_class_name("submit").find_element_by_tag_name("input").click()
