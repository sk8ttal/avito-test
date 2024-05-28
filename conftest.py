from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.links import Links
import pytest


class WebDriver:
    _driver = None
    _url = Links.BASE_URL

    @classmethod
    def driver(cls):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(cls._url)
        return driver
        

    @classmethod
    def get_instance(cls):
        if cls._driver is None:
            cls._driver = cls.driver()
            window = cls._driver.window_handles[-1]
            cls._driver.switch_to.window(window)
        return cls._driver
