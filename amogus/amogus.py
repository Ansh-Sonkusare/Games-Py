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
	def check_if_tasks(self):
		return self.__tasks.is_empty()
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
	murdered={self.__murdered} \n\
	tasks={self.__tasks}" 


class Ship:
	__slots__ = ["__locations", "__tasks" , "__cafetaria"   , "__survived" , "__murdered" , "__imp"]
	
	def __init__ (self,tasks , imposters = 1 ):

		self.__imp = imposters
		# initialisation
		self.__survived = node_stack.Stack()
		self.__murdered = node_stack.Stack()
		__colours = ["Black", "Blue", "Brown", "Cyan", "Green", "Pink", "Purple", "Red", "White",  "Yellow"]
		random.shuffle(__colours)
		# random.shuffle(tasks)
		self.__tasks = tasks
		self.__locations= dict()
		crewmates = 10 - imposters	
		
		self.__cafetaria = array_queue.Queue(crewmates)

		if(imposters>4 or imposters < 1):
			raise ValueError
		crewmates = 10 - imposters	

		
		tasks_per_crew = math.ceil(len(self.__tasks)/crewmates)

		for task in tasks:
			self.__locations[task.get_location()] = False
	
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
			# print(self.__cafetaria)
		locations = self.__locations
	
			
	def check_result(self):
		print(self.__cafetaria.is_empty())
		if(self.__cafetaria.is_empty()):
			# m = [str(i) for i in self.__murdered]
			# s = [str(i) for i in self.__survived]

			print(f"murdered: {self.__murdered}" )
			print(f"surviving: {self.__survived}" )
			return False
		return True


	def get_locations(self):
		return self.__locations
	def next_turn(self):
		print(self.__cafetaria)

		loc = list(self.__locations.keys())
		lic = self.__locations.copy()
		for i in range(self.__imp):
			l = random.choice(loc)
			lic[l] = True
		c = self.__cafetaria.dequeue()
		t = c.next_task()
		print(lic[t.get_location()])
		print(c.check_if_tasks() == False)
		em = c.check_if_tasks()
		if(lic[t.get_location()]):
			print(str(c) + " has been killed")
			c.kill()
			self.__murdered.push(c)
		elif(em == False):
			print(str(c) + " has returned to cafeteria")
			self.__cafetaria.enqueue(c)
		elif(em):
			print(repr(c))
			self.__survived.push(c)
		print((self.__cafetaria))
		
		# print(repr(c))


def main():
	p = parse_Tasks('tasks_01.csv')
	p = p[1:-4]
	i = input()
	if(i.strip() == ''):
		return
	elif(int(i)):
		s = Ship(p , i)
	else:
		s = Ship(p , 4)
	

main()
