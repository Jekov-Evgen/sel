from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_to_cart():
    driver.get("https://demo.opencart.com/")
    time.sleep(2)

    first_product = driver.find_element(By.CLASS_NAME, "product-layout")
    first_product.click()
    time.sleep(2)

    add_to_cart_button = driver.find_element(By.ID, "button-cart")
    add_to_cart_button.click()
    time.sleep(2)

    alert = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Success: You have added" in alert

    print("Тест добавления в корзину прошел успешно.")

test_add_to_cart()

driver.quit()