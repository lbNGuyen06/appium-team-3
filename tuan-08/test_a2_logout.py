"""Tuần 8 – A2: Menu → LOGOUT và các ngoại lệ Selenium/Appium."""
import pytest
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import click, login, visible


def logout(driver):
    click(driver, "test-Menu")
    click(driver, "test-LOGOUT")
    visible(driver, "test-Username")


def test_a2_logout_returns_to_login(logged_in, evidence):
    logout(logged_in)
    visible(logged_in, "test-Password")
    visible(logged_in, "test-LOGIN")
    evidence()


def test_a2_no_such_element_after_logout(logged_in, evidence):
    logout(logged_in)
    # find_element không chờ (implicit wait = 0) nên ném ngay NoSuchElementException.
    with pytest.raises(NoSuchElementException):
        logged_in.find_element(By.ACCESSIBILITY_ID, "test-PRODUCTS")
    assert logged_in.find_elements(By.ACCESSIBILITY_ID, "test-Cart") == []
    evidence()


def test_a2_timeout_waiting_products_after_logout(logged_in, evidence):
    logout(logged_in)
    with pytest.raises(TimeoutException):
        WebDriverWait(logged_in, 3).until(
            EC.visibility_of_element_located((By.ACCESSIBILITY_ID, "test-PRODUCTS"))
        )
    evidence()


def test_a2_stale_element_after_logout(logged_in, evidence):
    cart = visible(logged_in, "test-Cart")
    assert cart.is_displayed()
    logout(logged_in)
    # Phần tử cũ không còn trên màn hình mới: Appium báo stale (hoặc không tìm thấy).
    with pytest.raises((StaleElementReferenceException, NoSuchElementException)):
        cart.is_displayed()
    evidence()


def test_a2_login_again_after_logout(logged_in, evidence):
    logout(logged_in)
    login(logged_in)
    assert visible(logged_in, "test-PRODUCTS").is_displayed()
    evidence()


def test_a2_screenshot_hook_on_failure(logged_in, evidence):
    """Chụp tay bằng save_screenshot; hook trong conftest tự chụp khi test lỗi."""
    logout(logged_in)
    shot = evidence("login-screen")
    assert shot.exists() and shot.stat().st_size > 0
