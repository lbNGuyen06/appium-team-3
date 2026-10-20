import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from helpers import badge, click, product, visible


def test_a2_add_remove(logged_in, evidence):
    driver = logged_in
    for count, name in enumerate(["Sauce Labs Backpack", "Sauce Labs Bike Light"], 1):
        product(driver, name).find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-ADD TO CART").click()
        badge(driver, count)
    click(driver, "test-Cart")
    WebDriverWait(driver, 15).until(
        lambda d: len(d.find_elements(
            AppiumBy.ACCESSIBILITY_ID, "test-Item")) == 2
    )
    product(driver, "Sauce Labs Backpack").find_element(
        AppiumBy.ACCESSIBILITY_ID, "test-REMOVE").click()
    badge(driver, 1)
    items = driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Item")
    assert len(items) == 1
    assert items[0].find_element(
        AppiumBy.XPATH, './/*[@text="Sauce Labs Bike Light"]').is_displayed()
    evidence()


def test_a2_drag_to_cart(logged_in, evidence):
    driver = logged_in
    handle = product(driver, "Sauce Labs Backpack").find_element(
        AppiumBy.ACCESSIBILITY_ID, "test-Drag Handle"
    )
    target = visible(driver, "test-Cart drop zone").rect
    # Android native dùng gesture cảm ứng thay vì chuỗi thao tác chuột desktop.
    driver.execute_script("mobile: dragGesture", {
        "elementId": handle.id,
        "endX": int(target["x"] + target["width"] / 2),
        "endY": int(target["y"] + target["height"] / 2),
        "speed": 600,
    })
    badge(driver, 1)
    click(driver, "test-Cart")
    cart_content = visible(driver, "test-Cart Content")

    items = WebDriverWait(driver, 15).until(
        lambda _: cart_content.find_elements(
            AppiumBy.ACCESSIBILITY_ID, "test-Item"
        )
    )
    assert len(items) == 1

    backpack_title = items[0].find_element(
        AppiumBy.XPATH, './/*[@text="Sauce Labs Backpack"]'
    )
    assert backpack_title.is_displayed()
    evidence()


def test_a2_empty_cart_exception(logged_in, evidence):
    click(logged_in, "test-Cart")
    visible(logged_in, "test-CONTINUE SHOPPING")
    assert logged_in.find_elements(
        AppiumBy.ACCESSIBILITY_ID, "test-Item") == []
    with pytest.raises(NoSuchElementException):
        logged_in.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Item")
    evidence()
