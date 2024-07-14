
#заполнение формы на сайте
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys('Alexander')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(4)').send_keys('Semenov')
    browser.find_element(By.CSS_SELECTOR, 'body > div > form > div > input:nth-child(6)').send_keys('sema@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "text" #название файла без расширения
    file_path = os.path.join(current_dir, 'text') #снова без расширения

    file_input = browser.find_element(By.CSS_SELECTOR, '#file')
    file_input.send_keys(file_path)

    button = browser.find_element(By.XPATH, "/html/body/div/form/button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла