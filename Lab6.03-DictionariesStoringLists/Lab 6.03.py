daily_to_do_list_lab = {
  "sunday":[],
  "monday":[],
  "tuesday":[],
  "wednesday":[],
  "thursday":[],
  "friday":[],
  "saturday":[]
}

re_working = 0

while re_working == 0:
  ask_action = input('What would you like to do:')
  ask_day = input('Which day:')
  ask_day = ask_day.lower()
  if ask_action == 'add':
    if ask_day in daily_to_do_list_lab:
      print("What would you like to add to " + ask_day + "'s to-do list?")
      thing = input()
      daily_to_do_list_lab[ask_day].append(thing)
      print("Done!")
  elif ask_action == 'get':
    for i in range(0,len(daily_to_do_list_lab[ask_day])):
      print('You have to',daily_to_do_list_lab[ask_day][i]+".")
  elif ask_action == 'quit':
    break
  else:
    print("Unknown input,please try again!")

print("return 0")
