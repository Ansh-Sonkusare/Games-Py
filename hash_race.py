import math
from subprocess import call
from time import time
from traceback import print_tb


def hash_first_char(s):
    return ord(s[0])

def hash_sum(s):
    h = 0
    for i in range(len(s)):
        h += ord(s[i])
    return h

def hash_positional_sum(s):
    h = 0
    for i in range(len(s)):
        h += ord(s[i]) * (31**(len(s)-(i+1)))  
    return h
def build_colision_counter(fn):
    with open("long_line_words.txt" , "r") as f:
        collisions = {}
        arr_word = f.readlines()
       
        for w in arr_word:
            h = fn(w)
            if(h not in collisions.keys()):
                collisions[h] = 0
            else:
                collisions[h] = collisions[h]+1

    return collisions


    
    return ar[0] + "." + ar[1]

def test(collisions:dict , fn:callable):
    with open("long_line_words.txt" , "r") as f:
        
        words = f.readlines()
        l = len(words)
        print("hash function:", fn.__name__)
        a = time()   
        build_colision_counter(fn)
        b = time()     
        elapsed_time = (b-a)
        print("total collisions rate: "  + str(round(sum(collisions.values())*100/l , 2)) + "%"  )
        vals = list(collisions.values())
        val_max = max(vals)
     
        print("maximum collisions:" ,val_max)

        print("spread: " + str(round((l-sum(collisions.values()))*100/l , 2)) + "%" )
        print("speed: " + str(round((elapsed_time),2)) + " secconds" )
def main():
    arr_of_func = [hash , hash_first_char , hash_sum , hash_positional_sum]
    for f in (arr_of_func):
        d = build_colision_counter(f)
        test(d , f)
        print()


main()