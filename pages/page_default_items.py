from conftest import WebDriver
from web_driver_items.base_items import WebItem

class PageDefaultItems:  
    driver = WebDriver.get_driver()  
    inputs = lambda name, description: WebItem(f"//input[@name='{name}']", f"Инпут для ввода {description}")   
    panel_buttons = lambda name, description: WebItem(f"//a[text()='{name}']", f"Кнопка  {description}")
