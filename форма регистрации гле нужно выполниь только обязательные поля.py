from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
    input1.send_keys("Мистер Алехандро")
    input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
    input2.send_keys("Игоревич")
    input3 = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
    input3.send_keys("successinb@gmail.com")
    input4 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[1]/input')
    input4.send_keys("2137511057")
    input5 = browser.find_element(By.XPATH, '/html/body/div/form/div[2]/div[2]/input')
    input5.send_keys("501 s new hampshire ave 134")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()