# from threading import Timer
#
# def task(name):
#     print('hello %s'%name)
#
# t = Timer(1,task,args=('race',))
# t.start()

from threading import Timer
import random

class Code:
    def __init__(self):
        self.make_cache()

    def make_cache(self,interval=2):
        self.cache = self.make_code()
        print(self.cache)
        self.t = Timer(interval,self.make_cache)
        self.t.start()

    def make_code(self,n=4):
        res = ''
        for i in range(n):
            s1 = str(random.randint(1,9))
            res += s1
        return res

    def check(self):
        while True:
            code = input('>>>:').strip()
            if code.upper() == self.cache:
                print("success")
                self.t.cancel()
                break



obj = Code()
obj.check()
