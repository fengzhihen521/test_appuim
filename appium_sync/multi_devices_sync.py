#并发启动运行多个模拟器
from appium import webdriver
import yaml
from time import ctime
import multiprocessing #导入多进程


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
    return driver

#定义进程组
desired_process=[]

for i in range(len(devices_list)):
    port = 4723+2*i
    #定义进程
    desired = multiprocessing.Process(target=appium_desired,args=(devices_list[i],port))
    desired_process.append(desired) #添加到进程组

if __name__ == '__main__':
    #执行所有进程
    for desired in desired_process:
        desired.start()
    #关闭所有进程
    for desired in desired_process:
        desired.join()