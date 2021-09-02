from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.python.org")
assert "Python" in driver.title
element = driver.find_element_by_name("q")
element.clear()
element.send_keys("pycon")
element.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source
driver.close()




