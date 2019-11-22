#Yudong lin, Jack Anderson, Emily hoffart
#At that time I was working with someone who nearly did nothing...

def higher_lower(list_int):
print(max(list_int))

list_input=[1,2,3,4,5,9,7,6]
higher_lower(list_input)

#2
def draw_7(x,y):
for i in range(y):
my_string = ''
for i in range(x): 
my_string += '*'
print(my_string)
draw_7(3,4)


#3
vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
def count_vowels(a_string):
global vowel_list
vowel_letter_num = 0
for list_letter in a_string:
if list_letter in vowel_list:
vowel_letter_num += 1
print(vowel_letter_num)
count_vowels("This sentence has no vowels")


#4
fruit_list = ['apple', 'berry','melon']
num = []
vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
def count_vowels2(a_string):
global vowel_list
vowel_letter_num = 0
for list_letter in a_string:
if list_letter in vowel_list:
vowel_letter_num += 1
return vowel_letter_num

def count_v2(list_t):
global num
count_f = len(list_t)
countv2 = 0
for i in range(count_f):
num += str(count_vowels2(list_t[countv2]))
countv2 += 1
print(num)
count_v2(fruit_list)

#5
def parallelogram(num):
for i in range(1):
my_string = ''
for i in range(num):
my_string += "*"
print(my_string)
count = 1
for i in range(num):
my_string2 = ''
for i in range(count):
my_string2 += " "
for i in range(num-1):
my_string2 += "*"
count += 1
num -= 1
print(my_string2)
parallelogram(3)
