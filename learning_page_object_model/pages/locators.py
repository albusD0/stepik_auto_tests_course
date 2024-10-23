from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "span a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    USER_REG_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    USER_REG_PASS_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    USER_REG_PASS_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTT = (By.CSS_SELECTOR, '#register_form > button')
 
class ProductPageLocators():
    CART_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_SUM = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_IN_CART_TITLE = (By.CSS_SELECTOR, "#messages .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alertinner")
    
class CartPageLocators():
    CART_EMPTY = (By.CSS_SELECTOR, "#content_inner")
    MSG_CART_EMPTY = (By.XPATH, "//*[@id='messages']/div[2]/div/p[1]")            
