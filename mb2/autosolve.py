# utility functions

from bs4 import BeautifulSoup
from mb2.mb2_3 import mb3
import time
import re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from mbutil.utility import *

binary = FirefoxBinary("/usr/bin/firefox")

driver = webdriver.Firefox(firefox_binary=binary)
driver.get("https://mathebattle.de/")


while True:
    # Wait for URL to change be a battle URL
    while re.match("http[s]://mathebattle.de/edu_battles/start/[0-9]{4}", driver.current_url) == None:
        time.sleep(1)

    time.sleep(1)

    URL = driver.current_url

    form = driver.find_element_by_id("EduBattleStartForm")
    sel = form.find_elements_by_tag_name("input")
    sel[4].click()  # select 3
    sel[5].click()  # submit form

    time.sleep(1)

    div = driver.find_element_by_class_name("exercise_question")

    soup = BeautifulSoup(div.get_attribute("innerHTML"), features="html.parser")
    g, t, _ = soup.find_all("p")

    termElem = g.find_all("math")[1]
    f = parse_graph(termElem)
    x0 = parse_x0(t.mrow)

    print(f, x0)

    res = str(mb3(f, x0))

    print(res)
    time.sleep(1)

    inp = driver.find_element_by_class_name("value_form").find_element_by_tag_name("input")
    inp.send_keys(res)

    while not (re.match("http[s]://mathebattle.de/edu_battles/play", driver.current_url) == None):
        time.sleep(1)

    driver.get(URL)