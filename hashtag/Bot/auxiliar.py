import pyautogui
import time

time.sleep(5)
x, y = pyautogui.position()
print("Posicao atual do mouse:")
print("x = "+str(x)+" y = "+str(y))