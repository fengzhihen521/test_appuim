#检测接口是否可用和释放端口
import socket
import os

#检测接口是否可用
def check_port(host,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#使用IPv4

    try:
        s.connect((host,port))#传入
        s.shutdown(2)#关闭

    except OSError as msg:
        print('port %s is available!' %port)#打印异常
        #print(msg)
        return True
    else:
        print('port %s already be in use!' %port)
        return False

#释放端口
def release_port(port):
    #查找对应端口的pid
    cmd_find = 'netstat -ano |findsts %s'%port
    #print(cmd_find)

    #返回命令执行后的结果
    result=os.popen(cmd_find).read()
    #print(result)

    if str(port) and 'LISTENING' in result:
        #获取端口对应的pid进程
        i = result.index('LISTENING')#获取到LISTENING的索引位置
        start = i+len('LISTENING')+7#是有LISTENING+7获取pid位置
        end = result.index('\n')#获取到\n的索引位置
        pid = result[start:end]#获取到start和end中间的pid信息

        #关闭被占用端口的pid
        cmd_kill = 'kaskkill -f -pid %s' %pid #关闭进程
        #print(cmd_kill)
        os.popen(cmd_kill)#执行关闭进程
    else:
        print('port %s is available' %port)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4723
    #check_port(host,port) #传入host,port
    release_port(port)