import psutil
import json
import csv
from os.path import isfile


class Guardian:
    def __init__(self):
        self.connections_list = set()


    def get_input(self, text):
        return input(text)


    """Takes an input from the user on whether or not they want to start the program"""
    def user_input(self):
        user = self.get_input("Would you like to start monitoring? [y/n]\n")
        if user.upper() == "Y":
            print("Now monitoring your established connections")
            self.check_csv()
            self.monitor()
        elif user.upper() != "N":
            print("Please type [y] for yes, or [n] for no ")
            self.user_input()
        else:
            return "Exiting the program"


    """The main chunk of the application. This method monitors the established connections found within psutil.net_connections()
    and checks if they are already blacklisted or whitelisted within the status.json file. If so, then the program will ignore it.
    If not then the user is prompted with user_prompt()."""
    def monitor(self):
        self.check_csv()
        while True:
            for connection in psutil.net_connections():
                # connection contains the pid, name of the process, status, and when the process started
                if connection.status == psutil._common.CONN_ESTABLISHED:
                    process = psutil.Process(connection.pid)
                    self.connections_list.add(process)

            for connection in self.connections_list:
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

                    self.user_prompt(status, application_name, application_path)


    """Checks to see if the csv file already exists on the machine, if not create one for them."""
    def check_csv(self):
        if not isfile("blacklist_log.csv"):
            log = open("blacklist_log.csv", "w")
            writer = csv.writer(log)
            writer.writerow(["Application Name", "Application Path"])
            log.close()

        if not isfile("status.json"):
            data = {"whitelist": [], "blacklist": []}
            status_file = open("status.json", "w")
            json.dump(data, status_file)
            status_file.close()


    """Prompts the user whether they want to blacklist or whitelist the application"""
    def user_prompt(self, status, application_name, application_path):
        while True:
            try:
                response = self.get_input(
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
                    self.output_log(application_name, application_path)
                    break
            except PermissionError:
                print("Please close the csv file before answering No\n")


    """Writes the application name and path to the end of the csv file."""
    def output_log(self, application_name, application_path):
        log = open("blacklist_log.csv", "a")
        writer = csv.writer(log)
        writer.writerow([application_name, application_path])
        log.close()


if __name__ == "__main__":
    Guardian().user_input()
