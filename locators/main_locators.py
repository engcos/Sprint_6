from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button_header = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    order_button_footer = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")

    scooter_image = (By.XPATH, ".//*[@alt='Scooter blueprint']")
    question_locator = (By.XPATH, ".//div[@id='accordion__heading-{}']")
    answer_locator = (By.XPATH, ".//div[@id='accordion__panel-{}']")
    specific_question_8 = (By.XPATH, ".//div[@id='accordion__heading-7']")