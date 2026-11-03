"""Mỗi test có phiên mới và minh chứng riêng; không chạy Appium khi import."""
import os
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from helpers import login

ROOT = Path(__file__).parent


@pytest.fixture
def driver(request):
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Android Emulator",
        "appium:udid": os.environ["ANDROID_UDID"],
        "appium:appPackage": "com.swaglabsmobileapp",
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "appium:noReset": False,
    })
    session = webdriver.Remote(os.getenv("APPIUM_URL", "http://127.0.0.1:4723"), options=options)
    # Không trộn implicit wait dương với explicit wait.
    session.implicitly_wait(0)
    try:
        # Giảm chờ idle mặc định 10s; vẫn dùng explicit wait cho trạng thái UI.
        session.update_settings({"waitForIdleTimeout": 1000})
        yield session
    finally:
        session.quit()


@pytest.fixture
def logged_in(driver):
    login(driver)
    return driver


@pytest.fixture
def evidence(request, driver):
    folder = ROOT / "anh"
    folder.mkdir(exist_ok=True)

    def save(suffix="result", element=None):
        path = folder / f"{request.node.name}-{suffix}.png"
        ok = element.screenshot(str(path)) if element else driver.save_screenshot(str(path))
        assert ok and path.stat().st_size > 0, f"Không lưu được {path}"
        return path
    return save


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed and "driver" in item.funcargs:
        folder = ROOT / "debug"
        folder.mkdir(exist_ok=True)
        driver = item.funcargs["driver"]
        try:
            driver.save_screenshot(str(folder / f"{item.name}.png"))
            (folder / f"{item.name}.xml").write_text(driver.page_source, encoding="utf-8")
        except Exception as exc:
            # Lỗi lưu debug không được che nguyên nhân test thất bại.
            report.sections.append(("Không lưu được debug", str(exc)))
