#string="AB5, AC6, AB4, AB45, AB2, AE78, BC45, AG6700, AB1, AZ54, *$-these symbols do not prevent pattern search|'_\/ AB4 AB13 AB4654AB3ZE44 #even without commas or spaces# YT76, TB4, BU75, CD18"

def parser(string):
	graph={}
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
			# City1 is departure and City2 is arrival:
			# If there is no road departing from City1 in the graph yet:
			if coordinate[0] not in graph: 
				graph.update({coordinate[0]:{coordinate[1]:full_distance}}) # adds road from City1 to City2
			# If City1 already exists in the graph without any road to City2:
			elif coordinate[1] not in graph[coordinate[0]]:
				graph[coordinate[0]].update({coordinate[1]:full_distance}) # adds road from City1 to City2
			# If there is already a road from City1 to City2 in the graph, the script keeps the shortest road from City1 to City2:
			elif full_distance < graph.get(coordinate[0]).get(coordinate[1]):
				graph[coordinate[0]].update({coordinate[1]:full_distance})
			#print(graph.get(coordinate[0]).get(coordinate[1]))
	# Roadmap completed:
	return(graph)

#print(parser(string))