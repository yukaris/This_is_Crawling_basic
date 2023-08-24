import requests
from bs4 import BeautifulSoup
import pyautogui
import time

# 크롤링 탐지 정책으로 페잇와 크롤링 뉴스 순서 차이 발생 가능
# time.sleep(0.5)초 정도 부여하니 정상적으로 작동

keyword = pyautogui.prompt("검색어를 입력하세요.")
lastPage = int(pyautogui.prompt("마지막 페이지 번호를 입력해 주세요"))
pageNum = 1

for i in range(1, lastPage*10, 10):
    print(f"{pageNum} 페이지 입니다.=============================")
    response = requests.get(f"https://search.naver.com/search.naver?nso=&page=4&qdt=-1&query={keyword}&start={i}&where=web")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select(".link_tit")    # 클래스 선택자 news_tit

    for link in links:
        title = link.text   # 태그 안에 텍스트 요소
        url = link.attrs['href']    # href 속성 값
        print(title, url)
    pageNum = pageNum + 1
    time.sleep(0.5)