import unittest

from selenium import webdriver
from pages.home.login_page import LoginPage


class LoginTest(unittest.TestCase):
    def test_validLogin(self):
        baseUrl = "https://www.linkedin.com/home"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        lp = LoginPage(driver)
        lp.login("wankhadechetan281@gmail.com", "Chetan@95")

        dashboard_icon = driver.find_element_by_class_name("scaling-icon")
        if dashboard_icon is not None:
            print("Login Successful")
        else:
            print("Login Not Successful")
