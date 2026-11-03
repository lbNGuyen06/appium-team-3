"""Hàm dùng chung tuần 6, chưa tổ chức Page Object (dành cho tuần 11)."""
from decimal import Decimal

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

CATALOG = {
    "Sauce Labs Backpack": Decimal("29.99"),
    "Sauce Labs Bike Light": Decimal("9.99"),
    "Sauce Labs Bolt T-Shirt": Decimal("15.99"),
    "Sauce Labs Fleece Jacket": Decimal("49.99"),
    "Sauce Labs Onesie": Decimal("7.99"),
    "Test.allTheThings() T-Shirt (Red)": Decimal("15.99"),
}


def visible(driver, name, timeout=20):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, name))
    )


def click(driver, name):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, name))
    ).click()


def login(driver):
    def fill(name, value):
        # Giao diện React Native có thể dựng lại phần tử khi app vừa mở.
        def enter(d):
            field = d.find_element(AppiumBy.ACCESSIBILITY_ID, name)
            if not field.is_displayed():
                return False
            field.clear()
            field.send_keys(value)
            return True
        WebDriverWait(driver, 25, ignored_exceptions=(
            NoSuchElementException, StaleElementReferenceException,
        )).until(enter)
    fill("test-Username", "standard_user")
    fill("test-Password", "secret_sauce")
    if driver.is_keyboard_shown():
        driver.hide_keyboard()
    click(driver, "test-LOGIN")
    visible(driver, "test-PRODUCTS")


def scroll(driver):
    # Chọn đúng phần tử cuộn thay vì vùng tọa độ có thể chạm khoảng trống.
    container = visible(driver, "test-PRODUCTS")
    return driver.execute_script("mobile: scrollGesture", {
        "elementId": container.id,
        "direction": "down", "percent": 0.55,
    })


def collect_catalog(driver):
    """Đọc theo thứ tự, loại trùng do hai lần cuộn chồng nhau."""
    products = {}
    for _ in range(20):
        for item in driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Item"):
            try:
                name = item.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Item title").text
                price = item.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Price").text
            except NoSuchElementException:
                # Thẻ ở mép màn hình chưa có đủ tên/giá sẽ được đọc ở lần cuộn sau.
                continue
            products[name] = Decimal(price.replace("$", "").strip())
        if not scroll(driver):
            # Đọc lại viewport cuối sau thao tác cuộn cuối.
            for item in driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Item"):
                names = item.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Item title")
                prices = item.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Price")
                if names and prices:
                    products[names[0].text] = Decimal(prices[0].text.replace("$", "").strip())
            break
    else:
        raise AssertionError("Chưa đến cuối danh sách sau 20 lần cuộn")
    # Dữ liệu chuẩn Swag Labs standard_user có 6 sản phẩm; không chấp nhận chỉ 1.
    assert products == CATALOG, f"Thiếu/sai sản phẩm: {products}"
    return products


def product(driver, title):
    return driver.find_element(
        AppiumBy.XPATH,
        f'//*[@content-desc="test-Item"][.//*[@text="{title}"]]',
    )


def badge(driver, expected):
    def matches(d):
        texts = visible(d, "test-Cart").find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        numbers = [e.text for e in texts if e.text.isdigit()]
        return numbers == ([str(expected)] if expected else [])
    WebDriverWait(driver, 15).until(matches, f"Huy hiệu giỏ không bằng {expected}")


def sort_by(driver, label):
    click(driver, "test-Modal Selector Button")
    locator = (AppiumBy.XPATH, f'//*[@text="{label}"]')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(locator)).click()
    WebDriverWait(driver, 15).until(EC.invisibility_of_element_located(locator))
    visible(driver, "test-Item")
