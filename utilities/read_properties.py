import configparser


config = configparser.RawConfigParser()
config.read("./configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_login_url():
        return config.get("common data", "login_url")

    @staticmethod
    def get_matches_url():
        return config.get("common data", "matches_url")

    @staticmethod
    def get_phone_number_field():
        return config.get("selectors data", "phone_number_field")

    @staticmethod
    def get_password_field():
        return config.get("selectors data", "password_field")

    @staticmethod
    def get_login_button():
        return config.get("selectors data", "login_button")

    @staticmethod
    def get_deposit_button():
        return config.get("selectors data", "deposit_button")

    @staticmethod
    def get_mobile_home_page():
        return config.get("selectors data", "mobile_home_page")

    @staticmethod
    def get_phone_number():
        return config.get("authentication data", "phone_number")

    @staticmethod
    def get_password():
        return config.get("authentication data", "password")

    @staticmethod
    def get_confirm_password():
        return config.get("authentication data", "confirm_password")
