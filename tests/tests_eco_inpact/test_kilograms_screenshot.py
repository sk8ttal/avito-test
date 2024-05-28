from pages.base_page import BasePage

class TestKilogramsScreenshot:
     
    def test(self):     
        BasePage()\
            .open_inpact_page()\
            .open_eco_inpact_page()\
            .take_screenshot_of_kilograms()
            
