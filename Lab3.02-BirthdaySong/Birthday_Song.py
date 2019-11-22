#coding=utf-8
#import
import random
# Put the function for birthday song here
# Name: birthday_song
# Purpose: birthday_song prints out a personalized birthday song
name_input = input("What is your name:") 
def birthday_song(name):
  i = "Happy birthday "+ name + "! Here is a birthday song for you!"
  return i
# Put the function for picking 5 cards here
number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
print(random.choice(suit),random.choice(number))
print(random.choice(suit),random.choice(number))
print(random.choice(suit),random.choice(number))
print(random.choice(suit),random.choice(number))
print(random.choice(suit),random.choice(number))
# Put code here to call your functions.
a = birthday_song(name_input)
print(a)
