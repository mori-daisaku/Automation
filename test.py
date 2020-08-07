import time
from datetime import datetime
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

LOGIN_ID = 'username'
LOGIN_PASSWORD = 'password'

#Amazon Nintendo Switch
ITEM_URL = 'https://www.amazon.co.jp/dp/B07WXL5YPW'
#店舗名
ACCEPT_SHOP = 'Amazon'
#上限価格
LIMIT_VALUE = 32978

def failure_message(str):
    print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'),str)

if __name__ == '__main__':
    #ブラウザの起動
    try:
        driver.get(ITEM_URL)
        #driver.get("https://www.amazon.co.jp/")
    except:
        failure_message('ブラウザの起動に失敗しました')
        exit()


time.sleep(2)

elem_search_btn = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]")
elem_search_btn.click()

time.sleep(2)

elem_search_word = driver.find_element_by_id("ap_email")
elem_search_word.send_keys("username")

elem_search_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
elem_search_btn.click()

time.sleep(2)

elem_search_word = driver.find_element_by_id("ap_password")
elem_search_word.send_keys("password")

elem_search_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input")
elem_search_btn.click()
