import unittest
from main import TrainRoads

class RailroadTest(unittest.TestCase):

	def setUp(self):
		string ="AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
		self.railroad = RailRoad()
		self.railroad.build(string)


	def test_distance(self):
		# Test 1:
		self.assertEqual(self.distance_between_towns("ABC"),9)

	"""def test_searchpath_1(self):
		dico_test = {}
		self.railroad.search_paths( '', 'A', 0, 1, dico_test)
		self.assertEqual(dico_test, {'A': 0, 'AB' : 5, 'AD' : 5, 'AE' : 7})


	def test_searchpath_2(self):
		dico_test = {}
		self.railroad.search_paths( '', 'A', 0, 2, dico_test)
		self.assertEqual(dico_test, {'A': 0, 'AB' : 5, 'AD' : 5, 'AE' : 7, 'ABC' : 9, 'AEB' : 10, 'ADE' : 11, 'ADC': 13 })

	def test_possibles(self):
		self.assertEqual(self.railroad.possibles('A', 2),{'A': 0, 'AB' : 5, 'AD' : 5, 'AE' : 7, 'ABC' : 9, 'AEB' : 10, 'ADE' : 11, 'ADC': 13 } )


	def test_depart_arrival(self):
		self.assertEqual(self.railroad.depart_arrival('C', 'C', 3), {'CEBC': 9, 'CDC': 16, 'C':0})

	def test_dep_arr_stops(self):
		self.assertEqual(self.railroad.dep_arr_stops('C', 'C', 3), {'CEBC': 9})


	# Test 6 :
	def test6(self):
		self.assertEqual(len(self.railroad.depart_arrival('C', 'C', 3))-1, 2)

	# Test 7 :
	def test7(self):
		self.assertEqual(len(self.railroad.dep_arr_stops('A', 'C', 4)),3)

	# Test 8 :
	def test8(self):
		self.assertEqual(self.railroad.dist_min('A', 'C'),9)


	# Test 9 :
	def test9(self):
		self.assertEqual(self.railroad.dist_min('C', 'C'),9)

	# Test 10 :
	def test10(self):
		self.assertEqual(self.railroad.nb_chemin_max('C', 'C',30)-1,7)"""

if __name__ == '__main__':
	unittest.main()