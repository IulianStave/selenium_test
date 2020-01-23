from selenium import webdriver

from selenium.webdriver.common.by import By
from src.base_page import BasePage
from src.cop_page import CopPage
from src.base_element import BaseElement
import time

URL_AC = 'https://atmosphere.copernicus.eu/'
SEARCH_CSS_SELECTOR = 'search-toggle.search-label'
# Test setup

SEARCH_ATTR = 'for'
SEARCH_FOR = 'search-tggle'
browser = webdriver.Firefox()


# Perform the actaul test

myPage = CopPage(browser, URL_AC)
myPage.go()
search_label = myPage.search_label
# print(search_label)
# print(search_label.web_element.text)
assert search_label.web_element.get_attribute(SEARCH_ATTR) == SEARCH_FOR
search_label.click()
# search_button = myPage.button(By.CLASS_NAME, SEARCH_CSS_SELECTOR)
# assert search_button.text == SEARCH_TEXT
# search_button.click()
search_input = myPage.search_input
# search_input.input_text('copernicus')
myPage.enter_search_text('air copernicus')
myPage.click_on_search
# print(myPage.search_submit)
# myPage.click_on_search
time.sleep(10)
browser.quit()
