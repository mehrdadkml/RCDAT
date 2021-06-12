from selenium import webdriver


driver = webdriver.Chrome('chromedriver')
driver.get('https://www.linkedin.com')

username = driver.find_element_by_class_name('login-email')
username.send_keys('******@gmail.com')
password = driver.find_element_by_class_name('login-password')
password.send_keys('****')

log_in_button = driver.find_element_by_class_name('login-submit')

log_in_button = driver.find_element_by_class_id('login submit-button')

log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

log_in_button.click()
