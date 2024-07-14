'''
Открыть страницу
Нажать на кнопку на экране
Принять confirm на всплывшем окне
На новой странице решить капчу для роботов, чтобы получить число с ответом и ввести его в поле

'''

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link) #Открыть страницу
    browser.find_element(By.CSS_SELECTOR,'body > form > div > div > button').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR,'#input_value').text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR,'#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR,'body > form > div > div > button').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()