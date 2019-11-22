#There are still many problems,so I really hope that someone can help me...
import random
import time
#start_asking part:
print('Welcome to game:Tic Tac Toe!')
time.sleep(1)
print("This virsion is developed for getting more data.")
ai_winter = 1
p1_name = "Winter's AlphaGo 1.0.0 beta-p1"
p2_name = "Winter's AlphaGo 1.0.0 beta-p2"
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
          if game_table[j] == "X":
            print(p1_name,'wins!')
          if game_table[j] =="O":
            print(p2_name,'wins!')
          cek_num += 1
          break
  for z in range(0,size_input-2):
    for j in range(z*size_input,(z+1)*size_input):
      if game_table[j] != ' ':
        if game_table[j] == game_table[j+size_input] and game_table[j] == game_table[j+2*size_input]:
          if game_table[j] == "X":
            print(p1_name,'wins!')
          if game_table[j] =="O":
            print(p2_name,'wins!')
          cek_num += 1
          break
  for i in range(0,size_input-2):
    for j in range(i*size_input+2,(i+1)*size_input):
      if game_table[j] != ' ':
        if game_table[j] == game_table[j+size_input-1] and game_table[j] == game_table[j+2*(size_input-1)]:
          if game_table[j] == "X":
            print(p1_name,'wins!')
          if game_table[j] =="O":
            print(p2_name,'wins!')
          cek_num += 1
          break
  for i in range(0,size_input-2):
    for j in range(i*size_input,(i+1)*size_input-2):
      if game_table[j] != ' ':
        if game_table[j] == game_table[j+size_input+1] and game_table[j] == game_table[j+2*size_input+2]:
          if game_table[j] == "X":
            print(p1_name,'wins!')
          if game_table[j] =="O":
            print(p2_name,'wins!')
          cek_num += 1
          break

############################################
# The smartest AI beta 1.0.0:
def ai_choice_p1():
  num_ai = 0
  global row_input
  global column_input
  if round_num == 0:
     game_table[4] = 'X'
     print(p1_name,"put O on [2,2]")
  else:
    if num_ai == 0:
      for z in range(0,size_input):
        for j in range(z*size_input,(z+1)*size_input-2):
          if game_table[j] != ' ':
            if game_table[j] == game_table[j+1] and game_table[j+2] == ' ':
                game_table[j+2] = 'X'
                num_ai = 1
            elif game_table[j+1] == game_table[j+2] and game_table[j] == ' ':
                game_table[j] = 'X'
                num_ai = 1
            elif game_table[j] == game_table[j+2] and game_table[j+1] == ' ':
                game_table[j+1] = 'X'
                num_ai = 1
    if num_ai == 0:
      for z in range(0,size_input-2):
        for j in range(z*size_input,(z+1)*size_input):
          if game_table[j] != ' ':
            if game_table[j] == game_table[j+size_input] and game_table[j+2*size_input] == ' ':
              game_table[j+2*size_input] = 'X'
              num_ai = 1
            elif game_table[j] == game_table[j+2*size_input] and game_table[j+size_input] == ' ':
              game_table[j+size_input] = 'X'
              num_ai = 1
            elif game_table[j+size_input] == game_table[j+2*size_input] and game_table[j] == ' ':
              game_table[j] = 'X'
              num_ai = 1
    if num_ai == 0:
      for i in range(0,size_input-2):
        for j in range(i*size_input+2,(i+1)*size_input):
          if game_table[j] != ' ':
            if game_table[j] == game_table[j+size_input-1] and game_table[j+2*(size_input-1)] == ' ':
              game_table[j+2*(size_input-1)] = 'X'
              num_ai = 1
            elif game_table[j] == game_table[j+2*(size_input-1)] and game_table[j+size_input-1] == ' ':
              game_table[j+size_input-1] = "X"
              num_ai = 1
            elif game_table[j+size_input-1] == game_table[j+2*(size_input-1)] and game_table[j] == ' ':
              game_table[j] = "X"
              num_ai = 1
    if num_ai == 0:
      for i in range(0,size_input-2):
        for j in range(i*size_input,(i+1)*size_input-2):
          if game_table[j] != ' ':
            if game_table[j] == game_table[j+size_input+1] and game_table[j+2*size_input+2] == " ":
              game_table[j+2*size_input+2] = "X"
              num_ai = 1
            elif game_table[j] == game_table[j+2*size_input+2] and game_table[j+size_input+1] == " ":
              game_table[j+size_input+1] = "X"
              num_ai = 1
            elif game_table[j+size_input+1] == game_table[j+2*size_input+2] and game_table[j] == " ":
              game_table[j] = "X"
              num_ai = 1
      if num_ai == 0:
        while num_ai == 0:
          row_input = random.randint(1,size_input)
          column_input = random.randint(1,size_input)
          if game_table[(row_input-1)*size_input+column_input-1] == ' ':
            game_table[(row_input-1)*size_input+column_input-1]= 'X'
            break
        print("Winter's AlphaGo 1.0.0 beta put X on ["+str(row_input)+','+str(column_input)+']')
  num_ai = 0

def ai_choice_p2():
  num_ai = 0
  global row_input
  global column_input
  if round_num == 1:
    choice_i = random.randint(1,4)
    if choice_i == 1:
      game_table[0] = "O"
    elif choice_i == 2:
      game_table[2] = "O"
    elif choice_i == 3:
      game_table[6] = "O"
    elif choice_i == 4:
      game_table[8]= "O"
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
  num_ai = 0
#############################################
round_num = 0
print_table()
while round_num != size_input * size_input:
  while cek_num == 0:
    print(p1_name,", now it is your turn:")
    time.sleep(1)
    ai_choice_p1()
    print_table()    
    check_winer()
    round_num +=1
    if cek_num != 0:
      break
    if round_num == size_input * size_input:
      break
    print(p2_name,", now it is your turn:")
    time.sleep(1)
    ai_choice_p2()
    print_table()
    check_winer()
    round_num +=1
    if round_num == size_input * size_input:
      break

if round_num == size_input * size_input and cek_num ==0:
    print('Tie game!')
