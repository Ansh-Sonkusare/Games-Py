import pokemon
import pokedex
import random

def battle(party1:list, party2:list):
    def faint(a , b):
        if(a.is_fainted()):
            
            # print(a.is_fainted)
            print(f"{a} has fainted and is out of battle")
            
        else:
            party1.append(a)


        if(b.is_fainted()):
            # print(a.is_fainted)
            print(f"{b} has fainted and is out of battle")
            
        else:
            party2.append(b)
            


    r = 1
    while 0 < len(party1) and 0 < len(party2):
        # print(party1)
        


        print("Round:" , r)
        r += 1
        print("Party 1 : " , set(party1))
        print("Party 2 : " , set(party2))
        a , b = party1.pop(), party2.pop()
        if(a.type == b.type):
            if(a.health_points == b.health_points):

                print(f"{a} and {b} battle to draw")
                party1.append(a)
                party2.append(b)
                random.shuffle(party1)
                random.shuffle(party2)
            elif(a.health_points > b.health_points):
                print(f"{a} has won the round")
             
                b.lose_round(a.get_damage())
                faint(a,b)
            elif(a.health_points < b.health_points):
                print(f"{b} has won the round")
        
                a.lose_round(b.get_damage())
                faint(a,b)

    
        elif( a.type == "Grass" and b.type == "Water"):
            print(f"{a} has won the round")
     
            b.lose_round(a.get_damage())
            
            
            faint(a,b)
            
        elif( a.type == "Water" and b.type == "Fire"):
            print(f"{a} has won the round")
      

            b.lose_round(a.get_damage())
            faint(a,b)
            
        elif( a.type == "Fire" and b.type == "Grass"):
            print(f"{a} has won the round")
         
           
            b.lose_round(a.get_damage())
            faint(a,b)
        else:
            print(f"{b} has won the round")
      
       

            a.lose_round(b.get_damage())
            faint(a,b)
        # print(len(party1) , len(party2))
        if(len(party1) == 0):
            
            print("Winning Party:" , set(party2))
        if(len(party2) == 0):
            print("Winning Party:" , set(party1))
        input("press enter for next round")
       
    


            

fl = "data/pokemons.csv"

pkd = pokedex.Pokedex()
pkd.load(fl)
a , b = pkd.create_parties()
battle(a,b)