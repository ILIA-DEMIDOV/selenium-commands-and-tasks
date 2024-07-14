#Открыть страницу
#Считать значение для переменной x.
#Посчитать математическую функцию от x.
#Проскроллить страницу вниз.
#Ввести ответ в текстовое поле.
#Выбрать checkbox "I'm the robot".
#Переключить radiobutton "Robots rule!".
#Нажать на кнопку "Submit".


import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://SunInJuly.github.io/execute_script.html"  # указали ссылку страницы
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))  #указали функцию по которой будем считать

try:
    browser = webdriver.Chrome()
    browser.get(link)   #Открыть страницу
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text #Считать значение для переменной x
    y = calc(x) #Посчитать математическую функцию от x

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y) #Ввести ответ в текстовое поле.

    button = browser.find_element(By.CSS_SELECTOR, "#peopleRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) #Проскроллить страницу вниз в область кнопки People rule

    checkbox = browser.find_element(By.CSS_SELECTOR,'#robotCheckbox').click() #кликаем нужный чекбокс
    radiobutton = browser.find_element(By.CSS_SELECTOR,'#robotsRule').click() #кликаем нужную радиокнопку

    submit = browser.find_element(By.CSS_SELECTOR,'body > div > form > button').click() #отправляем субмит

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

#Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
#Делается это с помощью следующего скрипта:

#return arguments[0].scrollIntoView(true);

