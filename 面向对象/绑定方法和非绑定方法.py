
class Animal:
	
	def __init__(self):
		self.name = "race"

	#绑定方法 绑定到类
	@classmethod
	def go(self):
		print("go go go ...")

	#非绑定方法 谁都可以调用 不自动传值
	@staticmethod
	def talk():
		return "animal class"


Animal().go()

people = Animal()
people.talk()
