from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
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