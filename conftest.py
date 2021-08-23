import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.chrome.options import Options as CH_Options

# pytest -s -v --browser_name=firefox test_cmd.py
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default='firefox',
    #                  help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru or en")


@pytest.fixture(scope='function')
def browser(request):
    # browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    print(user_language)
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    browser = webdriver.Firefox(
        executable_path='/home/myadmin/PycharmProjects/geckodriver',
        firefox_profile=fp)

    yield browser
    browser.quit()