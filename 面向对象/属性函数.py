
class Attrbute:
	def __init__(self):
		self.name = "race"

	@property
	def get_name(self):
		return "my name is %s" %self.name

attr = Attrbute()
print(attr.get_name)	