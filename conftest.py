import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru or en")


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(
        executable_path='/home/myadmin/PycharmProjects/geckodriver',
        firefox_profile=fp)

    yield browser
    browser.quit()