import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


# @pytest.fixture()
# def driver_setup():
#     options = Options()
#     # options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(options=options)
#     driver.maximize_window()
#     try:
#         WebDriverWait(driver, timeout=10).until(
#             lambda d: d.execute_script(
#                 'return document.readyState') == 'complete'
#         )
#     finally:
#         yield driver

#     driver.quit()
