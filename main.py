class TrainRoads:
	# Class initialization:
	def __init__(self):
		self.graph = {}
		self.roadlist= []
	def parser(self, string):
		# Loop to detect "letter-letter-digit" patterns from the input and to insert roads in the graph map:
		for i in range(len(string)):
			if string[i].isalpha() and string[i+1].isalpha() and string[i+2].isdigit():
				
				# Gathering the "letter-letter-digit" patterns in one string:
				coordinate = ''.join([string[i], string[i+1], string[i+2]])
				full_distance=str(coordinate[2])
				
				# Checking whether the distance is made of more than one digit:
				for n in range(1,len(string)-i-2):
					if string[i+2+n].isdigit():
						# Appends additional digits if any:
						coordinate = coordinate+"%s" %string[i+2+n]
						full_distance= full_distance+"%s" %string[i+2+n]
					else:	# Stops appending further characters if downstream characters are non-digit.
						break
				full_distance=int(full_distance)
				coordinate=coordinate.upper()
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
		return self.graph

	def distance_between_towns(self, path):
		# Eliminating undesired characters from the input:
		for i in path:
			if i in " -?.!/;:0123456789":
				path.replace(i,'')
		path=path.upper()
		#Adding the distances between each cities to the total:
		total=0
		try:
			for i in range(len(path)-1):
				total += self.graph.get(path[i]).get(path[i+1])
			return total
		except KeyError:
			return "NO SUCH ROUTE"
		except TypeError:
			return "NO SUCH ROUTE"

	def roadlist_creation(self):
		# This function creates a list of all possible roads between towns according to the graph:
		graphlist=[]
		for i in self.graph:
			for j in self.graph[i]:
				graphlist.append(i+j)				
		# This part creates all the possible ways between all the cities according to existing roads on the graph:
		self.roadlist=graphlist
		for i in self.roadlist:
			# This limit avoids the list of possible routes to be infinite, it can be set to a higher or lower value if needed:
			if len(i)==12:
				break
			else:
				for j in graphlist:
					if j[0]==i[-1]:
						way = ''.join([i, j[1]])
						if way not in self.roadlist:
							self.roadlist.append(way)
		return self.roadlist
	
	def number_of_roads(self, start, end, fix_or_max, stops):
		roadlist=self.roadlist
		# This part checks if the selected cities are accessible on the graph. If not, the function returns NO SUCH ROUTE.
		graphlist=[]
		for i in self.graph:
			for j in self.graph[i]:
				graphlist.append(i+j)
		if start not in [i[0] for i in graphlist]:
			return "NO SUCH ROUTE"
		elif end not in [i[1] for i in graphlist]:
			return "NO SUCH ROUTE"
		else:
			try:
				# Creating a list with all the possible routes leaving from the departure city of interest:
				startlist=[i for i in roadlist if i[0]==start]
				# Verifying again that all routes end with the right end city:
				checklist=[i for i in startlist if i[-1]==end]
				if fix_or_max=='max':
					# If the user chose maximum, the method prints all the routes from 0 stops to maximum:
					final_list=[i for i in checklist if len(i)<=stops+1]
					return len(final_list)
				elif fix_or_max=='fix':
					# If the user chose fixed, the method prints only the routes with a fixed number of stops:
					final_list=[i for i in checklist if len(i)==stops+1]
					return len(final_list)
			except:
				return "The program could not calculate the number of routes with this input."
	
	def shortest_route(self, start, end):
		roadlist=self.roadlist
		# This part checks if the selected cities are accessible on the graph. If not, the function returns NO SUCH ROUTE.
		graphlist=[]
		for i in self.graph:
			for j in self.graph[i]:
				graphlist.append(i+j)
		if start not in [i[0] for i in graphlist]:
			return "NO SUCH ROUTE"
		elif end not in [i[1] for i in graphlist]:
			return "NO SUCH ROUTE"
		else:
			try:
				# Keeping only the routes starting with the defined city:
				startlist=[i for i in roadlist if i[0]==start]
				# Verifying again that all routes end with the right end city:
				checklist=[i for i in startlist if i[-1]==end]
				distance_list=[]
				# Calculating all the distances for the possible routes from start city to end city:
				for i in checklist:
					total=0
					for j in range(len(i)-1):
						# The distances are obtained from the original graph:
						total += self.graph.get(i[j]).get(i[j+1])
					# The empty list is filled the distances of all possible routes:	
					distance_list.append(total)
				# To determine the shortest distance of all routes:
				shortest=min(distance_list)
				return shortest
			except:
				return "The program could not calculate the shortest route with this input."
	
	def routes_with_specified_distance(self, start, end, max_distance):
		roadlist=self.roadlist
		# This part checks if the selected cities are accessible on the graph. If not, the function returns NO SUCH ROUTE.
		graphlist=[]
		for i in self.graph:
			for j in self.graph[i]:
				graphlist.append(i+j)
		if start not in [i[0] for i in graphlist]:
			return "NO SUCH ROUTE"
		elif end not in [i[1] for i in graphlist]:
			return "NO SUCH ROUTE"
		else:
			try:		
				# Keeping only the routes starting with the defined city:
				startlist=[i for i in roadlist if i[0]==start]
				# Verifying again that all routes end with the right end city:
				checklist=[i for i in startlist if i[-1]==end]
				# Calculating all the distances for the possible routes from start city to end city:
				distance_list=[]
				for i in checklist:
					total=0
					for j in range(len(i)-1):
						# The distances are obtained from the original graph:
						total += self.graph.get(i[j]).get(i[j+1])
					# The empty list is filled the distances of all possible routes:	
					distance_list.append(total)					
				restricted_list = [i for i in distance_list if i<max_distance]
				return len(restricted_list)
			except:
				return "The program could not calculate the number of routes with this input."			

# Object creation:
objet = TrainRoads()

# Calling function that returns the graph:
objet.parser("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")
# Calling function that creates all possibles roads from graph:
objet.roadlist_creation()
# Question 1
print(objet.distance_between_towns("ABC"))
# Question 2
print(objet.distance_between_towns("AD"))
# Question 3
print(objet.distance_between_towns("ADC"))
# Question 4
print(objet.distance_between_towns("AEBCD"))
# Question 5
print(objet.distance_between_towns("AED"))
# Question 6
print(objet.number_of_roads('C', 'C', 'max', 3))
# Question 7
print(objet.number_of_roads('A', 'C', 'fix', 4))
#Question 8: The length of the shortest route (in terms of distance to travel) from A to C.
print(objet.shortest_route('A', 'C'))
#Question 9: The length of the shortest route (in terms of distance to travel) from B to B.
print(objet.shortest_route('B', 'B'))
#Question10: The number of different routes from C to C with a distance of less than 30.
print(objet.routes_with_specified_distance('C', 'C', 30))
