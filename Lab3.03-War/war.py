# Play the game WAR
import random
print('Welcome to the game WAR!')
# shuffled_deck: will return a shuffled deck to the user
#input:
#output: a list representing a shuffled deck
def shuffled_deck():
  basic_deck = list(range(2, 15)) * 4
  random.shuffle(basic_deck)
  return basic_deck
# name: player_turn
# purpose: takes in a player name and draws/removes a card from the deck,
#  prints "user drew card x", and returns the value
# input: player_name as string, deck as list
# returns: integer
def player_turn(player_name, deck):
  card = deck.pop(0)
  print (player_name + " drew card " + str(card))
  return card
# name: compare_scores
# !! Fill in the rest of this contract
def compare_cards(p1_card,p2_card):
  if p1_card > p2_card:
    return 1
  elif p1_card < p2_card:
    return -1
  else:
    return 0
# Put your main code that calls our functions here.
deck = shuffled_deck()
p1_score = 0
p2_score = 0
p1_card = 0
p2_card = 0
war_score = 0
player_name1 = str(input('What is the name of first player:'))
player_name2 = str(input('What is the name of second player:'))

while(len(deck)>0):
  p1_card = player_turn(player_name1,deck)
  p2_card = player_turn(player_name2,deck)
  if compare_cards(p1_card,p2_card) == 1:
    p1_score = p1_score + 2
    print(player_name1,"has high card")
  elif compare_cards(p1_card,p2_card) == -1:
    p2_score = p2_score + 2
    print(player_name2,"has high card")
  elif compare_cards(p1_card,p2_card) == 0:
    print('War')
    war_score = war_score + 4
    if compare_cards(p1_card,p2_card) == 1:
      print("p1_name" + war_score + "cards")
      p1_score = p1_score + war_score
      war_score = 0 
    elif compare_cards(p1_card,p2_card) == -1:
      p2_score = p2_score + war_score
      print("p2_name" + war_score + "cards")
      war_score = 0
  print(player_name1 + ':' + str(p1_score))
  print(player_name2 + ':' + str(p2_score))
  print(' ')


print('Final Score')
print(player_name1+":"+str(p1_score))
print(player_name2+":"+str(p2_score))
if p1_score > p2_score:
  print('Winner:' + player_name1)
else:  
  print('Winner:' + player_name2)
