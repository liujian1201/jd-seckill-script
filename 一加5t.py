#_*_coding:utf-8_*_
import os
import time,datetime
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys  
#修改时间，用户密码，产品页面

#修改时间
startTime = datetime.datetime(2017,12,6,17,32,20)
while datetime.datetime.now() < startTime:
    print("%s:时间还没到" %(time.strftime("%Y-%m-%d %X", time.localtime())))
    time.sleep(1)
print('Program now starts on %s' % startTime)
print('Executing...')



chromedriver = "D:\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
mobileEmulation = {'deviceName': 'iPhone 6 Plus'}



# 不加载图片提升速度
prefs = {"profile.managed_default_content_settings.images":2}

options = webdriver.ChromeOptions()

#chrome无参数报错
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('mobileEmulation', mobileEmulation)

# 无界面配置，需要验证码时需要注释掉
options.add_argument("--headless")
options.add_experimental_option("prefs",prefs)


driver = webdriver.Chrome(chromedriver,chrome_options=options)


def buy():
    driver.find_element_by_link_text("立即抢购").click()


def olpay():
    try:
        driver.find_element_by_link_text("在线支付").click()
    except Exception:
        print("无在线支付按钮")
    
        
        
def submit():
    try:
        driver.find_element_by_link_text("提交订单").click()
    except Exception:
        print("无提交订单按钮")
        
 


#下面填入京东的用户名以及密码
jd_up = {"ue":"95489424@qq.com","pd":"Yeyu8197"}


def login():
    driver.get('https://m.jd.com/')
    
#    print(driver.title)
    
    if driver.find_element_by_class_name("jd-search-icon-login"):
        driver.find_element_by_class_name("jd-search-icon-login").click()

    time.sleep(0.2)

#    print(driver.title)

    if driver.find_element_by_id("username"):
        user = driver.find_element_by_id("username")
        user.clear()
        user.send_keys(jd_up["ue"])

    time.sleep(0.1)
        
    if driver.find_element_by_id("password"):
        pwd = driver.find_element_by_id("password")
        pwd.clear()
        pwd.send_keys(jd_up["pd"])
    if driver.find_element_by_id("loginBtn"):
        driver.find_element_by_id("loginBtn").click()

    time.sleep(1)

##一加5t
##https://item.m.jd.com/product/5716985.html
##360 n6 pro
##https://item.m.jd.com/product/5782095.html    

    print(driver.title)
    

    while True:
        try:
#修改产品页面
            driver.get('https://item.m.jd.com/product/5716985.html')

            print(driver.title)
#时间间隔设置
            time.sleep(1)
            
            buy()
            
            time.sleep(0.5)

            if (submit()):
                pass
            else:
                olpay()

            time.sleep(0.5)

            if dirver.find_element_by_id("tryBtn"):
                continue
                #dirver.find_element_by_id("tryBtn").click()
            else:
                print("%s :抢购成功！"%(time.strftime("%Y-%m-%d %X", time.localtime())))
                break

           
        except Exception:
            if (driver.find_element_by_link_text("立即预约")):
                print("%s : 还未开始抢购！" %(time.strftime("%Y-%m-%d %X", time.localtime())))


        
##    while True:
##        if driver.find_element_by_link_text("立即抢购"):
##            driver.find_element_by_link_text("立即抢购").click()
##        elif driver.find_element_by_link_text("立即预约"):
##            time.sleep(0.1)
##            print("还在没到开抢时间")
##            break


        
    time.sleep(3)
##购物车    
    driver.get('https://wqs.jd.com/order/orderlist_merge.shtml')




    

if __name__ == '__main__':
    login()


#driver.close()

