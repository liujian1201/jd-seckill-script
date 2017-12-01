#_*_coding:utf-8_*_
from selenium import webdirver
import datetime
import time


mobileEmulation = {'deviceName': 'Apple iPhone 6'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', chrome_options=options)

def login(uname,pwd):
    if driver.find_element_by_link_text("你好，请登录"):
        driver.find_element_by_link_text("你好，请登录").click()
    if driver.find_element_by_link_text("账户登录"):
        driver.find_element_by_link_text("账户登陆").click()
    if driver.find_element_by_link_text("loginname"):
        driver.find_element_by_link_text("loginname").click()
    if driver.find_element_by_link_text("nloginpwd"):
        driver.find_element_by_link_text("nloginpwd").click()
    if driver.find_element_by_link_text("loginsubmit"):
        driver.find_element_by_link_text("loginsubmit").click()
    
    time.sleep(1)
    driver.get("https://cart.jd.com/cart.action")
    if driver.find_element_by_link_text("去结算"):
        driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    print('login success:',now.strftime('%Y-%m-%d %H:%M:%S'))

    

def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buy_on_time:
            while True:
                try:
                    driver.find_element_by_id('order-submit').click()
                except:
                    time.sleep(0.1)
        time.sleep(0.1)


driver.get("https://www.jd.com")
print driver.title


#login('替换成你的账号','替换成你的密码')
#buy_on_time('2017-12-04 10:00:01')

