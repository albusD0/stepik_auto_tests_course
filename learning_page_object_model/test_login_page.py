from .pages.login_page import LoginPage

def test_is_login_url_right(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    page = LoginPage(browser, link)   
    page.open()                      
    page.should_be_login_url(link)      
    
def test_login_form_present(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    page = LoginPage(browser, link)   
    page.open()                      
    page.should_be_login_form()      
    
def test_register_form_present(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/accounts/login/"
    page = LoginPage(browser, link)   
    page.open()                      
    page.should_be_register_form()
    