#滑动
from app.capability import driver
from time import sleep

#获取屏幕尺寸
def get_size():
    x = driver.get_window_size()['width'] #获取x轴
    y = driver.get_window_size()['height'] #获取y轴
    return x,y
l = get_size()
print(l)

#滑动方法
def swipeleft():
    l = get_size()
    x1 = int(l[0]*0.9)#起点，向左滑动
    y1 = int(l[1] * 0.5)#从屏幕中间开始滑动
    x2 = int(l[0] * 0.1)#终点，向左滑动
    driver.swipe(x1,y1,x2,y1,1000)#执行从左向右滑动，持续时间1秒

for i in range(2):
    swipeleft() #调用滑动方法
    sleep(0.5)

driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()
