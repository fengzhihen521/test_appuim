#多点触控操作-地图
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction #导入连续滑动
from appium.webdriver.common.multi_action import MultiAction #导入多点触控

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0.1'
desired_caps['deviceName']='127.0.0.1:22471'

desired_caps['app']='/Users/chabuduoxiansheng/Desktop/com.baidu.BaiduMap.apk'
desired_caps['appPackage']='com.baidu.BaiduMap'
desired_caps['appActivity']='com.baidu.baidumaps.WelcomeScreen'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5) #等待时间

#获取屏幕尺寸

x = driver.get_window_size()['width'] #获取x轴
y = driver.get_window_size()['height'] #获取y轴


driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()

#滑动操作
def pinch():#缩小
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    pinch_action = MultiAction(driver)

    #缩小向两边进行滑动并等待一秒的时间
    action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000).release()
    action1.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000).release()

    #加载滑动并执行
    pinch_action.add(action1,action2) #加载滑动
    pinch_action.perform() #执行

def zoom():#放大
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    pinch_action = MultiAction(driver)

    #放大向中间进行滑动并等待一秒的时间
    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000).release()
    action1.press(x=x * 0.6, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000).release()

    #加载滑动并执行
    pinch_action.add(action1,action2) #加载滑动
    pinch_action.perform() #执行

#调试
if __name__ == '__main__':
    for i in range(3):
        pinch()
        zoom()
