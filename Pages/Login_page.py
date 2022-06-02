from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver=driver

    def login(self,username,password):
        loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "email")
        emailField.send_keys("test@email.com")

        passwordField = self.driver.find_element(By.ID, "password")
        passwordField.send_keys("abcabc")


    def login_lTEST(self,username,password):
        loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "email")
        emailField.send_keys("test@email.com")

        passwordField = self.driver.find_element(By.ID, "password")
        passwordField.send_keys("abcabc")
