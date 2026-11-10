
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def logged_in_driver():

    # Open Chrome
    driver = webdriver.Chrome()

    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Enter login credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    time.sleep(2)

    # Click Login
    driver.find_element(By.ID, "login-button").click()

    # Wait for Products page
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    time.sleep(3)

    yield driver

    # Keep browser visible before closing
    time.sleep(3)
    driver.quit()


def get_product_names(driver):

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    return [product.text for product in products]


def test_all_products_displayed(logged_in_driver):

    driver = logged_in_driver

    products = get_product_names(driver)

    print("Products displayed:", products)

    assert len(products) == 6

    time.sleep(3)


def test_price_low_to_high(logged_in_driver):

    driver = logged_in_driver

    dropdown = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )

    dropdown.click()

    dropdown.find_element(
        By.CSS_SELECTOR, "option[value='lohi']"
    ).click()

    time.sleep(3)

    prices = driver.find_elements(
        By.CLASS_NAME, "inventory_item_price"
    )

    price_values = [
        float(price.text.replace("$", ""))
        for price in prices
    ]

    assert price_values == sorted(price_values)

    print("Low to high:", price_values)


def test_price_high_to_low(logged_in_driver):

    driver = logged_in_driver

    dropdown = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )

    dropdown.click()

    dropdown.find_element(
        By.CSS_SELECTOR, "option[value='hilo']"
    ).click()

    time.sleep(3)

    prices = driver.find_elements(
        By.CLASS_NAME, "inventory_item_price"
    )

    price_values = [
        float(price.text.replace("$", ""))
        for price in prices
    ]

    assert price_values == sorted(
        price_values, reverse=True
    )

    print("High to low:", price_values)


def test_name_a_to_z(logged_in_driver):

    driver = logged_in_driver

    dropdown = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )

    dropdown.click()

    dropdown.find_element(
        By.CSS_SELECTOR, "option[value='az']"
    ).click()

    time.sleep(3)

    names = get_product_names(driver)

    assert names == sorted(names, key=str.lower)

    print("Name A-Z:", names)


def test_name_z_to_a(logged_in_driver):

    driver = logged_in_driver

    dropdown = driver.find_element(
        By.CLASS_NAME, "product_sort_container"
    )

    dropdown.click()

    dropdown.find_element(
        By.CSS_SELECTOR, "option[value='za']"
    ).click()

    time.sleep(3)

    names = get_product_names(driver)

    assert names == sorted(
        names, key=str.lower, reverse=True
    )

    print("Name Z-A:", names)
