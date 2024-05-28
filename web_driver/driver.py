from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.links import Links
import pytest


class WebDriver:
    _driver = None
    _url = Links.BASE_URL

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            cls._driver = webdriver.Chrome(options=options)
            cls._driver.maximize_window()
            cls._driver.get(cls._url)
        window = cls._driver.window_handles[-1]
        cls._driver.switch_to.window(window)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.close()
            cls._driver.quit()
            cls._driver = None