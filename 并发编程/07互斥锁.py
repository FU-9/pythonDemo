#进程间共享的东西会存在竞争，例如：终端，硬盘上的空间
#进程必须共享同一把锁，才会阻止竞争，会牺牲效率
#原理：把并发变为串行
from multiprocessing import Process,Lock
import time

def task(name,mutex):
    mutex.acquire()#加锁
    print("%s 1" %name)
    time.sleep(1)
    print("%s 2" %name)
    time.sleep(1)
    print("%s 3" %name)
    mutex.release()#解锁

if __name__ == '__main__':
    mutex = Lock()
    for i in range(3):
        p = Process(target=task,args=("进程%s"%i,mutex))
        p.start()

#互斥锁与join的区别
#join是把整个进程都变为串行
#互斥锁 可以把代码片段变为串行
