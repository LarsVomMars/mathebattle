# utility functions

from bs4 import BeautifulSoup
from mb2_3 import mb3
import time
import re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


def parse_mfrac(mfrac) -> str:
    mns = mfrac.find_all("mn")
    num = mns[0].string
    den = mns[1].string
    return f"{num}/{den}"


def parse_msup(msup) -> str:
    base = msup.mi.string
    exp = msup.mn.string
    return f"{base}**{exp}"


def parse_mo(mo) -> str:
    return mo.string


def parse_graph(math) -> str:
    mrow_childs = math.mrow.findChildren("mrow", recursive=False)
    eq = ""
    for eq_parts in mrow_childs:
        ctr = 0
        extra_part = eq_parts.findChildren("mo", recursive=False)
        if len(extra_part) == 1:
            eq += extra_part[0].string
        for part in eq_parts.findChildren("mrow", recursive=False):
            for part_val in part:
                if part_val.name == "mo":
                    eq += f"{part_val.string}1*"
                elif part_val.name == "mn":
                    eq += part_val.string
                elif part_val.name == "mfrac":
                    if ctr == 0:
                        eq += "+"
                    eq += f"{parse_mfrac(part_val)}"
                elif part_val.name == "msup":
                    if ctr >= 1:
                        eq += "*"
                    eq += f"{parse_msup(part_val)}"
            ctr += 1
    eq = eq.replace("*+", "*").replace("+*", "*")
    return eq


def parse_x0(mrow) -> str:
    c = mrow.find_all("mn")
    print(len(c), c)
    if len(c) == 1:
        return int(c[0].string)
    return f"{c[0].string}/{c[1].string}"


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