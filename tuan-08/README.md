# Tuần 8 — A2: Đăng xuất & ngoại lệ

| Test | Nội dung | Hàm chính |
|---|---|---|
| `test_a2_logout_returns_to_login` | Menu → LOGOUT về màn đăng nhập | `click`, `visible` |
| `test_a2_no_such_element_after_logout` | Không còn PRODUCTS | `pytest.raises`, `NoSuchElementException` |
| `test_a2_timeout_waiting_products_after_logout` | Chờ PRODUCTS quá hạn | `TimeoutException` |
| `test_a2_stale_element_after_logout` | Dùng lại phần tử cũ | `StaleElementReferenceException` |
| `test_a2_login_again_after_logout` | Đăng nhập lại sau khi thoát | `login` |
| `test_a2_screenshot_hook_on_failure` | Chụp ảnh minh chứng | `save_screenshot` |

Hook `pytest_runtest_makereport` trong `conftest.py` tự lưu ảnh + XML vào `debug/` khi test lỗi.

```powershell
$env:ANDROID_UDID = 'emulator-5554'
.\.venv\Scripts\python.exe -m pytest tuan-08 -v --tb=short --color=no
```

Chạy riêng thư mục tuần 8, không chạy chung với tuần khác (trùng tên `helpers`/`conftest`).
