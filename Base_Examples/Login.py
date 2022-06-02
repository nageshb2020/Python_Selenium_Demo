from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Login():

    def ValidateLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        loginLink = driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()
        driver.fi
        emailField = driver.find_element(By.ID, "email")
        emailField.send_keys("test@email.com")

        passwordField = driver.find_element(By.ID, "password")
        passwordField.send_keys("abcabc")
