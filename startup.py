#! var/bin/python3
from pprint import pprint
import psutil
import json
import csv
from os.path import isfile

connections_list = set()

if not isfile("blacklist_log.csv"):
    log = open("blacklist_log.csv", "w")
    writer = csv.writer(log)
    writer.writerow(["Application Name", "Application Path"])
    log.close()

def monitor():
    print("Now monitoring your established connections")
    while True:
        for connection in psutil.net_connections():
            # process contains the pid, name of the process, status, and when the process started
            if connection.status == psutil._common.CONN_ESTABLISHED:
                process = psutil.Process(connection.pid)
                connections_list.add(process)

        for connection in connections_list:
            status_file = open("status.json", "r")
            status = json.load(status_file)
            status_file.close()
            application_name = connection.name()
            application_path = connection.exe()

            if psutil.pid_exists(connection.pid):
                if (
                    application_path in status["whitelist"]
                    or application_path in status["blacklist"]
                ):
                    continue

                while True:
                    response = input(
                        f"Would you like to whitelist {application_name}? [y/n]\n"
                    )

                    if response.upper() == "Y":
                        status["whitelist"].append(application_path)
                        status_file = open("status.json", "w")
                        json.dump(status, status_file)
                        status_file.close()
                        break

                    elif response.upper() == "N":
                        status["blacklist"].append(application_path)
                        status_file = open("status.json", "w")
                        json.dump(status, status_file)
                        status_file.close()
                        output_log(application_name, application_path)
                        break


def output_log(application_name, application_path):
    log = open("blacklist_log.csv", "a")
    writer = csv.writer(log)
    writer.writerow([application_name, application_path])
    log.close()


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
