# Lab-4.04-Part-I---Shopping-List
We need a shopping list! But it is in python...

Lab 4.04 Part I - Shopping List
Part 1
The goal of this lab is to practice using and accessing items from lists of lists. 

You have a few errands to run and have created a few shopping list to help you remember what to buy. You stored your notes in a nested list, shopping_cart. This program will allow the user to ask for a specific item by it's index or update what items are in the cart. The user can request you print all the items in a specific shopping list.

Schedule
shopping_cart = [
['tooth paste', 'q-tips', 'milk'],
['milk', 'candy', 'apples'],
['planner', 'pencils', 'q-tips']
]
User Inputs
update
The program will ask which shopping list the user wants to update, which position it should update, and the new value to update.
print
The program will ask which shopping list the user wants to print from and afterwards will request which position it should print.
print all
The program will ask which shopping list the user wants to print and will print all of the items associated with that shopping list.
Functions
update_list
Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, and a string representing the new item to add to that shopping list.
print_item
Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.
print_list

Takes an int representing the index of the shopping list to print.
Feel free to add more functions as you see fit

Example
>>>What would you like to do? print all
Which shopping list would you like to print? 1
tooth paste, q-tips, milk
