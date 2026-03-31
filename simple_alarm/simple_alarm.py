import time
import subprocess

ALARAM_TIME = "19:55"
AUDIO_FILE = "/home/ren/Music/Dead Eyes - Promoting Sounds, Powfu, Ouse.flac"

while True :
    current_time = time.strftime("%H:%M")
    if current_time == ALARAM_TIME :
        print("ALARM!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        subprocess.Popen([
            "vlc",
            "--intf", "dummy",
            "--play-and-exit",
            AUDIO_FILE
        ])
        break
    time.sleep(1)

    