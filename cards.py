import random
from collections import Counter
from operator import itemgetter

#global variables
x = 1
deck = [] 
hands=[]
card=[]
winners = []

#construct and shuffle the deck
print "building 52-card deck..."
print ''
while  x < 14:
    card = [x+1,'s']
    deck.append(card)
    card = []
    card = [x+1,'h']
    deck.append(card)
    card = []
    card = [x+1,'c']
    deck.append(card)
    card = []
    card = [x+1,'d']
    deck.append(card)
    card = []
    x += 1
print deck
print ''
print "shuffling..."
print ''

random.shuffle(deck)
print ''
print deck
print ''

#deals player cards
player = 0
while player <9:
    hand = ['seat' + str(player+1),deck[player],deck[player + 9]]
    hands.append(hand)
    print hands[player]
    player=player+1

#deals community cards
community = [deck[21],deck[22],deck[23],deck[25],deck[27]]
print ''
print "community cards"
print community 
print ''

s=1
#constucts and evaluates hands
while s < 10:
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

    #quads evaulator
    fourofakind=[]
    f=1
    while f <= len(sorted_straight_cards):
        if straight_cards.count(sorted_straight_cards[f-1]) == 4:
            fourofakind.append(sorted_straight_cards[f-1])
        f = f+1
    sorted(fourofakind, reverse=True)
    if len(fourofakind) >= 1:
        print "quad " + str(fourofakind[0]) + "'s"
        madehand = True
        winner = [s,2,fourofakind[0],0]

        #else:
        #print "no quads"

    #full house evaluator 
    boat=[]
    y=1
    while y <= len(sorted_straight_cards) and madehand == False:
        if straight_cards.count(sorted_straight_cards[y-1]) == 3:
            #print "trip " + str(sorted_straight_cards[y-1])
            boat.append(sorted_straight_cards[y-1])
            j=1
            while j <= len(sorted_straight_cards):
                if straight_cards.count(sorted_straight_cards[j-1]) >= 2 and sorted_straight_cards[j-1] != boat[0]:
                     boat.append(sorted_straight_cards[j-1])
                j=j+1
        y = y+1
    #sorted(boat, reverse=True)
    if len(boat) >= 2:
        print  str(boat[0]) + " full of " + str(boat[1])
        madehand = True
        winner = [s,3,boat[0],boat[1]]   
    #else:
        #print "no boat"

    #flush evaluator 
    i=1
    spade_flush_cards = []
    heart_flush_cards = []
    diamond_flush_cards = []
    club_flush_cards = []
    while i <= 7 and madehand == False:
        if seat1[i-1][1] == 's':
            #spades = spades + 1
            spade_flush_cards.append(seat1[i-1][0])
        elif seat1[i-1][1] == 'd':
            #diamonds = diamonds + 1
            diamond_flush_cards.append(seat1[i-1][0])
        elif seat1[i-1][1] == 'c':
            #clubs = clubs + 1
            club_flush_cards.append(seat1[i-1][0])
        elif seat1[i-1][1] == 'h':
            #hearts = hearts + 1
            heart_flush_cards.append(seat1[i-1][0])
        i += 1
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
    #else:
        #print "no flush"

    
    #straight evaluator 
    if len(sorted_straight_cards) >= 5 and sorted_straight_cards[0] - sorted_straight_cards[1] == 1 and sorted_straight_cards[1] - sorted_straight_cards[2] == 1 and sorted_straight_cards[2] - sorted_straight_cards[3] == 1 and sorted_straight_cards[3] - sorted_straight_cards[4] == 1  and madehand == False:
        print str(sorted_straight_cards[0]) + " high straight"
        madehand = True
        winner = [s,5,sorted_straight_cards[0],0]
    elif len(sorted_straight_cards) >= 6 and sorted_straight_cards[1] - sorted_straight_cards[2] == 1 and sorted_straight_cards[2] - sorted_straight_cards[3] == 1 and sorted_straight_cards[3] - sorted_straight_cards[4] == 1 and sorted_straight_cards[4] - sorted_straight_cards[5] == 1  and madehand == False:
        print str(sorted_straight_cards[1]) + " high straight"
        madehand = True
        winner = [s,5,sorted_straight_cards[1],0]
    elif len(sorted_straight_cards) >= 7 and sorted_straight_cards[2] - sorted_straight_cards[3] == 1 and sorted_straight_cards[3] - sorted_straight_cards[4] == 1 and sorted_straight_cards[4] - sorted_straight_cards[5] == 1 and sorted_straight_cards[5] - sorted_straight_cards[6] == 1  and madehand == False:
        print str(sorted_straight_cards[2]) + " high straight"
        madehand = True
        winner = [s,5,sorted_straight_cards[2],0]
   # else:
        #print "no straight"

 
    #trips evaluator 
    trips=[]
    y=1
    while y <= len(sorted_straight_cards)  and madehand == False:
        if straight_cards.count(sorted_straight_cards[y-1]) == 3:
            #print "trip " + str(sorted_straight_cards[y-1])
            trips.append(sorted_straight_cards[y-1])
        y = y+1
    sorted(trips, reverse=True)
    if len(trips) >= 1:
        print "trip " + str(trips[0])
        madehand = True
        winner = [s,6,trips[0],0]
    #else:
        #print "no trips"

    twopair=[]
    z=1
    while z <= len(sorted_straight_cards) and madehand == False:
        if straight_cards.count(sorted_straight_cards[z-1]) == 2:
            twopair.append(sorted_straight_cards[z-1])
            #print "pair of " + str(sorted_straight_cards[z-1])
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

    s = s+ 1
    winners.append(winner)
    
print ''
#print winners
winners.sort(key=itemgetter(1))
#print winners
champian = [winners[0]]
t=0
while t < len(winners)-1:
    if winners[t+1][1] == winners[0][1]:
        champian.append(winners[t+1])
    t+=1
champian.sort(key=itemgetter(2), reverse=True)
champian.sort(key=itemgetter(3), reverse=True)

#print champian

print "winner seat: " + str(champian[0][0])
print ''







    





