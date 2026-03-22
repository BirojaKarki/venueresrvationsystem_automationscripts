from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self,driver):
        self.driver=driver 
        #locators
        self.username_textbox=(By.XPATH,"//input[@placeholder='Enter your email']")
        self.password_textbox=(By.XPATH,"//input[@placeholder='Enter your password']")
        self.login_button=(By.XPATH,"//button[@type='submit']")
        self.error_message=((By.XPATH,"//*[contains(text(),'Invalid')]"))
        #Actions
    def open_page(self,url):
        self.driver.get(url)
    
    def enter_username(self,username):
        self.driver.find_element(*self.username_textbox).clear()
        self.driver.find_element(*self.username_textbox).send_keys(username)
    
    def enter_password(self,password):
        self.driver.find_element(*self.password_textbox).clear()
        self.driver.find_element(*self.password_textbox).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

   
