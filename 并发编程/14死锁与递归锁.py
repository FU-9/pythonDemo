# 死锁
# from threading import Thread,Lock
# import time
#
# mutexA = Lock()
# mutexB = Lock()
#
# class MyThread(Thread):
#
#     def run(self):
#         self.f1()
#         self.f2()
#
#     def f1(self):
#         mutexA.acquire()
#         print("%s 拿到了A锁"%self.name)
#         mutexB.acquire()
#         print("%s 拿到了B锁"%self.name)
#         mutexB.release()
#         mutexA.release()
#
#     def f2(self):
#         mutexB.acquire()
#         print("%s 拿到了B锁"%self.name)
#         mutexA.acquire()
#         print("%s 拿到了A锁"%self.name)
#         mutexA.release()
#         mutexB.release()
#
#
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = MyThread()
#         t.start()











#递归锁
# 可以连续acquire多次 每qcquire一次计数器+1 只要计数不为0 就不会被其他线程抢到
from threading import Thread,RLock
import time

mutexB = mutexA = RLock()

class MyThread(Thread):

    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print("%s 拿到了A锁"%self.name)
        mutexB.acquire()
        print("%s 拿到了B锁"%self.name)
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print("%s 拿到了B锁"%self.name)
        mutexA.acquire()
        print("%s 拿到了A锁"%self.name)
        mutexA.release()
        mutexB.release()



if __name__ == '__main__':
    for i in range(10):
        t = MyThread()
        t.start()
