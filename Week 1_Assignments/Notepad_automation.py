import pyautogui
import time

# Small delay so you can switch to desktop
time.sleep(3)

# Open Start menu (Windows)
pyautogui.press('win')
time.sleep(1)

# Type Notepad and open it
pyautogui.write('notepad', interval=0.1)
pyautogui.press('enter')
time.sleep(2)

# Type text in Notepad
message = """
Hello 👋

This file was created automatically using PyAutoGUI.
Python is powerful and fun!

- Automated by Sakthi 😎
"""
pyautogui.write(message, interval=0.05)

# Save the file (Ctrl + S)
pyautogui.hotkey('ctrl', 's')
time.sleep(1)

# Type file name
pyautogui.write('pyautogui_demo.txt', interval=0.1)
time.sleep(1)

# Press Enter to save
pyautogui.press('enter')
time.sleep(1)

# Close Notepad
pyautogui.hotkey('alt', 'f4')
