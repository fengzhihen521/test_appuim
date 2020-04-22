#并发启动多个appium服务
from time import ctime
import subprocess
import multiprocessing #导入多进程


def appium_start(host,port):
    bootstrap_port = str(port+1)#将端口转换成字符串
    cmd = 'start /b appium -a '+host+'-p'+str(port)+'-bp'+str(bootstrap_port)#启动命令

    print('%s at %s'%(cmd,ctime()))
    #存放启动日志
    subprocess.Popen(cmd,shell=True,stdout=open('./appium_log/'+str(port)+'.log','a'),stderr=subprocess.STDOUT)

#定义进程组
desired_process=[]

for i in range(2):
    host = '127.0.0.1'
    port = 4723+2*i
    #定义进程
    appium = multiprocessing.Process(target=appium_start,args=(host,port))
    desired_process.append(appium) #添加到进程组

if __name__ == '__main__':
    #执行所有进程
    for appium in desired_process:
        appium.start()
    #关闭所有进程
    for appium in desired_process:
        appium.join()