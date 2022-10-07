from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver

    def set_phone_number(self, phone_number):
        self.driver.find_element(By.ID, "").clear()
        self.driver.find_element(By.ID, "").send_keys(phone_number)

    def set_password(self, password):
        self.driver.find_element(By.ID, "").clear()
        self.driver.find_element(By.ID, "").send_keys(password)

    def cling_login(self):
        self.driver.find_element(By.ID, "").click()
