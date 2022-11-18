#! var/bin/python3
from pprint import pprint
import psutil
import json

connections_list = set()
blacklist = []


def monitor():
    print("Now monitoring your established connections")
    while True:
        for connection in psutil.net_connections():
            # process contains the pid, name of the process, status, and when the process started
            if connection.status == psutil._common.CONN_ESTABLISHED:
                process = psutil.Process(connection.pid)
                connections_list.add(process)
                # print(process.exe())

        for connection in connections_list:
            whitelist_file = open("whitelist.json", "r")
            whitelist = json.load(whitelist_file)
            whitelist_file.close()

            if psutil.pid_exists(connection.pid):
                if (
                    connection.exe() in whitelist["paths"]
                    or connection.exe() in blacklist
                ):
                    continue

                while True:
                    response = input(
                        f"Would you like to whitelist {connection.name()}? [y/n]\n"
                    )

                    if response.upper() == "Y":
                        whitelist["paths"].append(connection.exe())
                        whitelist_file = open("whitelist.json", "w")
                        json.dump(whitelist, whitelist_file)
                        whitelist_file.close()
                        break

                    elif response.upper() == "N":
                        blacklist.append(connection.exe())
                        break


def user_input():
    user = input("Would you like to start monitoring? [y/n]\n")
    if user.upper() == "Y":
        monitor()
    elif user.upper() != "N":
        print("Please type [y] for yes, or [n] for no ")
        user_input()
    else:
        print("Exiting the program")


user_input()
