import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running conftest demo method setUp")
    yield
    print("Running conftest demo method tearDown")


# @pytest.yield_fixture(scope="module")
# def oneTimeSetUp():
#     print("Running oneTimeSetUp")
#     yield
#     print("Running oneTimeTearDown")


#  used for test_command_line_args.py
@pytest.yield_fixture(scope="class")  # For particular module(ex test_case_demo1.py) use scope='module' for  particular class use scope='class'
def oneTimeSetUp(request,browser):
    print("Running oneTimeSetUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # if browser == 'firefox':
    #     print("Running Test on Firefox")
    #     baseURL = "https://www.linkedin.com/home"
    #     driver = webdriver.Firefox()
    #     driver.get(baseURL)
    # else:
    #     baseURL = "https://www.linkedin.com/home"
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(baseURL)
    #     print("Running Test on Chrome")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running oneTimeTearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operations")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
