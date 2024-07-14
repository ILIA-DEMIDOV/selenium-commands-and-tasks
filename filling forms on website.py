
#заполнение формы на сайте
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://parsinger.ru/selenium/1/1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "input")


    input1 = browser.find_element(By.CSS_SELECTOR,'input[name="first_name"].form-control')
    input1.send_keys("Мистер Алехандро")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='last_name'].form-control")
    input2.send_keys("Игоревич")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"].form-control.city')
    input3.send_keys("лосанжелес")
    #time.sleep(2)
    input4 = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"].form-control#country')
    input4.send_keys("США")
    #time.sleep(2)
    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла