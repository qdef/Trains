#string =  AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7

string = input("Welcome to TrainRoads! \n"
               "Please enter the coordinates of your map with the format 'AB1, BC3 ...': \n")

class TrainRoads:
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
	
	def number_of_roads(self):
		start_condition=False
		end_condition=False
		set_condition=False
		max_condition=False
		# Asking for inputs: departure city, arrival city and number of maximum stops:
		while start_condition==False:
			start=input("Please enter the departure city (example: A) \n")
			if len(start)==1 and start.isalpha():
				start_condition=True
			else:
				print("Your input is incorrect. Please enter only one letter.\n")
		while end_condition==False:
			end=input("Please enter the arrival city (example: D) \n")
			if len(end)==1 and end.isalpha():
				end_condition=True
			else:
				print("Your input is incorrect. Please enter only one letter.\n")
		while set_condition==False:
			fix_or_max=input("Do you want all the roads with a fixed number of stops (answer 'fix') or with a maximum number of stops (enter 'max')? \n")
			if fix_or_max=='fix' or fix_or_max=='Fix' or fix_or_max=='FIX' or fix_or_max=='max' or fix_or_max=='Max' or fix_or_max=='MAX':
				set_condition=True
			else:
				print("Your input is incorrect. Please answer with 'fix' or 'max'.\n")
		fix_or_max.lower()
		if fix_or_max=='max':
			while max_condition==False:
				max_stops=input("Please enter the maximum number of stops from %s to %s:\n" %(start.upper(), end.upper()))
				if len(max_stops)!=0 and int(max_stops)<11 and max_stops.isdigit():
					max_condition=True
					max_stops=int(max_stops)
				else:
					print("Your input is incorrect. Please only enter a digit between 1 and 10.\n")
		elif fix_or_max=='fix':
			while max_condition==False:
				fix_stops=input("Please enter the fixed number of stops from %s to %s:\n" %(start.upper(), end.upper()))
				if len(fix_stops)!=0 and int(fix_stops)<11 and fix_stops.isdigit():
					max_condition=True
					fix_stops=int(fix_stops)
				else:
					print("Your input is incorrect. Please only enter a digit between 1 and 10.\n")	
		start=start.upper()
		end=end.upper()
		
		
		# This part creates a list of all possible routes according to the graph:
		graphlist=[]
		for i in self.graph:
			for j in self.graph[i]:
				graphlist.append(i+j)
		# This part checks if the departure city exists on the map:
		if start not in [i[0] for i in graphlist]:
			print("There is no city %s on your graph." %(start))
		# This part checks if the arrival city exists on the map:
		elif end not in [i[1] for i in graphlist]:
			print("The city %s does not exist on your graph." %(end))
		else:
		# This part creates all the possible ways between all the cities according to the existing roads with the arrival of interest.
		# I know it's really ugly but that's the best I have so far.
			roadlist=[]
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
			# Creating a list with all the possible routes leaving from the departure city of interest:
			startlist=[i for i in roadlist if i[0]==start]
			if fix_or_max=='max':
				final_list=[i for i in startlist if len(i)<=max_stops+1]
				print("There are %s roads going from %s to %s with a maximum of %s stops: %s." %(len(final_list), start, end, max_stops, final_list))
			elif fix_or_max=='fix':
				final_list=[i for i in startlist if len(i)==fix_stops+1]
				print("There are %s roads going from %s to %s with exactly %s stops: %s." %(len(final_list), start, end, fix_stops, final_list))


#string = AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
# self.graph = {'A': {'B': 5, 'D': 5, 'E': 7}, 'B': {'C': 4}, 'C': {'D': 8, 'E': 2}, 'D': {'C': 8, 'E': 6}, 'E': {'B': 3}} 
	

objet = TrainRoads(string)
objet.parser()


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