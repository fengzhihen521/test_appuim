from appium import webdriver #导入appium
from selenium.common.exceptions import NoSuchElementException #导入错误日志

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:22471'
desired_caps['platformVersion']='6.0.1'
#desired_caps['udid']='udid值' #真机需要输入udid

desired_caps['app']='/Users/chabuduoxiansheng/Desktop/kaoyan3.1.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

desired_caps['noReset']='True' #True屏蔽弹窗，False不屏蔽弹窗

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5) #等待时间

def check_cancelBtn():
    print('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print('check skipBtn')

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
check_skipBtn()
