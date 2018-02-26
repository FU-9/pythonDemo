from multiprocessing import Process
import time,os

def task(name):
    print("%s is running,parent id is <%s>" %(os.getpid(),os.getppid()))
    time.sleep(3)
    print("%s is done" %os.getpid())

if __name__ == "__main__":
    p = Process(target=task,args=('子进程1',))
    p.start() #仅仅只是给操作系统发送了一个信号

    print(p.pid)
    print('主进程 id:%s' %os.getpid())
