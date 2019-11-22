vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
def de_vowel(a_string):
  global vowel_list
  de_vowel_string = []
  for list_letter in a_string:
    if list_letter not in vowel_list:
      de_vowel_string.append(list_letter)
  return("".join(de_vowel_string))
def count_vowels(a_string):
  global vowel_list
  vowel_letter_num = 0
  for list_letter in a_string:
    if list_letter in vowel_list:
      vowel_letter_num += 1
  print(vowel_letter_num)
no_vowels = de_vowel("This sentence has no vowels")
count_vowels("This sentence has no vowels")
print(no_vowels)
