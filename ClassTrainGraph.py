string="AB50, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"

class ClassTrain:
	def __init__(self, string):
		self.string = string
		self.graph = {}
		distance= int
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
				# City1 is departure and City2 is arrival:
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
	
	def distance_route(self):
		depart = input("Please enter a departure point:")
		if depart not in self.graph:
			print("Sorry, there is not road departing from this location.")
			depart = input("Please enter a departure point:")
		arrivee = input("Please enter an arrival point:")
		if arrivee not in self.graph.get(depart):
			print("Sorry, there is not road leading to this location.")
			arrivee = input("Please enter another arrival point:")
		total=0
		if arrivee in self.graph.get(depart):
			self.distance= self.graph.get(depart).get(arrivee)
			return self.distance

			#for k in self.graph[depart]:
				#if arrivee in self.graph[depart]:
	

objet = ClassTrain(string)
objet.parser()
objet.distance_route()
print(objet.distance)