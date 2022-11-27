# Guardian

**About** <br>
Guardian is an application that monitors the established connections found on the device, and decides whether to whitelist
or blacklist the application that is sending an established connection.<br> <br>
Whitelisted applications are saved within the status.json file. <br> <br>
Blacklisted applications are saved within the status.json file as well, but it is also written and logged into a csv file called "blacklist_log.csv". There it contains the unwanted application's name and file path.<br> <br>

**Purpose** <br>
The purpose of Guardian is to have the user be more of aware of what is making a connection on the user's device. <br> <br>


**Installation and Use** <br>
To run make sure Python is installed on your machine.

Windows:
    run "pip install psutil" in your terminal to install psutils
    run "python startup.py" to run the program

Mac:
    run "pip3 install psutil" in your terminal
    run "python3 startup.py" to run the program

**Blacklist and Whitelist**
TODO