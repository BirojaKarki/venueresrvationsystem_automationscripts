from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils.helpers import wait_for_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class AddVenuePage:

    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 15)
        #locators
        self.addvenue_button=(By.XPATH,"//button[normalize-space()='Add Venue']")
        self.venuename_textbox=(By.XPATH,"//input[@placeholder='Enter venue name']")
        self.location_textbox=(By.XPATH,"//input[@placeholder='e.g. Banepa, Kathmandu, etc.']")
        self.images_button=(By.XPATH,"//input[@type='file']")
        self.description_textbox=(By.XPATH,"//textarea[@placeholder='Describe your venue...']")
        self.price_textxbox=(By.XPATH,"//input[@placeholder='Rs']")
        self.capacity_textbox=(By.XPATH,"//input[@placeholder='e.g. 100']")
        self.maplocation=(By.XPATH,"//div[contains(@class,'gm-style')]")
        self.save_venue=(By.XPATH,"//button[normalize-space()='Save Venue']")

    def wait_for_element(self, by, locator):
          return self.wait.until(EC.visibility_of_element_located((by, locator)))

#Actions
    def open_page(self,url):
        self.driver.get(url) 
    def click_addvenue(self):
        self.wait_for_element(*self.addvenue_button).click()
    def enter_venuename(self,venue_name):
        self.wait_for_element(*self.venuename_textbox).send_keys(venue_name)
    def enter_location(self,location):
        self.driver.find_element(*self.location_textbox).send_keys(location)
    def enter_images(self,image_path):
        self.driver.find_element(*self.images_button).send_keys(image_path)
    def enter_description(self,description):
        self.driver.find_element(*self.description_textbox).send_keys(description)
    def enter_price(self,price):
        self.driver.find_element(*self.price_textxbox).send_keys(price)
    def  enter_capacity(self,capacity):
        self.driver.find_element(*self.capacity_textbox).send_keys(capacity)
    
    def map(self, x_offset=None, y_offset=None):
    # Wait for map to be fully visible
        map_element = self.wait_for_element(*self.maplocation)

    # Get map size
        width = map_element.size['width']
        height = map_element.size['height']

    # Set offsets: default to center if None or too big
        if x_offset is None or x_offset > width:
           x_offset = width // 2
        if y_offset is None or y_offset > height:
           y_offset = height // 2
        time.sleep(2)
    # Perform click
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(map_element, x_offset, y_offset).click().perform()
        time.sleep(2)
    def save_button(self):
        self.wait_for_element(*self.save_venue).click()
        WebDriverWait(self.driver, 5).until(lambda d: "owner-dashboard" in d.current_url or True)