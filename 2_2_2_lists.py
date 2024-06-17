from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    num = int(num1.text) + int(num2.text)
    print(num)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(num))
    submit_button = browser.find_element(By.CSS_SELECTOR, "button")
    submit_button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

#select = Select(browser.find_element(By.TAG_NAME, "select"))
#select.select_by_value("1") # ищем элемент с текстом "Python"