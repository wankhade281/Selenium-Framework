from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _Signin_link = "nav__button-secondary"
    _email_field = "username"
    _password_field = "password"
    _login_button = "//button[@class='btn__primary--large from__button--floating']"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickSigninLink(self):
        self.elementClick(self._Signin_link, locatorType="class")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickSiginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email, password):
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickSiginButton()
