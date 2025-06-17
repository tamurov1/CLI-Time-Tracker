
import time
import json
import os
from datetime import datetime

LOG_FILE = os.path.expanduser("~/.cli_usage_stats.json")
INTERVAL = 10 # secs between checks

def load_stats():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_stats(stats):
    with open(LOG_FILE, 'w') as f:
        json.dump(stats, f, indent=2)

def track_time():
    stats = load_stats()
    today = datetime.now().strftime("%Y-%m-%d")
    start_time = time.time()

    try:
        while True:
            time.sleep(INTERVAL)
            elapsed = int(time.time() - start_time)
            stats[today] = stats.get(today, 0) + INTERVAL
            save_stats(stats)
            start_time = time.time()
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    track_time()
