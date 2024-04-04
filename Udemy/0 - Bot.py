import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.click(x = 206, y = 412)

d = 1
while d <= 81:
    p = 1
    while p <= 81:
        pyautogui.press('F2')
        pyautogui.press('Left')
        
        i = 1
        while i <= 4:
            pyautogui.press('delete')
            i += 1

        pyautogui.press('enter')
        pyautogui.press('down')