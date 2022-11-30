import node_stack
import random

class Task:
	__slots__=["__name", "__location"]

	def __init__(self, name, location):
		self.__name = name
		self.__location = location

	def get_location(self):
		return self.__location
	

	def __str__ (self):
		return f"{self.__name} in {self.__location} "
	def __repr__(self):
		return f"{self.__name} in {self.__location}"

def parse_Tasks(file):
	tasks = []
	a = ""
	with  open(file,'r') as f:
		for i in f.readlines():
			j = ((i.split(",")))
			task = Task(j[0] , j[1].strip())
			tasks.append(task)
			# a = a+n+" in " + l
	print(a)
	return tasks



class Crewmate:
	__slots__=["__color", "__tasks"]
	
	def __init__ (self,color):
		
		self.__color = color
		self.__tasks=node_stack.Stack()

	def assign_task(self,task):
		self.__tasks.push(task)

	def next_task(self):
		return self.__tasks.pop()

	def __str__ (self):
		String = self.__color + "crewmate"
		if self.__murdered:
			String += "(deceased)"
		return String
	def __repr__(self) -> str:
		print("Crewmate:")
		print(f"    color={self.__color}" )
		print(f"    murdered={self.__color}" )
		print(f"    tasks={self.__tasks}" )


class Ship:
	__slots__ = ["__locations", "__tasks" , "__colours" , "__cafetaria" ]
	
	def __init__ (self,tasks , imposters = 1 ):
		self.__colours = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White",  "Yellow"]
		random.shuffle(self.__colours)
		self.__tasks = tasks
		self.__locations= dict()

		if(imposters>4 or imposters < 1):
			raise ValueError
		crewmates = 10 - imposters	

		for task in tasks:
			location = task.get_location()
			if(location not in self.__locations.keys()):
				self.__locations[task.get_location()] = []
				# self.__locations[task.get_location()].append(task)
			self.__locations[task.get_location()].append(task)
		
		for i in range(crewmates):
			crew = Crewmate(self.__colours.pop())
			n_of_task = random.randint(3,6)
			for i in range(n_of_task):
				crew.assign_task(self.__tasks.pop())
		locations = self.__locations


	def get_locations(self):
		return self.__locations

p = parse_Tasks('tasks_01.csv')
s = Ship(p)
print(s.get_locations())