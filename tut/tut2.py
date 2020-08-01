from selenium import webdriver
import selenium.webdriver.common.keys
driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
driver.get('https://www.youtube.com/')
search = driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys('ag7842')
searchbuttons = driver.find_element_by_xpath(
    '//*[@id="search-icon-legacy"]/yt-icon')
searchbuttons.click()

driver.close()  # it will close the first opened website
driver.quit()  # it will close the all opened website
