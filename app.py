from flask import Flask, request
from flask_restful import Resource, Api
import json

#Create a engine for connecting to SQLite3.
#Assuming salaries.db is in your app root folder


app = Flask(__name__)
api = Api(app)

class Map:
    def __init__(self):
        self.testVal = 0
        self.xPositionMax = self.yPositionMax =  2147483647
        self.xPositionMin = self.yPositionMin  = -2147483648
        self.carList = [Car(i) for i in range(1,4)]

    def calcDistance(self, initialX, initialY, finalX, finalY):
        return abs(initialX - finalX) + abs(initialY - finalY)

    def tick(self):
        for car in self.carList:
            self.moveCar(car)
        return 'Map tick occured'

    def moveCar(self,car):
        if(car.xPosition < car.xPositionDestination):
            car.xPosition += 1
        elif(car.xPosition > car.xPositionDestination):
            car.xPosition -= 1
        elif(car.yPosition < car.yPositionDestination):
            car.yPosition += 1
        elif(car.yPosition > car.yPositionDestination):
            car.yPosition -= 1
        
        if(car.xPosition == car.xPositionDestination and car.yPosition == car.yPositionDestination):
            car.available = True

    def book(self, booking):
        distances = []
        for i in range(0,len(self.carList)):
            carDistanceFromDestination = self.calcDistance(self.carList[i].xPosition, self.carList[i].yPosition, self.carList[i].xPositionDestination, self.carList[i].yPositionDestination)
            distances.append((carDistanceFromDestination,i))

        distances.sort(key=lambda tup: tup[1])

        
        carBooking = {}
        for i in range(0,len(distances)):
            if self.carList[i].available == True:
                carBooking['car_id'] = i
                carBooking['total_time'] = distances[i]
                self.carList[i].available = False
                self.carList[i].xPositionDestination = booking.xPositionDestination
                self.carList[i].yPositionDestination = booking.yPositionDestination
                break


        return json.dumps(carBooking)

    def reset(self):
        self.carList = [Car(i) for i in range(1,4)]
        return 'Map successfully reset'

    def printCarLocations(self):
        for car in self.carList:
            print("car_id ",car.car_id) 
            print("car x destination ",car.xPositionDestination) 
            print("car y destination ",car.yPositionDestination)
            print("car x position ",car.xPosition) 
            print("car y position ",car.yPosition) 


    def incrTestVal(self):
        self.testVal += 1
        return self.printTestVal()

    def printTestVal(self):
        data = {}
        data['testVal'] = self.testVal
        return json.dumps(data)

class Car:
    def __init__(self,car_id):
        self.xPosition = 0
        self.yPosition = 0
        self.car_id = car_id
        self.xPositionDestination = 0
        self.yPositionDestination = 0
        self.available = True

class Booking:
    def __init__(self,xPositionDestination,yPositionDestination):
        self.xPositionDestination = xPositionDestination
        self.yPositionDestination = yPositionDestination


Map = Map()

'''
Booking = Booking(2,2)
Map.bookCar(Booking)
Map.printCarLocations()
Map.tick()
Map.tick()
Map.tick()
Map.tick()
Map.printCarLocations()
'''

@app.route('/api/reset', methods=['GET'])
def reset():
    return Map.reset()

@app.route('/api/book', methods=['POST'])
def book():
    data = request.get_json()
    return json.dumps(data)

@app.route('/api/tick', methods=['GET'])
def tick():
    return Map.tick()

@app.route('/api/printTestVal', methods=['GET'])
def testVal():
    return Map.printTestVal()

@app.route('/api/incrTestVal', methods=['GET'])
def incrTestVal():
    return Map.incrTestVal()


if __name__ == '__main__':
     app.run()