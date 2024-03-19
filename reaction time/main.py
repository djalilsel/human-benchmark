import pyautogui
    
while True:
        img = pyautogui.screenshot(region=(0, 200, 10, 10))
        colors = img.getcolors()[0][1]
        if colors == (75, 219, 106):
            pyautogui.click()


