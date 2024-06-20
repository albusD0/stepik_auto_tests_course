from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/math.html")
    inp_value = browser.find_element(By.CSS_SELECTOR, "span[id='input_value'")
    x = inp_value.text
    print(x)
    y = calc(x)    
    print(y)
    answer = browser.find_element(By.CSS_SELECTOR, "input[id='answer'")
    answer = answer.send_keys(y)
    
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()
    
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
    
