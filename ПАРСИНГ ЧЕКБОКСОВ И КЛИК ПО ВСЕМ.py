#ПАРСИНГ ВСЕХ ЧЕКБОКСОВ -> КЛИК НА ВСЕ ЧЕКБОКСЫ -> НАЖАТИЕ КОПКИ В КОНЦЕ
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://parsinger.ru/selenium/4/4.html"
sum_numbers = 0
try:
    browser = webdriver.Chrome()
    browser.get(link)
    checkboxes = browser.find_elements(By.CSS_SELECTOR, 'input[type="checkbox"]')
    for checkbox in checkboxes:
        checkbox.click()

    # Находим и нажимаем на кнопку
    button = browser.find_element(By.XPATH,'/html/body/div/div[2]/input')
    button.click()
finally:
    # Закрываем браузер
    time.sleep(10)

# не забываем оставить пустую строку в конце файла"

