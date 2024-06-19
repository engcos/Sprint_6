from conftest import *
from pages.order_page import *
from data import *
import allure

class TestCreateOrder:
    @allure.title('Verify successful order creation')
    @allure.description('This test verifies the successful creation of an order')
    @pytest.mark.parametrize(
        'name, surname, address, phone_number, comment',
        [
            (name_1, surname_1, address_1, phone_number_1, comment_1),
            (name_2, surname_2, address_2, phone_number_2, comment_2),
        ]
    )
    def test_create_order(self, driver, name, surname, address, phone_number, comment):
        order_page = OrderPageScooter(driver, order_page_url)
        order_page.fill_personal_info(name, surname, address, phone_number)
        order_page.fill_scooter_order_form(comment)
        order_page.confirm_order()

        assert order_page.get_order_status() == 'Посмотреть статус'

    @allure.title('Verify redirection to the main page of Scooter')
    @allure.description('This test verifies that the returned text matches the expected value')
    def test_transition_main(self, driver):
        order_page = OrderPageScooter(driver, order_page_url)
        order_page.go_to_main_page()

        assert order_page.get_main_page_text() == actual_text

