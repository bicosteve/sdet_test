from selenium.webdriver.common.by import By

from page_object.login import Login
from test_cases.conftest import setup
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGenerator


class Test_Login:
    login_url = ReadConfig.get_login_url()
    phone_number = ReadConfig.get_phone_number()
    password = ReadConfig.get_password()
    logger = LogGenerator.denerate_logs()
    deposit_button = ReadConfig.get_deposit_button()

    def test_login(self, setup):
        driver = setup
        driver.get(self.login_url)

        self.logger.info("****Testing Logging*****")

        login_page = Login(driver)

        login_page.set_phone_number(self.phone_number)
        login_page.set_password(self.password)
        login_page.click_login_button()

        driver.implicitly_wait(5)
        deposit_button = driver.find_element(By.XPATH, self.deposit_button).is_enabled()

        if deposit_button:
            assert True
            self.logger.info("***Login Test Passed***")
            driver.close()
        else:
            self.loger.error("****Login Test Failed***")
            driver.close()
            assert False


"""''
pytest -s -v html=reports/report.html test_cases/test_login.py
pytest -s -v --html=reports/report.html test_cases/test_login.py


"""
