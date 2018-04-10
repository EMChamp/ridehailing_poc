class Car:
    def __init__(self,car_id):
        self.xPosition = 0
        self.yPosition = 0
        self.car_id = car_id
        self.xPositionPassenger = 0
        self.yPositionPassenger = 0
        self.xPositionDestination = 0
        self.yPositionDestination = 0
        self.goToPassenger = False
        self.goToDestination = False