from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print(f"Error navigating to {url}: {e}")

    def wait_for_element_to_be_clickable(self, locator, timeout):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException as e:
            print(f'Error: {e}')

    def click(self, locator):
        element = self.wait_for_element_to_be_clickable(locator, 3)
        element.click()

    def sendkeys(self, locator, text):
        element = self.wait_for_element_to_be_clickable(locator, 3)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_element_to_be_clickable(locator, 3)
        return element.text
