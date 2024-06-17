import pytest, math, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

#@pytest.fixture(scope="session")
#def test_authorize_stepik(browser, login, password):
@pytest.mark.parametrize('login, password', [("alvrath@gmail.com", "_ggL26-alV24")])
@pytest.mark.parametrize('link', [('https://stepik.org/lesson/236895/step/1'), ("https://stepik.org/lesson/236896/step/1"), ("https://stepik.org/lesson/236897/step/1"), ("https://stepik.org/lesson/236898/step/1"), ("https://stepik.org/lesson/236899/step/1"), ("https://stepik.org/lesson/236903/step/1"), ("https://stepik.org/lesson/236904/step/1"), ("https://stepik.org/lesson/236905/step/1")])
def test_put_a_number_stepik(browser, link, login, password):
    browser.get(link)
    button = browser.find_element(By.ID, "ember459")
    button.click()
    login_btn = browser.find_element(By.ID, "id_login_email")
    login_btn.send_keys(login)
    password_btn = browser.find_element(By.ID, "id_login_password")
    password_btn.send_keys(password)
    in_btn = browser.find_element(By.XPATH, "//button[text()='Войти']")
    in_btn.click()
    text_in = browser.find_element(By.CSS_SELECTOR, "textarea")
    text_in.send_keys(math.log(int(time.time() + 3.8)))

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    submit_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    #time.sleep(5)
    submit_btn.click()
    time.sleep(5)
    message = browser.find_element(By.CLASS_NAME, "attempt-message_correct")
    assert "Correct!" in message.text