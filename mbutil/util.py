import re
import time
from time import sleep
from os import getenv as ge

from selenium import webdriver
from sympy import N

from mathew.geometry import Point, Vector
# import webbrowser

import asyncio

from pyppeteer import launch

def sanitize_input(eq: str):
    return eq.replace("^", "**").replace("e", "E")


def round_res(res) -> str:
    return str(N(res).round(2))


async def mb_login(browser):
    page = await browser.newPage()
    await page.goto('https://mathebattle.de/users/login')
    sleep(1)
    await (await page.querySelector('#UserUsername')).type(ge("MB_USERNAME"))
    await (await page.querySelector('#UserPassword')).type(ge("MB_PASSWORD"))
    await (await page.querySelector('.submit input')).click()
    return page


async def open_browser():
    return await launch(headless=True if ge('MB_HEADLESS', 'False') == 'True' else False)


async def open_page(page, url_ext: str):
    await page.goto(f"https://mathebattle.de/edu_battles/start/{url_ext}")
    sleep(2)
    return page


async def select_task(page, num: int):
    inputs = await page.J('#EduBattleStartForm input')
    await inputs[1 + num].click()
    await inputs[-1].click()
    await page.waitForNavigation()
    return page


def create_point(s: str) -> Point:
    split = s.split(',')
    return Point(float(split[0]), float(split[1]), float(split[2]))


def create_vector(s: str) -> Vector:
    split = s.split(',')
    return Vector(float(split[0]), float(split[1]), float(split[2]))
