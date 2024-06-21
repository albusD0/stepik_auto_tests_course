from .pages.product_page import ProductPage
import pytest, time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]) 
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
