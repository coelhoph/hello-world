import random

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
cards = []

for  suit in suits:
  for rank in ranks:
    card = str(rank) + ' of ' + str(suit)
    cards.append(card)
    
count = (len(cards))
print(f'There are {str(count)} cards in the deck.')
print('Dealing ...')

hand = []
deal = 0
deck = len(cards) - 1

while len(hand) < 5:
  card_number = random.randint(0,int(deck))
  card = cards[card_number]
  cards.remove(str(card))
  hand.append(card)
  deal += 1
  deck -= 1
 
else:
  print(f'There are {len(cards)} cards in the deck.')
  print('Player has the following cards in their hand:')
  print(hand)
