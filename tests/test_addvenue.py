from pages.addvenue_page import AddVenuePage
import csv
import pytest
from utils.helpers import wait_for_url,wait_for_element
from selenium.webdriver.common.by import By
import time
def get_addvenue_data():
    data=[]
    with open ("data/test_data_addvenue.csv",newline="") as file:
        reader=csv.DictReader(file)
        for row in reader:
            data.append(row)

        return data
    
@pytest.mark.parametrize("test_data",get_addvenue_data())
def test_addvenue(driver,test_data,logged_in_driver):
    addvenue=AddVenuePage(logged_in_driver)
    addvenue.click_addvenue()
    addvenue.enter_venuename(test_data["venue_name"])
    addvenue.enter_location(test_data["location"])
    addvenue.enter_images(test_data["image_path"])
    addvenue.enter_description(test_data["description"])
    addvenue.enter_price(test_data["price"])
    addvenue.enter_capacity(test_data["capacity"])
    addvenue.map()  # ✅ correct
    addvenue.save_button()
    time.sleep(6)
    assert verify_venue_add(logged_in_driver,test_data["venue_name"])

def verify_venue_add(driver,venue_name):
    try:
        driver.get("http://localhost:5173/owner-dashboard")
        venue_element= wait_for_element(By.XPATH, f"//h3[normalize-space()='{venue_name}']")
        assert venue_element.is_displayed()
        print(f"✅ Venue '{venue_name}' added successfully")
        return True
    except:
        print(f"❌ Venue '{venue_name}' NOT found")
        return False
    
    