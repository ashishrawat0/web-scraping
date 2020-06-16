import requests
from bs4 import BeautifulSoup
res = requests.get(
    'https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(res.text, 'lxml')
title = soup.select('.mw-headline')
for i in soup.select('.mw-headline'):
    print(i.text)
