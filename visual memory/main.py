import numpy as np
import pyautogui
import keyboard
import cv2
import time

shapes = []
record = 'nothing'

def click():
    while len(shapes) > 0:
        print(shapes[0][0] + 500, shapes[0][1] + 250)
        pyautogui.click(shapes[0][0] + 500, shapes[0][1] + 250)
        shapes.remove(shapes[0])

def check():
    img = pyautogui.screenshot(region=(500,250, 1400 - 500,700 - 250))
    img_np = np.array(img)
    img_rgb = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(img_grey, 250, 255, cv2.THRESH_BINARY) 
    contours, _ = cv2.findContours( 
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    i = 0
    for contour in contours:
        M = cv2.moments(contour) 
        if M['m00'] != 0.0: 
            x = int(M['m10']/M['m00']) 
            y = int(M['m01']/M['m00']) 
        if not [x, y] in shapes:
            shapes.append([x, y])

while True:
    if keyboard.is_pressed('x'):
        record = 'check'
    if record == 'check':
        check()
        if(len(shapes) > 0):
            time.sleep(1)
            record = 'click'
    if record == 'click':
        click()
        time.sleep(2)
        record = 'check'