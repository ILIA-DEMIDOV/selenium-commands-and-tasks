'''
Открыть страницу
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ

'''

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link) #Открыть страницу
    browser.find_element(By.CSS_SELECTOR,'body > form > div > div > button').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x = browser.find_element(By.CSS_SELECTOR,'#input_value').text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR,'#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR,'body > form > div > div > button').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()