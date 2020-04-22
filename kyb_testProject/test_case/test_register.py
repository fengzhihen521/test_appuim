from kyb_testProject.common.myunit import StartEnd
from kyb_testProject.businessView.registerView import RegisterView
import logging
import random
import unittest

class Registertest(StartEnd):

    #用户注册用例
    def test_user_register(self):
        logging.info('=========test_user_register===========')
        r = RegisterView(self.driver)

        # 随机填写用户名
        username = 'zxw2020' + 'lyp' + str(random.randint(1000, 9999))
        # 随机填写密码
        password = 'zxw2020' + str(random.randint(1000, 9999))
        # 随机填写邮箱
        email = '51lyp' + str(random.randint(1000, 9999)) + '@163.com'

        self.assertTrue(r.register_action(username, password, email))#断言

if __name__ == '__main__':
    unittest.main()
