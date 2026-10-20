from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers import collect_catalog


def test_a3_scroll_all_products(logged_in, evidence):
    products = collect_catalog(logged_in)
    assert len(products) == 6
    evidence("bottom-screen")


def test_a3_uiscrollable_and_element_screenshot(logged_in, evidence):
    # Bước 1: Cuộn đến sản phẩm bằng UiScrollable (yêu cầu bài).
    logged_in.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).setMaxSearchSwipes(15)'
        '.scrollIntoView(new UiSelector().text("Sauce Labs Onesie"))',
    )
    # Bước 2: Tìm lại chính xác phần tử bằng XPath sau khi cuộn.
    # UiScrollable trả về element reference có thể có .text rỗng trên React Native
    # (phần tử cha hoặc tham chiếu cũ); tìm lại bằng explicit wait đảm bảo ổn định.
    target = WebDriverWait(logged_in, 10).until(
        EC.visibility_of_element_located(
            (AppiumBy.XPATH, '//*[@text="Sauce Labs Onesie"]')
        )
    )
    # Bước 3: Xác nhận nội dung và trạng thái hiển thị.
    assert target.text == "Sauce Labs Onesie"
    assert target.is_displayed()
    # Bước 4: Chụp ảnh riêng phần tử và toàn màn hình.
    evidence("element", element=target)
    evidence("full-screen")
