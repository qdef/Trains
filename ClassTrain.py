from ParserFunction import parser

string="AB5, EF4, ED12, CD15, AF7, EF56, , EA4, AC1, AC56, AD4, CD8, EF45"

class GraphBuilder:
	def __init__(self, string):
		self.string = string
		self.graph = graph
				
	def parser(self):
		self.graph = parser(self.string)
	
a=GraphBuilder(string)
a.parser()
print(a.graph)

