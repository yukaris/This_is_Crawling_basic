from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 제거
chrome_options.add_experimental_option("excludeSwitches", ["enable-loging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 로그인 주소
driver.implicitly_wait(5)   # 웹페이지 로딩 대기 시간 설정
driver.maximize_window()    # 화면 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

def first_login_test():
    # 너무 빨리 넘어가 그림 확인 작업 추가되어 로그인 실패된다.
    id = driver.find_element(By.CSS_SELECTOR, "#id")
    id.click()
    id.send_keys('yyukaris')

    pw = driver.find_element(By.CSS_SELECTOR, "#pw")
    pw.click()
    pw.send_keys('sena0722Na#')

    btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
    btn.click()

def login():
    # 너무 빨리 넘어가 그림 확인 작업 추가되어 로그인 실패된다.
    id = driver.find_element(By.CSS_SELECTOR, "#id")
    id.click()
    pyperclip.copy('yyukaris')
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)

    pw = driver.find_element(By.CSS_SELECTOR, "#pw")
    pw.click()
    pyperclip.copy('sena0722Na#')
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)

    btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
    btn.click()

first_login_test()