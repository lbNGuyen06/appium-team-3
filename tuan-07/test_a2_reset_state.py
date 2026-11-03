"""Tuần 7 – A2: Trạng thái ứng dụng & Menu → RESET APP STATE."""
import pytest
from appium.webdriver.common.appiumby import AppiumBy as By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from conftest import APP_PACKAGE
from helpers import badge, click, product, visible

# Giá trị trả về của query_app_state.
NOT_RUNNING = 1
RUNNING_IN_FOREGROUND = 4


def add_to_cart(driver, name):
    product(driver, name).find_element(By.ACCESSIBILITY_ID, "test-ADD TO CART").click()


def reset_app_state(driver):
    click(driver, "test-Menu")
    click(driver, "test-RESET APP STATE")
    # Menu đóng lại khi thao tác hoàn tất.
    WebDriverWait(driver, 15).until(
        EC.invisibility_of_element_located((By.ACCESSIBILITY_ID, "test-RESET APP STATE"))
    )


def test_a2_reset_app_state_clears_cart_badge(logged_in, evidence):
    driver = logged_in
    add_to_cart(driver, "Sauce Labs Backpack")
    add_to_cart(driver, "Sauce Labs Bike Light")
    badge(driver, 2)
    reset_app_state(driver)
    badge(driver, 0)
    click(driver, "test-Cart")
    visible(driver, "test-CONTINUE SHOPPING")
    assert driver.find_elements(By.ACCESSIBILITY_ID, "test-Item") == []
    evidence()


# Lỗi đã biết của app demo: sau RESET APP STATE nút sản phẩm có thể vẫn hiển thị REMOVE.
@pytest.mark.xfail(reason="Swag Labs demo: nút sản phẩm không đổi lại ADD TO CART sau reset", strict=False)
def test_a2_reset_app_state_restores_add_button(logged_in, evidence):
    driver = logged_in
    add_to_cart(driver, "Sauce Labs Backpack")
    badge(driver, 1)
    reset_app_state(driver)
    badge(driver, 0)
    button = WebDriverWait(driver, 10).until(
        lambda d: product(d, "Sauce Labs Backpack").find_element(
            By.ACCESSIBILITY_ID, "test-ADD TO CART")
    )
    assert button.is_displayed()
    evidence()


def test_a2_terminate_and_activate_app(logged_in, evidence):
    driver = logged_in
    add_to_cart(driver, "Sauce Labs Backpack")
    badge(driver, 1)

    assert driver.terminate_app(APP_PACKAGE)
    WebDriverWait(driver, 15).until(
        lambda d: d.query_app_state(APP_PACKAGE) == NOT_RUNNING
    )

    driver.activate_app(APP_PACKAGE)
    WebDriverWait(driver, 20).until(
        lambda d: d.query_app_state(APP_PACKAGE) == RUNNING_IN_FOREGROUND
    )
    # App không lưu phiên đăng nhập: mở lại phải quay về màn đăng nhập.
    visible(driver, "test-Username")
    assert not driver.find_elements(By.ACCESSIBILITY_ID, "test-PRODUCTS")
    evidence()


@pytest.mark.parametrize("no_reset", [True, False], ids=["noReset_true", "noReset_false"])
def test_a2_no_reset_capability(driver_factory, no_reset):
    driver = driver_factory(no_reset=no_reset)
    caps = driver.capabilities
    assert caps.get("noReset", caps.get("appium:noReset")) is no_reset
    visible(driver, "test-Username")
