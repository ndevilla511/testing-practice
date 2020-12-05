import pytest
from selenium import webdriver
from tests import config as cfg

# this function will let you define a command prompt option for py.test to specify which browser to run
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )


@pytest.fixture(scope="class")
def setup(request): # passing the request parameter will make whatever functions, objects, variables that you attach to request.cls accessible to the class you attach this fixture to, but only if the scope="class"
    browser_name = request.config.getoption("browser_name")
    print(request.config.rootdir)
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Ie()

    if request.cls is not None:
        request.cls.driver = driver  # this will make the driver object accessible
    driver.implicitly_wait(10)
    driver.get(cfg.LOGIN_URL)
    driver.maximize_window()
    driver.find_element_by_name("username").send_keys(cfg.USERNAME)
    driver.find_element_by_name("password").send_keys(cfg.PASSWORD)
    driver.find_element_by_name("password").submit()
    yield driver # if you need to return a value from this fixture function, you can use yield in place of return
    # any code after yield will run after all the tests are finished
    driver.close()

@pytest.fixture(scope="class")
def navigate_to_campaigns(request):
    request.cls.driver.get(cfg.CAMPAIGNS_URL)