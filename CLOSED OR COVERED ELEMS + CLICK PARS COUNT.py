#Открыть страницу
#на сайте мы видим закрытые элементы кнопки - нужно спарсить список всех кнопок - нажать их и с каждой нажатой кнопки забрать число
#проблема в том что если элемент перекрыт нам нужно сделать его видимым для этого используем метод "Скролл до видимости"
#все полученые числа просуммировать в счетчик




import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://parsinger.ru/scroll/4/index.html"  # указали ссылку страницы
sum = 0 #создали счетчик суммы
try:
    browser = webdriver.Chrome()
    browser.get(link)   #Открыть страницу
    buttons = browser.find_elements(By.CLASS_NAME, 'btn') #собрали все элементы "Кнопки" в список по классу btn
    for button in buttons: #циклом для каждой кнопки из списка "Кнопки"
        browser.execute_script("arguments[0].scrollIntoView(true);", button) #делаем ее видимой для селениума
        button.click() #нажимаем на кнопку и получаем сверху число
        num = browser.find_element(By.CSS_SELECTOR, "#result") #парсим это число
        sum += int(num.text) #присоединяем число к счетчику суммы

        '''for cookie in cookies:
            if 'expiry' in cookie:
                expiry_value = cookie['expiry']
                if expiry_value > max_expiry_value:
                    max_expiry_value = expiry_value
                    max_expiry_link = link
    browser.back()
    browser.get(max_expiry_link)
    element = browser.find_element(By.ID, 'result' ).text
    print(list)
    print("Ссылка с самым долгим сроком жизни куки:", max_expiry_link)

    list = [item.get_attribute('href') for item in browser.find_elements(By.TAG_NAME, 'a')]
    cookies_array = []


    for link in list:
            # Переход по ссылке
        browser.get(link)

            # Получение всех cookie на странице
        cookies = browser.get_cookies()

            # Добавление куков в список
        cookies_array.extend(cookies)
            for cookie in cookies_array:
                if 'expiry' in cookie:
                    expiry_value = cookie['expiry']
                    if expiry_value > max_expiry_value:
                        max_expiry_value = expiry_value
                        max_expiry_link = link

            print("Ссылка с самым долгим сроком жизни куки:", max_expiry_link)
    #{'domain': 'parsinger.ru', 'expiry': 1747191265, 'httpOnly': False, 'name': 'foo2', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'bar1'}
    browser = webdriver.Chrome()
    browser.get(page_with_longest_expiry)
    result_element = browser.find_element_by_id("result")
    result = int(result_element.text)'''

finally:
    print(sum)
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

#Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
#Делается это с помощью следующего скрипта:

#return arguments[0].scrollIntoView(true);

