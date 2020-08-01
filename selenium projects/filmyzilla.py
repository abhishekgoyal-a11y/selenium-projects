from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


def number_extractor(text):
    number = '1234567890'
    numbere = ""
    for num in text:
        if num in number:
            numbere += num
        else:
            pass
    return numbere


driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
driver.get(
    'https://filmyzilla.pink/category/284/Hollywood-hindi-dubbed-movies-2020/default/1.html')
inputext = driver.find_element_by_xpath('/html/body/div[2]/form/input[1]')
inputext.send_keys('dhamaal', Keys.ENTER)
for i in range(2):
    try:
        inputext.send_keys(Keys.ENTER)
    except:
        pass
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    if driver.title in 'dhamaal site:filmyzilla.pink - Google Search':
        try:
            link1 = driver.find_element_by_xpath(
                f'//*[@id="rso"]/div[1]/div/div[1]/a')
            link1.click()
            movie_name = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/p[1]/font[2]/b')
            movie_link = driver.find_elements_by_class_name('listed')
            movie_inside_link = driver.find_elements_by_class_name('downLink')
            for j in range(len(movie_link)):
                movie_link[j].click()
                try:
                    movie_link[j].click()
                except:
                    pass
                for k in range(len(movie_inside_link)):
                    movie_inside_link[k].click()
                    try:
                        movie_inside_link[k].click()
                    except:
                        pass
        except:
            pass
    else:
        driver.close()
