from threading import Thread,Semaphore,currentThread
import time,random

sm = Semaphore(3)

def func():
    # sm.acquire()
    # print("%s in"%currentThread().getName())
    # time.sleep(random.randint(1,3))
    # sm.release()
    with sm:
        print("%s in"%currentThread().getName())
        time.sleep(random.randint(1,3))

if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=func)
        t.start()
