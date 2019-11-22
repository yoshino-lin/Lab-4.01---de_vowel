example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York."

#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()

#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")

#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")

# You can edit the paragraph in wordlist.py if you want different words.
question_ask = input("What word would you like to know the frequency of:").lower()

#the easiest way
if question_ask in example_word_list:
  if example_word_list.count(question_ask) == 1:
    print("'"+question_ask+"' occurs 1 time")
  else:
    print("'"+question_ask+"' occurs "+str(example_word_list.count(question_ask))+" times")
else:
  print("'"+question_ask+"' does not occur")

#but you want me...
count_word = 0
for i in range(0,len(example_word_list)):
  if example_word_list[i] == question_ask:
    count_word += 1
if count_word == 0:
  print("'"+question_ask+"' does not occur")
elif count_word == 1:
  print("'"+question_ask+"' occurs 1 time")
else:
  print("'"+question_ask+"' occurs "+str(count_word)+" times")
