from flask import Flask, request
from flask_restful import Api
import Map

app = Flask(__name__)
api = Api(app)

@app.route('/api/reset', methods=['GET'])
def reset():
    return Map.reset()

@app.route('/api/book', methods=['POST'])
def book():
    return Map.book(request.get_json())

@app.route('/api/tick', methods=['GET'])
def tick():
    return Map.tick()

if __name__ == '__main__':
    Map = Map.Map()
    app.run(threaded=True,port=8080)