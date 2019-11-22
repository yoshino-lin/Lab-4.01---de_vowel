import random
import time
#start_asking part:
print('Welcome to game:Tic Tac Toe!')
time.sleep(1)
print("Do you want to player with a AI?")
mode_choice = input('n for turn-by-turn based games(n/y)')
if mode_choice == 'n':
  ai_winter = 0
  p1_name = input('Player1, please enter your name:')
  p2_name = input('Player2, please enter your name:')
  print('Now we have: 3*3,4*4,5*5,customize:')
  size_choice_inp = int(input('Which size of the table do you want(1/2/3/4):'))
  #size_choice_inp
  if size_choice_inp == 1:
    size_input = 3
  if size_choice_inp == 2:
    size_input = 4
  if size_choice_inp == 3:
    size_input = 5
  if size_choice_inp == 4:
    size_input = int(input('How big do you want your table to be? Enter a number:'))
elif mode_choice == 'y':
  print('How dare you are to chooce beat me!')
  ai_winter = 1
  p1_name = input('Player, please enter your name:')
  p2_name = "Winter's AlphaGo 1.0.0 beta"
  size_input = 3
###########################################
game_table = []
for i in range(0,size_input*size_input):
  game_table.append(' ')
def print_table():
  for i in range(size_input):
    i_plus_one = int(i + 1)
    print(game_table[i*size_input:i_plus_one*size_input])
############################################
#check winner:
cek_num = 0
def check_winer():
  global cek_num
  for z in range(0,size_input):
    for j in range(z*size_input,(z+1)*size_input-2):
      if game_table[j] != ' ':
        if game_table[j] == game_table[j+1] and game_table[j] == game_table[j+2]:
          print(game_table[j],'wins!')
          cek_num += 1
          break
  for z in range(0,size_input-2):
    for j in range(z*size_input,(z+1)*size_input):
      if game_table[j] != ' ':
        if game_table[j] == game_table[j+size_input] and game_table[j] == game_table[j+2*size_input]:
          print(game_table[j],'wins!')
          cek_num += 1
          break
  for i in range(0,size_input-2):
    for j in range(i*size_input+2,(i+1)*size_input):
      if game_table[j] != ' ':
        if game_table[j] == game_table[j+size_input-1] and game_table[j] == game_table[j+2*(size_input-1)]:
          print(game_table[j],'wins!')
          cek_num += 1
          break
  for i in range(0,size_input-2):
    for j in range(i*size_input,(i+1)*size_input-2):
      if game_table[j] != ' ':
        if game_table[j] == game_table[j+size_input+1] and game_table[j] == game_table[j+2*size_input+2]:
          print(game_table[j],'wins!')
          cek_num += 1
          break

