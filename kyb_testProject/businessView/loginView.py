import logging
from kyb_testProject.common.common_fun import Common
from kyb_testProject.common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class LoginView(Common):
    username_type = (By.ID,'com.tal.kaoyan:id/login_email_edittext')#用户ID
    password_type = (By.ID,'com.tal.kaoyan:id/login_password_edittext')#密码ID
    loginBtn = (By.ID,'com.tal.kaoyan:id/login_login_btn')#登录ID
    tip_commit = (By.ID,'com.tal.kaoyan:id/tip_commit')#下线提示ID/退出确认按钮ID
    button_mysefl = (By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')#我的ID
    username = (By.ID,'com.tal.kaoyan:id/activity_usercenter_username')#用户名ID
    RightButton = (By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')#设置ID
    logoutBtn = (By.ID,'com.tal.kaoyan:id/setting_logout_text') #退出按钮ID

    def login_action(self,username,password):
        self.check_cancelBtn() #取消升级
        self.check_skipBtn() #跳过引导页面

        #输入用户名
        logging.info('============login_action==============')
        logging.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        #输入密码
        logging.info('password is:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        #点击登录
        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()

        #登录成功日志
        logging.info('login finished!')

    #下线通知
    def check_account_alert(self):
        logging.info('============check_account_alert===========')
        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('=========close tip_commit============')
            element.click()

    #是否登录检查
    def check_loginStatus(self):
        logging.info('============check_loginStatus===========')
        self.check_market_ad()  #广告
        self.check_account_alert() #下线

        try:
            self.driver.find_element(*self.button_mysefl).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login fail!')
            self.getScreenShot('ogin fail!') #失败截图
            return False #返回False
        else:
            logging.info('login success!')
            self.logout_action()#调用退出
            return True #返回True

    #退出
    def logout_action(self):
        logging.info('============logout_action===========')
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()


if __name__ == '__main__':
    driver=appium_desired()
    l=LoginView(driver)
    l.login_action('自学网2018','zxw2018a')
    l.check_loginStatus()