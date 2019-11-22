dictionary_lab = {
 'cat': 'a domestic feline', 
 'dog': 'a domestic canine', 
 'chair': 'furniture piece for sitting', 
 'car': 'automobile',
 'gg':'Good Game',
 'YOLO':'You Only Live Once',
 'jimmy':'a boy from south park who cannot walk and likes to shout out his name when he is very exciting.',
 'kenny':'a person from south park who always be killed',
 'south park':'a normal park',
 'cartman':'a fat axx in south park',
 'winter':'the smartest person all over the world',
 'smh':'Shake my hand'
 }
quit_value = False

while quit_value == False:
  word_input = input("What word would you like to look up:")
  if word_input =='quit!':
    break
  elif str.lower(word_input) in dictionary_lab:
    print(str(word_input)+": "+dictionary_lab[str.lower(word_input)])
  else:
    print("Sorry,",word_input,"is not defined.")
    add_ask = input("DO you want to update values and add key/value pairs to the dictionary?(y/n)")
    if add_ask == 'y':
      key_up = input("What is the key:")
      value_up = input("What is the value:")
      dictionary_lab.update({str(key_up):str(value_up)})
      print("Done!")
    else:
      print("Ok...")
