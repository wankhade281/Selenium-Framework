from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _signin_link = "Sign in"
    _email_field = "user_email"
    _password_field = "user_password"
    _signin_button = "Sign in"

    def getSigninLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._signin_link)

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getSigninButton(self):
        return self.driver.find_element(By.NAME, self._signin_button)

    def clickSigninLink(self):
        self.getSigninLink().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickSigninButton(self):
        self.getSigninButton().click()

    def login(self, email, password):
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickSigninButton()

