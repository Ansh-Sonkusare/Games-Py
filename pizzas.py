class Toppings:
    def __init__(self , name , code , price) -> None:
        self.name = name
        self.code = code 
        self.price = price

cheeses = {"f":["Fresh Mozzarella(f)" , 1.0] , "c":["Cheddar(c)" , 0.5] , "s":["Shredded Cheese(s)" , 0.0] , "n":["None(n)" , 0.0]}
meats = {"p":["Pepperoni(p)" , 1.5] , "s":["Sausage(s)" , 1.0] , "m":["MeatBall(m)" , 2.0] , "n":["None(n)" , 0.0]}
veggies = {"m":["Mushroom (m)" , 1.5] ,  "b" : ["Bell Peppers (b)" , 1.0] , "j":["Jalpeno Peppers" , 1.0]  , "n":["None(n)" , 0.0]}

class Pizza:
    def __init__(self,toppings) :
        self.tp = toppings
        self.price = sum([ i[1] for i in self.tp ]) + 5.0

        


def pizzas():
    dicts = ["cheeses", "meats","veggies"]
    dictt_func = [cheeses , meats , veggies]

    
    tp = []
    for o in dicts:
        idx = dicts.index(o)
        d = dictt_func[idx]
        # pizza = Pizza()

   
        print("choose one type of " + o[:-1] + " (0 for options)" )
        x = input()
        if(str(x) != str(0)):
            continue
        print(o + " Options:")
        for i in d:
            op = d   
            print(op[i][0] + " : $" + str(op[i][1]) , end=" ")
        print()
        y = str(input())
        while y in  d and y != "n":
            arr =  (tp) 
            if(y in arr):
                break

            arr.append(d[y])
            if(o == "cheeses"):
                break
            print(o + " Options:")
            for i in d:
                op = d   
                print(op[i][0] + " : $" + str(op[i][1]) , end=" ")
            y = input()
            
            print()
    print(tp)
    pizza = Pizza(tp)
    print(pizza.price)
    return pizza

def main():
    print("Welcome to Pizza Factory, where all orders include two pizzas!")
    print("For your first pizza ...")
    p1 = pizzas()
    print("For your second pizza ...")

    p2 = pizzas()
    print("One pizza with " ,end="")
    for i in p1.tp:
        print(i[0][:-3] , end=", ")
    print(": $" + str(p1.price))

    print("One pizza with " ,end="")
    for i in p2.tp:
        print(i[0][:-3] , end=", ")
    print(": $" + str(p2.price))
    print("total due: $ " + str(p1.price + p2.price))

main()