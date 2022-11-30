import arrays

class Queue:
    __slots__=['__front','__back','__size','__array']

    def __init__ (self,capacity=3):
        self.__array=arrays.Array(capacity)
        self.__front= 0
        self.__back = 0
        self.__size = 0

    # methods:
    # no double __ is public
    def is_empty(self):
        return self.__size == 0

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
        self.__array[self.__back] = value
        self.__back = (self.__back+1)% len(self.__array)
        self.__size +=1

        if self.__back == self.__front:
            self.__resize()
    
    # dequeue
    def dequeue(self):
        if self.__size <= 0:
            raise IndexError ("cannot dequeue from an empty queue")
        value = self.__array[self.__front]
        self.__front = (self.__front+1)% len(self.__array)
        self.__size -=1

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
    new_q = Queue(3)
    print(new_q)

    new_q.enqueue(5)
    new_q.enqueue(7)
    
    print(new_q)

    print(new_q.get_front())
    print(new_q.get_back())

    

    new_q.dequeue()
    print(repr(new_q))
    new_q.dequeue()
    print(new_q)


    new_q.enqueue(2)
    new_q.enqueue(3)
    new_q.enqueue(4)
    new_q.enqueue(5)
    new_q.enqueue(6)
    new_q.enqueue(7)
    print(new_q)

main()