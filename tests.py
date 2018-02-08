import unittest
from main import TrainRoads

class TestRoads(unittest.TestCase):

	def setUp(self):
		string ="AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
		self.railroad = TrainRoads()
		self.railroad.parser(string)
		self.railroad.roadlist_creation()
	
	def verify_graph(self, string):
		self.assertEqual(self.railroad.parser("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"), {'A': {'B': 5, 'D': 5, 'E': 7}, 'B': {'C': 4}, 'C': {'D': 8, 'E': 2}, 'D': {'C': 8, 'E': 6}, 'E': {'B': 3}})
		

	def test_distance(self):
		# Tests for questions 1 to 5:
		self.assertEqual(self.railroad.distance_between_towns("ABC"), 9)
		self.assertEqual(self.railroad.distance_between_towns("AD"), 5)
		self.assertEqual(self.railroad.distance_between_towns("ADC"), 13)
		self.assertEqual(self.railroad.distance_between_towns("AEBCD"), 22)
		self.assertEqual(self.railroad.distance_between_towns("AED"), "NO SUCH ROUTE")
	
	def test_number(self):
		# Tests for questions 6 and 7:
		self.assertEqual(self.railroad.number_of_roads('C', 'C', 'max', 3), 2)
		self.assertEqual(self.railroad.number_of_roads('A', 'C', 'fix', 4), 3)
	
	def test_shortest(self):
		# Tests for questions 8 and 9:
		self.assertEqual(self.railroad.shortest_route('A', 'C'), 9)
		self.assertEqual(self.railroad.shortest_route('B', 'B'), 9)
		
	def test_specific_distance(self):
		# Test for questions 10:
		self.assertEqual(self.railroad.routes_with_specified_distance('C', 'C', 30), 7)
	
if __name__ == '__main__':
	unittest.main()