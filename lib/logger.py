from datetime import datetime
import os

LOG_PATH = "data/user_logs.txt"

#Uses an external module and with open() to safely append logs.
def log_action(action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_logs.txt", "a") as file:
        file.write(f"[{timestamp}] {action}\n")

log_action("User logged in")
log_action("User updated profile")

#Gracefully handles file reading and missing file errors.
def search_logs(keyword):
    try:
        with open("user_logs.txt", "r") as file:
            for line in file:
                if keyword in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found.")

search_logs("profile")