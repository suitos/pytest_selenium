import pytest

from fixtures.browser import Browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="This is request browser",
        required=False
    )

    parser.addoption(
        "--url",
        action="store",
        default="https://www.afreecatv.com",
        help="This is opencart_url",
        required=False
    )


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    driver = Browser(url=url, browser=browser)

    driver.open_main_page()

    yield driver
    driver.quit()


"""
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name for testing")
    parser.addoption("--ver", action="store", default='', help="Browser version for testing")
    parser.addoption("--url", action="store", default='https://www.afreecatv.com', help="Url for testing")
"""
