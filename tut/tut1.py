from selenium import webdriver
driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
driver.get('https://icampus.bennett.edu.in/#/')
print(driver.title)
print(driver.page_source)
print(driver.current_url)
driver.close()
