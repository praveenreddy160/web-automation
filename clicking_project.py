from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# The 'detach' option keeps the browser open after the script finishes
chrome_options.add_experimental_option("detach", True)

# This calls the Chrome class constructor (__init__) with our options to create the driver object
driver = webdriver.Chrome(options=chrome_options)
# Configure the driver to wait up to 5 seconds when searching for elements if they aren't found immediately
driver.implicitly_wait(5)
driver.get('https://secure-retreat-92358.herokuapp.com/')
driver.find_element(By.NAME, value="fName").send_keys("Praveen")
driver.find_element(By.NAME, value="lName").send_keys("Reddy")
driver.find_element(By.NAME, value="email").send_keys("praveenreddy160@gmail.com")
driver.find_element(By.CSS_SELECTOR, value="button").click()