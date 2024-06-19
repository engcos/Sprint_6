from locators.order_locators import OrderPageLocators
from pages.base_page import BasePage
import allure

class OrderPageScooter(BasePage):

    @allure.step('Filling in the name field')
    def enter_name(self, name):
        self.enter_text(OrderPageLocators.input_name, name)

    @allure.step('Filling in the surname field')
    def enter_surname(self, surname):
        self.enter_text(OrderPageLocators.input_surname, surname)

    @allure.step('Filling in the address field')
    def enter_address(self, address):
        self.enter_text(OrderPageLocators.input_address, address)

    @allure.step('Selecting a metro station')
    def select_metro_station(self):
        self.click_element(OrderPageLocators.input_metro_station)
        self.click_element(OrderPageLocators.button_select_metro_station)

    @allure.step('Filling in the phone number field')
    def enter_phone_number(self, phone_number):
        self.enter_text(OrderPageLocators.input_phone_number, phone_number)

    @allure.step('Clicking the "Next" button')
    def click_next_button(self):
        self.click_element(OrderPageLocators.button_next)

    @allure.description('Combining steps for filling personal information')
    def fill_personal_info(self, name, surname, address, phone_number):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.select_metro_station()
        self.enter_phone_number(phone_number)
        self.click_next_button()

    @allure.step('Selecting the delivery date')
    def select_delivery_date(self):
        self.click_element(OrderPageLocators.input_delivery_date)
        self.click_element(OrderPageLocators.date_selector)

    @allure.step('Selecting the rental duration')
    def select_rental_duration(self):
        self.click_element(OrderPageLocators.input_rental_duration)
        self.click_element(OrderPageLocators.rental_duration_selector)

    @allure.step('Selecting the scooter color')
    def choose_scooter_color(self):
        self.click_element(OrderPageLocators.input_scooter_color)

    @allure.step('Adding a comment')
    def add_comment(self, comment):
        self.enter_text(OrderPageLocators.input_comment, comment)

    @allure.step('Clicking the "Order" button')
    def click_order_button(self):
        self.click_element(OrderPageLocators.button_order)

    @allure.description('Combining steps for filling scooter order form')
    def fill_scooter_order_form(self, comment):
        self.select_delivery_date()
        self.select_rental_duration()
        self.choose_scooter_color()
        self.add_comment(comment)
        self.click_order_button()

    @allure.step('Clicking the "Yes" button to confirm order')
    def confirm_order(self):
        self.click_element(OrderPageLocators.button_confirm_order)

    @allure.step('Retrieving the status of the order')
    def get_order_status(self):
        return self.get_text(OrderPageLocators.button_check_order_status)

    @allure.step('Clicking the scooter logo to return to main page')
    def go_to_main_page(self):
        self.click_element(OrderPageLocators.logo_scooter)

    @allure.step('Retrieving main page text')
    def get_main_page_text(self):
        return self.get_text(OrderPageLocators.main_page_text)
