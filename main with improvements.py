#string =  AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

#Starting program with a string input to define the road map:
string = input("Welcome to TrainRoads! \n"
               "Please enter the coordinates of your map with the format 'AB1, BC3 ...': \n")

class TrainRoads:
	# Class initialization:
	def __init__(self):
		self.graph = {}
		self.start = ''
		self.end = ''
		self.fix_or_max = ''
		self.max_stops = int
		self.fix_stops = int
		self.roadlist = []
		self.final_list = []
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
		return(self.graph)

	def print_graph(self):
		print("The roadmap generated from your coordinates is: \n",self.graph,"\n")

	def distance_between_towns(self):
		path=input("Please enter your path (example: ABCDE) \n")
		# Eliminating undesired characters from the input:
		for i in path:
			if i in " ?.!/;:0123456789":
				path.replace(i,'')
		path=path.upper()
		#Adding the distances between each cities to the total:
		total=0
		try:
			for i in range(len(path)-1):
				total += self.graph.get(path[i]).get(path[i+1])
			print("The total distance for the path %s is %s kilometers.\n" %(path, total))
		except KeyError:
			print("NO SUCH ROUTE")
		except TypeError:
			print("NO SUCH ROUTE")
	
	def requested_inputs(self):
		start_condition=False
		end_condition=False
		set_condition=False
		max_condition=False
		# Asking for input: departure city
		while start_condition==False:
			self.start=input("Please enter the departure city (example: A) \n")
			if len(self.start)==1 and self.start.isalpha():
				start_condition=True
			else:
				print("Your input is incorrect. Please enter only one letter.\n")
		# Asking for input: arrival city
		while end_condition==False:
			self.end=input("Please enter the arrival city (example: D) \n")
			if len(self.end)==1 and self.end.isalpha():
				end_condition=True
			else:
				print("Your input is incorrect. Please enter only one letter.\n")
		# Asking whether the user wants a fixed or a maximum number of stops:
		while set_condition==False:
			self.fix_or_max=input("Do you want all the roads with a fixed number of stops (answer 'fix') or with a maximum number of stops (enter 'max')? \n")
			if self.fix_or_max=='fix' or self.fix_or_max=='Fix' or self.fix_or_max=='FIX' or self.fix_or_max=='max' or self.fix_or_max=='Max' or self.fix_or_max=='MAX':
				set_condition=True
			else:
				print("Your input is incorrect. Please answer with 'fix' or 'max'.\n")
		self.fix_or_max.lower()
		# If the user chose 'maximum', the program asks for the maximum number of stops:
		if self.fix_or_max=='max':
			while max_condition==False:
				self.max_stops=input("Please enter the maximum number of stops from %s to %s:\n" %(self.start.upper(), self.end.upper()))
				if len(self.max_stops)!=0 and int(self.max_stops)<11 and self.max_stops.isdigit():
					max_condition=True
					self.max_stops=int(self.max_stops)
				else:
					print("Your input is incorrect. Please only enter a digit between 1 and 10.\n")
		# If the user chose 'fixed', the program asks for the maximum number of stops:
		elif self.fix_or_max=='fix':
			while max_condition==False:
				self.fix_stops=input("Please enter the fixed number of stops from %s to %s:\n" %(self.start.upper(), self.end.upper()))
				if len(self.fix_stops)!=0 and int(self.fix_stops)<11 and self.fix_stops.isdigit():
					max_condition=True
					self.fix_stops=int(self.fix_stops)
				else:
					print("Your input is incorrect. Please only enter a digit between 1 and 10.\n")	
		self.start=self.start.upper()
		self.end=self.end.upper()
		
	def roadlist_creation(self):	
		# This part creates a list of all possible routes according to the graph:
		graphlist=[]
		for i in self.graph:
			for j in self.graph[i]:
				graphlist.append(i+j)
		# This part checks if the departure city exists on the map:
		if self.start not in [i[0] for i in graphlist]:
			print("There is no city %s on your graph." %(self.start))
		# This part checks if the arrival city exists on the map:
		elif self.end not in [i[1] for i in graphlist]:
			print("The city %s does not exist on your graph." %(self.end))
		else:
		# This part creates all the possible ways between all the cities according to the existing roads with the arrival of interest.
		# I know it's really ugly but that's the best I have so far.
			#roadlist=[]
			for i in graphlist:
				way=i
				if i[1]==self.end:
					if way not in self.roadlist:
						self.roadlist.append(way)
				for j in graphlist:
					if j[0]==i[1]:
						way1=way+j[1]
						if j[1]==self.end:
							if way1 not in self.roadlist:
								self.roadlist.append(way1)			
						for k in graphlist:
							if k[0]==j[1]:
								way2=way1+k[1]
								if k[1]==self.end:
									if way2 not in self.roadlist:
										self.roadlist.append(way2)						
								for l in graphlist:
									if l[0]==k[1]:
										way3=way2+l[1]
										if l[1]==self.end:
											if way3 not in self.roadlist:
												self.roadlist.append(way3)								
										for m in graphlist:
											if m[0]==l[1]:
												way4=way3+m[1]
												if m[1]==self.end:
													if way4 not in self.roadlist:
														self.roadlist.append(way4)									
												for n in graphlist:
													if n[0]==m[1]:
														way5=way4+n[1]
														if n[1]==self.end:
															if way5 not in self.roadlist:
																self.roadlist.append(way5)
														for o in graphlist:
															if o[0]==n[1]:
																way6=way5+o[1]
																if o[1]==self.end:
																	if way6 not in self.roadlist:
																		self.roadlist.append(way6)
																for p in graphlist:
																	if p[0]==o[1]:
																		way7=way6+p[1]
																		if p[1]==self.end:
																			if way7 not in self.roadlist:
																				self.roadlist.append(way7)
																		for q in graphlist:
																			if q[0]==p[1]:
																				way8=way7+q[1]
																				if q[1]==self.end:
																					if way8 not in self.roadlist:
																						self.roadlist.append(way8)
																				for r in graphlist:
																					if r[0]==q[1]:
																						way9=way8+r[1]
																						if r[1]==self.end:
																							if way9 not in self.roadlist:
																								self.roadlist.append(way9)
																						for s in graphlist:
																							if s[0]==r[1]:
																								way10=way9+s[1]
																								if s[1]==self.end:
																									if way10 not in self.roadlist:
																										self.roadlist.append(way10)	
		return(self.roadlist)
	
	def number_of_roads(self):
		# Creating a list with all the possible routes leaving from the departure city of interest:
		startlist=[i for i in self.roadlist if i[0]==self.start]
		if self.fix_or_max=='max':
			# If the user chose maximum, the method prints all the routes from 0 stops to maximum:
			self.final_list=[i for i in startlist if len(i)<=self.max_stops+1]
			print("There are %s roads going from %s to %s with a maximum of %s stops: %s." %(len(self.final_list), self.start, self.end, self.max_stops, self.final_list))
		elif self.fix_or_max=='fix':
			# If the user chose fixed, the method prints only the routes with a fixed number of stops:
			self.final_list=[i for i in startlist if len(i)==self.fix_stops+2]
			print("There are %s roads going from %s to %s with exactly %s stops: %s." %(len(self.final_list), self.start, self.end, self.fix_stops, self.final_list))
	
	def shortest_route(self):
		pass
	
	def routes_with_specified_distance(self):
		pass

