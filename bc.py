import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open the Cookie Clicker game website
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    # Wait for the "English" button to appear and click it
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
    )
    language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
    language.click()

    # Wait for the cookie element to appear
    WebDriverWait(driver, 10).until(\
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )
    cookie = driver.find_element(By.ID, "bigCookie")

    while True:
        # Click the cookie to generate cookies
        cookie.click()

        # Get current number of cookies
        cookies_count = driver.find_element(By.ID, "cookies").text.split(" ")[0]
        cookies_count = int(cookies_count.replace(",", ""))

        # Iterate through product elements and buy the first affordable one
        for i in range(4):
            product_price = driver.find_element(By.ID, "productPrice" + str(i)).text.replace(",", "")

            if not product_price.isdigit():
                continue

            product_price = int(product_price)

            if cookies_count >= product_price:
                product = driver.find_element(By.ID, "product" + str(i))
                product.click()
                break

        # Wait briefly before the next click (optional, adjust as needed)
        time.sleep(0.1)

finally:
    # Close the browser window at the end
    driver.quit()
