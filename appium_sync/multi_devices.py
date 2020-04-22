#启动运行多个模拟器,跳过升级和引导页面
from appium import webdriver
import yaml
from time import ctime
from appium_sync.kyb_test import KybTest

with open('/Users/chabuduoxiansheng/PycharmProjects/appuim/appium_sync/desired_capsa.yaml','r') as file:
    data=yaml.load(file)

devices_list=['127.0.0.1:62001','127.0.0.1:7556'] #所有连接的设备

def appium_desired(udid,port):
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['udid'] = udid

    desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    print('appium port:%s start run %s at %s'%(port,udid,ctime()))

    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)

    k = KybTest()
    k.check_cancelBtn()
    k.check_skipBtn()
    return driver


if __name__ == '__main__':
    appium_desired(devices_list[0],4723)
    appium_desired(devices_list[1],4725)