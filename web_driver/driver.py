from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from config.links import Links
import pytest
# from driver_actions import Actions


class WebDriver():
    _driver = None
    _url = Links.BASE_URL

    @classmethod
    def get_new_driver(cls):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(cls._url)
        return driver

    # @pytest.fixture(scope="function")
    @classmethod
    def get_instance(cls):
        if cls._driver is None:
            cls._driver = WebDriver.get_new_driver()
        try:
            WebDriverWait(cls._driver, timeout=10).until(
                lambda d: d.execute_script(
                    'return document.readyState') == 'complete'
            )
        finally:
            return cls._driver
