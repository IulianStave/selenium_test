import unittest
from selenium import webdriver

search_label_css_selector = '.search-toggle.search-label'
header_css_selector = 'div.search--listing > header'
search_input_id = 'edit-search-api-fulltext'
results_class = 'views-row'
search_text = 'air'
no_results_css_selector = 'div.search--listing > header'


class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(5)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("https://atmosphere.copernicus.eu/")
        # inst.driver.title

    def test_search_by_text(self):
        # get the search textbox
        self.search_label = self.driver.find_element_by_css_selector(search_label_css_selector)
        # print('\n\n\nLabel search element:::', self.search_label)
        self.search_label.click()
        self.search_input = self.driver.find_element_by_id(search_input_id)
        # print('\n\n\nInput element::: ', self.search_input)
        self.search_input.clear()
        # enter search keyword and submit
        self.search_input.send_keys(search_text)
        self.search_input.submit()
        # # get the list of elements which are displayed after the search
        # # currently on result page using find_elements_by_class_name method
        results = self.driver.find_elements_by_class_name(results_class)
        self.header = self.driver.find_element_by_css_selector(header_css_selector)
        first_page_no_results = int(self.header.text.split()[3])
        total_results = int(self.header.text.split()[5])
        value_to_check = 10
        if total_results == first_page_no_results:
            value_to_check = total_results
        self.assertEqual(len(results), first_page_no_results)

    # def test_search_by_name(self):
        # get the search textbox
        # self.search_field = self.driver.find_element_by_name("q")
        # # enter search keyword and submit
        # self.search_field.send_keys("Python class")
        # self.search_field.submit()
        # # get the list of elements which are displayed after the search
        # # currently on result page using find_elements_by_class_name method
        # list_new = self.driver.find_elements_by_class_name("r")
        # self.assertEqual(8, len(list_new))

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)