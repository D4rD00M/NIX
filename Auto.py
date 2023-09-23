import time
import pyautogui

pyautogui.hotkey('win','r')
pyautogui.typewrite('powershell')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.typewrite('cd Desktop/NIX/NIX ; python main.py')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.hotkey('win','r')
pyautogui.typewrite('powershell')
pyautogui.hotkey('enter')
time.sleep(5)
pyautogui.typewrite('cd Desktop/NIX/NIX/NIX/Features ;python click_mouse.py 1370 80 ; python click_mouse.py 1450 880 ; Invoke-Item MYFeatures.txt' )
pyautogui.hotkey('enter')