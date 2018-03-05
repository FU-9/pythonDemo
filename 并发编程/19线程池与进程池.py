from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random

def task():
    print("name %s" %os.getpid())
    time.sleep(random.randint(1,3))

if __name__ == '__main__':
    pool = ProcessPoolExecutor(4)
    # for i in range(10):
    #     pool.submit(task)
    pool.map(task,(1,2,3,4))

    pool.shutdown(wait=True)#关闭池入口 相当于pool.close()+pool.join()
    print("主")

#submit 异步提交任务
#result 取得结果
#shutdown(wait=True)#关闭池入口 相当于pool.close()+pool.join()
#add_done_callback(fn)回调函数

#线程池同进程池
