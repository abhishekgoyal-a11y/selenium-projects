import os
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# pyautogui.hotkey('win', 'r')
# pyautogui.keyDown('enter')
# time.sleep(2)
# pyautogui.typewrite('hello word')
# pyautogui.keyDown('enter')


# def open_cmd():
#     pyautogui.hotkey('win', 'l')


# def write_cmd(text):
#     pyautogui.hotkey('win', 'r')
#     pyautogui.keyDown('enter')
#     time.sleep(2)
#     pyautogui.typewrite(text)
#     pyautogui.keyDown('enter')

# write_cmd('pip install pyautogui')
# driver = webdriver.Chrome(
#     "C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe")
# driver.get('https://www.google.com/search?rlz=1C1CHBF_enIN828IN828&sxsrf=ALeKk00lLozl_SQ51gCfwJGWBTDIjs1oZQ%3A1585475437072&ei=bW-AXuaQBL2Q4-EPsr6JkAc&q=dog&oq=dog&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIECCMQJzIECAAQQzIFCAAQkQIyBQgAEJECMgQIABBDMgQIABBDMgQIABBDMgQIABBDOgQIABBHOgUIABCDAToCCABQhL8FWI7BBWCewgVoAHABeACAAYYCiAGyA5IBBTAuMS4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwim--ehtL_oAhU9yDgGHTJfAnIQ4dUDCAs&uact=5')
# driver.find_element_by_xpath(
#     '//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input').clear()
# time.sleep(1)
# driver.find_element_by_xpath(
#     '//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input').send_keys('pip install tenrflow')
# driver.find_element_by_xpath(
#     '//*[@id="tsf"]/div[2]/div[1]/div[2]/button').click()
# time.sleep(1)
# try:
#     driver.find_element_by_xpath('//*[@id="fprsl"]').click()
# except:
#     pass
# import wikipedia
# for i in range(len(os.listdir('C:/Users/HP/Desktop'))):
#     print(os.listdir(
#         f"C:/Users/HP/Desktop/{os.listdir('C:/Users/HP/Desktop')[i]}"))
# print(os.listdir('C:/Users/HP/Desktop')[0])
text = input()
# make_new_folder = ['make new folder', 'make new directory',
#                    'new folder', 'new folder name as']
# for i in range(len(make_new_folder)):
#     if text[0:len(make_new_folder[i])] == make_new_folder[i]:
#         text = text.replace(make_new_folder[i], "")
#         text = text.replace(" ", "")
#         os.mkdir(f"C:/Users/HP/Desktop/{text}")


google = ["search about", "open google and search", "open google and search about",
          'in google search this', 'in google search about', "google", "google search about"]
for j in range(len(google)):
    if text[0:len(google[j])] == google[j]:
        text = text.replace(google[j], "")
        text = text.replace(" ", "")
        driver = webdriver.Chrome(
            "C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe")
        driver.get('https://www.google.com/search?source=hp&ei=tjuAXrPhAsqT4-EPoLGuoAc&q=+pen&oq=+pen&gs_lcp=CgZwc3ktYWIQAzIFCAAQgwEyBQgAEIMBMgUIABCDATIFCAAQgwEyBQgAEIMBMgUIABCDATICCAAyAggAMgIIADICCABQkEhYrkhg5JECaABwAHgDgAGPA4gB8wqSAQUyLTEuM5gBAKABAaoBB2d3cy13aXqwAQA&sclient=psy-ab&ved=0ahUKEwizlPr4gr_oAhXKyTgGHaCYC3QQ4dUDCAY&uact=5')
        driver.maximize_window()
        inputtext = driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
        inputtext.clear()
        time.sleep(1)
        inputtext.send_keys(text)
        driver.find_element_by_xpath(
            '//*[@id="tsf"]/div[2]/div[1]/div[2]/button').click()
        try:
            driver.find_element_by_xpath(
                '//*[@id="taw"]/div[2]/div/p/a').click()
        except:
            pass
