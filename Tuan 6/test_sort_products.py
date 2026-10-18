from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Cau hinh Appium
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554"
options.app_package = "com.swaglabsmobileapp"
options.app_activity = ".SplashActivity"
options.no_reset = True

driver = None

try:
    # Ket noi voi Appium Server
    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    # Implicit wait: moi lan find_element(s) se cho toi da 2 giay
    driver.implicitly_wait(2)

    # Explicit wait: cho toi da 20 giay cho tung dieu kien cu the
    wait = WebDriverWait(driver, 20)

    # Dang nhap vao Swag Labs
    username = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Username")
        )
    )
    username.send_keys("standard_user")

    password = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Password")
        )
    )
    password.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "test-LOGIN")
        )
    )
    login_button.click()

    # Cho man hinh PRODUCTS hien thi
    wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
        )
    )

    # Mo danh sach lua chon sap xep
    sort_button = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "test-Modal Selector Button")
        )
    )
    sort_button.click()

    # Chon sap xep gia tu thap den cao
    price_low_high = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.XPATH, '//*[@text="Price (low to high)"]')
        )
    )
    price_low_high.click()

    # Cho menu sort dong va danh sach san pham hien thi lai
    wait.until(
        EC.invisibility_of_element_located(
            (AppiumBy.XPATH, '//*[@text="Price (low to high)"]')
        )
    )
    wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "test-Item")
        )
    )

    def lay_san_pham_hien_thi():
        """Tra ve dict {ten san pham: gia} cua cac san pham dang hien tren man hinh"""
        ket_qua = {}
        for item in driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "test-Item"):
            try:
                ten = item.find_element(
                    AppiumBy.ACCESSIBILITY_ID, "test-Item title"
                ).text
                gia = item.find_element(
                    AppiumBy.ACCESSIBILITY_ID, "test-Price"
                ).text
                ket_qua[ten] = float(gia.replace("$", "").strip())
            except Exception:
                # San pham bi che mot phan hoac vua bi cuon di -> bo qua
                continue
        return ket_qua

    # Lay san pham theo thu tu hien thi, vua doc vua cuon xuong
    san_pham = {}

    # Gioi han 20 lan cuon de tranh lap vo han
    for _ in range(20):
        san_pham.update(lay_san_pham_hien_thi())

        # Cuon danh sach san pham xuong
        can_scroll = driver.execute_script(
            "mobile: scrollGesture",
            {
                "left": 50,
                "top": 200,
                "width": 300,
                "height": 500,
                "direction": "down",
                "percent": 0.3
            }
        )

        # Het danh sach (khong cuon duoc nua) thi dung
        if not can_scroll:
            break

    # Doc them lan cuoi vi lan cuon cuoi co the vua hien them san pham
    san_pham.update(lay_san_pham_hien_thi())

    prices = list(san_pham.values())
    print("San pham thu duoc:", san_pham)
    print("Danh sach gia thu duoc:", prices)

    # Kiem tra da lay duoc it nhat 1 san pham (khong can biet truoc so luong)
    assert len(prices) > 0, "Khong lay duoc san pham nao"
    print("Tong so san pham:", len(prices))

    # Kiem tra gia da tang dan
    assert prices == sorted(prices), (
        f"Gia san pham chua tang dan: {prices}"
    )

    print("PASS: Sap xep gia tu thap den cao thanh cong")

except TimeoutException as e:
    print("FAIL: Het thoi gian cho phan tu")
    print("Chi tiet loi:", e)

except Exception as e:
    print("FAIL: Kiem thu sap xep san pham")
    print("Chi tiet loi:", e)

finally:
    if driver:
        driver.quit()