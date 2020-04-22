#自动启动appium服务
import subprocess #导入连接输入/输出/错误
from time import ctime

def appium_start(host,port):
    bootstrap_port = str(port+1)#将端口转换成字符串
    cmd = 'start /b appium -a '+host+'-p'+str(port)+'-bp'+str(bootstrap_port)#启动命令

    print('%s at %s'%(cmd,ctime()))
    #存放启动日志
    subprocess.Popen(cmd,shell=True,stdout=open('./appium_log/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

if __name__ == '__main__':
    host = '127.0.0.1'
    # port = 4723
    # appium_start(host,port)#启动单个
    for i in range(2):
        port = 4723+2*i
        appium_start(host,port)#启动多个
