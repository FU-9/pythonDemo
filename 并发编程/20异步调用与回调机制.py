#提交任务的两种方式
#同步调用：提交任务后，就在原地等待任务执行完毕，拿到结果，在执行下一行代码，导致程序是串行执行

#异步执行：提交完任务后不在等待任务执行完毕
from concurrent.futures import ThreadPoolExecutor
import time,random
def la(name):
    print('%s is laing'%name)
    time.sleep(random.randint(1,3))
    res = random.randint(10,20)
    return {"name":name,"res":res}

def weight(shit):
    shit = shit.result()
    name = shit.get('name')
    size = shit.get('res')
    print("%s la <%s>"%(name,size))

if __name__ == '__main__':
    pool = ThreadPoolExecutor(10)
    pool.submit(la,'alex').add_done_callback(weight)
