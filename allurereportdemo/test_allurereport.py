import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestAllure:
    @allure.severity(allure.severity_level.MINOR)
    def test_signinpage(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.linkedin.com/home")
        self.driver.maximize_window()
        time.sleep(5)
        status = self.driver.find_element_by_xpath("//h1[@class='hero__headline hero__headline--basic']").is_displayed()
        self.driver.close()
        if status == True:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        driver = webdriver.Chrome()
        driver.get("https://www.linkedin.com/home")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name("nav__button-secondary").click()
        driver.find_element_by_id("username").send_keys("wankhadechetan281@gmail.com")
        driver.find_element_by_id("password").send_keys("Chetan@95")
        driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()
        # status = driver.find_element_by_id("feed-tab-icon").is_displayed()
        title = driver.title
        time.sleep(5)
        if title == "LinkedIn121":
            assert True
        else:
            allure.attach(driver.get_screenshot_as_png(), name="TestLoginScreen", attachment_type=AttachmentType.PNG)
            driver.close()
            assert False
        # print("Title of a Login Page =-->=-->=-->=-->=-->=-->",driver.title)
        # if status == True:
        #     assert True
        # else:
        #     assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_profile(self):
        pytest.skip("Right Now skipped I will implement later")

# To run test and save into directory of pycharm reports:--> py.test -s -v --alluredir="/home/admin1/Demo1/PycharmProjects/selenium-framework/allurereportdemo/reports" test_allurereport.py
# To Generate a report:--> allure serve /home/admin1/Demo1/PycharmProjects/selenium-framework/allurereportdemo/reports
# To add a path to the system:--> export PATH="/home/admin1/Downloads/allure-commandline-2.13.1/allure-2.13.1/bin/:$PATH"