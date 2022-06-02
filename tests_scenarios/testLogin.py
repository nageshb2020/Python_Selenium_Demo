from selenium import webdriver
from selenium.webdriver.common.by import By
import Pages.Login_page

import time

class Logintest():
    baseURL = "https://letskodeit.teachable.com/"
    driver = webdriver.Chrome("D:\Driver\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)

    lp=Pages.Login_page(driver)
    lp.LoginPage('username', 'password')

