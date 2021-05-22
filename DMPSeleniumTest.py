from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://dealeradmin.securecomwireless.com")
print(driver.title)


user = driver.find_element_by_name("email")
user.send_keys("user1")
user.send_keys(Keys.RETURN)


