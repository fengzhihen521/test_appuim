from kyb_testProject.common.myunit import StartEnd
from kyb_testProject.businessView.loginView import LoginView
import unittest
import logging

class TestLogin(StartEnd):

    csv_file = '/Users/chabuduoxiansheng/PycharmProjects/appuim/kyb_testProject/data/account.csv'

    #@unittest.skip('skip test_login_zxw2018')  # 暂时不执行
    def test_login_zxw2018(self):
        logging.info('======test_login_zxw2018=====')
        l=LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,2)#读取文件

        l.login_action(data[0],data[1])#使用用户名和密码
        self.assertTrue(l.check_loginStatus()) #检测是否登录成功

    #@unittest.skip('skip test_login_zxw2017') #暂时不执行
    def test_login_zxw2017(self):
        logging.info('======test_login_zxw2017=====')
        l=LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,1)#读取文件

        l.login_action(data[0],data[1])#使用用户名和密码
        self.assertTrue(l.check_loginStatus()) #检测是否登录成功

    #@unittest.skip('skip test_login_error')  # 暂时不执行
    def test_login_error(self):
        logging.info('======test_login_error=====')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,3)#读取文件

        l.login_action(data[0],data[1])#使用用户名和密码
        self.assertTrue(l.check_loginStatus(),msg='login fail!') #检测是否登录成功,登录失败提示login fail!

if __name__ == '__main__':
    unittest.main()