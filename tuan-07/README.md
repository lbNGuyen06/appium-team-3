# Tuần 7 — A2: Trạng thái ứng dụng & Reset App State

| Test | Nội dung | Hàm chính |
|---|---|---|
| `test_a2_reset_app_state_clears_cart_badge` | Thêm 2 sản phẩm → Menu → RESET APP STATE → giỏ rỗng | `EC.invisibility_of_element_located` |
| `test_a2_reset_app_state_restores_add_button` | Nút sản phẩm quay lại ADD TO CART (lỗi đã biết của app) | `pytest.mark.xfail` |
| `test_a2_terminate_and_activate_app` | Đóng rồi mở lại app → về màn đăng nhập | `terminate_app`, `activate_app`, `query_app_state` |
| `test_a2_no_reset_capability[True/False]` | Capability `noReset` được phiên ghi nhận | `noReset` |

Chạy từ thư mục gốc (cấu hình Appium như `tuan-06/README.md`), chạy riêng thư mục tuần 7:

```powershell
$env:ANDROID_UDID = 'emulator-5554'
.\.venv\Scripts\python.exe -m pytest tuan-07 -v --tb=short --color=no
```

Không chạy chung với `tuan-06` trong một lệnh pytest (trùng tên module `helpers`/`conftest`).
Ảnh minh chứng ở `anh/`, ảnh/XML khi lỗi ở `debug/`.
