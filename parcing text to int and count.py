#открыть страницу
#спарсить уравнение
#подсчитать
#открыть выпадающий список
#выбрать в списке число полученное в результате уравнения
#отправитб


import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://parsinger.ru/selenium/6/6.html"

try:
    browser = webdriver.Chrome()
    browser.get(link) #Открыть страницу
    primer = eval(browser.find_element(By.CSS_SELECTOR,'#text_box').text) # мы нашли элемент далее с помощью .текст превратили в строку а затем с помощью ЭВАЛ
    select = Select(browser.find_element(By.CSS_SELECTOR,'#selectId'))   #превратили строку в численное уровенение
    select.select_by_visible_text(str(primer)) #в выпавшем окне выбираем наш вариант
    browser.find_element(By.CSS_SELECTOR, '#sendbutton').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

print(primer)
print(type(primer))
#print(result)
#print(type(result))