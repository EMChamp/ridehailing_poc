from flask import Flask, request
from flask_restful import Api
import json

app = Flask(__name__)
api = Api(app)

class Map:
    def __init__(self):
        self.testVal = 0
        self.xPositionMax = self.yPositionMax =  2147483647
        self.xPositionMin = self.yPositionMin = -2147483648
        self.carList = [Car(i) for i in range(1,4)]

    def calcDistance(self, initialX, initialY, finalX, finalY):
        initialX = int(initialX)
        initialY = int(initialY)
        finalX = int(finalX)
        finalY = int(finalY)
        return abs(initialX - finalX) + abs(initialY - finalY)

    def tick(self):
        for car in self.carList:
            self.moveCar(car)

        return self.printCarLocations()

    def moveCar(self,car):
        # Go to passenger first, then go to destination
        if car.goToPassenger:
            if(car.xPosition < car.xPositionPassenger):
                car.xPosition += 1
                return
            elif(car.xPosition > car.xPositionPassenger):
                car.xPosition -= 1
                return
            elif(car.yPosition < car.yPositionPassenger):
                car.yPosition += 1
                return
            elif(car.yPosition > car.yPositionPassenger):
                car.yPosition -= 1
            else:
                car.goToPassenger = False
                car.goToDestination = True
        
        if car.goToDestination:
            if(car.xPosition < car.xPositionDestination):
                car.xPosition += 1
            elif(car.xPosition > car.xPositionDestination):
                car.xPosition -= 1
            elif(car.yPosition < car.yPositionDestination):
                car.yPosition += 1
                return
            elif(car.yPosition > car.yPositionDestination):
                car.yPosition -= 1
            else:
                car.goToDestination = False

        return

    def isValidCoordinates(self, xPositionPassenger, yPositionPassenger, xPositionDestination, yPositionDestination):
        coordinateList = [xPositionPassenger, yPositionPassenger, xPositionDestination, yPositionDestination]
        return all([x < self.xPositionMax and x > self.xPositionMin for x in coordinateList])

    def book(self, booking):
        try:
            xPositionPassenger = int(booking['source']['x'])
            yPositionPassenger = int(booking['source']['y'])
            xPositionDestination = int(booking['destination']['x'])
            yPositionDestination = int(booking['destination']['y'])
        except:
            return 'Error: Could not convert booking to valid ints'

        if not self.isValidCoordinates(xPositionPassenger, yPositionPassenger, xPositionDestination, yPositionDestination):
            return 'Error: Coordinates not in range'


        distances = []
        for i in range(0,len(self.carList)):
            carDistanceFromPassenger = self.calcDistance(self.carList[i].xPosition, self.carList[i].yPosition, xPositionPassenger, yPositionPassenger)
            distances.append((carDistanceFromPassenger,i))

        distances.sort(key=lambda tup: tup[1])

        carBooking = {}
        for i in range(0,len(distances)):
            if self.carList[i].goToPassenger == False and self.carList[i].goToDestination == False:
                carBooking['car_id'] = i
                carToPassenger = self.calcDistance(self.carList[i].xPosition, self.carList[i].yPosition, xPositionPassenger, yPositionPassenger)
                passengerToDestination = self.calcDistance(xPositionPassenger, yPositionPassenger, xPositionDestination, yPositionDestination)
                carBooking['total_time'] = carToPassenger + passengerToDestination
                self.carList[i].goToPassenger = True
                self.carList[i].xPositionPassenger = xPositionPassenger
                self.carList[i].yPositionPassenger = yPositionPassenger
                self.carList[i].xPositionDestination = xPositionDestination
                self.carList[i].yPositionDestination = yPositionDestination
                break


        return json.dumps(carBooking)

    def reset(self):
        self.carList = [Car(i) for i in range(1,4)]
        return 'Map successfully reset'

    def printCarLocations(self):
        carLocations = ''
        for car in self.carList:
            carLocations += ("car_id " + str(car.car_id) + "<br />")
            carLocations += ("car x destination " + str(car.xPositionDestination) + "<br />")
            carLocations += ("car y destination " + str(car.yPositionDestination) + "<br />")
            carLocations += ("car x passenger " + str(car.xPositionPassenger) + "<br />")
            carLocations += ("car y passenger " + str(car.yPositionPassenger) + "<br />")
            carLocations += ("car x position " + str(car.xPosition) + "<br />")
            carLocations += ("car y position " + str(car.yPosition) + "<br />")

        return carLocations

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

class Booking:
    def __init__(self,xPositionDestination,yPositionDestination):
        self.xPositionDestination = xPositionDestination
        self.yPositionDestination = yPositionDestination

@app.route('/api/reset', methods=['GET'])
def reset():
    return Map.reset()

@app.route('/api/book', methods=['POST'])
def book():
    return Map.book(request.get_json())

@app.route('/api/tick', methods=['GET'])
def tick():
    return Map.tick()

@app.route('/api/print', methods=['GET'])
def printCarLocations():
    return Map.printCarLocations()

if __name__ == '__main__':
    Map = Map()
    app.run(threaded=True)