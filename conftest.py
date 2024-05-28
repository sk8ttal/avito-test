import pytest

from web_driver.driver import WebDriver 

@pytest.fixture(scope="class", autouse=True)
def driver():
    yield WebDriver.get_driver()
    WebDriver.quit_driver()
