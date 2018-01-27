class Box(object):
	"""docstring for Box"""
	count = 0
	def __init__(self):
		self.length = 0
		self.width = 0
		self.height = 0
		self.__d = 0
		self.addCount()

	def getD(self):
		self.__d = self.length * self.width * self.height
		print('d',self.__d)

	def addCount(self):
		Box.count += 1
		
box1 = Box()
box1.length = 1
box1.width = 1
box1.height = 1
box1.getD()
box1.count = 1
print('count',Box.count)	

box2 = Box()
box2.length = 2
box2.width = 2
box2.height = 1
box2.getD()
print('count',box2.count)		