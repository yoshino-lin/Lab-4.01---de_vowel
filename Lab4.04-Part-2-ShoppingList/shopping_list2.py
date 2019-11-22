my_floor = ['apt1a', 'apt1b', 'apt1c']
def apartments_on_floor(list_in):
  for i in range(0,len(list_in)):
    print(list_in[i])

apartments_on_floor(my_floor)

print('----------------')

my_building = [
['apt1a', 'apt1b', 'apt1c'],
['apt2a', 'apt2b', 'apt2c'],
['apt3a', 'apt3b', 'apt3c']
]

def apartments_in_building(list_inp):
  for i in range(0,len(list_inp)):
    for j in range(0,len(list_inp[i])):
      print(list_inp[i][j])
    
apartments_in_building(my_building)

print('----------------')
print('Here is the answer for Lab 4:04 Part 2 - Shopping List:')

schedule = [
['q-tips', 'pencils', 'planner'],
['apples', 'candy', 'milk'],
['milk', 'q-tips', 'toothe paste']
]

def all_in_one(list_in1):
  list_out = []
  for i in range(len(list_in1)):
    list_out += list_in1[i]
  print(list_out)
  
all_in_one(schedule)

def count_q_tips(list_in2):
  q_tips = 0
  for i in range(0,len(list_in2)):
    for j in range(0,len(list_in2[i])):
      if list_in2[i][j] == 'q-tips':
        q_tips += 1
  print(q_tips)
  
count_q_tips(schedule)

def drink_more_milk(list_in3):
  for i in range(0,len(list_in3)):
    for j in range(0,len(list_in3[i])):
      if 'milk' not in list_in3[i]:
        list_in3[i].append('milk')
  print(list_in3)

drink_more_milk(schedule)

def if_you_give_a_moose_a_cookie(list_in4):
  for i in range(0,len(list_in4)):
    for j in range(0,len(list_in4[i])):
      if list_in4[i][j] == 'milk':
        list_in4[i][j] = 'cookies'
  print(list_in4)
  
if_you_give_a_moose_a_cookie(schedule)

########################################
print('bounus:(from lab4.02 bonus)')

shopping_cart_list = [
['tooth paste','q-tips','milk'],
['milk','candy','apples'],
['planner','pencils','q-tips']
]

def shopping_cart(list_in_b):
  for i in range(0,len(list_in_b)):
    list_in_b[i].reverse()
  list_in_b.reverse()

shopping_cart(shopping_cart_list)
print(shopping_cart_list)
