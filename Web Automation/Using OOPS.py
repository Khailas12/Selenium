import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.seleniumeasy.com/test/basic-first-form-demo.html"


class Main(webdriver.Chrome):
    def __init__(self, path=r"C:\SeleniumDriver", teardown=False):
        self.path = path
        self.teardown = teardown
        os.environ["PATH"] += self.path
        super(Main, self).__init__()
        print("one")

    def first_page(self):
        self.get(URL)
        self.implicitly_wait(3)
        print("twooo")

    # def message(self):

    #     id = self.find_element_by_link_text("user-message")
    #     # id.send_keys("Hello World")

    #     try:
    #         button = self.find_element_by_class_name("btn btn-default")
    #         button.click()
    #     except:
    #         print("\n No element with this class name. Skipping the process")

    def sum(self):
        sum1 = self.find_element_by_id("sum1")
        sum2 = self.find_element_by_id("sum2")

        sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD4)
        sum2.send_keys(Keys.NUMPAD6, Keys.NUMPAD8)

        try:
            button = self.find_element_by_class_name("at-cm-no-button")
            button.click()
        except:
            print("\n No element with this class name. Skipping the process")

    def button(self):
        btn = self.find_element_by_css_selector(
            "button[onclick='return total()']")
        btn.click()
        print("two")

    def final(self):
        WebDriverWait(self, 33).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "progress-label"),   # Element filteration
                'Complete!'     # The expected text
            )
        )
        print("Four")

    def __exit__(self, exc_type, exc_val, exc_to):
        if self.teardown:
            self.quit()
            print("Exit")


with Main() as mn:
    mn.first_page()
    mn.message()
    mn.sum()
    mn.button()
    mn.final()
    print("Done")
