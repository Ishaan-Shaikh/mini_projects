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

while True:
    current_time = time.strftime("%H:%M")
    if current_time == ALARM_TIME:
        print("ALARM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        subprocess.Popen([
        "zenity",
        "--info",
        "--title=Alarm",
        f"--text=The set time {alarm_time_str} {ampm.upper()} is now!",
        "--width=300"
        ])
        break
    time.sleep(1)