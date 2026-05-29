import pytest
from utils.browser_setup import get_driver
from pages.login_page import LoginPage
from utils.helpers import wait_for_url

@pytest.fixture
def driver():
    driver = get_driver()
    
    yield driver
    driver.quit()
@pytest.fixture
def logged_in_driver(driver):
    driver.get("http://localhost:5173/login")
    login = LoginPage(driver)
    login.enter_username("hmgsamir8@gmail.com")  # can also use test data
    login.enter_password("123qweasdzxc")
    login.click_login()
    wait_for_url(driver, "dashboard")  # wait until dashboard is loaded
    return driver

