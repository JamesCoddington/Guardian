#! var/bin/python3

def monitor():
  print("Now Monitoring your nuts")

def user_input():
  user = input("Would you like to start monitoring? [Y/n]\n")
  if user.upper() == "Y":
    monitor()
  elif user.upper() != "N":
    print("Please type Y for yes, or N for no")
    user_input()
  else:
    print("Exiting Program")

user_input()