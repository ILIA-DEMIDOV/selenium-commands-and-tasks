# заполняем все формы
# берем все элементы и заполняем каждый

#заполнение формы на сайте
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://parsinger.ru/selenium/1/1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CLASS_NAME, 'form')

    for element in elements:
        element.send_keys("aaa")
    button = browser.find_element(By.XPATH, "//*[@id='btn']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# не забываем оставить пустую строку в конце файла"

