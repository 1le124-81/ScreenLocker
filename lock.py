from datetime import datetime
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox
import pyautogui
import time

# simple tkinter window to get user input
answer = simpledialog.askstring("Input", "Lock time (H:MM):")

print(answer)

# validation function for the correct time format
def is_x_xx(text):
    if not text:
        return False

    parts = text.split(":")
    if len(parts) != 2:
        return False
    
    if len(text) < 4 or len(text) > 5:
        return False
    
    if text[0] == '0':
        return False

    h, m = parts
    if not h.isdigit() or not m.isdigit():
        return False

    h = int(h)
    m = int(m)

    
    return 1 <= h <= 12 and 0 <= m <= 59

is_x_xx(answer)
# ends code if is wrong format
if not is_x_xx(answer):
    messagebox.showinfo("Info", "Invalid time format.")
    sys.exit()
#adds 0 if the user input is less than 4 characters to make it a valid time format
if len(answer) <= 4:
    answer = "0" + answer
    print("text adjusted")
    print(answer)

a = 0
print(answer)

# while time is less than 1800 seconds (30 minutes), check the current time every second
while a <=1800: 
    formatted = datetime.now().strftime("%I:%M")
    print(formatted + "aaa")
    a += 1
    print(f'running {a}')
    #if is time, then alert.
    if formatted == answer:
        print("TIME UP!")
        

        print("answer is valid. proceeding...")
        pyautogui.press("space")   
        messagebox.showwarning("lock", "screen locked.")
        sys.exit()

    time.sleep(1)
messagebox.showwarning("lock", "lock cancelled.")
sys.exit()