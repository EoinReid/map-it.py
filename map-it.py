#! python3
import webbrowser
import pyperclip
import sys
import urllib.parse

address = ""

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

url_address = urllib.parse.quote_plus(address)

webbrowser.open("https://www.google.ie/maps/search/?api=1&query=" +url_address)
