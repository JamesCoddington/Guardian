#! var/bin/python3
import psutil
import json
import csv
from os.path import isfile


# Takes an input from the user on whether or not they want to start the program
def user_input():
    user = input("Would you like to start monitoring? [y/n]\n")
    if user.upper() == "Y":
        monitor()
    elif user.upper() != "N":
        print("Please type [y] for yes, or [n] for no ")
        user_input()
    else:
        print("Exiting the program")


# The main chunk of the application. This method monitors the established connections found within psutil.net_connections()
# and checks if they are already blacklisted or whitelisted within the status.json file. If so, then the program will ignore it.
# If not then the user is prompted with user_prompt().
def monitor():
    print("Now monitoring your established connections")
    check_csv()
    while True:
        for connection in psutil.net_connections():
            # connection contains the pid, name of the process, status, and when the process started
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

                user_prompt(status, application_name, application_path)


# Checks to see if the csv file already exists on the machine, if not create one for them.
def check_csv():
    if not isfile("blacklist_log.csv"):
        log = open("blacklist_log.csv", "w")
        writer = csv.writer(log)
        writer.writerow(["Application Name", "Application Path"])
        log.close()


# Prompts the user whether they want to blacklist or whitelist the application
def user_prompt(status, application_name, application_path):
    while True:
        try:
            response = input(f"Would you like to whitelist {application_name}? [y/n]\n")

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
        except PermissionError:
            print("Please close the csv file before answering No\n")


# Writes the application name and path to the end of the csv file.
def output_log(application_name, application_path):
    log = open("blacklist_log.csv", "a")
    writer = csv.writer(log)
    writer.writerow([application_name, application_path])
    log.close()


if __name__ == "__main__":
    connections_list = set()
    user_input()
