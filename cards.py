import random
from collections import Counter
from operator import itemgetter

#global variables
deck = [] 
hands=[]
card=[]
winners = []
face_values = (2,3,4,5,6,7,8,9,10,11,12,13,14)
players = 9
suits = ('s','h','c','d')


#construct and shuffle the deck
print ''
print "building 52-card deck..."
print ''

for i in face_values:
    for j in suits:
        card = [i,j]
        deck.append(card)
        card = []

print deck
print ''
print "shuffling..."
random.shuffle(deck)
print ''
print deck
print ''

#deals player cards
i=0
while i < players:
    hand = ['seat' + str(i+1),deck[i],deck[i + 9]]
    hands.append(hand)
    print hands[i]
    #player=player+1
    i+=1

#deals community cards
community = [deck[21],deck[22],deck[23],deck[25],deck[27]]
print ''
print "community cards"
print community 
print ''


#check if a flush is possible and if the board is paired
community_flush =[]
community_pairs =[]
flush_possible = False
board_paired = False
for c in community:
    community_flush.append(c[1])
    community_pairs.append(c[0])
for c in suits:
    if community_flush.count(c) >= 3:
        flush_possible = True
for p in community_pairs:
    if community_pairs.count(p) >= 2:
        board_paired = True

#flush_possible = True

