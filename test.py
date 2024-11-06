import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestOpenCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("https://demo.opencart.com/")
        time.sleep(2)

        first_product = driver.find_element(By.CLASS_NAME, "product-layout")
        first_product.click()
        time.sleep(2)

        add_to_cart_button = driver.find_element(By.ID, "button-cart")
        add_to_cart_button.click()
        time.sleep(2)

        alert = driver.find_element(By.CLASS_NAME, "alert-success").text
        self.assertIn("Success: You have added", alert)

    def test_search_product(self):
        driver = self.driver
        driver.get("https://demo.opencart.com/")
        time.sleep(2)

        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("MacBook")
        search_box.submit()
        time.sleep(2)

        product_titles = driver.find_elements(By.CLASS_NAME, "product-thumb")
        self.assertGreater(len(product_titles), 0, "Товар не найден в результатах поиска")

    def test_navigation_to_login(self):
        driver = self.driver
        driver.get("https://demo.opencart.com/")
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, "My Account").click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(2)

        self.assertIn("account/login", driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()