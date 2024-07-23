from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")

my_element = driver.find_element(By.ID, 'cricle-btn')
my_element.click()

try:
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'percenttext'),  
            '100%' 
        )
    )
    print("Download completed successfully!")
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
