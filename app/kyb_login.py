#输入用户名、密码登录
from app.capability import driver,NoSuchElementException

def login():
    driver.implicitly_wait(2)  # 等待时间
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
    driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('xiaodashu')

    driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('liuyuepeng0106')
    driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()


try:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
    # driver.find_element_by_name() #name定位
    # driver.find_element_by_class_name() #class定位
    # driver.find_element_by_xpath() #xpath定位
except NoSuchElementException:
    login()
else:
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl').click()
    driver.find_element_by_id('com.tal.kaoyan:id/activity_usercenter_userheader').click()
    login()