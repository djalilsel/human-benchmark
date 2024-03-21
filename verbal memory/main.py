from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://humanbenchmark.com/tests/verbal-memory')

words = []

while True:
    try:
        word = driver.find_element(By.CSS_SELECTOR, 'div.word')
        buttons = driver.find_elements(By.CSS_SELECTOR, 'button.css-de05nr')
        for button in buttons:
            if button.text == 'SEEN':
                seen = button
            elif button.text == 'NEW':
                new = button
        if word.text in words:
            seen.click()
        else:
            words.append(word.text)
            new.click()
    except:
        pass
