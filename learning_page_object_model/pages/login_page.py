from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.USER_REG_EMAIL)
        password_1_field = self.browser.find_element(*LoginPageLocators.USER_REG_PASS_1)
        password_2_field = self.browser.find_element(*LoginPageLocators.USER_REG_PASS_2)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTT)
        email_field.send_keys(email)
        password_1_field.send_keys(password)
        password_2_field.send_keys(password)
        button.click()


    def should_be_login_page(self, link):
        self.should_be_login_url(link)
        self.should_be_login_form()
        self.should_be_register_form()
        
    def should_be_login_url(self, link):
        assert self.browser.current_url == link, 'Неверная страница'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Отсутствует форма ввода логина / пароля"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Отсутствует форма регистрации"