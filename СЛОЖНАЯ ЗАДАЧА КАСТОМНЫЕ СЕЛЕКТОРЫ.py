# Открыть страницу
'''собрать все контейнеры в лист - для этого мы использовали кастомный селектор уточнив конкретику
роботаем по каждому контейнеру'''
#кликаем на все квадратики
#в выпадающем окне выбираем тот же код
#выбираем и кликаем чекбокс и вставляем данные
#нажимаем проверить
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://parsinger.ru/selenium/5.5/5/1.html"  # указали ссылку страницы
try:
    browser = webdriver.Chrome()
    browser.get(link)  # Открыть страницу
    time.sleep(2)
    containers = browser.find_elements(By.CSS_SELECTOR, 'div[style*="background-color"]') #собрали все контейнеры ,
    # проблема была  в том что тэг DIV использовался еще в других элементах так что пришлось делать кастомный селектор
    # элементы выглядили так: <div style="background-color: rgb(176, 196, 222); width: 100%;">
    #                         <div style="background-color: rgb(211, 211, 211); width: 100%;">
    #так что мы взяли общую часть "(style=background-color)" и сделали CSS_SELECTOR, 'div[style*="background-color"]'
    for container in containers:
        num_of_color = container.find_element(By.TAG_NAME, 'span').text #получили код цвета элемента
        our_button = container.find_element(By.CSS_SELECTOR, f'button[data-hex="{num_of_color}"]') #выбрали кнопку используя селектор с f строкой
        our_button.click() #кликнули выбраную кнопку
        dropdown = container.find_element(By.TAG_NAME, 'select') #выбрали на странице выпадающий список
        select = Select(dropdown) #выбрали на странице выпадающий список - 2
        select.select_by_value(num_of_color) #выбрали в списке нужное нам значение относительно нашей переменной
        checkbox = container.find_element(By.CSS_SELECTOR, 'input[type*= "checkbox"]').click()
        # определили чекбокс и кликнули его
        pole = container.find_element(By.CSS_SELECTOR, 'input[type*= "text"]').send_keys(num_of_color)
        # определили поле ввода и ввели туда данные нашего цвета
    '''теперь нам нужно прожать конкретную группу кнопок ,для этого соберем все кнопки в кучу и выберем те где надпись Проверить'''
    buttons = browser.find_elements(By.TAG_NAME,"button") #собрали все кнопки со страницы
    check_buttons = [button for button in buttons if button.text == "Проверить"]
    # Фильтруем кнопки, оставляя только те, у которых текст равен "Проверить" создав новый список
    # Проходим по каждой кнопке в списке и кликаем на нее:
    for button in check_buttons:
        button.click()
    last_button = browser.find_element(By.XPATH,'/html/body/button').click()
    #финальная кнопка

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

