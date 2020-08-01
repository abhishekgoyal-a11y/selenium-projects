from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import pytesseract
import os
from PIL import Image


driver = webdriver.Chrome(
    'C:/Users/HP/Desktop/Drivers/chromedriver_win32/chromedriver.exe')
driver.get('http://resumefilling.com/Login.aspx')
username = driver.find_element_by_xpath('//*[@id="txt_regid"]')
username.send_keys('294RFJ04042020')
password = driver.find_element_by_xpath('//*[@id="txt_password"]')
password.send_keys('189340')
button = driver.find_element_by_xpath('//*[@id="btn_login"]')
button.click()
driver.maximize_window()


# select number of form


def dropd(text):
    drop = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_drp_pagejump"]')
    dropmenu = Select(drop)
    dropmenu.select_by_index(text)

# personal details


def firstnamed(text):
    firstname = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_firstname"]')
    firstname.clear()
    firstname.send_keys(text)


def middlenamed(text):
    middlename = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_middlename"]')
    middlename.clear()
    middlename.send_keys(text)


def lastnamed(text):
    lastname = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_lastname"]')
    lastname.clear()
    lastname.send_keys(text)


def DOBd(text):
    DOB = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_dob"]')
    DOB.clear()
    DOB.send_keys(text)


def genderd(text):
    gender = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_gender"]')
    gender.clear()
    gender.send_keys(text)


def nationd(text):
    nation = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_nationality"]')
    nation.clear()
    nation.send_keys(text)


def marriedd(text):
    married = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_maritalstatus"]')
    married.clear()
    married.send_keys(text)


def passportd(text):
    passport = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_passport"]')
    passport.clear()
    passport.send_keys(text)


def hobbiesd(text):
    hobbies = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_hobbies"]')
    hobbies.clear()
    hobbies.send_keys(text)


def languaged(text):
    language = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_languageknown"]')
    language.clear()
    language.send_keys(text)
# communication details


def addressd(text):
    address = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_address"]')
    address.clear()
    address.send_keys(text)


def landmarkd(text):
    landmark = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_landmark"]')
    landmark.clear()
    landmark.send_keys(text)


def cityd(text):
    city = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_city"]')
    city.clear()
    city.send_keys(text)


def stated(text):
    state = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_state"]')
    state.clear()
    state.send_keys(text)


def pincoded(text):
    pincode = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_pincode"]')
    pincode.clear()
    pincode.send_keys(text)


def mobiled(text):
    mobile = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_mobile"]')
    mobile.clear()
    mobile.send_keys(text)


def emailidd(text):
    emailid = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_emailid"]')
    emailid.clear()
    emailid.send_keys(text)


# qualification details
def sscresultd(text):
    sscresult = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_sscresult"]')
    sscresult.clear()
    sscresult.send_keys(text)


def sscboardd(text):
    sscboard = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_sscuniversity"]')
    sscboard.clear()
    sscboard.send_keys(text)


def sscrpassingyeard(text):
    sscrpassingyear = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_sscyear"]')
    sscrpassingyear.clear()
    sscrpassingyear.send_keys(text)


def hscresultd(text):
    hscresult = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_hscresult"]')
    hscresult.clear()
    hscresult.send_keys(text)


def hscboardd(text):
    hscboard = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_hscuniversity"]')
    hscboard.clear()
    hscboard.send_keys(text)


def hscrpassingyeard(text):
    hscrpassingyear = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_hscyear"]')
    hscrpassingyear.clear()
    hscrpassingyear.send_keys(text)


def diplomadegree(text):
    diplomadegree = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_diplomadegree"]')
    diplomadegree.clear()
    diplomadegree.send_keys(text)


def diplomaresultd(text):
    diplomaresult = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_diplomaresult"]')
    diplomaresult.clear()
    diplomaresult.send_keys(text)


def diplomaboardd(text):
    diplomaboard = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_diplomauniversity"]')
    diplomaboard.clear()
    diplomaboard.send_keys(text)


def diplomarpassingyeard(text):
    diplomarpassingyear = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_diplomayear"]')
    diplomarpassingyear.clear()
    diplomarpassingyear.send_keys(text)


def graduationdegreed(text):
    graduationdegree = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_graduationdegree"]')
    graduationdegree.clear()
    graduationdegree.send_keys(text)


def graduationresultd(text):
    graduationresult = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_graduationresult"]')
    graduationresult.clear()
    graduationresult.send_keys(text)


def graduationboard(text):
    graduationboard = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_graduationuniversity"]')
    graduationboard.clear()
    graduationboard.send_keys(text)


def graduationrpassingyear(text):
    graduationrpassingyear = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_graduationyear"]')
    graduationrpassingyear.clear()
    graduationrpassingyear.send_keys(text)


def postgraduationdegreed(text):
    postgraduationdegree = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_postgraduationdegree"]')
    postgraduationdegree.clear()
    postgraduationdegree.send_keys(text)


def postgraduationresultd(text):
    postgraduationresult = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_postgraduationresult"]')
    postgraduationresult.clear()
    postgraduationresult.send_keys(text)


def postgraduationboardd(text):
    postgraduationboard = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_postgraduationuniversity"]')
    postgraduationboard.clear()
    postgraduationboard.send_keys(text)


def postgraduationrpassingyeard(text):
    postgraduationrpassingyear = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_postgraduationyear"]')
    postgraduationrpassingyear.clear()
    postgraduationrpassingyear.send_keys(text)


def highestleveleducationd(text):
    highestleveleducation = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_highestleveleducation"]')
    highestleveleducation.clear()
    highestleveleducation.send_keys(text)


# employment details


def yeard(text):
    year = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_totalworkyear"]')
    year.clear()
    year.send_keys(text)


def monthd(text):
    month = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_totalworkmonth"]')
    month.clear()
    month.send_keys(text)


def totalcompaniesworkedd(text):
    totalcompaniesworked = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_totalcompanieswork"]')
    totalcompaniesworked.clear()
    totalcompaniesworked.send_keys(text)


def lastcurrentemployerd(text):
    lastcurrentemployer = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_lastcurrentemploye"]')
    lastcurrentemployer.clear()
    lastcurrentemployer.send_keys(text)


def submitd():
    submitbutton = driver.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_btn_submit"]')
    submitbutton.click()

