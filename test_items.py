import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    # Настройка WebDriver (в данном случае используем Chrome, можно заменить на Firefox и т.д.)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_to_basket_button_exists(browser):
    # URL страницы товара
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    # Открытие страницы товара
    browser.get(url)
    
    # Проверка наличия кнопки добавления в корзину
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button is not None, "Кнопка добавления в корзину не найдена"
