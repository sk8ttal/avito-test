from pages.page_default_items import PageDefaultItems as PID
from pages.inpact_page.eco_inpact_page import EcoInpactPage


class InpactPage():
    def open_eco_inpact_page(self) -> EcoInpactPage:
        PID.panel_buttons("Экосчётчик", "Экосчётчик").click()
        
        return EcoInpactPage()