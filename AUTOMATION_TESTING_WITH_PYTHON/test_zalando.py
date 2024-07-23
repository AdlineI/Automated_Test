import pytest 
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CHROME_DRIVER_PATH = "/Applications/chromedriver-mac-x64 2/chromedriver"

def setup_module(module):
    global driver
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.zalando.dk")

def teardown_module(module):
    driver.quit()

def test_presence_of_elements():
    wait = WebDriverWait(driver, 10)

    shopping_cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".z-navicat-header_navToolItem-bag")))
    print("Shopping cart found: ", shopping_cart is not None)
    assert shopping_cart is not None

     
   




    if __name__ == "__main__":
        pytest.main()
