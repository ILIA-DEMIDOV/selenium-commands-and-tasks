#Открыть страницу
#Посчитать сумму заданных чисел
#Выбрать в выпадающем списке значение равное расчитанной сумме
#Нажать кнопку "Submit"

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"
total = 0
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, '#num1').text
    num2 = browser.find_element(By.CSS_SELECTOR, '#num2').text
    total = int(num1) + int(num2)

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(total))
    #browser.find_element(By.CSS_SELECTOR, '#dropdown').click()
    #browser.find_element(By.CSS_SELECTOR, "[value=total]").click()

    submit = browser.find_element(By.XPATH, "/html/body/div/form/button")
    submit.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

# не забываем оставить пустую строку в конце файла"

