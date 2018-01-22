a = iter(range(10))

try:
	for i in range(100):
		print(next(a))
except StopIteration as e:
	# 检测到异常时执行
	print('except')
else:
	# 代码块没有异常时执行
	print('else')
finally:
	# 是否有异常都会执行
	print("finally")

# 主动触发异常
# raise TypeError('类型错误')

count = 0
while True:
	count += 1
	assert 3 > count
	print(count)