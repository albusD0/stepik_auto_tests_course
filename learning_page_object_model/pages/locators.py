from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
 
class ProductPageLocators():
    CART_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.XPATH, "//article/div[1]/div[2]/p[1]")
    CART_SUM = (By.XPATH, "//div[2]/div/div[1]/div[3]/div/p[1]/strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_IN_CART_TITLE = (By.CSS_SELECTOR, "#messages .alertinner strong")