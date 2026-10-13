
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


# Khai báo cấu hình để Appium kết nối với máy ảo Android
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554"
options.app_package = "com.swaglabsmobileapp"
options.app_activity = ".SplashActivity"

# Kết nối đến Appium Server và mở ứng dụng
driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

try:
    # Tìm ô Username bằng accessibility id đã xác nhận từ giao diện
    username = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "test-Username"
    )

    # Kiểm tra ô Username có hiển thị hay không
    assert username.is_displayed(), "Ô Username không hiển thị"

    print("PASS: Ô Username tồn tại và đang hiển thị")

finally:
    # Đóng phiên kiểm thử sau khi hoàn thành
    driver.quit()