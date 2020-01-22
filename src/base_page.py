from selenium.webdriver.common.by import By

from src.base_element import BaseElement


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go(self):
        self.driver.get(self.url)

    def button(self, locator):
        # locator = (By.ID, 'b1')
        return BaseElement(
            driver=self.driver,
            locator=locator
            )
