table_loc = [1,2,3,4,5,6,7,8,9]
time_num = 0
#first round
while time_num < 9:
  time_num = time_num + 1
  print('This is the',time_num,'time!')
  print('This is turn for X!')
  player_int= int(input('Where do you want to put the number(from 1 to 9):'))
  table_loc[player_int - 1]= 'X'
  if time_num == 9:
    break
  print(table_loc[0:3])
  print(table_loc[3:6])
  print(table_loc[6:9])
  print('-----------------')
#X round over
  time_num = time_num + 1
  print('This is the',time_num,'time!')
  print('This is turn for O!')
  player_int= int(input('Where do you want to put the number(from 1 to 9):'))
  table_loc[player_int - 1] = 'O'
  print(table_loc[0:3])
