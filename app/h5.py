#APP中H5页面切换
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0.1'
desired_caps['deviceName']='127.0.0.1:22471'
# desired_caps['udid']='udid值' #真机需要输入udid
# desired_caps['automationName']='uiautomator2' #配置uiautomator2

desired_caps['app']='/Users/chabuduoxiansheng/Desktop/dr.fone3.2.0.apk'
desired_caps['appPackage']='com.wondershare.drfone'
desired_caps['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'

# desired_caps['noReset']='False' #True屏蔽弹窗，False不屏蔽弹窗
# desired_caps['unicodeKeyboard']='True' #用户名为中文需要配置
# desired_caps['reseKeyboard']='True' #用户名为中文需要配置

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3) #等待时间

driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

#等待元素加载
WebDriverWait(driver,10).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))

driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

WebDriverWait(driver,10).until(lambda x:x.find_element_by_class_name('android.widget.LinearLayout'))

#切换contexts
contexts = driver.contexts
print(contexts) #打印contexts结果（NATIVE_APP', 'WEBVIEW_com.wondershare.drfone）
#切换到H5
driver.switch_to.context('WEBVIEW_com.wondershare.drfone') #取contexts结果中的值切换到H5
driver.find_element_by_id('email').send_keys('liu@163.com')
driver.find_element_by_class_name('btn_send active').click()
#切换回APP
driver.switch_to.context('NATIVE_APP') #取contexts结果中的值切换到APP
driver.find_element_by_class_name('android.widget.ImageButton').click()