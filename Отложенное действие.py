#Отложенное действие
'''
Открыть страницу
Подождать пока текст не станет 100
нажать на кнопку когда текст ст анет нужным
Пройти капчу для робота и получить число-ответ

'''

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link) #Открыть страницу

    WebDriverWait(browser, "12").until( #здесь мы устанавливаем время ожидания 12 секунд
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "100")) #text to be present in element - it means we are waiting
    # until in element(#price) appears text 100 then will be used next step
    browser.find_element(By.CSS_SELECTOR, '#book').click() # next step that used after element is appeared

    x = browser.find_element(By.CSS_SELECTOR,'#input_value').text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR,'#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR,'#solve').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()