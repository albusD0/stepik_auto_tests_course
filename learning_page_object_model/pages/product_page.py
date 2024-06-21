from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math



class ProductPage(BasePage):
    def should_add_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_BTN)
        cart_link.click()
        
    def what_price_is(self):
        what_price = self.browser.find_element(*ProductPageLocators.PRICE)
        return what_price.text
    
    def is_cart_equal_to_price(self):
        cart_sum = self.browser.find_element(*ProductPageLocators.CART_SUM)
        return cart_sum.text
        
    def should_be_product_title(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return product_title.text
    
    def should_be_product_title_in_cart(self):
        product_in_cart_title = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_TITLE)
        return product_in_cart_title.text
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")