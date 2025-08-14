import os
import time
from datetime import datetime

WATCHED_DIR = "watched"
LOG_FILE = "agent.log"

def ensure_watched_dir():
    if not os.path.exists(WATCHED_DIR):
        os.makedirs(WATCHED_DIR)

def get_files_snapshot():
    return set(os.listdir(WATCHED_DIR))

def log_event(event):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} - {event}\n")
    print(event)

def main():
    print(f"Starting automation agent. Watching folder: {WATCHED_DIR}")
    ensure_watched_dir()
    seen_files = get_files_snapshot()

    while True:
        time.sleep(2)  # Check every 2 seconds
        current_files = get_files_snapshot()
        new_files = current_files - seen_files
        if new_files:
            for filename in new_files:
                log_event(f"New file detected: {filename}")
        seen_files = current_files

if __name__ == "__main__":
    main()
