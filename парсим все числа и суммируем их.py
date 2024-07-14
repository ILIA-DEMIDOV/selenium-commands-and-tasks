# парсим все числа по тегу p и суммируем их

from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/3/3.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    result = browser.find_elements(By.TAG_NAME, 'p')
    total = 0
    for s in result:
        total += int(s.text)
print(total)