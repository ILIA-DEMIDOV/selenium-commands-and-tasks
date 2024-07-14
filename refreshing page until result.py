'''
Открыть страницу
Обновлять страницу пока не появится число
считать появившееся число

'''

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://parsinger.ru/methods/1/index.html"


try:
    browser = webdriver.Chrome()
    browser.get(link) #Открыть страницу
    elem = browser.find_element(By.CSS_SELECTOR,'#result').text
    while elem == 'refresh page':
        browser.refresh()
        elem1 = browser.find_element(By.CSS_SELECTOR, '#result').text
        if elem1 != 'refresh page':
            break
    print(elem1)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()