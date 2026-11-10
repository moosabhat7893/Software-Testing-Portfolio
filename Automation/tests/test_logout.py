
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def logged_in_driver():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    # Login
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))

    time.sleep(2)

    yield driver

    time.sleep(3)
    driver.quit()


def logout(driver):

    # Open navigation menu
    driver.find_element(By.ID, "react-burger-menu-btn").click()

    time.sleep(2)

    # Click Logout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "logout_sidebar_link")
        )
    ).click()

    time.sleep(3)


def test_logout_option_visible(logged_in_driver):

    driver = logged_in_driver

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    time.sleep(2)

    logout_button = driver.find_element(
        By.ID, "logout_sidebar_link"
    )

    assert logout_button.is_displayed()

    print("Logout option is visible")


def test_successful_logout(logged_in_driver):

    driver = logged_in_driver

    logout(driver)

    login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "login-button")
        )
    )

    assert login_button.is_displayed()

    print("Logout successful")


def test_protected_page_after_logout(logged_in_driver):

    driver = logged_in_driver

    logout(driver)

    # Try opening protected inventory page
    driver.get("https://www.saucedemo.com/inventory.html")

    time.sleep(3)

    page_text = driver.find_element(
        By.TAG_NAME, "body"
    ).text

    assert "You can only access" in page_text

    print("Protected page access blocked")


def test_browser_back_after_logout(logged_in_driver):

    driver = logged_in_driver

    logout(driver)

    # Press browser Back
    driver.back()

    time.sleep(3)

    # Verify user is not restored to Products page
    assert "inventory.html" not in driver.current_url

    print("Browser Back did not restore authenticated session")


def test_login_again_after_logout(logged_in_driver):

    driver = logged_in_driver

    logout(driver)

    # Login again
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )

    assert "inventory.html" in driver.current_url

    print("Login after logout successful")
