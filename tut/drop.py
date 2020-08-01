from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
driver.maximize_window()
driver.get('https://nad.ndml.in/NAD/studentRegistrationWithOutAaddhaar.html')
institutetype = driver.find_element_by_id('nsm_ai_Type')
institutetypedrp = Select(institutetype)
institutetypedrp.select_by_visible_text('University')
state = driver.find_element_by_id('nsm_univ_state')
statedrp = Select(state)
statedrp.select_by_visible_text('Uttar Pradesh')
time.sleep(2)
nameofinstitution = driver.find_element_by_name('nsm_brd_univ_id')
nameofinstitutiondrp = Select(nameofinstitution)
nameofinstitutiondrp.select_by_visible_text('Bennett University')
