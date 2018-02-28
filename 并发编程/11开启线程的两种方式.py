# 方式一
# from threading import Thread
#
# def Thread_():
#     print('开启了一个线程')
#
#
# if __name__ == '__main__':
#     T = Thread(target=Thread_)
#     T.start()
#     print('主线程')


# 方式二
from threading import Thread

class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('开了一个线程')


if __name__ == '__main__':
    t1 = MyThread('race')
    t1.start()
    print('主')
