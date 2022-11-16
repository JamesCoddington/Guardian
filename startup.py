#! var/bin/python3
from pprint import pprint
import psutil
import json

whitelist_file = open("whitelist.json")
connections_list = set()
black_list = []

def monitor():
  print("Now monitoring your nuts up close and personal")
  
  for connection in psutil.net_connections():
      process = psutil.Process(connection.pid)
      # process contains the pid, name of the process, status, and when the process started
      # process.exe() shows us the file location
      if connection.status == psutil._common.CONN_ESTABLISHED:
        connections_list.add(process.exe())
        # print(process.exe())
  pprint(connections_list)

  for connection in connections_list:
    whitelist = json.dumps(whitelist_file)
    if connection in whitelist['path'] or connection in black_list:
      continue

    response = input(f"Would you like to whitelist {connection}? [y/n]\n")
    if response.upper() == "Y":
        pass
      # If they do not want to whitelist add to blacklist
        # Black list is saved locally while the whitelist should be it's own json file

def user_input():
  user = input("Would you like to start monitoring? 🤓 [y/n]\n")
  if user.upper() == "Y":
    monitor()
  elif user.upper() != "N":
    print("Please type [y] for yes, or [n] for no 😡")
    user_input()
  else:
    print("Exiting this bitch 💀")

user_input()