import time
import subprocess
from clock_convert import clock_convert

# twelve_hr_format -> time
alarm_time_str = "3:37"  # DEFAULT TIME = 3:37 pm
ampm = "pm"

ALARM_TIME = clock_convert(alarm_time_str, ampm)
AUDIO_FILE = "/home/ren/Music/Dead Eyes - Promoting Sounds, Powfu, Ouse.flac"

while True:
    current_time = time.strftime("%H:%M")
    if current_time == ALARM_TIME:
        print("ALARM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        subprocess.Popen([
            "vlc",
            "--intf", "dummy",
            "--play-and-exit",
            AUDIO_FILE
        ])
        break
    time.sleep(1)