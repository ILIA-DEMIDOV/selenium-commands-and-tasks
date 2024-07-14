#Открыть страницу
#на сайте мы видим серые поля с значениями -нужно значения перенести в синие поля а в серых удалить
#далее на каждой строке нажать кнопку проверить
#лучше всего спарсить все группы элементов в несколько списков и затем сгрупировтаь списки функцией zip()
#далее мы работаем по каждой группе




import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://parsinger.ru/selenium/5.5/4/1.html"  # указали ссылку страницы
try:
    browser = webdriver.Chrome()
    browser.get(link)   #Открыть страницу
    grays = browser.find_elements(By.CSS_SELECTOR, "[color=\"gray\"]") #парсим все серые окна и значения в них в список
    blues = browser.find_elements(By.CSS_SELECTOR, "[color=\"blue\"]") #парсим все синие окна в список
    buttons = browser.find_elements(By.CSS_SELECTOR, ".parent button") #парсим все кнопки
    for gray, blue, button in zip(grays, blues, buttons): #функцией ZIP создаем новый спсиок где все по группам (серое окно, синее , кнопка)
        blue.send_keys(gray.text) #в синее шлем значение серого
        gray.clear() #чистим серое
        button.click() #кнопку нажимаем
    browser.find_element(By.CSS_SELECTOR, "#checkAll").click() #далее нажимаем финальную кнопку
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


