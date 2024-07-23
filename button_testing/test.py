from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
sum1 = driver.find_element(By.NAME, 'sum1')
sum2 = driver.find_element(By.NAME, 'sum2')

sum1.send_keys('20')
sum2.send_keys('20')

gettotal = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
gettotal.click()

try:
    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'displayvalue'))
    )
    print("Result is:", result.text)
except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
