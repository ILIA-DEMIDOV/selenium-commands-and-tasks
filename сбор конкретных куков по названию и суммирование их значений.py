# Открыть страницу
'''
задача собрать все куки , из них есть те что называются secret cookies и у них етсь значения value
собрать все значения value от всех secret cookies
'''
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = 'https://parsinger.ru/methods/3/index.html'  # указали ссылку страницы
sum = 0                #сделали счетчик
try:
    browser = webdriver.Chrome()
    browser.get(link)  # Открыть страницу
    time.sleep(2)

    cookies = browser.get_cookies()         #собрали все куки
    for cookie in cookies:
        # Проверяем, начинается ли имя cookie с "secret_cookie"
        if cookie['name'].startswith('secret_cookie_'):
            #если да тогда берем значения из секретного кука
            value = int(cookie['value'])
            sum += value             #и прибавляем его к сумме

    # Выводим полученную сумму
    print("Сумма числовых значений всех четных secret_cookie_: ", sum)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

