
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():

    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("inventory.html")
        )

        assert "inventory.html" in driver.current_url

        time.sleep(3)

    finally:
        driver.quit()


@pytest.mark.parametrize("username, password, expected_error", [
    ("wrong_user", "secret_sauce",
     "Epic sadface: Username and password do not match any user in this service"),

    ("standard_user", "wrong_password",
     "Epic sadface: Username and password do not match any user in this service"),

    ("", "",
     "Epic sadface: Username is required"),

    ("locked_out_user", "secret_sauce",
     "Epic sadface: Sorry, this user has been locked out.")
])


def test_invalid_login(username, password, expected_error):

    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        error_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "[data-test='error']")
            )
        )

        actual_error = error_element.text

        assert actual_error == expected_error

        time.sleep(2)

    finally:
        driver.quit()
