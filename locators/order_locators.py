from selenium.webdriver.common.by import By

class OrderPageLocators:
    input_name = (By.XPATH, ".//*[@placeholder='* Имя']")
    input_surname = (By.XPATH, ".//*[@placeholder='* Фамилия']")
    input_address = (By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']")
    input_metro_station = (By.XPATH, ".//*[@placeholder='* Станция метро']")
    button_select_metro_station = (By.XPATH, ".//button[@value='3']")
    input_phone_number = (By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, ".//button[text()='Далее']")
    rental_info_text = (By.XPATH, ".//*[text()='Про аренду']")

    input_delivery_date = (By.XPATH, ".//*[@placeholder='* Когда привезти самокат']")
    date_selector = (By.XPATH, ".//*[@aria-label='Choose воскресенье, 16-е июня 2024 г.']")
    input_rental_duration = (By.XPATH, ".//*[text()='* Срок аренды']")
    rental_duration_selector = (By.XPATH, ".//*[@class='Dropdown-menu']/div[text()='трое суток']")
    input_scooter_color = (By.XPATH, ".//input[@id='black']")
    input_comment = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
    button_order = (By.XPATH, ".//button[contains(@class, 'Button_Middle')][text()='Заказать']")

    order_confirmation_text = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    button_confirm_order = (By.XPATH, ".//button[text()='Да']")

    button_check_order_status = (By.XPATH, ".//button[text()='Посмотреть статус']")

    logo_scooter = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    main_page_text = (By.XPATH, ".//*[text()='Привезём его прямо к вашей двери,']")
