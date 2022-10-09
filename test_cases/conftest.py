import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeWebService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    return webdriver.Chrome(service=ChromeWebService(ChromeDriverManager().install()))