class TrainRoads:
	# Class initialization:
	def __init__(self):
		self.graph = {}

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

	def roadlist_creation(self, start, end):
		# This function creates a list of all possible routes according to the graph:
		graphlist=[]
		roadlist=[]
		for i in self.graph:
			for j in self.graph[i]:
				graphlist.append(i+j)
		# This part creates all the possible ways between all the cities according to the existing roads with the arrival of interest.
		# I know it's really ugly for now, I will come back to that part later. It works well but the "for loop" cascade is limited to 11 stops.
		for i in graphlist:
			way=i
			if i[1]==end:
				if way not in roadlist:
					roadlist.append(way)
			for j in graphlist:
				if j[0]==i[1]:
					way1=way+j[1]
					if j[1]==end:
						if way1 not in roadlist:
							roadlist.append(way1)			
					for k in graphlist:
						if k[0]==j[1]:
							way2=way1+k[1]
							if k[1]==end:
								if way2 not in roadlist:
									roadlist.append(way2)						
							for l in graphlist:
								if l[0]==k[1]:
									way3=way2+l[1]
									if l[1]==end:
										if way3 not in roadlist:
											roadlist.append(way3)								
									for m in graphlist:
										if m[0]==l[1]:
											way4=way3+m[1]
											if m[1]==end:
												if way4 not in roadlist:
													roadlist.append(way4)									
											for n in graphlist:
												if n[0]==m[1]:
													way5=way4+n[1]
													if n[1]==end:
														if way5 not in roadlist:
															roadlist.append(way5)
													for o in graphlist:
														if o[0]==n[1]:
															way6=way5+o[1]
															if o[1]==end:
																if way6 not in roadlist:
																	roadlist.append(way6)
															for p in graphlist:
																if p[0]==o[1]:
																	way7=way6+p[1]
																	if p[1]==end:
																		if way7 not in roadlist:
																			roadlist.append(way7)
																	for q in graphlist:
																		if q[0]==p[1]:
																			way8=way7+q[1]
																			if q[1]==end:
																				if way8 not in roadlist:
																					roadlist.append(way8)
																			for r in graphlist:
																				if r[0]==q[1]:
																					way9=way8+r[1]
																					if r[1]==end:
																						if way9 not in roadlist:
																							roadlist.append(way9)
																					for s in graphlist:
																						if s[0]==r[1]:
																							way10=way9+s[1]
																							if s[1]==end:
																								if way10 not in roadlist:
																									roadlist.append(way10)	
		return roadlist
	
	def number_of_roads(self, start, end, fix_or_max, stops):
		roadlist=self.roadlist_creation(start, end)
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
		roadlist=self.roadlist_creation(start, end)
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
		roadlist=self.roadlist_creation(start, end)
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
