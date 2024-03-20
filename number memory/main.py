from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/number-memory')
while True:
    try:
        elem = driver.find_element(By.CLASS_NAME, 'big-number')
        number = elem.text
        time.sleep(2)
        done = False
        while not done:
            try:
                input = driver.find_element(By.TAG_NAME, 'input')
                input.send_keys(number)
                i = 1
                while (not done) or (i != 3):
                    try:
                        confirm = driver.find_element(By.CSS_SELECTOR, 'button.css-de05nr')
                        confirm.click()
                        done = True
                        i+=1
                    except:
                        pass
            except:
                pass
    except:
        pass
        