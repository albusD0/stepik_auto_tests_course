from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
 
class ProductPageLocators():
    CART_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_SUM = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_IN_CART_TITLE = (By.CSS_SELECTOR, "#messages .alertinner strong")