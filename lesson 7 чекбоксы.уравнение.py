#поиск числа
#математическое уравнение
#чекбоксы

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/get_attribute.html"
y = 0
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x_value = x_element.get_attribute("valuex")
    y = calc(x_value)

    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)

    option1 = browser.find_element(By.XPATH, "//*[@id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.XPATH, "//*[@id='robotsRule']")
    option2.click()

    submit = browser.find_element(By.XPATH, "/html/body/div/form/div/div/button")
    submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# не забываем оставить пустую строку в конце файла"

