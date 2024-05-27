from pages.base_page import BasePage

class TestFullInvalidData:
     
    def test_main(self):     
        BasePage()\
            .open_eco_inpact_page()\
            .take_screenshot_of_kilograms()
            
