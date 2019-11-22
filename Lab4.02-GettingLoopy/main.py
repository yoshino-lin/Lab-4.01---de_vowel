#def part
def fruit_pluralizer(list_of_strings): 
  num_of_fruit = 0
  num_int = 0
  list_after = []
  while num_of_fruit != len(list_of_strings):
    if list_of_strings[num_int].endswith('y'):
      list_after.append(list_of_strings[num_int] + 'ies')
      num_int +=1
      num_of_fruit +=1
    elif list_of_strings[num_int][-1] in 'sx' or list_of_strings[num_int][-2:] in ['sh', 'ch']:
      list_after.append(list_of_strings[num_int] + 'es')
      num_int +=1
      num_of_fruit +=1
    else:
      list_after.append(list_of_strings[num_int] + 's')
      num_int +=1
      num_of_fruit +=1
  return list_after
#main part:  
fruit_list = ['apple', 'berry', 'melon']
print("Single Fruit: " + str(fruit_list))
fruit_list = fruit_pluralizer(fruit_list)
print("No longer single Fruit: " + str(fruit_list))

####################################################

#use easy code to do easy things
#more ideas about reverse please see reverse.py
def my_reverse(string_to_reverse): 
    return string_to_reverse[::-1]
reversed = my_reverse('apples')
print(reversed)

####################################################

#bonus!
def reverse_strings_in_list(list_will_reverse):
  num_of_fruit = 0
  num_int = 0
  list_after_reverse = []
  while num_of_fruit != len(list_will_reverse):
      list_after_reverse.append(list_will_reverse[num_int][::-1])
      num_int +=1
      num_of_fruit +=1
  return list_after_reverse
reversed_list = reverse_strings_in_list(['apples','banana','orange'])
print(reversed_list)
