from web_driver_items.base_items import WebItem
from pages.inpact_page.inpact_page import InpactPage
from pages.page_default_items import PageDefaultItems as PDI

class BasePage:
    def open_inpact_page(self) -> InpactPage:
        PDI.panel_buttons("Польза", "Польза").click()
        
        return InpactPage()
    
    