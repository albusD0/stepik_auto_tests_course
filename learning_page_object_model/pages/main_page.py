from .base_page import BasePage
from .locators import MainPageLocators
#from .login_page import LoginPage - можно раскавычить, если пользоваться первым способом

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
#       return LoginPage(browser=self.browser, url=self.browser.current_url) - можно раскавычить, если пользоваться первым способом

        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Отсутствует ссылка на страницу ввода логина и пароля"