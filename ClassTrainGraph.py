#string = AB5, BC4, CD8, dc8, de6, AD5, BD100, CE2, EB3, EA7

string = input("Please enter the coordinates of your map with the format 'AB1, BC3 ...':\n")

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
		
		start=input("Please enter the departure city (example: A) \n")
		while len(start)>1 or len(start)==0 or start.isalpha()==False:
			print("Your input is invalid. Please enter only one letter.\n")
			start=input("Please enter your starting city (example: A) \n")
			
		end=("Please enter your starting city (example: D) \n")
		while len(end)>1 or len(end)==0 or end.isalpha()==False:
			print("Your input is invalid. Please enter only one letter.\n")
			start=input("Please enter your starting city (example: A) \n")
			
		max_stops=("Please enter the maximum number of stops from %s to %s:\n" %(start, end))
		while len(max_stops)==0 or max_stops.isdigit()==False:
			print("Your input is invalid. Please only enter digits.\n")
			max_stops=("Please enter the maximum number of stops from %s to %s:\n" %(start, end))
		
		for k in max_stops:
			
		
		

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
                         "\n>If you want to know the shortest road from one town to another: enter 'D'.\n")
	
	if question == 'A' or question=='a':
		objet.print_graph()
		
	elif question == 'B' or question=='b':
		objet.distance_between_towns()
		
	elif question == 'C' or question=='c':
		print("This function is still in progress.")
		
	elif question == 'D' or question=='d':
		objet.number_of_roads()
		
	else:
		print("Sorry, this input does not match any requirements.\n")
	
	next_question=input("Do you have any other requests? (Yes/No)\n")
	
	if next_question=='Yes' or next_question=='yes':
		pass
	
	elif next_question=='No' or next_question=='no':
		print("Thank you for using TrainRoads!")
		break
	else:
		print("Please answer with Yes or No.")