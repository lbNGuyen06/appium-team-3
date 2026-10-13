"""Ba trường hợp đăng nhập tuần 5; xem testcases.md trước khi đọc code."""

import os
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    # Mỗi test mở phiên mới và đặt lại app để không phụ thuộc test trước.
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.udid = os.environ["ANDROID_UDID"]
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = False
    session = webdriver.Remote("http://127.0.0.1:4723", options=options)
    try:
        yield session
    finally:
        session.quit()


def visible(driver, accessibility_id):
    # Chờ phần tử hiển thị thay vì dừng cứng bằng time.sleep.
    return WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
    )


def login(driver, username, password):
    visible(driver, "test-Username").send_keys(username)
    password_input = visible(driver, "test-Password")
    password_input.clear()
    if password:
        password_input.send_keys(password)
    # Đóng bàn phím nếu đang hiện để không che nút LOGIN.
    if driver.is_keyboard_shown():
        driver.hide_keyboard()
    visible(driver, "test-LOGIN").click()


def save_evidence(driver, name):
    folder = Path(__file__).parent / "anh"
    folder.mkdir(exist_ok=True)
    assert driver.save_screenshot(str(folder / name)), "Không lưu được ảnh minh chứng"


def assert_login_error(driver, expected):
    error = visible(driver, "test-Error message")
    # Nhãn lỗi nằm trong TextView con của khung thông báo Android.
    messages = [error.text] + [
        element.text for element in error.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    ]
    assert expected in messages, f"Thông báo thực tế: {messages!r}"
    assert visible(driver, "test-LOGIN").is_displayed()
    assert not driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")


def test_login_success(driver):
    login(driver, "standard_user", "secret_sauce")
    assert visible(driver, "test-PRODUCTS").is_displayed()
    save_evidence(driver, "TC01-dang-nhap-thanh-cong.png")


def test_login_locked_user(driver):
    login(driver, "locked_out_user", "secret_sauce")
    assert_login_error(driver, "Sorry, this user has been locked out.")
    save_evidence(driver, "TC02-tai-khoan-bi-khoa.png")


def test_login_empty_password(driver):
    login(driver, "standard_user", "")
    assert_login_error(driver, "Password is required")
    save_evidence(driver, "TC03-bo-trong-mat-khau.png")
