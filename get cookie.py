'''
Открыть страницу
выбрать все эелементы
циклом пройти по каждому элементу и очистить поле

'''

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pprint import pprint



link = "https://parsinger.ru/methods/3/index.html"


try:
    with webdriver.Chrome() as browser:
        webdriver.get(link)
        cookies = browser.get_cookies()
    for i in cookies:
        print(i[-1])


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
