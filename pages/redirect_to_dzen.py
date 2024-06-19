from locators.Dzen_Locators import *
from pages.base_page import *
import allure

class RedirectToDzen(BasePage):

    @allure.step('Clicking the Yandex logo')
    def click_yandex_logo(self):
        self.click_element(DzenPageLocators.yandex_logo_button)

    @allure.step('Switching to Yandex page and returning the URL')
    def get_yandex_main_page_url(self):
        self.switch_to_next_tab()
        self.wait_for_element(DzenPageLocators.yandex_main_page_logo)
        return self.get_current_url()
