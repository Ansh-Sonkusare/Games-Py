import math
import random


def print_grid(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print (arr[i][j], end = " "),
        print ()
def make_sudoku(N):
    reg_dict = dict()
    sq = int(math.sqrt(N))
    puzzle =  dict()
    board  = [[0 for row in range(N)] for col in range(N)]
    rows = [set() for i in range(N)]
    cols = [set() for i in range(N)]
    regs = [[set() for i in range(sq)] for j in range(sq)  ]
    count = 1
    while count <= N: 
        row = random.randint(0,N-1) 
        col = random.randint(0,N-1)
        
        if board[row][col]==0:
            
            board[row][col] = count
            rows[row].add(count)
            cols[col].add(count)
            
            regs[row//sq][col//sq].add(count)
            
            count +=1

    return({"board" : board,"row_sets" : rows , "col_sets":cols , "reg_sets":regs})
    # print(board)
def get_square(puzle , row , col):
    value = puzle["board"][row][col]
    r = puzle["row_sets"][row]
    c = puzle["col_sets"][col]
    sq = int(math.sqrt(len(puzle["board"])))
    reg = puzle["reg_sets"][row//sq][col//sq]
    return {'value':value,"row_set" : r , "col_set":c , "reg_set": reg}
def move(puzle , row , col , new_val):
    p = get_square(puzle , row,col)
    if(puzle["board"][row][col] != 0):
        return False
    if(new_val not in p["row_set"] and new_val not in p["col_set"] and new_val not in p["reg_set"]):
        puzle["board"][row][col] = new_val
        return True
    return False
puzzle = make_sudoku(100)
# puzzle = {'board': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 7, 0, 0, 0, 0], [0, 0, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 6, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 0, 9, 8]], 'row_sets': [set(), set(), {1, 7}, {3}, {5}, set(), {6}, {2, 4}, {8, 9}], 'col_sets': [{1, 2}, set(), {3}, {5}, {6, 7}, set(), set(), {9}, {8, 4}], 'reg_sets': [[{1}, {7}, set()], [{3}, {5}, set()], [{2}, {6}, {8, 9, 4}]]}
# print_grid(puzzle["board"])
print("------------------------------------------")
def fill_puzzle(puzzle):
    n = len(puzzle["board"])
    # print(puzzle["board"])
    counter = 0
    for i in range( (n**4) ):
        if(counter>= (n*n)*75/100):
            break

 
        r = random.randint(0,8)
        c = random.randint(0,8)
        num = random.randint(1,9)
        b = move(puzzle , r , c, num)
        if(b):
            counter +=1
    print(counter)
    # print_grid(puzzle["board"])
    return puzzle
fill_puzzle(puzzle)

