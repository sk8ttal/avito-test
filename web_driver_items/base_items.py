from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC 
from tools.waiter import Waiter
from web_driver.driver import WebDriver

class WebItem:
    def __init__(self, locator, description):
        self.locator = locator
        self.description = description
        self.locator_type = By.XPATH
        
        self.driver = WebDriver.get_driver()
        self.web_driver_wait = lambda timeout: WebDriverWait(self.driver, timeout, poll_frequency=1)
        self.waiter = Waiter()
        
        try: 
            self.element_is_present()
        finally:
            self.element = self.driver.find_element(By.XPATH, self.locator)

    def hover(self):
        try:
            self.element_is_present()
        finally:
            print(f"Наведение на {self.description}")
            ActionChains(self.driver).move_to_element(self.element).perform()
            self.waiter.static_wait_s(1)

    def click(self):
        try:
            self.element_is_present()
        finally:
            print("Нажатие на " + self.description)
            self.element.click()
            self.waiter.static_wait_s(1)

    def double_click(self):
        try:
            self.element_is_present()
        finally:
            print("Двойное нажатие на " + self.description)
            self.element.click()
            self.element.click()
            self.waiter.static_wait_s(1)
 
    def send_keys(self, text):
        try:
            self.element_is_present()
        finally:
            print(f"Ввод текста {text} в {self.description}")
            self.element.send_keys(text)
            self.waiter.static_wait_s(1)
    
    def screenshot(self, name = None):
        if name is None:
            name = self.description
        
        try:
            self.hover()
        finally:
            print(f"Скриншот элемента {self.description}")
            self.element.screenshot(f"output/{name}.png")
            self.waiter.static_wait_s(1)
            
    def assert_text(self, text):
        try:
            self.element_is_present()
        finally:
            print(f"Проверка текста {self.description}")
            assert self.element.text == text, f"Не совпадает текст {self.description}"
            self.waiter.static_wait_s(1)
                
        
    def element_is_visible(self, timeout=5):
        return self.web_driver_wait(timeout).until(EC.visibility_of_element_located((self.locator_type, self.locator)))
    
    def element_is_present(self, timeout=10):
        return self.web_driver_wait(timeout).until(EC.presence_of_element_located((self.locator_type, self.locator)))
    
    def element_is_clickable(self, timeout=5):
        return self.web_driver_wait(timeout).until(EC.element_to_be_clickable((self.locator_type, self.locator)))
    
    def element_is_invisible(self, timeout=5):
        return self.web_driver_wait(timeout).until(EC.invisibility_of_element_located((self.locator_type, self.locator)))
    
