#Открыть страницу
#Получите значения всех элементов выпадающего списк
#посчитать все числа в выпавшем списке
#ввести ответ
#Нажать кнопку "Submit"

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://parsinger.ru/selenium/6/6.html"

try:
    browser = webdriver.Chrome()
    browser.get(link) #Открыть страницу
    primer = browser.find_element(By.CSS_SELECTOR,'#text_box').text

    def calc(x):
        return str(primer)


    result = browser.find_elements(By.TAG_NAME, 'option') #посчитать все числа в выпавшем списке
    total = 0 #создали переменную суммы
    for s in result: #для каждого числа в списке плюсануть его значение в сумму
        total += int(s.text)

    browser.find_element(By.CSS_SELECTOR,'#input_result').send_keys(total) #найти поле ввода и ввести туда сумму
    browser.find_element(By.CSS_SELECTOR, '#sendbutton').click() #найти кнопку оправить и кликнуть ее
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# не забываем оставить пустую строку в конце файла"

