from sympy import N

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import re
import time


def sanitize_input(eq: str):
    return eq.replace("^", "**").replace("e", "E")


def round_res(res):
    return N(res).round(2)


def open_page(driver):
    driver.get("https://mathebattle.de")
    while re.match("http[s]://mathebattle.de/edu_battles/start/[0-9]{4}", driver.current_url) == None:
        time.sleep(1)
    # time.sleep(1)
    return driver.current_url


def get_webdriver():
    # TODO: Driver for other browsers ..
    binary = FirefoxBinary("/usr/bin/firefox")
    driver = webdriver.Firefox(firefox_binary=binary)
    return driver
