import pyautogui
import keyboard
import time
    
record = 's'
pos = []
length = len(pos)
i = 1

def click():
    while len(pos) > 0:
        pyautogui.click(pos[0])
        pos.remove(pos[0])

def check(x, y):
 if pyautogui.pixelMatchesColor(x, y, (255, 255, 255)):
    if not (x, y) in pos:
        pos.append((x, y))
    elif pos[len(pos) - 1] != (x, y):
        pos.append((x, y))
   
while True:
    if keyboard.is_pressed('r'):
        record = 'r'
    if (keyboard.is_pressed('l') == True) | (record == 'l'):
        record = 's'
        print(pos)
        length = len(pos)
        i = i + 1
        click()
        record = 'r'
    if record == 'r':
        print(len(pos), length)
        if(len(pos) > length):
            time.sleep(0.5)
            record = 'l'
        check(821, 334)
        check(960, 334)
        check(1087, 330)
        check(833, 477)
        check(968, 458)
        check(1075, 477)
        check(819, 612)
        check(961, 600)
        check(1096, 607)
        
            