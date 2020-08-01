from selenium import webdriver
import selenium.webdriver.common.keys
import time
driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
driver.get('https://www.youtube.com/')

driver.get('http://lms.bennett.edu.in/login/index.php')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
