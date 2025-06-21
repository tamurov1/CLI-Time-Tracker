# CLI-TRACKER

**Creator:** Dmytrii Tamurov  
**Current Version:** 0.1d

---

## Overview

**CLI-TRACKER** is a lightweight Python-based tool designed to help users track the amount of time they spend in the command-line interface (CLI). Whether you're a developer, sysadmin, or just curious about your terminal habits, this tracker runs silently in the background and logs your usage data to a local file.

---

## Features

- **Time Tracking**  
  Automatically tracks how long you spend in the terminal during each session.

- **Daily Logging**  
  Saves usage data to a local JSON file (`~/.cli_usage_stats.json`), organized by date.

- **Minimal Resource Usage**  
  Runs in the background with minimal CPU and memory impact.

- **Easy to Run**  
  Start tracking in one command. View stats anytime.

---

## Installation

```bash
git clone https://github.com/yourusername/cli-tracker.git
cd cli-tracker
python3 cli_tracker.py

## View Your Stats

To see how much time you've spent in the CLI, run:

python3 view_stats.py
