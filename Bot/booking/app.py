import booking.constants as const
from selenium import webdriver
import os


class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\SeleniumDriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(5)
        self.maximize_window()
        
    def __exit__(self, exc_type, exc_val, exc_to):
        if self.teardown:
            self.quit()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
    
    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
            # f'a[data-modal-header-async-url-param="changed_currency=1;selected_currency=GBP;top_currency=1"]'
        )
        selected_currency_element.click()
    
    def language(self, lang=None):
        language_element = self.find_element_by_css_selector(
            f'button[data-tooltip-text="Choose your language"]'
        )
        language_element.click()
        
        select_language_element = self.find_element_by_css_selector(
            f'a[hreflang="{lang}"]'
        )
        select_language_element.click()
        print("Language done")
        
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        
        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()
        
    def calendar(self, check_in, check_out):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]'
        )
        check_in_element.click()
        
        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]'
        )
        check_out_element.click()
    
    
    def select_adults(self, count=1):
        selection_element = self.find_element_by_id(
            'xp__guests__toggle'
        )
        selection_element.click()
        
        while True:
            increase_button_element = self.find_element_by_css_selector(
                'button[aria-label="Increase number of Adults"]'
            )
            for _ in range(count - 1):
                increase_button_element.click()
                
            
    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()
        
        
            