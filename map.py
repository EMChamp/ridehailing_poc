class Map:

	def __init__(self):
		self.xPositionMax = 100
		self.yPositionMax = 100



class Car:

	def __init__(self):
		self.xPosition = 0
		self.yPosition = 0

		self.xPositionDestination = None
		self.xPositionDestination = None


carList = [Car() for i in range(3)]

for car in carList:
	print(car.xPosition) 