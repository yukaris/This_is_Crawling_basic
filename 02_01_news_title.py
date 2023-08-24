import requests
from bs4 import BeautifulSoup
# 네이버에서 삼성전자 검색 후 뉴스 탭 결과
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")    # 클래스 선택자 news_tit

for link in links:
    title = link.text
    url = link.attrs['href']  # 링크 주소
    print(title, url)