#constucts the best possible 5-card poker hands for each player
s=1
while s <= players:
    madehand = False
    winner = []
    #builds the 7-card hands
    seat1 = hands[s-1][1:] + community
    print ''
    print "seat " + str(s)
    print seat1[:2]
    
    #some pre-prosessing for evaluating everything except flushes
    straight_cards=[]
    i = 0
    while i < 7:
        straight_cards.append(seat1[i-1][0])
        i +=1
    unique_straight_cards = set(straight_cards) 
    sorted_straight_cards = sorted(unique_straight_cards, reverse=True)

    #straigh flush and flush pre-processing
    if flush_possible == True:
        i=1
        spade_flush_cards = []
        heart_flush_cards = []
        diamond_flush_cards = []
        club_flush_cards = []
    
        while i <= 7 and madehand == False:
            if seat1[i-1][1] == 's':
                spade_flush_cards.append(seat1[i-1][0])
            elif seat1[i-1][1] == 'd':
                diamond_flush_cards.append(seat1[i-1][0])
            elif seat1[i-1][1] == 'c':
                club_flush_cards.append(seat1[i-1][0])
            elif seat1[i-1][1] == 'h':
                heart_flush_cards.append(seat1[i-1][0])
            i += 1
    
    #straigh flush evaluator
 
    #spade_flush_cards = [10,12,9,8,11,4]
    if flush_possible == True:
        if len(spade_flush_cards) >= 5 and sorted(spade_flush_cards,reverse=True)[0]-sorted(spade_flush_cards,reverse=True)[1] == 1 and sorted(spade_flush_cards,reverse=True)[1]-sorted(spade_flush_cards,reverse=True)[2] == 1 and sorted(spade_flush_cards,reverse=True)[2]-sorted(spade_flush_cards,reverse=True)[3] == 1 and sorted(spade_flush_cards,reverse=True)[3]-sorted(spade_flush_cards,reverse=True)[4] == 1:
            print "straight flush, spades (" + str(sorted(spade_flush_cards, reverse=True)[0]) + " high)"
            winner = [s,1,(sorted(spade_flush_cards, reverse=True)[0]),0]
            madehand = True
        
        elif madehand == False and len(diamond_flush_cards) >= 5 and sorted(diamond_flush_cards,reverse=True)[0]-sorted(diamond_flush_cards,reverse=True)[1] == 1 and sorted(diamond_flush_cards,reverse=True)[1]-sorted(diamond_flush_cards,reverse=True)[2] == 1 and sorted(diamond_flush_cards,reverse=True)[2]-sorted(diamond_flush_cards,reverse=True)[3] == 1 and sorted(diamond_flush_cards,reverse=True)[3]-sorted(diamond_flush_cards,reverse=True)[4] == 1:
            print "straight flush, diamond (" + str(sorted(diamond_flush_cards, reverse=True)[0]) + " high)"
            winner = [s,1,(sorted(diamond_flush_cards, reverse=True)[0]),0]
            madehand = True
        
        elif madehand == False and len(heart_flush_cards) >= 5 and sorted(heart_flush_cards,reverse=True)[0]-sorted(heart_flush_cards,reverse=True)[1] == 1 and sorted(heart_flush_cards,reverse=True)[1]-sorted(heart_flush_cards,reverse=True)[2] == 1 and sorted(heart_flush_cards,reverse=True)[2]-sorted(heart_flush_cards,reverse=True)[3] == 1 and sorted(heart_flush_cards,reverse=True)[3]-sorted(heart_flush_cards,reverse=True)[4] == 1:
            print "straight flush, heart (" + str(sorted(heart_flush_cards, reverse=True)[0]) + " high)"
            winner = [s,1,(sorted(heart_flush_cards, reverse=True)[0]),0]
            madehand = True

        elif madehand == False and len(club_flush_cards) >= 5 and sorted(club_flush_cards,reverse=True)[0]-sorted(club_flush_cards,reverse=True)[1] == 1 and sorted(club_flush_cards,reverse=True)[1]-sorted(club_flush_cards,reverse=True)[2] == 1 and sorted(club_flush_cards,reverse=True)[2]-sorted(club_flush_cards,reverse=True)[3] == 1 and sorted(club_flush_cards,reverse=True)[3]-sorted(club_flush_cards,reverse=True)[4] == 1:
            print "straight flush, club (" + str(sorted(club_flush_cards, reverse=True)[0]) + " high)"
            winner = [s,1,(sorted(club_flush_cards, reverse=True)[0]),0]
            madehand = True
        
      


    #quads evaulator
    fourofakind=[]
    f=1
    while f <= len(sorted_straight_cards):
        if straight_cards.count(sorted_straight_cards[f-1]) == 4:
            fourofakind.append(sorted_straight_cards[f-1])
        f +=1
    sorted(fourofakind, reverse=True)
    if len(fourofakind) >= 1:
        print "quad " + str(fourofakind[0]) + "'s"
        madehand = True
        winner = [s,2,fourofakind[0],0]


    #full house evaluator 
    if  board_paired == True and madehand == False:
        
        boat=[]
        y=1
        while y <= len(sorted_straight_cards) and madehand == False:
            if straight_cards.count(sorted_straight_cards[y-1]) == 3:
                boat.append(sorted_straight_cards[y-1])
                j=1
                while j <= len(sorted_straight_cards):
                    if straight_cards.count(sorted_straight_cards[j-1]) >= 2 and sorted_straight_cards[j-1] != boat[0]:
                        boat.append(sorted_straight_cards[j-1])
                    j+=1
            y +=1
            if len(boat) >= 2:
                print  str(boat[0]) + " full of " + str(boat[1])
                madehand = True
                winner = [s,3,boat[0],boat[1]]   


    #flush evaluator 
    if flush_possible == True and madehand == False:
            if len(spade_flush_cards) >= 5:
                print "spade flush (" + str(sorted(spade_flush_cards, reverse=True)[0]) + " high)"
                winner = [s,4,(sorted(spade_flush_cards, reverse=True)[0]),0]
                madehand = True
            elif len(diamond_flush_cards) >= 5:
                print "diamond flush (" + str(sorted(diamond_flush_cards, reverse=True)[0]) + " high)"
                madehand = True
                winner = [s,4,(sorted(diamond_flush_cards, reverse=True)[0]),0]
            elif len(heart_flush_cards) >= 5:
                print "heart flush (" + str(sorted(heart_flush_cards, reverse=True)[0]) + " high)"
                madehand = True
                winner = [s,4,(sorted(heart_flush_cards, reverse=True)[0]),0]
            elif len(club_flush_cards) >= 5:
                print "club flush (" + str(sorted(club_flush_cards, reverse=True)[0]) + " high)"
                madehand = True
                winner = [s,4,(sorted(club_flush_cards, reverse=True)[0]),0]

    
    #straight evaluator 
    
    z = 1
    while z <= 3 and madehand == False:
        
        if len(sorted_straight_cards) >= z+4 and sorted_straight_cards[z-1] - sorted_straight_cards[z] == 1 and sorted_straight_cards[z] - sorted_straight_cards[z+1] == 1 and sorted_straight_cards[z+1] - sorted_straight_cards[z+2] == 1 and sorted_straight_cards[z+2] - sorted_straight_cards[z+3] == 1:
            print str(sorted_straight_cards[z-1]) + " high straight"
            madehand = True
            winner = [s,5,sorted_straight_cards[z-1],0]
        z+=1

 
    #trips evaluator 
    
    if madehand == False:
        trips=[]
        y=1
        while y <= len(sorted_straight_cards):
            if straight_cards.count(sorted_straight_cards[y-1]) == 3:
                trips.append(sorted_straight_cards[y-1])
            y+=1
            sorted(trips, reverse=True)
            if len(trips) >= 1 and madehand == False:
                print "trip " + str(trips[0])
                madehand = True
                winner = [s,6,trips[0],0]


    #two pair, pair, and high card evaluator
    
    twopair=[]
    z=1
    while z <= len(sorted_straight_cards) and madehand == False:
        if straight_cards.count(sorted_straight_cards[z-1]) == 2:
            twopair.append(sorted_straight_cards[z-1])
        z = z+1

    sorted(twopair, reverse=True)
    if len(twopair) >= 2  and madehand == False:
        print "2 pair " + str(twopair[0]) + " and " + str(twopair[1])
        madehand = True
        winner = [s,7,twopair[0],twopair[1]]
    elif len(twopair) == 1  and madehand == False:
        print "pair of " + str(twopair[0])
        madehand = True
        winner = [s,8,twopair[0],0]
    elif madehand == False:
        print "no pairs, high card " + str(sorted_straight_cards[0])
        madehand = True
        winner = [s,9,sorted_straight_cards[0],0]

    s +=1 
    winners.append(winner)
    
print ''

#evaluates all hands and determines winner

winners.sort(key=itemgetter(1))
champian = [winners[0]]
t=0
while t < len(winners)-1:
    if winners[t+1][1] == winners[0][1]:
        champian.append(winners[t+1])
    t+=1
champian.sort(key=itemgetter(2), reverse=True)
champian.sort(key=itemgetter(3))# reverse=True)
print "winner seat: " + str(champian[0][0])
print ''




    





