from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла



class ProductPage(BasePage):
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


    def should_add_to_cart(self):
        cart_link = self.browser.find_element(*ProductPageLocators.CART_BTN)
        cart_link.click()
        prompt = browser.switch_to.alert
        prompt.send_keys("My answer")
        prompt.accept()