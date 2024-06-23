from conftest import *
import pytest
from data import FAQAnswers, URLs
from pages.main_page import *
import allure

class TestMainPage:

    @allure.title('Check the answers to questions match expected values')
    @allure.description('This test verifies that the answer to a question matches the expected value')
    @pytest.mark.parametrize(
        'question_num, expected_answer',
        [
            (0, FAQAnswers.answer_1),
            (1, FAQAnswers.answer_2),
            (2, FAQAnswers.answer_3),
            (3, FAQAnswers.answer_4),
            (4, FAQAnswers.answer_5),
            (5, FAQAnswers.answer_6),
            (6, FAQAnswers.answer_7),
            (7, FAQAnswers.answer_8),
        ]
    )
    def test_question_and_answer(self, driver, question_num, expected_answer):
        main_page = MainPage(driver, URLs.main_page_url)
        actual_answer = main_page.retrieve_answer_text(question_num)

        assert actual_answer == expected_answer

    @allure.title('Check redirection from the header order button to the order page')
    @allure.description('This test verifies that the URL matches the expected order page URL')
    def test_button_order_header(self, driver):
        main_page = MainPage(driver, URLs.main_page_url)

        assert main_page.click_order_button_top() == URLs.order_page_url

    @allure.title('Check redirection from the footer order button to the order page')
    @allure.description('This test verifies that the URL matches the expected order page URL')
    def test_button_order_footer(self, driver):
        main_page = MainPage(driver, URLs.main_page_url)

        assert main_page.click_order_button_bottom() == URLs.order_page_url