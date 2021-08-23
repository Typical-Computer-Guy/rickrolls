import pyautogui
import time
payload = " msedge https://www.youtube.com/watch?v=dQw4w9WgXcQ"
pyautogui.keyDown('win')
pyautogui.keyDown('r')
pyautogui.keyUp('win')
pyautogui.keyUp('r')
time.sleep(0.1)
pyautogui.typewrite(payload)
pyautogui.hotkey('enter')