#string = AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

objet = TrainRoads()
objet.parser(string)


#_________________________________________________________________________________________________________________


# This last part enables an interaction with the user through a Terminal or an IDE.
# Each possible answer from the user will call a method of the TrainRoads class.
# After each answer given by the called method, the code asks the User if he has another request.
# If he does, the program resumes and another class can be called, if not, the program ends.

while True:
	question = input(">If you want to see the roadmap generated from your input: enter 'A'."
                         "\n>If you want to know the distance of a path between several roads: enter 'B'."
	                 "\n>If you want to know the number of possible roads from one town to another: enter 'C'."
                         "\n>If you want to know the shortest road from one town to another: enter 'D'."
	                 "\n>To quit this program, enter 'EXIT'.\n")
	
	if question=='EXIT' or question=='exit' or question=='Exit':
		print("Thank you for using TrainRoads!")
		break
	
	while question not in "abcdABCD":
		print("INPUT ERROR: %s is not a valid input. Please enter A, B, C or D." %(question))
		question=input(">If you want to see the roadmap generated from your input: enter 'A'."
		               "\n>If you want to know the distance of a path between several roads: enter 'B'."
		               "\n>If you want to know the number of possible roads from one town to another: enter 'C'."
		               "\n>If you want to know the shortest road from one town to another: enter 'D'."
		               "\n>To quit this program, enter 'EXIT'.\n")		
	
	if question=='A' or question=='a':
		objet.print_graph()
		
	elif question=='B' or question=='b':
		objet.distance_between_towns()
		
	elif question=='C' or question=='c':
		objet.requested_inputs()
		objet.roadlist_creation()
		objet.number_of_roads()	
		
	elif question=='D' or question=='d':
		print("This function is still in progress.")
	
	next_question=input("Do you have any other requests? (Yes/No)\n")
	
	while next_question!='Yes' and next_question!='yes' and next_question!='No' and next_question!='no':
		print("Please answer with Yes or No.\n")
		next_question=input("Do you have any other requests? (Yes/No)\n")
	
	if next_question=='Yes' or next_question=='yes':
		pass
	
	elif next_question=='No' or next_question=='no':
		print("Thank you for using TrainRoads!")
		break