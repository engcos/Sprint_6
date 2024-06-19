from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class BasePage:

    @allure.step('Launching Firefox and opening the given URL')
    def __init__(self, driver, url):
        self.driver = driver
        self.open_url(url)

    @allure.step('Opening the URL')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Formatting the locator with a provided number')
    def format_locator(self, locator, num):
        method, template = locator
        formatted_locator = template.format(num)
        return method, formatted_locator

    @allure.step('Waiting for the element to be visible and returning it')
    def wait_for_element(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Clicking on the element')
    def click_element(self, locator, timeout=30):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step('Entering text into the element')
    def enter_text(self, locator, text, timeout=30):
        element = self.wait_for_element(locator, timeout)
        element.send_keys(text)

    @allure.step('Retrieving text from the element')
    def get_text(self, locator, timeout=30):
        element = self.wait_for_element(locator, timeout)
        return element.text

    @allure.step('Scrolling to the element')
    def scroll_to(self, locator, timeout=30):
        element = self.wait_for_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Getting the current page URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Switching to the next browser tab')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
