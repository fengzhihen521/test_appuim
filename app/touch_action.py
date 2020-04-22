#安装APP后连续滑动设置手势密码
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction #导入连续滑动
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException #导入错误日志
from time import sleep #导入等待时间

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0.1'
desired_caps['deviceName']='127.0.0.1:22471'

desired_caps['app']='/Users/chabuduoxiansheng/Desktop/mymoney.apk'
desired_caps['appPackage']='com.mymoney'
desired_caps['appActivity']='com.mymoney.biz.splash.SplashScreenActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5) #等待时间

#获取屏幕尺寸
def get_size():
    x = driver.get_window_size()['width'] #获取x轴
    y = driver.get_window_size()['height'] #获取y轴
    return x,y

#向左滑动方法
def swipeleft():
    l = get_size()
    x1 = int(l[0] * 0.9)#起点，向左滑动
    y1 = int(l[1] * 0.5)#从屏幕中间开始滑动
    x2 = int(l[0] * 0.1)#终点，向左滑动
    driver.swipe(x1,y1,x2,y1,1000)#执行从左向右滑动，持续时间1秒

#向上滑动方法
def swipeUp():
    l = get_size()
    x1 = int(l[0] * 0.5)#起点，向上滑动
    y1 = int(l[1] * 0.95)#从屏幕中间开始滑动
    y2 = int(l[1] * 0.35)#终点，向上滑动
    driver.swipe(x1,y1,x1,y2,1000)#执行从下向上滑动，持续时间1秒

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/next_btn'))

for i in range(2):
    swipeleft() #调用滑动方法
    sleep(0.5)

driver.find_element_by_id('com.mymoney:id/begin_btn').click()

try:
    closeBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
except NoSuchElementException:
    pass
else:
    closeBtn.click()

driver.find_element_by_id('com.mymoney:id/nav_setting_btn').click()

WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.mymoney:id/accbook_member_head_iv'))

swipeUp() #向上滑动

driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()

driver.find_element_by_id('com.mymoney:id/password_protected_briv').click()

driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv').click()
sleep(2)

#手势滑动
for i in range(2):
    # 按压后等到2秒,移动后停留2秒，再次移动后停留2秒，再次移动后停留2秒，释放按压，执行操作
    # press(按压)，move_to(移动)，release(释放)，perform(执行)
    TouchAction(driver)\
    .press(x=343,y=383).wait(1000)\
    .move_to(x=541,y=384).wait(1000)\
    .move_to(x=737,y=580).wait(1000)\
    .move_to(x=734,y=773).wait(1000)\
    .release().perform()
