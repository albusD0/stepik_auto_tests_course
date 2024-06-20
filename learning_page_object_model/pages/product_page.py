from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_BTN)
        cart_link.click()