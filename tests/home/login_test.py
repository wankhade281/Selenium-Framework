import os
import time
import unittest
import pytest
from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("wankhadechetan281@gmail.com", "chetan@123")
        # self.lp.login("wankhadechetan281@gmail.com", "Chetan@95")
        time.sleep(3)
        result1 = self.lp.verifyLoginSuccess()
        self.ts.mark(result1, "Login UnSuccessful")
        # assert result1 == True
        result2 = self.lp.verifyTitle()
        self.ts.markFinal("test_validTitle", result2, "Valid Title")
        # assert result2 == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login(" ", " ")
        result1 = self.lp.verifyLoginFailed()
        assert result1 == True

# To run test case:-->  py.test -s -v tests/home/login_test.py --browser chrome To generate html report into
# directory:--> py.test -s -v --html=./htmlreports/login_testreport.html --self-contained-html
# tests/home/login_test.py --browser chrome
