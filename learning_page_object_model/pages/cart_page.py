from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
   def should_be_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.CART_EMPTY), "Корзина не пуста"
