import unittest, app

class TestMapApps(unittest.TestCase):
	def test_book(self):
		booking = {}
		booking['source'] = 1
		booking['source'] = 1
		booking['destination'] = 2
		booking['destination'] = 2
		testMap = app.Map()
		testMap.bookCar(booking)
		assert testMap.carList[0].xPositionPassenger == 1

if __name__ == '__main__':
    unittest.main()