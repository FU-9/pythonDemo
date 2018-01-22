
class Attrbute:
	def __init__(self):
		self.name = "race"

	@property
	def _name(self):
		return "my name is %s" %self.name

	@_name.setter
	def _name(self,name):
		self.name = name

attr = Attrbute()
attr._name = "alex"
print(attr._name)	