import os
import unittest
import pytest
from ddt import ddt, data, unpack
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSet", "setUp")
@ddt
class ApplicationFormTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSet):
        self.ap = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    @data(("Chetan", "Chetan123", "Chetan123"), )
    @unpack
    def test_register(self, UserName, Pwd, cnfPwd):
        self.ap.form_fill(UserName,Pwd,cnfPwd)
        result = self.ap.verifyOnRegisterPage()
        assert result == True