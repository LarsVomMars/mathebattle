"""
Python parser for the MathML spec - at least the parts I need atm
https://www.w3.org/TR/REC-MathML/chap3_1.html
"""

# TODO: Debug stuff


from bs4 import BeautifulSoup
from bs4.element import Tag, PageElement

from mbutil.util import sanitize_input


class MATHML:
    def __init__(self):
        self.__methods = {
            "mi": self.__m,
            "mn": self.__m,
            "mo": self.__m,
            "mrow": self.__mrow,
            "mfrac": self.__mfrac,
            "msup": self.__msup,
        }

    def __validate_html(self, html: str) -> bool:
        try:
            return bool(BeautifulSoup(html, "html.parser").find())
        except Exception as e:
            return False

    def __add_ast(self, eq: str, np: str) -> str:
        return "*" if len(eq) > 1 and eq[-1] not in "+-*/" or len(np) > 1 and np[0] not in "+-*/" else ""

    def __m(self, m: Tag) -> str:
        return m.string.strip()

    def __mfrac(self, mfrac: Tag) -> str:
        eq = ""  # a/b
        # Method valid for two children …
        for child in mfrac.children:
            if self.__validate_html(str(child)):
                if len(eq) == 0:
                    num = self.__methods[child.name](child)
                    eq += "(" + (f"({num})" if len(num) > 1 else f"{num}")
                else:
                    den = self.__methods[child.name](child)
                    eq += "/" + (f"({den})" if len(den) > 1 else f"{den}") + ")"
        return eq.strip()

    def __msup(self, msup: Tag) -> str:
        eq = ""  # a**b
        # Method valid for two children …
        for child in msup.children:
            if self.__validate_html(str(child)):
                if len(eq) == 0:
                    base = self.__methods[child.name](child)
                    eq += f"({base})" if len(base) > 1 else f"{base}"
                else:
                    exp = self.__methods[child.name](child)
                    eq += "**" + (f"({exp})" if len(exp) > 1 else f"{exp}")
        return eq.strip()

    def __mrow(self, mrow: Tag) -> str:
        eq = ""
        for child in mrow.children:
            if self.__validate_html(str(child)):
                next_part = self.__methods[child.name](child)
                eq += self.__add_ast(eq, next_part) + next_part
        return eq.strip()

    def parse(self, math: PageElement) -> str:
        eq = ""
        for child in math.children:
            if self.__validate_html(str(child)):
                next_part = self.__methods[child.name](child)
                eq += self.__add_ast(eq, next_part) + next_part
        return sanitize_input(eq)
