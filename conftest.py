import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: en, ru, etc.')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    
    print('\nstart chrome browser for test..')
    options = ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    print('\nquit browser..')
    browser.quit()

def test_example(browser):
    # Example test that uses the browser fixture
    browser.get('https://www.example.com')
    assert 'Example Domain' in browser.title
