Requirements:
Requires Python 3 and Flask framework (install using 'pip install flask', might need to use 'pip3 install flask' if you have python2 installed as well)

Flask Website: http://flask.pocoo.org/docs/dev/installation/

Instructions:
To run the webserver on port 8080, use 'python3 api.py'. 

To run the unit test script use 'python3 test.py'

Endpoints:
/api/tick - Advances the map state by 1 tick and prints out car statistics
/api/reset - Resets all cars on the map to their original state
/api/book - Book a car by sending a JSON-encoded booking object with a format like { "source": { "x": "1", "y": "1" }, "destination": { "x": "3"
, "y": "3" }}, responds with a JSON string indicating car_id and total journey time


