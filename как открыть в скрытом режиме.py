import time
import math
#224592
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    options_chrome = webdriver.ChromeOptions()
    options_chrome.add_argument('--headless')
    with webdriver.Chrome(options=options_chrome) as browser:
        url = 'https://stepik.org/course/104774')
        browser.get(url)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


