import pyautogui
import cv2 
import numpy as np 
import keyboard
import matplotlib.pyplot as plt
import win32gui
import win32ui
import win32con




w = 1920
h = 1080  
bmpfilenamename = "out.bmp"


  ## maybe faster screenshot
# while True:
#     if keyboard.is_pressed('q'):
#         windows = pyautogui.getAllWindows()
#         aim_trainer_windows = [window for window in windows if "Google Chrome" in window.title]
#         print(aim_trainer_windows[0].title)
#         hwnd = win32gui.FindWindow(None, aim_trainer_windows[0].title)
#         wDC = win32gui.GetWindowDC(hwnd)
#         dcObj=win32ui.CreateDCFromHandle(wDC)
#         cDC=dcObj.CreateCompatibleDC()
#         dataBitMap = win32ui.CreateBitmap()
#         dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
#         cDC.SelectObject(dataBitMap)
#         cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
#         dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

#         dcObj.DeleteDC()
#         cDC.DeleteDC()
#         win32gui.ReleaseDC(hwnd, wDC)
#         win32gui.DeleteObject(dataBitMap.GetHandle())
                
target = cv2.imread('target.png', cv2.IMREAD_COLOR)
wi, hi = target.shape[:-1]
while True:
    
        image = pyautogui.screenshot(region=(500,170, 1400 - 500,700 -170))
        image = np.array(image)
        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        res = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
        threshold = 0.5
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            pyautogui.click(pt[0]+ wi/2 + 500, pt[1] + hi/2 + 170)
            break
    
        
