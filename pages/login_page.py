from enum import Enum

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    ID_INPUT = (By.ID, "uid")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_AUTH_BTN = (By.XPATH, '//*[@onclick="login();"]')

    class LoginType(Enum):
        COMMON = "COMMON"
        SNS = "SNS"

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, login_type, username, userpw):
        if login_type == LoginPage.LoginType.COMMON:
            self.sendkeys(self.ID_INPUT, username)
            self.sendkeys(self.PASSWORD_INPUT, userpw)
            self.click(self.LOGIN_AUTH_BTN)
