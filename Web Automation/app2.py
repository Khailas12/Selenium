import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += f"C:\SeleniumDriver"
driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.implicitly_wait(3)

try:
    button = driver.find_element_by_class_name("at-cm-no-button")   # this will clear the pop up
    button.click()
except:
    print("\nNo element with this class name. Skipping this process")
    
    
sum1 = driver.find_element_by_id("sum1")
sum2 = driver.find_element_by_id("sum2")


sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5)  # only enters after assigning the keys we've provided. which returns 15 in here
sum2.send_keys(12)


btn = driver.find_element_by_css_selector("button[onclick='return total()']")   # This makes the above above key (Keys.HOME) to be executed without entering anything
btn.click()




