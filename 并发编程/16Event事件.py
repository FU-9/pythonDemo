from threading import Thread,Event,currentThread
import time

event = Event()

def conn():
    n = 0
    while not event.is_set():
        if n == 3:
            print('%s try too many times'%currentThread().getName())
            return
        print('%s try %s'%(currentThread().getName(),n))
        event.wait(1)
        n+=1
    print("succent")


def check():
    print("%s is checking"%currentThread().getName())
    time.sleep(5)
    event.set()


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=conn)
        t.start()

    c = Thread(target=check)
    c.start()


'''
event.is_set()返回event的状态值
event.wait()如果event.is_set = False 将阻塞线程
event.set()设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()恢复event的状态值为False
'''
