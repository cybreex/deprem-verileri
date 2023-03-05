# Coded by Yusuf Kibar
# .-. coding: utf-8 .-.

import colorama
from colorama import Fore
import bs4
from bs4 import BeautifulSoup
import requests

url = "http://www.koeri.boun.edu.tr/scripts/lst4.asp"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
pre = soup.find("pre")
text = pre.text
liste = text.split("\n")
print("\n".join(liste[4:8]))
