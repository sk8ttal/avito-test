from web_driver_items.base_items import WebItem


class InpactPage:
    def __init__(self):
        self.card = lambda bottom_text, description: WebItem(f"//div[text()='{bottom_text}']/ancestor::div[@class='desktop-impact-item-eeQO3']", description)
    
    def take_screenshot_of_kilograms(self):
        self.card("не попало в атмосферу", "Карточка килограммов CO2").screenshot("#1")
        return self
    
    def take_screenshot_of_liters(self):
        self.card("было сохранено", "Карточка литров воды").screenshot("#2")
        return self
    
    def take_screenshot_of_kilowats(self):
        self.card("было сэкономлено", "Карточка кВт*ч энергии").screenshot("#3")
        return self