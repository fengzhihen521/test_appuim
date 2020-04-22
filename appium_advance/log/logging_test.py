import logging #导入日志

#logging.basicConfig(level=logging.DEBUG) #设置级别
#logging.basicConfig(level=logging.INFO) #设置级别

#logging.basicConfig(level=logging.INFO,filename='runlig.log') #设置级别后将日志文件保存

#设置级别后将日志文件保存成规定格式显示
logging.basicConfig(level=logging.INFO,filename='runlig.log',filemode='w',
                                        #日志文件名             是否覆盖或继续写入
                    format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')
                              #时间         模块名称          行号          日志级别      日志信息
#输入日志
logging.debug('debug info')
logging.info('hello 51zxw')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')

