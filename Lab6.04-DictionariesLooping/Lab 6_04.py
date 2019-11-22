example_paragraph = "It was a beautiful day in New York City. Our hero Ariana Grande was on a walk from the Standard to Duane Reade. Ariana Grande was walking rather quickly because she had lived in New York for a few months. All of a sudden a slimy donut appeared out of nowhere. Ariana Grande decided to prance foolishly instead of dealing with the situation. Thrown off from Duane Reade Ariana Grande decides to go to Times Square instead. What a beautiful day in New York."

#make all letters lowercase
example_paragraph_lower = example_paragraph.lower()

#remove all periods
example_paragraph_lower_no_punctuation = example_paragraph_lower.replace(".", "")

#convert paragraph into a list of individual strings
example_word_list = example_paragraph_lower_no_punctuation.split(" ")

#eaist way(4 lines!!)
def find_max_value(input_paragraph):
  input_paragraph.replace('.','')
  input_paragraph = input_paragraph.split()
  from collections import Counter
  print(Counter(input_paragraph))

#but you want me...
def find_max_value(inp_para):
  inp_para.replace('.','')
  inp_para = inp_para.split()
  new_dic = {}
  word_list = [1,0]
  for i in range(0,len(inp_para)):
    if inp_para[i] not in new_dic:
      new_dic.update({str(inp_para[i]):int(0)})
    if inp_para[i] in new_dic:
      new_dic[inp_para[i]] += 1

 #bonues:
 #print(sorted(new_dic.items(), key=lambda d: d[1], reverse=True))

  for i in range(4):
    for k in new_dic:
      if new_dic[k] > word_list[1]:
        word_list[1] = new_dic[k]
        word_list[0] = k
    print(word_list[0],',',word_list[1])
    del new_dic[word_list[0]]
    word_list = [1,0]

find_max_value(example_paragraph)
