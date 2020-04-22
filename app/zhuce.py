#随机生成用户名、密码、邮箱注册考研帮
from app.capability import driver,NoSuchElementException
import random #导入随机生成

driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()

#选择头像
driver.find_elements_by_id('com.tal.kaoyan:id/item_image')[4].click()
driver.find_element_by_id('com.tal.kaoyan:id/save').click()

#注册+填写用户名
username = 'zxw2020'+'LYP'+str(random.randint(1000,9999))
print('username: %s'%username)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(username)

#注册+填写密码
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').click()
password = 'zxw2020'+str(random.randint(1000,9999))
print('password: %s'%password)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(password)
driver.implicitly_wait(3) #等待时间

#注册+填写邮箱
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').click()
email = '51lyp'+str(random.randint(1000,9999))+'@163.com'
print('email: %s'%email)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)

#点击注册按钮
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

#选择院校
driver.find_element_by_id('com.tal.kaoyan:id/perfectinfomation_edit_school_name').click()
driver.find_elements_by_id('com.tal.kaoyan:id/more_forum_title')[0].click()
driver.find_elements_by_id('com.tal.kaoyan:id/university_search_item_name')[6].click()

#选择专业
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[4].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[0].click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[0].click()

#点击进入考研帮
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()
