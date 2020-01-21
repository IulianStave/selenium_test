from selenium.webdriver.common.by import By
from selenium import webdriver
from src.base_element import BaseElement
from src.base_page import BasePage

URL_AC = 'https://atmosphere.copernicus.eu/'
SEARCH_CSS_SELECTOR = 'search-toggle.search-label'
# Test setup

SEARCH_ATTR = 'for'
SEARCH_FOR = 'search-toggle'
browser = webdriver.Chrome()


class CopPage(BasePage):
    default_url = 'https://atmosphere.copernicus.eu/'
    search_label_css_selector = 'search-toggle.search-label'

    @property
    def search_label(self):
        return super().button(
            by=By.CLASS_NAME,
            value='search-toggle.search-label')


