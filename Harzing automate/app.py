import pyautogui
import subprocess
import time
import searchCheck

# Prompt the user for title words
title_words = input("Please enter the title words: ")

# Launch the application
subprocess.Popen(r"C:\Program Files\Harzing's Publish or Perish 8\pop8win.exe")
time.sleep(2)
pyautogui.click(x=752, y=458)

# Enter title
time.sleep(1)
pyautogui.click(x=676, y=457)
pyautogui.write(title_words)

# Start search
pyautogui.click(x=1423, y=393)
searchCheck.wait_for_color(529, 193, (116, 247, 90))  # Wait for search to complete

# Export actions
pyautogui.click(x=578, y=187)
pyautogui.click(x=338, y=140)
pyautogui.click(x=421, y=323)
time.sleep(1)
pyautogui.click(x=1819, y=458)
