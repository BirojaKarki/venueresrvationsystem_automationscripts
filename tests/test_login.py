from pages.login_page import LoginPage
import csv
import pytest
from utils.helpers import wait_for_url
#Function to read csv
def get_login_data():
    data=[]
    with open("data/test_data_login.csv", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

@pytest.mark.parametrize("test_data",get_login_data())
def test_login(driver,test_data):
    driver.get("http://localhost:5173/login")
    login=LoginPage(driver)
    login.enter_username(test_data["username"])
    login.enter_password(test_data["password"])
    login.click_login()

    
    if test_data["expected_result"]=="passed":
        wait_for_url(driver, "dashboard") 
        assert "owner-dashboard" in driver.current_url or "admin-dashboard" in driver.current_url
        print("Login passed",test_data["username"])
    else:
        assert "login" in  driver.current_url,"failed the login"
        print("login failed")    