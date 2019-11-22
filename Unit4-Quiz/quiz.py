def max_value(integer_input):
  for i in range(1,integer_input+1):
     print(i)

max_value(10)

print('-----------------')

def compare_lists(list1,list2):
  if len(list1) != len(list2):
    print('erro! We need two lists of the same length!')
  else:
    for i in range(0,len(list1)):
      print('For [' + str(i) + ']:')
      if list1[i] > list2[i]:
        print('List2 has bigger value:' + str(list1[i]))
      elif list1[i] < list2[i]:
        print('List1 has bigger value:' + str(list2[i]))
      else:
        print('Both list1 and list 2 have the same value:' + str(list2[i]))

l1 = [0,1,2]
l2 = [2,3,4]

compare_lists(l1,l2)

print('-----------------')

def vertical_stars_and_stripes():
  for i in range(6):
    if i%2 == 0:
      str_1 = ''
      for i in range(3):
        str_1 += '*-'
      print(str_1)
    else:
      str_1 = ''
      for i in range(3):
        str_1 += '-*'
      print(str_1)
  
vertical_stars_and_stripes()

print('-----------------')

def find_secret(lists_b,item_search):
  for i in range(0,len(lists_b)):
    for j in range(0,len(lists_b[i])):
      if lists_b[i][j] == item_search:
        print(i,j)

list_of_lists = [
['where', 'is', 'the'], 
['very', 'secret', 'word'], 
['i', 'can', 'find'] 
] 
secret_item = 'secret' 
find_secret(list_of_lists, secret_item)
