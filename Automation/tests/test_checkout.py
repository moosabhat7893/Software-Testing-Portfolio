
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def checkout_driver():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    # Login
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Wait for Products page
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    time.sleep(2)

    # Add Backpack
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()

    time.sleep(2)

    # Open cart
    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    wait.until(
        EC.url_contains("cart.html")
    )

    time.sleep(2)

    # Click Checkout
    driver.find_element(By.ID, "checkout").click()

    # Wait for checkout information form
    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "first-name")
        )
    )

    time.sleep(2)

    yield driver

    time.sleep(3)
    driver.quit()


def test_checkout_page_displayed(checkout_driver):

    driver = checkout_driver

    assert "checkout-step-one.html" in driver.current_url
    assert driver.find_element(By.ID, "first-name").is_displayed()

    print("Checkout information page displayed")


def test_empty_first_name(checkout_driver):

    driver = checkout_driver

    driver.find_element(By.ID, "last-name").send_keys("Bhat")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    driver.find_element(By.ID, "continue").click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[data-test='error']")
        )
    ).text

    assert "First Name is required" in error

    print("Empty first name validation passed")


def test_empty_last_name(checkout_driver):

    driver = checkout_driver

    driver.find_element(By.ID, "first-name").send_keys("Moosa")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    driver.find_element(By.ID, "continue").click()

    error = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    ).text

    assert "Last Name is required" in error

    print("Empty last name validation passed")


def test_empty_postal_code(checkout_driver):

    driver = checkout_driver

    driver.find_element(By.ID, "first-name").send_keys("Moosa")
    driver.find_element(By.ID, "last-name").send_keys("Bhat")

    driver.find_element(By.ID, "continue").click()

    error = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    ).text

    assert "Postal Code is required" in error

    print("Empty postal code validation passed")


def test_valid_customer_information(checkout_driver):

    driver = checkout_driver

    driver.find_element(By.ID, "first-name").send_keys("Moosa")
    driver.find_element(By.ID, "last-name").send_keys("Bhat")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    time.sleep(2)

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )

    assert "checkout-step-two.html" in driver.current_url

    print("Valid customer information accepted")


def test_order_overview_and_price(checkout_driver):

    driver = checkout_driver

    driver.find_element(By.ID, "first-name").send_keys("Moosa")
    driver.find_element(By.ID, "last-name").send_keys("Bhat")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )

    time.sleep(3)

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    names = [product.text for product in products]

    assert "Sauce Labs Backpack" in names

    subtotal = driver.find_element(
        By.CLASS_NAME, "summary_subtotal_label"
    ).text

    tax = driver.find_element(
        By.CLASS_NAME, "summary_tax_label"
    ).text

    total = driver.find_element(
        By.CLASS_NAME, "summary_total_label"
    ).text

    assert subtotal == "Item total: $29.99"
    assert tax == "Tax: $2.40"
    assert total == "Total: $32.39"

    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Total:", total)


def test_successful_order_completion(checkout_driver):

    driver = checkout_driver

    driver.find_element(By.ID, "first-name").send_keys("Moosa")
    driver.find_element(By.ID, "last-name").send_keys("Bhat")
    driver.find_element(By.ID, "postal-code").send_keys("560001")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two.html")
    )

    time.sleep(3)

    driver.find_element(By.ID, "finish").click()

    confirmation = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "complete-header")
        )
    ).text

    assert confirmation == "Thank you for your order!"

    print("Order completed successfully")
