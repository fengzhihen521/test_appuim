import logging
from kyb_testProject.common.desired_caps import appium_desired
from kyb_testProject.common.common_fun import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random #导入随机生成
import time

class RegisterView(Common):
    register_text = (By.ID,'com.tal.kaoyan:id/login_register_text')#注册按钮ID
    register_userheader = (By.ID,'com.tal.kaoyan:id/activity_register_userheader') #注册头像ID
    item_image = (By.ID,'com.tal.kaoyan:id/item_image') #注册头像图片ID
    save = (By.ID,'com.tal.kaoyan:id/save') #注册头像保存

    register_username = (By.ID,'com.tal.kaoyan:id/activity_register_username_edittext') #注册用户名ID
    register_password = (By.ID,'com.tal.kaoyan:id/activity_register_password_edittext') #注册密码ID
    register_email = (By.ID,'com.tal.kaoyan:id/activity_register_email_edittext') #注册邮箱ID
    register_btn = (By.ID,'com.tal.kaoyan:id/activity_register_register_btn') #立即注册按钮ID

    perfectinfomation_school = (By.ID,'com.tal.kaoyan:id/perfectinfomation_edit_school_name') #选择院校ID
    perfectinfomation_major = (By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_major') #选择专业ID
    perfectinfomation_goBtn = (By.ID,'com.tal.kaoyan:id/activity_perfectinfomation_goBtn') #进入考研帮按钮ID

    #选择院校
    forum_title = (By.ID,'com.tal.kaoyan:id/more_forum_title')
    university = (By.ID,'com.tal.kaoyan:id/university_search_item_name')

    #选择专业
    major_subject_title = (By.ID,'com.tal.kaoyan:id/major_subject_title')
    major_group_title = (By.ID,'com.tal.kaoyan:id/major_group_title')
    major_search_item_name = (By.ID,'com.tal.kaoyan:id/major_search_item_name')

    #用户中心
    button_mysefl = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')#我的ID
    username = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')#用户名ID

    #注册
    def register_action(self,register_username,register_password,register_email):
        self.check_cancelBtn()#跳过升级
        self.check_skipBtn()#跳过导航

        #点击注册按钮
        logging.info('============register_action=============')
        self.driver.find_element(*self.register_text).click()


        #点击注册头像
        logging.info('set userheader')
        self.driver.find_element(*self.register_userheader).click()
        self.driver.find_elements(*self.item_image)[4].click()
        self.driver.find_element(*self.save).click()

        #注册用户名、密码、邮箱
        logging.info('username is %s'%register_username)
        self.driver.find_element(*self.register_username).click()
        self.driver.find_element(*self.register_username).send_keys(register_username)

        logging.info('username is %s'%register_password)
        self.driver.find_element(*self.register_password).click()
        self.driver.find_element(*self.register_password).send_keys(register_password)

        logging.info('username is %s'%register_email)
        self.driver.find_element(*self.register_email).click()
        self.driver.find_element(*self.register_email).send_keys(register_email)

        #立即注册
        self.driver.find_element(*self.register_btn).click()
        time.sleep(3)

        #判断是否注册成功
        try:
            self.driver.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.error('register fail!')#打印失败日志
            self.getScreenShot('register fail!') #失败截图
            return False
        else:
            self.add_register_info() #完善资料
            #判断注册后是否登录
            if self.check_register_status():
                return True
            else:
                return False

    #完善资料
    def add_register_info(self):
        logging.info('========add_register_info=========')

        #选择院校
        logging.info('select school')
        self.driver.find_element(*self.perfectinfomation_school).click()
        self.driver.find_elements(*self.forum_title)[0].click()
        self.driver.find_elements(*self.university)[6].click()

        #选择专业
        logging.info('select major')
        self.driver.find_element(*self.perfectinfomation_major).click()
        self.driver.find_elements(*self.major_subject_title)[4].click()
        self.driver.find_elements(*self.major_group_title)[0].click()
        self.driver.find_elements(*self.major_search_item_name)[0].click()

        #点击进入考研帮按钮
        self.driver.find_element(*self.perfectinfomation_goBtn).click()

    #注册后是否登录检查
    def check_register_status(self):
        logging.info('============check_register_status===========')
        self.check_market_ad() #广告

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('register fail!')
            self.getScreenShot('register fail!') #失败截图
            return False #返回False
        else:
            logging.info('register success!')
            return True #返回True

if __name__ == '__main__':
    driver = appium_desired()
    register = RegisterView(driver)

    #随机填写用户名
    username = 'zxw2020'+'lyp'+str(random.randint(1000,9999))
    #随机填写密码
    password = 'zxw2020'+str(random.randint(1000,9999))
    #随机填写邮箱
    email = '51lyp'+str(random.randint(1000,9999))+'@163.com'

    register.register_action(username,password,email)