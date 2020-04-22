import unittest
from BSTestRunner import BSTestRunner
import time
import logging

#指定测试用例路径
test_dir = '/Users/chabuduoxiansheng/PycharmProjects/appuim/kyb_testProject/test_case'
#指定报告存放路径
report_dir = '/Users/chabuduoxiansheng/PycharmProjects/appuim/kyb_testProject/reports'

#加载测试用例=指定用例路径+执行的用例名称
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

#定义报告时间格式
now = time.strftime('%Y-%m-%d %H_%M_%s')

#指定报告存放路径和名字
report_name = report_dir + '/'+ now + 'test_report.html'

#已二进制的方式打开文件
with open(report_name,'wb') as f:
    #指定文件+命名title+描述
    runner = BSTestRunner(stream=f,title='kyb Test Report',description='kyb Android app test report')
    logging.info('start run test case...')
    runner.run(discover) #执行指定用例
