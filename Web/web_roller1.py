from pyweb import pydom

page_message = "Testing output"


def roll(event):
    pydom["p#output"].html = page_message
