from threading import Thread,currentThread,active_count,enumerate
import time

def task():
    print('%s is running'%currentThread().getName())#获取进程名
    time.sleep(3)
    print('%s is done'%currentThread().getName())

if __name__ == '__main__':
    t = Thread(target=task,name="线程")
    t.start()
    t.daemon = True #设置为守护进程
    print(t.isAlive())#线程是否存活
    t.setName('更改线程名')
    print(active_count())#活跃进程数
    print(enumerate())#活跃线程对象
    t.join()#将进程运行方式变为串行

    print('主')
