from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


TIMEOUT = 10


class BaseElement:
    """Wrapping a Selenium Web Element """
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        # self.driver.find_element(by=self.by, value=self.value)
        try:
            element = WebDriverWait(self.driver, timeout=TIMEOUT).until(
                EC.visibility_of_element_located(locator=self.locator)
                )
            self.web_element = element
        except TimeoutException:
            print(f'Element did not appear on page within {TIMEOUT} seconds')
            element = None
        return element

    def click(self):
        # self.web_element.click()
        try:
            element = WebDriverWait(self.driver, timeout=TIMEOUT).until(
                EC.element_to_be_clickable(locator=self.locator)
                )
            element.click()
        except TimeoutException:
            print(f'Element did not appear on page within {TIMEOUT} seconds')
            element = None
        return element

    @property
    def text(self):
        text = self.web_element.text
        return text
 
    def input_text(self, txt):
        self.web_element.clear()
        self.web_element.send_keys(txt)
        return None


