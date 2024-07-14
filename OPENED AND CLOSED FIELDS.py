#Открыть страницу
#Какие то поля открыты а какие то закрыты
#для каждого окна если оно открыто -очистим поле
#Нажать на кнопку "Submit".


import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://parsinger.ru/selenium/5.5/2/1.html"  # указали ссылку страницы

try:
    browser = webdriver.Chrome()
    browser.get(link)   #Открыть страницу
    cells = browser.find_elements(By.TAG_NAME, 'input')
    for cell in cells:
        if cell.is_enabled():
            cell.clear()

    browser.find_element(By.CSS_SELECTOR, '#checkButton').click()
    text_from_alert = browser.switch_to.alert.text
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
print(text_from_alert)
#Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
#Делается это с помощью следующего скрипта:

#return arguments[0].scrollIntoView(true);

