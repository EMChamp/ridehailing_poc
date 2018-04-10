import unittest, Map

class TestMapApp(unittest.TestCase):
	booking = {}
	booking['source'] = {}
	booking['source']['x'] = 1
	booking['source']['y'] = 1
	booking['destination'] = {}
	booking['destination']['x'] = 2
	booking['destination']['y'] = 2

	def test_book(self):
		testMap = Map.Map()
		testMap.book(self.booking)
		assert testMap.carList[0].xPositionPassenger == 1

	def test_tick(self):
		testMap = Map.Map()
		testMap.book(self.booking)
		testMap.tick()
		assert testMap.carList[0].xPosition == 1

	def test_reset(self):
		testMap = Map.Map()
		testMap.book(self.booking)
		testMap.tick()
		testMap.reset()
		assert testMap.carList[0].xPosition == 0

if __name__ == '__main__':
    unittest.main()