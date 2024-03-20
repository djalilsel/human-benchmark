from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import keyboard


driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/typing')

driver.implicitly_wait(5)
def type_text():
        elem = driver.find_element(By.CLASS_NAME, 'letters')
        print(elem.text)
        keyboard.write(elem.text)

while True:
    if keyboard.is_pressed('enter'):
        try:
            type_text()
        except:
            print("done!")