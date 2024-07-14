#открываем страницу на которой кнопка загорожена экраном внизу
#скроллим вниз чтобы увидеть кнопку
# испольщуем для этого метод execute_script c кодом JS внутри


import time
import math
#224592
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

#Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
#Делается это с помощью следующего скрипта:

#return arguments[0].scrollIntoView(true);

