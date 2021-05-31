import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path="chromedriver")
    yield browser
    browser.quit()