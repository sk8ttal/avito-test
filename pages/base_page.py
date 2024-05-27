from web_driver_items.base_items import WebItem
from pages.inpact_page import InpactPage
from pages.page_default_items import PageDefaultItems
from config.links import Links

class BasePage(PageDefaultItems):
    def open_eco_inpact_page(self) -> InpactPage:
        self.open(Links.ECO_INPACT_URL)
        
        return InpactPage()
    
    