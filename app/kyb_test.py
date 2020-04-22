#启动APP跳过引导页
from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['deviceName']='127.0.0.1:22471'
desired_caps['platformVersion']='6.0.1'
#desired_caps['udid']='udid值' #真机需要输入udid

desired_caps['app']='/Users/chabuduoxiansheng/Desktop/kaoyan3.1.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5) #等待时间

driver.find_element_by_id('android:id/button2').click()
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()

