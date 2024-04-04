import pyautogui
import time
d = 9

p = 1
while p <= 47:
    pyautogui.PAUSE = 0.5
    #PEGAR A INFORMACAO NO SITE E COLOCA NA AULA DESEJADA
    #PASSO 1: PEGAR AS INFORMAÇÕES NO SITE
    pyautogui.click(x = 1481, y = -1012, clicks= 3)
    pyautogui.press('delete')
    pyautogui.write(f'aula{p}.py')
    pyautogui.press('enter')
    pyautogui.click(x = 451, y = -217)
    pyautogui.click(x = 1353, y = -700)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')

    #PASSO 2: COLOCAR AS INFORMAÇÕES NO VSCODE
    pyautogui.click(x = 176, y = 166, clicks= 3)
    pyautogui.press('delete')
    pyautogui.write(f'aula{p}.py')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.click(x = 1656, y = 325)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'v')
    p += 1

# BOT CRIAR AQRUIVOS .PY
# p = 30
# while p <= 47:
#     pyautogui.PAUSE = 2
#     pyautogui.click(x = 396, y = 291, button='right')
#     pyautogui.click(x = 702, y = 329)
#     pyautogui.write(f'aula{p}.py')
#     pyautogui.press('enter')
#     pyautogui.click(x = 396, y = 291)
#     pyautogui.scroll(50000)
#     p += 1
