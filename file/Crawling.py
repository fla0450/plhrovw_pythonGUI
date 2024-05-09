import json
import time
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# --크롬창을 숨기고 실행-- driver에 options를 추가해주면된다
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

url = 'https://map.naver.com/v5/search'
driver = webdriver.Chrome()  # 드라이버 경로
# driver = webdriver.Chrome('./chromedriver',chrome_options=options) # 크롬창 숨기기
driver.get(url)
key_word = '양산시 남부시장'  # 검색어

# css 찾을때 까지 10초대기
def time_wait(num, code):
    try:
        wait = WebDriverWait(driver, num).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, code)))
    except:
        print(code, '태그를 찾지 못하였습니다.')
        driver.quit()
    return wait

# frame 변경 메소드
def switch_frame(frame):
    driver.switch_to.default_content()  # frame 초기화
    driver.switch_to.frame(frame)  # frame 변경

# 페이지 다운
def page_down(num):
    body = driver.find_element(By.CSS_SELECTOR, 'body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)

# css를 찾을때 까지 10초 대기
time_wait(10, 'div.input_box > input.input_search')

# (1) 검색창 찾기
search = driver.find_element(By.CSS_SELECTOR, 'div.input_box > input.input_search')
search.send_keys(key_word)  # 검색어 입력
search.send_keys(Keys.ENTER)  # 엔터버튼 누르기

sleep(1)

# (2) frame 변경
switch_frame('searchIframe')
# page_down(40)
sleep(3)

# 주차장 리스트
Restaurant_list = driver.find_elements(By.CSS_SELECTOR, 'li.VLTHu')
# 페이지 리스트
next_btn = driver.find_elements(By.CSS_SELECTOR, '.zRM9F> a')

# dictionary 생성
Restaurant_list = {'음식점 정보': []}

# 시작시간
start = time.time()
print('[크롤링 시작...]')
elements = driver.find_elements(By.CSS_SELECTOR,'li.VLTHu')
name = elements[0]
name.click()
print("클릭")
# for bin in range(len(next_btn))[1:]:
    # Restaurant_list = driver.find_element(By.CSS_SELECTOR,'li.VLTHu')
    # names = driver.find_element(By.CSS_SELECTOR,'li.VLTHu').click()


print('[데이터 수집 완료]\n소요 시간 :', time.time() - start)
driver.quit()  # 작업이 끝나면 창을 닫는다.

# json 파일로 저장
# with open('data/store_data.json', 'w', encoding='utf-8') as f:
#     json.dump(parking_dict, f, indent=4, ensure_ascii=False)