from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Cau hinh Appium
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554"
options.app_package = "com.swaglabsmobileapp"
options.app_activity = ".SplashActivity"


# Mo ung dung
def mo_ung_dung():
    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    return driver


# Ham lay noi dung thong bao loi
def lay_thong_bao_loi(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (
                AppiumBy.XPATH,
                '//*[@content-desc="test-Error message"]//android.widget.TextView'
            )
        )
    )


# Test 1: Dang nhap thanh cong
def test_dang_nhap_thanh_cong():
    driver = mo_ung_dung()

    try:
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Username"
        ).send_keys("standard_user")

        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Password"
        ).send_keys("secret_sauce")

        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
        ).click()

        # Cho toi da 10 giay de man hinh Products hien ra
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
            )
        )

        print("PASS TC01: Dang nhap thanh cong")

    except Exception as e:
        print("FAIL TC01: Dang nhap thanh cong")
        print("Chi tiet loi:", e)
        raise

    finally:
        driver.quit()


# Test 2: Tai khoan bi khoa
def test_tai_khoan_bi_khoa():
    driver = mo_ung_dung()

    try:
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Username"
        ).send_keys("locked_out_user")

        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Password"
        ).send_keys("secret_sauce")

        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
        ).click()

        # Lay TextView nam ben trong phan tu thong bao
        thong_bao = lay_thong_bao_loi(driver)
        noi_dung = thong_bao.text

        print("Noi dung thong bao TC02:", noi_dung)

        assert "locked out" in noi_dung.lower(), (
            "Thong bao khong dung: " + repr(noi_dung)
        )

        print("PASS TC02: Tai khoan bi khoa")

    except Exception as e:
        print("FAIL TC02: Tai khoan bi khoa")
        print("Chi tiet loi:", e)
        raise

    finally:
        driver.quit()


# Test 3: Bo trong mat khau
def test_bo_trong_mat_khau():
    driver = mo_ung_dung()

    try:
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-Username"
        ).send_keys("standard_user")

        # Khong nhap mat khau
        driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, "test-LOGIN"
        ).click()

        # Lay noi dung thong bao loi
        thong_bao = lay_thong_bao_loi(driver)
        noi_dung = thong_bao.text

        print("Noi dung thong bao TC03:", noi_dung)

        assert "password is required" in noi_dung.lower(), (
            "Thong bao khong dung: " + repr(noi_dung)
        )

        print("PASS TC03: Password is required")

    except Exception as e:
        print("FAIL TC03: Bo trong mat khau")
        print("Chi tiet loi:", e)
        raise

    finally:
        driver.quit()


# Chay lan luot 3 test case
if __name__ == "__main__":
    test_dang_nhap_thanh_cong()
    test_tai_khoan_bi_khoa()
    test_bo_trong_mat_khau()
