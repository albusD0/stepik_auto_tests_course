from .pages.product_page import ProductPage

def test_add_to_cart(browser, language):
    link = f"https://selenium1py.pythonanywhere.com/{language}/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_add_to_cart()