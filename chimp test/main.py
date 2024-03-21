import pyautogui
import cv2
import numpy as np
import pytesseract
import keyboard

record = False
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/djali/OneDrive/Desktop/DELETE/tesseract.exe"

while True:
    if keyboard.is_pressed('x'):
        record = not record
    screen = pyautogui.screenshot(region=(500, 170, 1400 - 500, 700 - 170))
    if not record:
        try:
            pos = cv2.matchTemplate(cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR), cv2.imread('continue.png'), cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(pos)
            if max_val > 0.8:
                pyautogui.click(max_loc[0] + 530, max_loc[1] + 200)
                record = True
        except:
            pass
    if record:
        img = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(img_grey, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        filtered_contours = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            is_inside = False
            for other_contour in contours:
                if contour is not other_contour:
                    other_x, other_y, other_w, other_h = cv2.boundingRect(other_contour)
                    if x > other_x and y > other_y and x + w < other_x + other_w and y + h < other_y + other_h:
                        is_inside = True
                        break
            if not is_inside:
                filtered_contours.append(contour)
        contours = filtered_contours

        positions = []
        text = []
        i = 0
        space = 5
        for counter in contours:
            x, y, w, h = cv2.boundingRect(counter)
            positions.append([x + w/2, y + h/2])
            degit = thresh[(y - space):(y+h + space), (x - space):(x+w  + space)]
            text.append(pytesseract.image_to_boxes(degit, lang='eng', config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789'))
            i+=1
        j = 0
        try:
            for b in text:
                b = b.split(' ')
                positions[j].append(int(b[0]))
                j+=1
            
            merged_positions = []
            i = 0
            while i < len(positions):
                merged_position = [positions[i][0], positions[i][1], str(positions[i][2])]
                j = i + 1
                while j < len(positions):
                    if (abs(positions[i][0] - positions[j][0]) < 35) & (abs(positions[i][1] - positions[j][1]) < 35):
                        merged_position[2] = str(positions[j][2]) + merged_position[2]
                        j += 1
                    else:
                        break
                merged_positions.append(merged_position)
                i = j
            positions = merged_positions

            positions.sort(key=lambda x: int(x[2]))
            while len(positions) > 0:
                pyautogui.click(int(positions[0][0]) + 500, int(positions[0][1]) + 170)
                positions.remove(positions[0])
            record = False
        except:
            pass    



        
 





