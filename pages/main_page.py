from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    LOGIN_BTN = (By.ID, 'loginBtn')
    PROFILE_BTN = (By.ID, 'profileBtn')

    def __init__(self, driver):
        super().__init__(driver)

    def click_login_btn(self):
        self.click(self.LOGIN_BTN)

    def login_on_pass(self):
        return self.get_text(self.PROFILE_BTN)
