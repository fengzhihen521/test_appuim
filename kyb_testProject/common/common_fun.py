from kyb_testProject.baseView.baseView import BaseView
from kyb_testProject.common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import os
import csv

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2') #升级
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip') #跳过

    wemedia_cacel = (By.ID,'com.tal.kaoyan:id/view_wemedia_cacel') #广告

    # 判断是否有升级按钮
    def check_cancelBtn(self):
        logging.info('==========check_cancelBtn=========')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancelBtn.click()

    #判断是否有导航跳过按钮
    def check_skipBtn(self):
        logging.info('=========check skipBtn=============')
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    # 获取屏幕尺寸
    def get_size(self):
        x = self.driver.get_window_size()['width']  # 获取x轴
        y = self.driver.get_window_size()['height']  # 获取y轴
        return x, y

    # 滑动方法
    def swipeleft(self):
        logging.info('swipeleft')
        l = self.get_size()
        x1 = int(l[0] * 0.9)  # 起点，向左滑动
        y1 = int(l[1] * 0.5)  # 从屏幕中间开始滑动
        x2 = int(l[0] * 0.1)  # 终点，向左滑动
        self.swipe(x1, y1, x2, y1, 1000)  # 执行从左向右滑动，持续时间1秒

    #定义时间
    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    #截图并方法
    def getScreenShot(self,module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__))+'/screenshots/%s_%s.png' %(module,time)#保存图片路径+命名+时间

        logging.info('get %s screenshots' %module) #截图日志
        self.driver.get_screenshot_as_file(image_file)#保存到指定路径

    #关闭广告提示
    def check_market_ad(self):
        logging.info('=========check_market_ad==========')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('=========close market ad============')
            element.click()

    #获取文件内容
    def get_csv_data(self,csv_file,line):
        logging.info('========get_csv_data=========')
        with open(csv_file,'r',encoding='utf-8-sig') as file: #读取文件
            reader = csv.reader(file) #将文件内容存到变量中
            for index,row in enumerate(reader,1):#读取每行的内容
                if index == line:#返回指定行
                    return row #返回每行的内容


if __name__ == '__main__':
    driver=appium_desired()
    com=Common(driver)
    com.check_cancelBtn()
    #com.check_skipBtn()
    com.swipeleft()
    com.getScreenShot('startApp')

    #普通的遍历方式
    list = ['这','是','一个','测试','数据']
    # for i in range(len(list)):
    #     print(i,list[i])

    #enumerate遍历方式
    list1 = ['这', '是', '一个', '测试', '数据']
    # for index,item in enumerate(list1):
    #     print(index,item)