from selenium import webdriver
import selenium.webdriver.common.keys
import time
driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')

driver.get('https://nad.ndml.in/NAD/studentRegistrationWithOutAaddhaar.html')
# implicitly_wait =  wait till the page is fully loaded
driver.implicitly_wait(10)
# after 10 second it will give command
name = driver.find_element_by_xpath('//*[@id="first_name"]')
name.send_keys("abhishek")
