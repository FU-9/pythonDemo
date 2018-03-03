from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random

def task():
    print("name %s" %os.getpid())
    time.sleep(random.randint(1,3))

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    # for i in range(10):
    #     pool.submit(task)
    pool.map(task,range(10))

    pool.shutdown(wait=True)#关闭池入口 相当于pool.close()+pool.join()
    print("主")


#线程池同进程池
