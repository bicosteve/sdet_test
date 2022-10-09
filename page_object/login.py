import configparser

from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")


class Login:

    phone_number_field = ReadConfig.get_phone_number_field()
    password_field = ReadConfig.get_password_field()
    login_button = ReadConfig.get_login_button()

    def __init__(self, driver):
        self.driver = driver

    def set_phone_number(self, phone_number):
        self.driver.find_element(By.XPATH, self.phone_number_field).clear()
        self.driver.find_element(By.XPATH, self.phone_number_field).send_keys(
            phone_number
        )

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field).clear()
        self.driver.find_element(By.XPATH, self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.CLASS_NAME, self.login_button).click()
