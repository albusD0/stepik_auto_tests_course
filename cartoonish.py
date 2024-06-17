from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://vk.com/app51797807"

try:
    browser = webdriver.Chrome()
    browser.get("https://vk.com/login")
    input_login = browser.find_element(By.CLASS_NAME, "VkIdForm__input")
    input_login.send_keys("alvrath")
    button_submit_login = browser.find_element(By.CLASS_NAME, "FlatButton.FlatButton--primary.FlatButton--size-l.FlatButton--wide.VkIdForm__button.VkIdForm__signInButton")
    button_submit_login.click()
    input_password = browser.find_element(By.CLASS_NAME, 'vkc__TextField__input')
    input_password.send_keys("vkalV2624")    
    button_submit_password = browser.find_element(By.CLASS_NAME, "vkuiButton.vkuiButton--sz-l.vkuiButton--lvl-primary.vkuiButton--clr-accent.vkuiButton--aln-center.vkuiButton--sizeY-regular.vkuiButton--stretched.vkuiTappable.vkuiTappable--sizeX-compact.vkuiTappable--hasHover.vkuiTappable--mouse")
    button_submit_password.click()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
    


