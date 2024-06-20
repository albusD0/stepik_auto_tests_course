from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest, time

def test_add_to_cart_button_is_present(browser, language):
    browser.implicitly_wait(5)
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed(), "Кнопки добавления в корзину нет"