############################################
# The smartest AI beta 1.0.0:
def ai_choice():
  num_ai = 0
  global row_input
  global column_input
  if ai_winter == 1 or ai_winter ==2:
    if round_num == 1:
      if game_table[4] != 'X':
        game_table[4] ='O'
        print("Winter's AlphaGo 1.0.0 beta put O on [2,2]")
      else:
        row_input = 1
        column_input = 1
        game_table[(row_input-1)*size_input+column_input-1]= 'O'
        print("Winter's AlphaGo 1.0.0 beta put O on [1,1]")
    else:
      if num_ai == 0:
        for z in range(0,size_input):
          for j in range(z*size_input,(z+1)*size_input-2):
            if game_table[j] != ' ':
              if game_table[j] == game_table[j+1] and game_table[j+2] == ' ':
                  game_table[j+2] = 'O'
                  num_ai = 1
              elif game_table[j+1] == game_table[j+2] and game_table[j] == ' ':
                  game_table[j] = 'O'
                  num_ai = 1
              elif game_table[j] == game_table[j+2] and game_table[j+1] == ' ':
                  game_table[j+1] = 'O'
                  num_ai = 1
      if num_ai == 0:
        for z in range(0,size_input-2):
          for j in range(z*size_input,(z+1)*size_input):
            if game_table[j] != ' ':
              if game_table[j] == game_table[j+size_input] and game_table[j+2*size_input] == ' ':
                game_table[j+2*size_input] = 'O'
                num_ai = 1
              elif game_table[j] == game_table[j+2*size_input] and game_table[j+size_input] == ' ':
                game_table[j+size_input] = 'O'
                num_ai = 1
              elif game_table[j+size_input] == game_table[j+2*size_input] and game_table[j] == ' ':
                game_table[j] = 'O'
                num_ai = 1
      if num_ai == 0:
        for i in range(0,size_input-2):
          for j in range(i*size_input+2,(i+1)*size_input):
            if game_table[j] != ' ':
              if game_table[j] == game_table[j+size_input-1] and game_table[j+2*(size_input-1)] == ' ':
                game_table[j+2*(size_input-1)] = 'O'
                num_ai = 1
              elif game_table[j] == game_table[j+2*(size_input-1)] and game_table[j+size_input-1] == ' ':
                game_table[j+size_input-1] = "O"
                num_ai = 1
              elif game_table[j+size_input-1] == game_table[j+2*(size_input-1)] and game_table[j] == ' ':
                game_table[j] = "O"
                num_ai = 1
      if num_ai == 0:
        for i in range(0,size_input-2):
          for j in range(i*size_input,(i+1)*size_input-2):
            if game_table[j] != ' ':
              if game_table[j] == game_table[j+size_input+1] and game_table[j+2*size_input+2] == " ":
                game_table[j+2*size_input+2] = "O"
                num_ai = 1
              elif game_table[j] == game_table[j+2*size_input+2] and game_table[j+size_input+1] == " ":
                game_table[j+size_input+1] = "O"
                num_ai = 1
              elif game_table[j+size_input+1] == game_table[j+2*size_input+2] and game_table[j] == " ":
                game_table[j] = "O"
                num_ai = 1
        if num_ai == 0:
          while num_ai == 0:
            row_input = random.randint(1,size_input)
            column_input = random.randint(1,size_input)
            if game_table[(row_input-1)*size_input+column_input-1] == ' ':
              game_table[(row_input-1)*size_input+column_input-1]= 'O'
              break
          print("Winter's AlphaGo 1.0.0 beta put O on ["+str(row_input)+','+str(column_input)+']')
  num_ai == 0
#############################################
round_num = 0
print_table()
if ai_winter == 0:
  while round_num != size_input * size_input:
    while cek_num == 0:
      print(p1_name,", now it is your turn:")
      row_input = int(input("Which row:"))
      column_input = int(input("Which column:"))
      while round_num != -1:
        if game_table[(row_input-1)*size_input+column_input-1] == ' ': 
          game_table[(row_input-1)*size_input+column_input-1]= 'X'
          break
        else:
          print('Please try again')
          print(p1_name,", now it is your turn:")
          row_input = int(input("Which row?"))
          column_input = int(input("Which column?"))
      print_table()    
      check_winer()
      round_num +=1
      if cek_num != 0:
        break
      if round_num == size_input * size_input:
        break
      print(p2_name,", now it is your turn:")
      row_input = int(input("Which row:"))
      column_input = int(input("Which column:"))
      while round_num != -1:
        if game_table[(row_input-1)*size_input+column_input-1] == ' ': 
          game_table[(row_input-1)*size_input+column_input-1]= 'O'
          break
        else:
          print('Please try again')
          print(p1_name,", now it is your turn:")
          row_input = int(input("Which row?"))
          column_input = int(input("Which column?"))
      print_table()
      check_winer()
      round_num +=1
elif ai_winter == 1:
    while round_num != size_input * size_input:
      while cek_num == 0:
        print(p1_name,", now it is your turn:")
        row_input = int(input("Which row:"))
        column_input = int(input("Which column:"))
        while round_num != -1:
          if game_table[(row_input-1)*size_input+column_input-1] == ' ': 
            game_table[(row_input-1)*size_input+column_input-1]= 'X'
            break
          else:
            print('Please try again')
            print(p1_name,", now it is your turn:")
            row_input = int(input("Which row?"))
            column_input = int(input("Which column?"))
        print_table()    
        check_winer()
        round_num +=1
        if cek_num != 0:
          break
        if round_num == size_input * size_input:
          break
        print("Now it is AlphaGo 1.0.0 beta's turn:")
        ai_choice()
        print_table()
        check_winer()
        round_num +=1

if round_num == size_input * size_input and cek_num == 0:
  print('Tie game!')
    
