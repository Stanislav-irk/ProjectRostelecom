import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage
from selenium.common.exceptions import TimeoutException


@pytest.fixture(params=["chrome"])
def initialize_driver(request):
    """Фикстура для инициализации драйвера."""
    if request.param == "chrome":
        driver = webdriver.Chrome()
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.maximize_window()
    yield
    print("\nClose Driver")
    driver.close()
    driver.quit()


@pytest.fixture()
def auth_page(request, initialize_driver):
    """Фикстура для создания экземпляра страницы авторизации."""
    auth_page = AuthPage(request.cls.driver)
    return auth_page


def pytest_configure(config):
    """Добавляем свой собственный маркер."""
    config.addinivalue_line("markers", "skip_if_captcha: mark test as skipped if CAPTCHA is present on the page")


@pytest.fixture(autouse=True)
def check_captcha(request, auth_page):
    """Фикстура для проверки наличия CAPTCHA на странице."""
    marker = request.node.get_closest_marker("skip_if_captcha")
    if marker:
        try:
            captcha_element = auth_page.find((By.CLASS_NAME, 'rt-captcha__image-con'))
            if captcha_element.is_displayed():
                pytest.skip("CAPTCHA is present on the page")
        except TimeoutException:
            pass
