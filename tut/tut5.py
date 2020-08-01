from selenium import webdriver
import selenium.webdriver.common.keys
import time
driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')

driver.get('https://nad.ndml.in/NAD/studentRegistrationWithOutAaddhaar.html')
radiobutton = driver.find_element_by_css_selector("input[id=nsm_nationality2]")
print(radiobutton.is_selected())
driver.close()
