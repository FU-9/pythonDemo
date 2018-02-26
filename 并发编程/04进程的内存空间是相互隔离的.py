from multiprocessing import Process

n = 100

def task():
    global n
    n = 0
    print("子进程：",n)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.join()
    print("主进程：",n)
