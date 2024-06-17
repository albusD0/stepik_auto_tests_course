from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys("Boris")
    first_name = browser.find_element(By.NAME, 'lastname')
    first_name.send_keys("Nadezhdin")
    first_name = browser.find_element(By.NAME, 'email')
    first_name.send_keys("boris@ya.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))	# получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')	# добавляем к этому пути имя файла
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(12)
    # закрываем браузер после всех манипуляций
    browser.quit()
