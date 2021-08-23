# check out the video on payloads (I used payloads here) :https://www.youtube.com/watch?v=Onz-Abnz03Q

# check out this video on how to convert this python file to .exe .... you can also add your custom icon and specify all features
# video link : https://www.youtube.com/watch?v=dKJyRzNSs6g

#program starts here:


import pyautogui # controls mouse and keyboard
import time # manages time functions
payload = " msedge https://www.youtube.com/watch?v=dQw4w9WgXcQ" # you can also use chrome in place of msedge ...
# I am using msedge because it is pre installed in every windows 10 computer

# press windows + r to open run
pyautogui.keyDown('win')
pyautogui.keyDown('r')
pyautogui.keyUp('win')
pyautogui.keyUp('r')
# wait for run to open
time.sleep(0.1)
#now write the payload
pyautogui.typewrite(payload)
#press enter
pyautogui.hotkey('enter')