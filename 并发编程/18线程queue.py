import queue

#第一种用法 先进先出
# q = queue.Queue(3)
# q.put('1')
# q.put('2')
# q.put('3')
#
# q.get()
# q.get()
# q.get()

#第二种用法 堆栈 后进先出
#
# q = queue.LifoQueue()
# q.put('1')
# q.put('2')
# q.put('3')
#
# q.get()#3
# q.get()#2
# q.get()#1

# 第三种用法 优先级队列
q = queue.PriorityQueue()
#put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((20,'a'))
q.put((10,'b'))
q.put((30,'c'))

print(q.get())#(10, 'b')
print(q.get())#(20, 'a')
print(q.get())#(30, 'c')
