from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get('https://nad.ndml.in/NAD/studentRegistrationWithOutAaddhaar.html')
driver.find_element_by_xpath('//*[@id="dob"]').clear()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="dob"]').send_keys('27-09-2020')
