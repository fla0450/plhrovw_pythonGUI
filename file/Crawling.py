import json
import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://map.naver.com/v5/search'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
key_word="양산 남부시장"

def time_wait(num,code):
    try:
        wait = WebDriverWait(driver,num).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,code))
        )
    except:
        print(code,'테그를 찾지 못하였습니다.')
        driver.quit()
    return wait
def switch_frame(frame):
    driver.switch_to.default_content()
    driver.switch_to.frame(frame)
def page_down(num):
    body = driver.find_element(By.CSS_SELECTOR,'body')
    body.click()
    for i in range(num):
        body.send_keys(Keys.PAGE_DOWN)
time_wait(10,'div.input_box > input.input_search')

search = driver.find_element(By.CSS_SELECTOR,'div.input_box > input.input_search')
search.send_keys(key_word)
search.send_keys(Keys.ENTER)

sleep(1)

switch_frame('searchIframe')
page_down(40)
sleep(3)
