from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 15 секунд, пока цена снизится до 100$
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), '100')
        )
    print(price)
    button = browser.find_element(By.ID, 'book')
    button.click()

    x = browser.find_element(By.ID, 'input_value').text
    answer_value = calc(x)
    print(x)
    print(answer_value)
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(answer_value)
    button_2 = browser.find_element(By.ID, 'solve')
    button_2.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла