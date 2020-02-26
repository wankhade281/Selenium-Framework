import os
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
        self.lp.login(os.getenv("USER_LOGIN"), os.getenv("USER_PASSWORD"))
        time.sleep(3)
        result = self.lp.verifyLoginSuccess()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(os.getenv("USER_LOGIN"), os.getenv("USER_PASSWORD"))
        result = self.lp.verifyLoginFailed()
        assert result == True

# To run test case:-->  py.test -s -v tests/home/login_test.py --browser chrome To generate html report into
# directory:--> py.test -s -v --html=./htmlreports/login_testreport.html --self-contained-html
# tests/home/login_test.py --browser chrome