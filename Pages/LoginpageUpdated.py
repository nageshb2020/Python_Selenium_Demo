from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _login_link = "Login1"
    _email_field = "email"
    _password_field = "password"
    _login_button = "commit"

    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def getLoginCount(self):
        return self.driver.find_elements(By.LINK_TEXT, self._login_link).size()

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPhoneField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        self.getLoginLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()