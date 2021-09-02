import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"


class Main(webdriver.Chrome):
    def __init__(self, path=r"C:\SeleniumDriver", teardown=False):
        self.path = path
        self.teardown = teardown
        os.environ["PATH"] += self.path
        super(Main, self).__init__()

    def first_page(self):
        self.get(URL)
        self.implicitly_wait(3)
        print("Site opened")

    def popup_skip(self):
        try:
            button = self.find_element_by_class_name("at-cm-no-button")
            button.click()
            print("Popup skipped")
        except:
            print("\n No element with this class name. Skipping the process")

    def message(self):
        msg = self.find_element_by_id("user-message")
        msg.send_keys("Hello World")

    def text_btn(self):
        btn = self.find_element_by_css_selector(
            "button[onclick='showInput();']")
        btn.click()
        print("text button clicked")

    def sum(self):
        sum1 = self.find_element_by_id("sum1")
        sum2 = self.find_element_by_id("sum2")

        sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD4)
        sum2.send_keys(Keys.NUMPAD6, Keys.NUMPAD8)

    def sum_button(self):
        btn = self.find_element_by_css_selector(
            "button[onclick='return total()']")
        btn.click()
        print("Sum button clicked")

    def final(self):
        try:   # Explicit Wait is code you define to wait for a certain condition to occur before proceeding further in the code
            WebDriverWait(self, 10).until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "progress-label"),   # Element filteration
                    'Complete!'     # The expected text
                )
            )
            print("Four")
        except:
            AttributeError
            print("\nPassed the AttributeError Succesfully")

    def __exit__(self, exc_type, exc_val, exc_to):
        if self.teardown:
            self.quit()
            print("Exit")


if __name__ == "__main__":
    with Main() as mn:
        mn.first_page()
        mn.popup_skip()
        mn.message()
        mn.text_btn()
        mn.sum()
        mn.sum_button()
        mn.final()
        print("Done")
