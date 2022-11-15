import csv
import pokemon
import random
class Pokedex:
    __slots__ = ["__pokemon_list"]
    def __init__(self) -> None:
        self.__pokemon_list = []
    
    def load(self , filename):
        with open(filename ,  mode ='r') as f:
            csvfile = csv.reader(f)
            c = 0
            for line in csvfile:
                if(c == 0):
                    c +=1
                    continue
                pk = pokemon.Pokemon(line[0] , line[1] , int(line[2]) , int(line[3]))
                self.__pokemon_list.append(pk)
        

    def create_parties(self):
        random.shuffle(self.__pokemon_list)
        first = []
        second = []
     
        for j in range(6):
            first.append(self.__pokemon_list.pop())
        for j in range(6):
            second.append(self.__pokemon_list.pop())
        return first , second                   