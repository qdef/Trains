#string =  AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7, AK8, IK27, OK78, HG8, FJ9, fr5 gv2 rf3 ze1

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
			print("The total distance for the path %s is %s.\n" %(path, total))
		except KeyError:
			print("NO SUCH ROUTE")
		except TypeError:
			print("NO SUCH ROUTE")
	
	
	def number_of_roads(self):
		start_condition=False
		end_condition=False
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
		
		while max_condition==False:
			max_stops=input("Please enter the maximum number of stops from %s to %s:\n" %(start.upper(), end.upper()))
			if len(max_stops)!=0 and max_stops.isdigit():
				max_condition=True
			else:
				print("Your input is incorrect. Please only enter digits.\n")
		
		start=start.upper()
		end=end.upper()
		max_stops=int(max_stops)
		
		if start not in self.graph:
			print("There is no route departing from %s." %(start))
		
		liste=[]
		way=''
		self.graph.get(start).value()
		
		
		
		for i in self.graph:
			for k in range(max_stops-1):
				way=(self.graph.get(i[k]).get(i[k+1]))
				if way[i]==start and way[k]==end:
					liste.append(way)
		print(liste)

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