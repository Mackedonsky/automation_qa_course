import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    chrome_binary_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    driver = webdriver.Chrome(ChromeDriverManager(driver_version='118.0.5993.70').install(),
                              chrome_options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
