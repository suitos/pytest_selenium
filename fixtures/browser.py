from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Browser:

    def __init__(self, url, browser):
        self.wd = None
        try:
            self.wd = self.get_webdriver(browser)
            self.wd.maximize_window()
        except ValueError as e:
            print(f'에러: {e}')

        self.url = url

    def get_webdriver(self, browser):
        if browser.lower() == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            # options.add_argument('headless')
            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()))
        elif browser.lower() == 'firefox':
            firefox_options = webdriver.FirefoxOptions()
            
            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError(f'알 수 없는 브라우저: {browser}')

    def open_main_page(self):
        self.wd.get(self.url)

    def quit(self):
        if self.wd:
            self.wd.quit()
