from .pages.product_page import ProductPage
import pytest, time


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, language): 
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_guest_cant_see_success_message(browser, language): 
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_message_disappeared_after_adding_product_to_basket(browser, language): 
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.should_disappear_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_disappeared

'''
@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]) 
def test_add_to_cart(browser, language, link):
    #link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    should_be_product_title = page.should_be_product_title()
    what_price_is = page.what_price_is()
    page.should_add_to_cart()
    page.solve_quiz_and_get_code()
    should_be_product_title_in_cart = page.should_be_product_title_in_cart()
    is_cart_equal_to_price = page.is_cart_equal_to_price()
    assert should_be_product_title == should_be_product_title_in_cart, "Название товара не совпадает"
    assert is_cart_equal_to_price == what_price_is, "Неверная цена товара"
    
'''