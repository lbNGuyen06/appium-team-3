"""Bài mẫu để học: mở Swag Labs và kiểm tra ô tên đăng nhập.

Mỗi thành viên cần tự gõ lại, hiểu code và viết chú thích bằng lời của mình.
"""

import os

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_smoke():
    # Appium dùng UiAutomator2 để điều khiển ứng dụng Android.
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.udid = os.environ["ANDROID_UDID"]
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    # Đưa ứng dụng demo về trạng thái ban đầu để thấy màn đăng nhập.
    options.no_reset = False

    # Code Python gửi lệnh đến Appium server đang chạy trên máy tính.
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    try:
        # Chờ tối đa 20 giây cho ô tên đăng nhập xuất hiện.
        username = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-Username")
            )
        )
        assert username.is_displayed(), "Không thấy ô tên đăng nhập"
    finally:
        # Luôn đóng phiên Appium, kể cả khi kiểm thử thất bại.
        driver.quit()
