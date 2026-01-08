from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
# The 'detach' option keeps the browser open after the script finishes
chrome_options.add_experimental_option("detach", True)

# This calls the Chrome class constructor (__init__) with our options to create the driver object
driver = webdriver.Chrome(options=chrome_options)
# Configure the driver to wait up to 5 seconds when searching for elements if they aren't found immediately
driver.implicitly_wait(5)
driver.get('https://www.amazon.com/gp/product/B09231NL5H/ref=ox_sc_act_title_1?smid=A21U86ONRH0Q7Z&psc=1#averageCustomerReviewsAnchor')

# Use the find_element method of the driver object to locate HTML elements by their class name
price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"The price of the item is {price_symbol.text}{price_whole.text}.{price_fraction.text}")
# driver.close()
# driver.quit()
