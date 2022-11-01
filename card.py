import random

def make_card(rank,suit):
    # initialising names inplace of rank
    dict = [0] * 14
    dict[1] = "Ace"
    dict[11] = "Jack"
    dict[12] = "Queen"
    dict[13] = "King"

    # initialising the card array 
    card = [0] * 4
    
    # finding names
    r = rank 
    sh = str(r) + suit[0]
    
    if(dict[rank] != 0):
        r = dict[rank]
        sh = str(r)[0] + suit[0]
    

    name = str(r) + " of " + suit
        


    if(suit == "Hearts" or suit == "Diamonds"):
        sh = "\033[31m " + sh + "\033[37m"
    else:
        sh = "\033[34m " + sh + "\033[37m"
        
    # filling the array 
    card[0] = rank
    card[1] = suit
    card[2] = name
    card[3] = sh

    # return the card as a form of tuple
    return tuple(card)
   
def make_deck():
    deck = []
    suites = ["Clubs", "Diamonds", "Hearts", "Spades"]
    for suit in suites:
        for rank in range(1 , 14):
            card = make_card(rank , suit)
            deck.append(card)
    return deck
    
def shuffle(deck):
    for i in range(0 , len(deck)):
        j = random.randint(0 , len(deck)-1)
        deck[i] , deck[j] = deck[j] , deck[i]

def draw(deck , hand):
    if(len(deck) == 0):
        return None
    card = deck.pop()
    hand.append(card)
    return card

def deal_one_hand(deck , n):
    hand  = []
    for _ in range(n):
        draw(deck, hand)
    return hand


d = make_deck() 
shuffle(d)

h = deal_one_hand(d , 12)

print(make_card(12 , "Diamonds"))