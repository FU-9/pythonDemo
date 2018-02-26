from multiprocessing import Process
import time

def task(name):
    print('%s is running' %name)
    time.sleep(3)
    print('%s is done' %name)

if __name__ == '__main__':
    p = Process(target=task,args=('子进程1',))
    p.start()
    #p.terminate()#杀死进程，仅仅给操作系统发送一个信号
    #print(p.is_alive())#查看进程是否存活
    print(p.name)#进程名 可以自定义名称Process(target=task,name="subprocess",args=('子进程1',))
    #p.join()#主进程等待子进程运行结束

    print('主进程')
