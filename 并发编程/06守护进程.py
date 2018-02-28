#守护进程会在主进程代码执行结束后就终止
#守护进程内无法在开启子进程，否则抛出异常

from multiprocessing import Process
import time

def task(name):
    print("%s is running " %name)
    time.sleep(3)
    print("%s is done " %name)

if __name__ == '__main__':
    p = Process(target=task,args=('子进程',))
    p.daemon = True #开启守护
    p.start()
    print('主')
