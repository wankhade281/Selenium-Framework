from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://www.linkedin.com/home"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("wankhadechetan281@gmail.com", "Chetan@95")

        userIcon = driver.find_element(By.XPATH, "//span[contains(text(),'Home')]")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")
