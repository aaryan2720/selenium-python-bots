import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

   
    def select_place_to_go(self, place_to_go):
        try:
            search_field = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.ID, ':re:'))
            )
            search_field.clear()
            search_field.send_keys(place_to_go)
            first_result = WebDriverWait(self, 10).until(
             EC.element_to_be_clickable((By.ID, 'autocomplete-results'))
         )
            first_result.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Search field or first result for place '{place_to_go}' not found. Error: {e}")

    def select_dates(self, check_in_date, check_out_date):
        try:
            check_in_element = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'td[data-date="2021-06-29"]'))
            )
            check_in_element.click()

            check_out_element = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'td[data-date="2021-06-30"]'))
            )
            check_out_element.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Check-in or check-out date elements not found. Error: {e}")

    def select_adults(self, count=1):
        try:
            selection_element = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.ID, 'xp__guests__toggle'))
            )
            selection_element.click()

            while True:
                decrease_adults_element = WebDriverWait(self, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'))
                )
                decrease_adults_element.click()

                adults_value_element = self.find_element(By.ID, 'group_adults')
                adults_value = adults_value_element.get_attribute('value')

                if int(adults_value) == 1:
                    break

            increase_button_element = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'))
            )

            for _ in range(count - 1):
                increase_button_element.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Guest selection elements not found. Error: {e}")

    def click_search(self):
        try:
            search_button = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
            )
            search_button.click()
        except (NoSuchElementException, TimeoutException) as e:
            print("Search button not found. Error: {e}")

