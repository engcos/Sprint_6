from locators.main_locators import *
from pages.base_page import *
import allure

class MainPage(BasePage):

    @allure.step('Locate and click on a question. Returns the text of the answer.')
    def retrieve_answer_text(self, question_number):
        question_locator = self.format_locator(MainPageLocators.question_locator, question_number)
        answer_locator = self.format_locator(MainPageLocators.answer_locator, question_number)
        self.wait_for_element(MainPageLocators.scooter_image)
        self.scroll_to(MainPageLocators.specific_question_8)
        self.wait_for_element(MainPageLocators.specific_question_8)
        self.click_element(question_locator)

        return self.get_text(answer_locator)

    @allure.step('Clicking the "Order" button at the top of the page')
    def click_order_button_top(self):
        self.click_element(MainPageLocators.order_button_header)
        return self.get_current_url()

    @allure.step('Clicking the "Order" button at the bottom of the page')
    def click_order_button_bottom(self):
        self.scroll_to(MainPageLocators.order_button_footer)
        self.click_element(MainPageLocators.order_button_footer)
        return self.get_current_url()
