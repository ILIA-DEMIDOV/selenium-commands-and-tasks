'''
сбор куки и работа с ними

'''

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pprint import pprint


link = "https://parsinger.ru/methods/3/index.html"


try:
    browser = webdriver.Chrome()
    browser.get(link) #Открыть страницу
    cookies = browser.get_cookies() #получить от страницы кукиес
    #получили все куки и загнали их в список словрей, например такой:
    #{'domain': 'parsinger.ru', 'httpOnly': False, 'name': 'secret_cookie_14', 'path': '/methods/3', 'sameSite': 'Lax', 'secure': False, 'value': '5700'}
    # теперь надо у от каждого словаря : если name кончается на четное число, тогда взять занчение value и сохранить себе - и затем их подсчитать
    selected_values =       [int(x['value'])             for x in cookies          if int(x['name']         .rsplit("_")         [-1]) % 2 == 0]
    #собрать список всех значений value            в каждом элементе куки   #если в названии элемента после симвлоа черты у последнего элемента число четное
    sum  = 0
    for i in selected_values:
        sum += i
    print(sum)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
