import logging
from utilities import custom_logger as cl
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _Signin_link = "nav__button-secondary"
    _email_field = "username"
    _password_field = "password"
    _login_button = "//button[@class='btn__primary--large from__button--floating']"
    _register_page = "bth_header heading-font text-left"
    _User_Name = ""
    _Password = ""
    _cnf_Password = ""
    _date_of_birth = "dob-3473a804-87e4-4c2b-91bd-9d490ff0dc42"

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

    def enterUserName(self, UserName):
        self.sendKeys(UserName, self._User_Name)

    def enterPwd(self, Password):
        self.sendKeys(Password, self._Password)

    def enterCnfPwd(self, cnfPwd):
        self.sendKeys(cnfPwd, self._cnf_Password)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickSiginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.clickSigninLink()
        self.waitForElement(self._login_button, locatorType="xpath")
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickSiginButton()

    def form_fill(self, UserName="", Pwd="", cnfPwd=""):
        self.waitForElement(self._register_page, locatorType="class")
        self.enterUserName(UserName)
        self.enterPwd(Pwd)
        self.enterCnfPwd(cnfPwd)

    def verifyLoginSuccess(self):
        result = self.isElementPresent("//span[contains(text(),'Home')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@id='error-for-password']", locatorType="xpath")
        return result

    def verifyOnRegisterPage(self):
        result = self.isElementPresent("bth_header heading-font text-left", locatorType="class")
        return result

    def verifyTitle(self):
        if "LinkedIn" in self.getTitle():
            return True
        else:
            return False