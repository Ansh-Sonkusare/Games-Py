class Task:
	__slots__=["__name", "__location"]

def __init__(self, name, location):
	self.__name = name
	self.__location = location

def get_location(self):
	Return self.__location

def __str__ (self):
	Return self.__name + “in” + self.__location
