from multiprocessing import Queue
q = Queue(3)

q.put('hello')#往队列里放入数据
q.put('word')

print(q.full())#判断队列满了吗


q.get()#在队列中取数据

print(q.empty())#队列是否为空

print(q.get())
