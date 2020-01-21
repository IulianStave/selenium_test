from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


TIMEOUT = 10


class BaseElement:
    """Wrapping a Selenium Web Element """
    def __init__(self, driver, by, value):
        self.driver = driver
        self.by = by
        self.value = value
        self.locator = (self.by, self.value)
        self.web_element = None
        self.find()

    def find(self):
        # self.driver.find_element(by=self.by, value=self.value)
        element = WebDriverWait(self.driver, timeout=TIMEOUT).until(
            EC.visibility_of_element_located(locator=self.locator)
            )
        self.web_element = element
        return None

    def click(self):
        # self.web_element.click()
        element = WebDriverWait(self.driver, timeout=TIMEOUT).until(
            EC.element_to_be_clickable(locator=self.locator)
            )
        element.click()
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text
    


