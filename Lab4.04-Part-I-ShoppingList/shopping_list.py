'''
my_building = [
['apt1a', 'apt1b', 'apt1c'],
['apt2a', 'apt2b', 'apt2c'],
['apt3a', 'apt3b', 'apt3c']
]
print(my_building)
print("first floor" + str(my_building[0]))
print("first floor, 3rd apartment" + str(my_building[0]))

ll = [
[1,4,9],
[16,25,36],
[49,64,81]
]

def add_one(list):
  for i in range(0,len(list)):
    for j in range(0,len(list)):
      list[i][j] += 1

add_one(ll)
print(ll)
'''
shopping_cart = [
['tooth paste', 'q-tips', 'milk'],
['milk', 'candy', 'apples'],
['planner', 'pencils', 'q-tips']
]

#1
def update_list(list_int):
  list_row = int(input('Which shopping list do you want to update:'))
  len_input = int(input('Which position it should update:'))
  new_value = input('Please enter a new value:')
  if len_input+1 > len(list_int):
    list_int[list_row].append(new_value)
  else:
    list_int[list_row][len_input] = new_value
  return list_int
#2
def print_item(list_int):
  row_int = int(input('Which shopping list do you want to print:'))
  len_int = int(input('Which position it should print:'))
  print(list_int[row_int][len_int])
#3
def print_list(list_int):
  row_int = int(input('Which shopping list do you want to print:'))
  print(list_int[row_int])

choice_input = 0

while choice_input != 'quit':
  choice_input = input('What would you like to do?')
#ask part
  if choice_input == 'update':
    update_list(shopping_cart)
  if choice_input == 'print':
    print_item(shopping_cart)
  if choice_input == 'print all':
    print_list(shopping_cart)
