import time
import unittest
import pytest
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("wankhadechetan281@gmail.com", "Chetan@95")
        time.sleep(3)
        result = self.lp.verifyLoginSuccess()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("wankhadechetan281@gmail.com", "chetan@915")
        result = self.lp.verifyLoginFailed()
        assert result == True
