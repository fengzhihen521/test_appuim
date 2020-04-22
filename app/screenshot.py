#保存截图
from app.capability import driver

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('xiaodashu')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('liuyuepeng01')

driver.save_screenshot('login.png') #保存到当前路径
driver.get_screenshot_as_file('./images/login1.png') #保存到指定路径

driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

