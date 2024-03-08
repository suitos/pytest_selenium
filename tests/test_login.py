from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_login(browser):
    main_page = MainPage(browser.wd)
    main_page.click_login_btn()
    login_page = LoginPage(browser.wd)
    login_page.login(LoginPage.LoginType.COMMON, "suitos", "dkssud12!?")

    assert main_page.login_on_pass() == "서준석"


def test_login2(browser):
    base_page = BasePage(browser.wd)
    url = "https://www.naver.com"
    base_page.navigate(url)
