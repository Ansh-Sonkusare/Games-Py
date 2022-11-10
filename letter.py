def make_letter_frequency(filename:str):
    file = open(filename , "r")
    d = {}
    f = file.read().split()
    for w in f:
        for a in w:
            a = a.lower()
            if(ord(a) > 96 and ord(a) < 123):
                if(a in d.keys()):
                    d[a] +=1
                else:
                    d[a] = 1
    file.close()
          
    return (d)
def print_letter_frequency(let_dic:dict):
    for i in let_dic.keys():
        print(str(i) + ":" + str(let_dic[i]))

    vals = let_dic.values()
    max_val = max(vals)
    idx = list(let_dic.values()).index(max_val)
    keys = list(let_dic.keys())
    print("the most popular letter: " + ( keys[idx] + " " + str(max_val) ))
    print()

def main():
    filename1 = "data/alice.txt"
    filename2 = "data/rit_mission.txt"

    filename = [filename1  , filename2]
    for f in filename:
        d = make_letter_frequency(f)
        print_letter_frequency(d)
main()