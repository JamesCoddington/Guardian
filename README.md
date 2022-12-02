# Guardian

## About

Guardian is an application that monitors the established network connections on your device and notifies you of new connections. Guardian also provides you with whitelist and blacklist functionality that allows you to ignore or log the connections of a specific process.

Guardian's approach to network montioring can be used to detect malicious applications like keyloggers when they try to exfiltrate user data.

Guardian provides an additional layer of functionality to computer systems that do not track network connections (such as clean installations of Windows or macOS).

Guardian is not an antivirus software and does not attempt to remove malicious applications from your machine. Guardian does tell you where to find the malicious application's executable.

## Purpose

The purpose of Guardian is to make the user more aware of the applications making connections on the user's device. This application can be used to detect keyloggers.

## Installation and use

Running Guardian requires that Python 3 is installed on your machine and in your system `PATH`.

Your Python installation may expose either a `python` or `python3` (`pip` or `pip3`) command. For simplicity, this guide will use `python`, but you should use the command that works with your machine.

To verify that your machine is ready to run Guardian, launch Terminal and run `python --version`. Ensure Python reports a version >= 3.

If you have trouble installing a compatible verison of Python, consult Python's installation guide [here](https://www.python.org/downloads/).

### Windows

To run Guardian on Windows, follow these steps:

1. Open Powershell and run `pip install psutil`. This installs the utility libraries Guardian uses to monitor your computer's network activity.

2. Navigate to the location of your Guardian installation in your terminal. Run `python startup.py` to start Guardian. 

### Mac

To run Guardian on macOS, follow these steps:

1. Open Terminal and run `pip install psutil` in your terminal. This installs the utility libraries Guardian uses to monitor your computer's network activity.

2. Navigate to the location of your Guardian installation in your terminal. Run `python startup.py` to start Guardian.

3. If you get an AccessDenied error you may need to login to your super user. To do this you can try running `sudo python startup.py`.

## Whitelist and blacklist

Guardian uses a whitelist and a blacklist to remember the process that are and aren't allowed to access your computer network. The application keeps track of these applications in `status.json`

When a process is added to the whitelist by the user, Guardian will stop notifying the user that the application is access their computer's network. This is useful for routine system processes that need access to the network.

When a process is added to the blacklist by the user, Guardian will log the location of the app in your files. These logs are available in Guardian's `blacklist_logs.csv` file. Each log entry contains the process's application's name and path.
