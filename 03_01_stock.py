import requests
from bs4 import BeautifulSoup

codes = ['005930','000660','035720']
for code in codes:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={code}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    val = soup.select_one("#_nowVal").text.replace(',','')
    print(val)