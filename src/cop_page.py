from selenium.webdriver.common.by import By
from selenium import webdriver
from src.base_element import BaseElement
from src.base_page import BasePage

URL_AC = 'https://atmosphere.copernicus.eu/'
SEARCH_CSS_SELECTOR = 'search-toggle.search-label'
# Test setup

SEARCH_ATTR = 'for'
SEARCH_FOR = 'search-toggle'
# browser = webdriver.Chrome()


class CopPage(BasePage):
    default_url = 'https://atmosphere.copernicus.eu/'
    search_label_css_selector = 'search-toggle.search-label'

    @property
    def search_label(self):
        locator = (By.CLASS_NAME, 'search-toggle.search-label')
        return super().button(locator)
    
    @property
    def search_input(self):
        locator = (By.ID, 'edit-search-api-fulltext')
        return super().button(locator)

    def enter_search_text(self, stxt):
        self.search_input.input_text(stxt)
    
    @property
    def search_submit(self):
        locator = (By.CLASS_NAME, 'button.js-form-submit.form-submit')
        return super().button(locator)

    @property
    def click_on_search(self):
        self.search_input.web_element.submit()
