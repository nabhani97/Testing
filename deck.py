# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
import itertools, random

arange = range(1,4)
brange = ["red", "blue", "green", "orange"]


#print(list(arange))
#print(list(brange))

theproduct = list(itertools.product(arange,brange))

print(theproduct)

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

print(deck)

# shuffle the cards
random.shuffle(deck)

print(deck)

print(list(range(5)))

# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
   
   
# simulate a game of snap
# 2 players = 100 rounds of snap
# keep track of hpw many rounds each player wins
# display how many rounds player A won and how many rounds player B won.
   
