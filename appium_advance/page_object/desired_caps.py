from appium import webdriver
import yaml
import logging
import logging.config
import os
# CON_LOG='../log/log.conf'
# logging.config.fileConfig(CON_LOG)
# logginga=logging.getLogger()

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'../log/log.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger()

def appium_desired():
    file = open('/Users/chabuduoxiansheng/PycharmProjects/appuim/appium_advance/yaml/desired_capsa.yaml', 'r')
    data = yaml.load(file)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()