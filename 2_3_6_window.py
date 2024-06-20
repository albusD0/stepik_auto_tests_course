from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
        
    x = browser.find_element(By.ID, "input_value").text
    print(x)
    calc = calc(x)
    print(calc)

   
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc)

    button_2 = browser.find_element(By.TAG_NAME, "button")
    button_2.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()
