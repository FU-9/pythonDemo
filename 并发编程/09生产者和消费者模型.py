from multiprocessing import Process,Queue
import time

def producer(q):
    for i in range(10):
        time.sleep(2)
        res = "数据%s"%i
        print('生产者生产了%s'%res)
        q.put(res)

def consumer(q):
    while True:
        res = q.get()
        if res is None:break
        time.sleep(1)
        print("消费者接受了%s"%res)


if __name__ == '__main__':
    q = Queue()

    #生产者们
    p1 = Process(target=producer,args=(q,))
    p2 = Process(target=producer,args=(q,))
    #消费者们
    c1 = Process(target=consumer,args=(q,))

    p1.start()
    p2.start()
    c1.start()
    p1.join()
    p2.join()

    q.put(None)#结束信号
