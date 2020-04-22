#并发启动appium服务和设备，如果占用就释放端口
from appium_sync.multi_appium import appium_start #导入启动appium服务
from appium_sync.multi_devices import appium_desired #导入启动运行多个模拟器
from appium_sync.cherk_port import *
from time import sleep
import multiprocessing

devices_list=['127.0.0.1:62001','127.0.0.1:7556']

def start_appium_action(host,port):
    if check_port(host,port):
        appium_start(host,port) #启动appium服务
        return True
    else:
        print('appium $s start fali' %port)
        return False


def start_devices_action(udid,port):
    host = '127.0.0.1'
    if start_appium_action(host.port):
        appium_desired(udid,port) #启动运行多个模拟器
    else:
        release_port(port) #释放端口

#并发启动线程组
def appium_start_sync():
    print('=========appium_start_sync=========')

    # 定义进程组
    desired_process = []

    for i in range(2):
        host = '127.0.0.1'
        port = 4723 + 2 * i
        # 定义进程
        appium = multiprocessing.Process(target=start_appium_action, args=(host, port))
        desired_process.append(appium)  # 添加到进程组

    # 执行所有进程
    for appium in desired_process:
        appium.start()
    # 关闭所有进程
    for appium in desired_process:
        appium.join()

    sleep(5)

#并发启动设备
def devices_start_sync():
    print('=========devices_start_sync=========')

    # 定义进程组
    desired_process = []

    for i in range(2):
        host = '127.0.0.1'
        port = 4723 + 2 * i
        # 定义进程
        appium = multiprocessing.Process(target=start_devices_action, args=(host, port))
        desired_process.append(appium)  # 添加到进程组

    # 执行所有进程
    for appium in desired_process:
        appium.start()
    # 关闭所有进程
    for appium in desired_process:
        appium.join()

if __name__ == '__main__':
    appium_start_sync()
    devices_start_sync()