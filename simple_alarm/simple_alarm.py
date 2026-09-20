#!/usr/bin/python3

import time
import subprocess
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from clock_convert import clock_convert

# twelve_hr_format -> time
while True:
    try:
        alarm_time_str = input("Enter alarm time (HH:MM in 12-hour format): ")
        ampm = input("Enter AM or PM: ").lower()
        
        if ampm not in ["am", "pm"]:
            print("Invalid input. Please enter 'am' or 'pm'.")
            continue
        
        ALARM_TIME = clock_convert(alarm_time_str, ampm)
        break
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def force_on_top(window_title, timeout=5):
    """Raise and set the window always-on-top (needed on Cinnamon,
    which opens new windows behind others due to focus-stealing prevention)."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        result = subprocess.run(
            ["wmctrl", "-l"], capture_output=True, text=True
        )
        for line in result.stdout.splitlines():
            if window_title in line:
                win_id = line.split()[0]
                subprocess.run(["wmctrl", "-i", "-r", win_id, "-b", "add,above"])
                subprocess.run(["wmctrl", "-i", "-a", win_id])
                return True
        time.sleep(0.1)
    return False


while True:
    current_time = time.strftime("%H:%M")
    if current_time == ALARM_TIME:
        print("ALARM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        subprocess.Popen([
            "canberra-gtk-play", "-i", "alarm-clock-elapsed"
        ])
        subprocess.Popen([
            "zenity",
            "--info",
            "--title=Alarm",
            f"--text=The set time {alarm_time_str} {ampm.upper()} is now!",
            "--width=300"
        ])
        force_on_top("Alarm")
        break
    time.sleep(1)
