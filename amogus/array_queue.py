import arrays

class Queue:
    __slots__=['__front','__back','__size','__array']

    def __init__ (self,capacity=3):
        self.__array=[]
        self.__front= 0
        self.__back = 0
        self.__size = 0

    # methods:
    # no double __ is public
    def is_empty(self):
        return self.__back == 0

    def size(self):
        return self.__size


    def __repr__(self):
        string =''
        i = self.__front
        while i != self.__back:
            string +=str(self.__array[i])+', '
            i = (i+1)
        return '[' + string[:-2] +']'

    # enqueue
    # add value 
    def enqueue(self,value):
        # print(self.__back)
        self.__array.append(value)
        # self.__back = (self.__back+1)% len(self.__array)
        self.__back +=1

        if self.__back == self.__front:
            self.__resize()
    
    # dequeue
    def dequeue(self):
        if self.__back <= 0:
            raise IndexError ("cannot dequeue from an empty queue")
        value = self.__array.pop(0)
        # self.__front = (self.__front+1)% len(self.__array)
        self.__back -=1

        return value

    # resize
    # __ means is private to class and cant get from main and anywhere else
    def __resize(self):
        new_array = arrays.Array(len(self.__array)* 2+1)
        i = self.__front
        j = 0
        for _ in range(self.__size):
            new_array [j] = self.__array[i]
            i - (i+1)% len(self.__array)
            j+=1
        self.__front = 0
        self.__back = j
        self.__array = new_array

    def get_front(self):
        return self.__array[self.__front]
    def get_back(self):
        return self.__array[self.__back-1]

def main():
    q = Queue(6)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    while True:
        input()
        a = q.dequeue()
        print(q)
        q.enqueue(a)
        print(q)


