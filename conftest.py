from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.links import Links
import pytest


class WebDriver:
    _driver = None
    _url = Links.BASE_URL

    @pytest.fixture
    def driver(cls):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(cls._url)
        cls._driver = driver
        yield driver
        driver.quit()
