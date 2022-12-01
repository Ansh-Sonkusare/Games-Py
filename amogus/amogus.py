import node_stack
import random
import array_queue
import math
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
	__slots__=["__color", "__tasks" ,"__murdered"]
	
	def __init__ (self,color):
		self.__murdered = False
		self.__color = color
		self.__tasks=node_stack.Stack()

	def assign_task(self,task):
		self.__tasks.push(task)

	def next_task(self):
		return self.__tasks.pop()
	def kill(self):
		self.__murdered = True
		return 
	def __str__ (self):
		String = self.__color + " crewmate"
		if self.__murdered:
			String += "(deceased)"
		return String
	def __repr__(self) -> str:
		return f"Crewmate:\n\
	color={self.__color} \n\
	murdered={self.__color} \n\
	tasks={self.__tasks}" 


class Ship:
	__slots__ = ["__locations", "__tasks" , "__cafetaria"  , "__locs_2" , "__survived" , "__murdered"]
	
	def __init__ (self,tasks , imposters = 1 ):


		# initialisation
		self.__locs_2 = dict()
		self.__survived = []
		self.__murdered = []
		__colours = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White",  "Yellow"]
		random.shuffle(__colours)
		self.__tasks = tasks
		self.__locations= dict()
		self.__cafetaria = array_queue.Queue()

		if(imposters>4 or imposters < 1):
			raise ValueError
		crewmates = 10 - imposters	

		# for task in tasks:
		# 	location = task.get_location()
		# 	if(location not in self.__locations.keys()):
		# 		self.__locations[task.get_location()] = []
		# 		# self.__locations[task.get_location()].append(task)
		# 	self.__locations[task.get_location()].append(task)
		tasks_per_crew = math.ceil(len(self.__tasks)/crewmates)


	
		for i in range(crewmates):
			# print(len(self.__tasks))
			if(len(self.__tasks) <= 0):
				break
			crew = Crewmate(__colours.pop())
			n_of_task = random.randint(tasks_per_crew,6)
			# print(n_of_task)
			for i in range(n_of_task):
				if(len(self.__tasks) <= 0):
					break
				crew.assign_task(self.__tasks.pop())
			self.__cafetaria.enqueue(crew)
		locations = self.__locations


	def get_locations(self):
		return self.__locations
	def next_turn(self):
		print(self.__cafetaria)
		print(self.__tasks)
		# print(__colours)
		print(self.__locations)

p = parse_Tasks('tasks_01.csv')
s = Ship(p[1:-4],4)
# print(repr(s.get_caf()))
s.next_turn()