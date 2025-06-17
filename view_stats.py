
import json
import os

LOG_FILE = os.path.expanduser("~/.cli_usage_stats.json")

def display():
    if not os.path.exists(LOG_FILE):
        print("No stats found.")
        return

    with open(LOG_FILE, 'r') as f:
        stats = json.load(f)

    for date, seconds in stats.items():
        minutes = seconds // 60
        print(f"{date}: {minutes} min")

if __name__ == "__main__":
    display()
