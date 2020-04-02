"""
Python parser for the MathML spec - at least the parts I need atm
https://www.w3.org/TR/REC-MathML/chap3_1.html
"""

# TODO: Debug stuff


from bs4 import BeautifulSoup
from bs4.element import Tag, PageElement


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

    def __add_ast(self, eq: str):
        return ("*" if eq[-1] not in "+-*/" else "") if len(eq) > 1 else ""

    def __m(self, m: Tag) -> str:
        return m.string

    def __mfrac(self, mfrac: Tag) -> str:
        eq = ""  # a/b
        # Method valid for two children …
        for child in mfrac.children:
            if self.__validate_html(str(child)):
                if len(eq) == 0:
                    num = self.__methods[child.name](child)
                    eq += f"({num})" if len(num) > 1 else f"{num}"
                else:
                    den = self.__methods[child.name](child)
                    eq += "/" + (f"({den})" if len(den) > 1 else f"{den}")
        return eq

    def __msup(self, msup: Tag) -> str:
        eq = ""  # a**b
        # Method valid for two children …
        for child in msup.children:
            if self.__validate_html(str(child)):
                if len(eq) == 0:
                    num = self.__methods[child.name](child)
                    eq += f"({num})" if len(num) > 1 else f"{num}"
                else:
                    den = self.__methods[child.name](child)
                    eq += "**" + (f"({den})" if len(den) > 1 else f"{den}")
        return eq

    def __mrow(self, mrow: Tag) -> str:
        eq = ""
        for child in mrow.children:
            if self.__validate_html(str(child)):
                eq += self.__add_ast(eq) + self.__methods[child.name](child)
        return eq

    def parse(self, math: PageElement) -> str:
        eq = ""
        for child in math.children:
            if self.__validate_html(str(child)):
                eq += self.__add_ast(eq) + self.__methods[child.name](child)
        return eq