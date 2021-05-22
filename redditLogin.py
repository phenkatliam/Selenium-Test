from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.reddit.com')

# clicking on the login button
login_btn = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div[2]/div[1]/a[1]')
login_btn.click()



driver.implicitly_wait(10)
page_title = driver.title


frame = driver.find_element_by_xpath("//iframe[@class='_25r3t_lrPF3M6zD2YkWvZU']")
driver.switch_to.frame(0)


print("alert accepted")
driver.implicitly_wait(10)

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//fieldset//input[@id='loginUsername']")))
username.send_keys('test_username')

pwd = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//fieldset//input[@id='loginPassword']")))
pwd.send_keys('password')

login_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//fieldset//button[@class='AnimatedForm__submitButton']")))
login_btn.click()