from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
import pytest, time

class TestUserAddToCartFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/accounts/login/"
        email = str(time.time()) + "@fake.com"
        password = str(time.time()) + "abC#"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser, language):
        link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        should_be_product_title = page.should_be_product_title()
        what_price_is = page.what_price_is()
        page.should_be_authorized_user()
        page.should_add_to_cart()
        page.solve_quiz_and_get_code()
        should_be_product_title_in_cart = page.should_be_product_title_in_cart()
        is_cart_equal_to_price = page.is_cart_equal_to_price()
        page.check_product_names(should_be_product_title, should_be_product_title_in_cart)
        page.check_prices(what_price_is, is_cart_equal_to_price)

    def test_user_cant_see_success_message_after_adding_product_to_cart(self, browser, language):
        link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_add_to_cart()
        page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


@pytest.mark.need_review

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
def test_user_can_add_to_cart(browser, language, link):
    page = ProductPage(browser, link)
    page.open()
    should_be_product_title = page.should_be_product_title()
    what_price_is = page.what_price_is()
    page.should_add_to_cart()
    page.solve_quiz_and_get_code()
    should_be_product_title_in_cart = page.should_be_product_title_in_cart()
    is_cart_equal_to_price = page.is_cart_equal_to_price()
    page.check_product_names(should_be_product_title, should_be_product_title_in_cart)
    page.check_prices(what_price_is, is_cart_equal_to_price)

@pytest.mark.need_review

def test_guest_cant_see_product_in_cart_opened_from_product_page(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart()

@pytest.mark.need_review

def test_guest_can_go_to_login_page_from_product_page(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link_on_product_page(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# Нижеуказанные тесты созданы на предыдущих этапах, их можно закомментить
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser, language): 
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 

def test_user_cant_see_success_message(browser, language): 
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
 
@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_cart(browser, language): 
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()
    page.should_disappear_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_disappeared