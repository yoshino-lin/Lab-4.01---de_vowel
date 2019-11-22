#How clever I am!

#1:
print('ql:')
def draw_7():
  for i in range(7):
    my_string = ''
    for i in range(0, 7): 
      my_string += '*'
    print(my_string)
draw_7()

#2:
print('q2:')
def stars_and_stripes():
  for i in range(3):
    my_string_1 = ''
    my_string_2 = ''
    for i in range(0,7): 
      my_string_1 += '*'
    for i in range(0,7): 
      my_string_2 += '-'
    print(my_string_1)
    print(my_string_2)
stars_and_stripes()

#3:
print('q4:')
#easiest way
for i in range(1,8):
  str1 = ""
  for j in range(1,i):
   str1 +=(str(j))
  print(str1)

#what happened is:
def increasing_triangle():
  count = 1
  my_string = ''
  for i in range(9):
    my_string += str(count)
    count += 1
    print(my_string)
increasing_triangle()

#4
print('q4:')
def vertical_stars_and_stripes():
  for i in range(7):
    my_string = ''
    for i in range(3): 
      my_string += '-'
      my_string += '*'
    my_string +='-'
    print(my_string)
vertical_stars_and_stripes()

#b1
print('b1:')
def b1():
  for i in range(1):
    my_string = ''
    for i in range(0, 8): 
      my_string += '*'
    print(my_string)
  for i in range(7):
    my_string = '*'
    for i in range(6):
      my_string += '-'
    my_string += '*' 
    print(my_string)
  for i in range(1):
    my_string = ''
    for i in range(0, 8): 
      my_string += '*'
    print(my_string)
b1()
  
#b2
print('b2:')
def balanced_triangle():
  count = 1
  for i in range(1):
    my_string = ''
    for i in range(7):
      my_string += str(count)
      count += 1
      print(my_string)
    for i in range(6): #a blank line for range(7)?
      count -= 1
      my_string = my_string.strip(str(count))
      print(my_string)
balanced_triangle()

#b3
print('b3:')
def b3(count): #count = how may rows do you want
  count2 = 1
  for i in range(count):
    my_string = ''
    for i in range(count):
      my_string += ' '
    count -= 1
    for i in range(count2):
      my_string += '*'
    count2 +=2
    print(my_string)
b3(3)
