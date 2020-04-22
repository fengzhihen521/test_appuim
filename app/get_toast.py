#toast验证
#coding=utf-8
from app.capability import driver
from selenium.webdriver.support.ui import WebDriverWait

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('xiaodashu')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('liuyuepeng01')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

error_message="用户名或密码错误，你还可以尝试4次"
limit_message="验证失败次数过多，请15分钟后再试"

#message='//*[@text=\'{}\']'.format(error_message) #xpath定位，format格式转换
message='//*[@text=\'{}\']'.format(limit_message) #format格式转换

toast_element=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath(message))
print(toast_element.text)

