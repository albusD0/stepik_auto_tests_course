from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    image_v = browser.find_element(By.TAG_NAME, "img")
    image_valuex = image_v.get_attribute("valuex")
    print(image_valuex)
    x = image_valuex
    y = calc(x)
    print(y)
    inp_y = browser.find_element(By.ID, "answer")
    inp_y = inp_y.send_keys(y)
    check_rob = browser.find_element(By.ID, "robotCheckbox")
    check_rob.click()
    radiob_check = browser.find_element(By.ID, "robotsRule")
    radiob_check.click()
    subm_b = browser.find_element(By.CSS_SELECTOR, "button")
    subm_b.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    # не забываем оставить пустую строку в конце файла
    
