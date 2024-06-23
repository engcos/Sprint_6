from conftest import *
from pages.redirect_to_dzen import *
from data import *
import allure

class TestRedirectToDzen:

    @allure.title('Verify redirection to Yandex main page')
    @allure.description('This test verifies that the specified text is part of the Yandex main page URL')
    def test_redirect_to_dzen(self, driver):
        redirect_page = RedirectToDzen(driver, URLs.main_page_url)
        redirect_page.click_yandex_logo()

        assert "dzen.ru" in redirect_page.get_yandex_main_page_url()
