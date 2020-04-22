#将yaml中的数据进行加载
from appium import webdriver
import yaml

file = open('desired_capsa.yaml','r')
data = yaml.load(file)

#将yaml中的数据进行加载
desired_caps = {}
desired_caps['platformName'] = data['platformName']
desired_caps['platformVersion'] = data['platformVersion']
desired_caps['deviceName'] = data['deviceName']

desired_caps['app'] = data['app']
desired_caps['appPackage'] = data['appPackage']
desired_caps['appActivity'] = data['appActivity']
desired_caps['noReset'] = data['noReset']

driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
