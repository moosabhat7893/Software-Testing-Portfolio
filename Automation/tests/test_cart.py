
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def logged_in_driver():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    time.sleep(2)

    yield driver

    time.sleep(3)
    driver.quit()


def add_product(driver, product_name):

    product = driver.find_element(
        By.XPATH,
        f"//div[contains(@class,'inventory_item')][.//div[text()='{product_name}']]"
    )

    product.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)


def open_cart(driver):

    driver.find_element(
        By.CLASS_NAME, "shopping_cart_link"
    ).click()

    time.sleep(2)


def test_add_one_product(logged_in_driver):

    driver = logged_in_driver

    add_product(driver, "Sauce Labs Backpack")

    badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert badge.text == "1"

    print("One product added successfully")


def test_add_multiple_products(logged_in_driver):

    driver = logged_in_driver

    add_product(driver, "Sauce Labs Backpack")
    add_product(driver, "Sauce Labs Bike Light")

    badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert badge.text == "2"

    print("Two products added successfully")


def test_view_cart(logged_in_driver):

    driver = logged_in_driver

    add_product(driver, "Sauce Labs Backpack")
    add_product(driver, "Sauce Labs Bike Light")

    open_cart(driver)

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    names = [product.text for product in products]

    assert "Sauce Labs Backpack" in names
    assert "Sauce Labs Bike Light" in names

    print("Cart products:", names)


def test_remove_one_product(logged_in_driver):

    driver = logged_in_driver

    add_product(driver, "Sauce Labs Backpack")
    add_product(driver, "Sauce Labs Bike Light")

    open_cart(driver)

    driver.find_element(
        By.ID, "remove-sauce-labs-bike-light"
    ).click()

    time.sleep(2)

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    names = [product.text for product in products]

    assert names == ["Sauce Labs Backpack"]

    print("One product removed successfully")


def test_remove_all_products(logged_in_driver):

    driver = logged_in_driver

    add_product(driver, "Sauce Labs Backpack")

    open_cart(driver)

    driver.find_element(
        By.ID, "remove-sauce-labs-backpack"
    ).click()

    time.sleep(2)

    products = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )

    assert len(products) == 0

    print("Cart is empty")


def test_continue_shopping(logged_in_driver):

    driver = logged_in_driver

    open_cart(driver)

    driver.find_element(
        By.ID, "continue-shopping"
    ).click()

    time.sleep(2)

    assert "inventory.html" in driver.current_url

    print("Returned to Products page")


def test_cart_persistence(logged_in_driver):

    driver = logged_in_driver

    add_product(driver, "Sauce Labs Backpack")
    add_product(driver, "Sauce Labs Bike Light")

    open_cart(driver)

    driver.find_element(
        By.ID, "continue-shopping"
    ).click()

    time.sleep(2)

    open_cart(driver)

    products = driver.find_elements(
        By.CLASS_NAME, "inventory_item_name"
    )

    names = [product.text for product in products]

    assert "Sauce Labs Backpack" in names
    assert "Sauce Labs Bike Light" in names

    print("Cart items persisted successfully")
