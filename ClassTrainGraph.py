#string = AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
string = input("Please enter the coordinates of your map with the format 'AB1, BC3 ...':")


class ClassTrain:
	def __init__(self, string):
		self.string = string
		self.graph = {}
	def parser(self):
		# Loop to detect "letter-letter-digit" patterns from the input and to insert roads in the graph map:
		for i in range(len(self.string)):
			if self.string[i].isalpha() and self.string[i+1].isalpha() and self.string[i+2].isdigit():
				
				# Gathering the "letter-letter-digit" patterns in one string:
				coordinate = ''.join([self.string[i], self.string[i+1], self.string[i+2]])
				full_distance=str(coordinate[2])
				
				# Checking whether the distance is made of more than one digit:
				for n in range(1,len(self.string)-i-2):
					if self.string[i+2+n].isdigit():
						# Appends additional digits if any:
						coordinate = coordinate+"%s" %self.string[i+2+n]
						full_distance= full_distance+"%s" %self.string[i+2+n]
					else:	# Stops appending further characters if downstream characters are non-digit.
						break
				full_distance=int(full_distance)
				# City1 is departure and City2 is arrival.
				# If there is no road departing from City1 in the graph yet:
				if coordinate[0] not in self.graph: 
					self.graph.update({coordinate[0]:{coordinate[1]:full_distance}}) # adds road from City1 to City2
				# If City1 already exists in the graph without any road to City2:
				elif coordinate[1] not in self.graph[coordinate[0]]:
					self.graph[coordinate[0]].update({coordinate[1]:full_distance}) # adds road from City1 to City2
				# If there is already a road from City1 to City2 in the graph, the script keeps the shortest road from City1 to City2:
				elif full_distance < self.graph.get(coordinate[0]).get(coordinate[1]):
					self.graph[coordinate[0]].update({coordinate[1]:full_distance})
				#print(graph.get(coordinate[0]).get(coordinate[1]))
		# Roadmap completed:
		return(self.graph)
	
	#The purpose of this problem is to help the railroad provide its customers with
	#information about the routes. In particular, you will compute the distance along a
	#certain route, the number of different routes between two towns, and the shortest route between two towns.
	

	def print_graph(self):
		print(self.graph)

	def distance_between_two_towns(self):
		depart = input("Please enter a departure point:")
		if depart not in self.graph:
			print("Sorry, there is not road departing from this location.")
			depart = input("Please enter another departure point:")
		arrivee = input("Okay, now please enter an arrival point:")
		if arrivee not in self.graph.get(depart):
			print("Sorry, there is not road leading to this location.")
			arrivee = input("Please enter another arrival point:")
		total=0
		if arrivee in self.graph.get(depart):
			self.distance= self.graph.get(depart).get(arrivee)
			print("The distance between %s and %s is %s" %(depart, arrivee, self.distance))
	#def number_of_roads(self):



objet = ClassTrain(string)
objet.parser()


question = input(">If you want to see the map generated from your input: enter 'map'."
                "\n>If you want to know the distance of a path: type the path if the format 'ABCDE'."
                "\n>If you want to know the number of possible roads from a town to another: enter the two towns with the format '!AC'. \n")


if question == 'map':
	objet.print_graph()
elif question[0].isalpha():
	objet.distance_between_two_towns()	
elif question[0] == '!':
	print("This function is still in progress.")
else:
	print("Sorry, this input does not match any requirements.")