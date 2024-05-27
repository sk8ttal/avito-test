from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from web_driver.driver import WebDriver
import time


class Waiter:
    def __init__(self, max_wait_s: int = 10, poll_frequency: int = 1):
        self.driver = WebDriver.get_instance()
        self.wait = WebDriverWait(self.driver, max_wait_s, poll_frequency)

    def static_wait_s(self, duration: int):
        '''
        <summary> Статическая задержа </summary>
        
        Используется для временной приостановки работы скрипта (по необходимости).
        
        Args:
        time: время ожидания в секундах
        '''
        time.sleep(duration)

    def wait_element(self, locator: str):
        '''
        <summary> Ожидает появление элемента страницы </summary>
        
        Args:
        locator: Xpath локатор элемента 
        '''
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
