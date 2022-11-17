#! var/bin/python3
from pprint import pprint
import psutil
import json

connections_list = set()
blacklist = []


def monitor():
    print("Now monitoring your nuts up close and personal")

    for connection in psutil.net_connections():
        process = psutil.Process(connection.pid)
        # process contains the pid, name of the process, status, and when the process started
        # process.exe() shows us the file location
        if connection.status == psutil._common.CONN_ESTABLISHED:
            connections_list.add(process.exe())
            # print(process.exe())

    for connection in connections_list:
        whitelist_file = open("whitelist.json", "r")
        whitelist = json.load(whitelist_file)
        whitelist_file.close()

        if connection in whitelist["paths"] or connection in blacklist:
            continue

        while True:
            response = input(f"Would you like to whitelist {connection}? [y/n]\n")

            if response.upper() == "Y":
                whitelist["paths"].append(connection)
                whitelist_file = open("whitelist.json", "w")
                json.dump(whitelist, whitelist_file)
                whitelist_file.close()
                break

            elif response.upper() == "N":
                blacklist.append(connection)
                break


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
