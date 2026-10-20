import json
import os
from pathlib import Path
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import click, product, visible


def test_a4_session_capabilities(driver, evidence):
    assert driver.session_id
    caps = driver.capabilities
    assert caps["platformName"].lower() == "android"
    assert caps.get("automationName", caps.get("appium:automationName", "")).lower() == "uiautomator2"
    assert caps.get("udid", caps.get("appium:udid")) == os.environ["ANDROID_UDID"]
    Path(__file__).with_name("session-info.json").write_text(
        json.dumps({"session_id": driver.session_id, "capabilities": caps}, indent=2),
        encoding="utf-8",
    )
    visible(driver, "test-Username")
    evidence()


def test_a4_menu_all_items_and_back(logged_in, evidence):
    driver = logged_in
    session_id = driver.session_id
    click(driver, "test-Menu")
    click(driver, "test-ALL ITEMS")
    WebDriverWait(driver, 15).until(
        EC.invisibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-ALL ITEMS"))
    )
    product(driver, "Sauce Labs Backpack").find_element(
        AppiumBy.ACCESSIBILITY_ID, "test-Item title"
    ).click()
    visible(driver, "test-BACK TO PRODUCTS")
    driver.back()
    visible(driver, "test-PRODUCTS")
    assert driver.session_id == session_id
    evidence()


def test_a4_menu_logout(logged_in, evidence):
    click(logged_in, "test-Menu")
    click(logged_in, "test-LOGOUT")
    visible(logged_in, "test-Username")
    assert not logged_in.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    evidence()
