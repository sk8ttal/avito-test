from web_driver.driver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

class PageDefaultItems:
    def __init__(self):
        self.driver = WebDriver.get_instance()     
        
    def open(self, PAGE_URL):
        self.driver.get(PAGE_URL)
        return self