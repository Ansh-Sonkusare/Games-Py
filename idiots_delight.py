import card

def deal_hand():
    deck     = card.make_deck()
    card.shuffle(deck)    
    hand = card.deal_one_hand(deck , 4)
    return hand ,  deck 

def discard(hand , n):

    if((len(hand) < 4) or (n != 4 and n != 2)):
        return hand
    if n == 4:
        print(1)
        for i in range(4):
            hand.pop()
        return hand
    if n == 2:
        hand = hand[:-3] + hand[-1:]
        print(1)
        return hand

def play_round(deck , hand):

    while(len(hand) < 4):
        card.draw(deck , hand)
    h = hand[::-1]
    # print(h[1][1] == h[2][1] )
    pr_hn(hand)

    if(h[0][0] == h[3][0]):
     

        hand = discard(hand, 4)
    if(h[1][1] == h[2][1] ):
        hand = discard(hand, 2)
        



    if(len(deck) > 0):
        card.draw(deck , hand)
      

    return deck , hand

def pr_hn(hand):
    for i in range(len(hand)):
        print(hand[i][3])

def main():
    hand , deck = deal_hand()
    while(len(deck) > 0):


        # pr_hn(hand)
        
        deck , hand = play_round(deck,hand)
        # pr_hn(hand)

    pr_hn(hand)

    
# print(h)
main()

# print(h)