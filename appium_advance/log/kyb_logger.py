#将yaml中的数据进行加载
from appium import webdriver
import yaml
import logging
from selenium.common.exceptions import NoSuchElementException #导入错误日志

file = open('../yaml/desired_capsa.yaml','r')
data = yaml.load(file)

#设置级别后将日志文件保存成规定格式显示
logging.basicConfig(level=logging.INFO,filename='runlig.log',filemode='a',
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')

#将yaml中的数据进行加载
desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']

desired_caps['app'] = data['app']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['noReset'] = data['noReset']

logging.info('qidong APP')
driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
driver.implicitly_wait(2) #等待时间

def check_cancelBtn():
    logging.info('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    logging.info('check skipBtn')

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info('no skipBtn')
    else:
        skipBtn.click()

check_cancelBtn()
check_skipBtn()