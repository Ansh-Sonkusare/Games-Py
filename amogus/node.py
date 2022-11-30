class Node:
    __slots__=["__value","__next"]

    # constructor
    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    # accessors
    def get_value(self):
        return self.__value
    def get_next(self):
        return self.__next
    
    # recursive printing funtion
def print_node(node_seq):
    if node_seq==None:
        return ''
    else:
        print(node_seq.get_value(),end=', ')
        print_node(node_seq.get_next())


    