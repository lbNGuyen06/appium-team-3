"""Tuần 7 – A2: phiên Appium tạo theo yêu cầu để thử capability noReset."""
import os
from pathlib import Path

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from helpers import login

ROOT = Path(__file__).parent
APP_PACKAGE = "com.swaglabsmobileapp"


def new_session(no_reset):
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Android Emulator",
        "appium:udid": os.environ["ANDROID_UDID"],
        "appium:appPackage": APP_PACKAGE,
        "appium:appActivity": "com.swaglabsmobileapp.MainActivity",
        "appium:noReset": no_reset,
        # Máy ảo chậm có thể làm lệnh adb vượt mặc định 20s.
        "appium:adbExecTimeout": 60000,
    })
    session = webdriver.Remote(os.getenv("APPIUM_URL", "http://127.0.0.1:4723"), options=options)
    # Không trộn implicit wait dương với explicit wait.
    session.implicitly_wait(0)
    session.update_settings({"waitForIdleTimeout": 1000})
    return session


@pytest.fixture
def driver_factory(request):
    sessions = []

    def create(no_reset=False):
        session = new_session(no_reset)
        sessions.append(session)
        # pytest_runtest_makereport đọc phiên gần nhất để lưu debug.
        request.node.debug_driver = session
        return session

    yield create
    for session in sessions:
        try:
            session.quit()
        except Exception:
            pass


@pytest.fixture
def driver(driver_factory):
    return driver_factory(no_reset=False)


@pytest.fixture
def logged_in(driver):
    login(driver)
    return driver


@pytest.fixture
def evidence(request, driver):
    folder = ROOT / "anh"
    folder.mkdir(exist_ok=True)

    def save(suffix="result", element=None):
        safe = request.node.name.replace("[", "_").replace("]", "")
        path = folder / f"{safe}-{suffix}.png"
        ok = element.screenshot(str(path)) if element else driver.save_screenshot(str(path))
        assert ok and path.stat().st_size > 0, f"Không lưu được {path}"
        return path
    return save


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    session = getattr(item, "debug_driver", None)
    if report.failed and session is not None:
        folder = ROOT / "debug"
        folder.mkdir(exist_ok=True)
        name = item.name.replace("[", "_").replace("]", "")
        try:
            session.save_screenshot(str(folder / f"{name}.png"))
            (folder / f"{name}.xml").write_text(session.page_source, encoding="utf-8")
        except Exception as exc:
            report.sections.append(("Không lưu được debug", str(exc)))
