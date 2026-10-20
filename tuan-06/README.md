# Tuần 6 — A1, A2, A3, A4

| Phần | File |
|---|---|
| Sắp xếp, chờ và timeout | `test_a1_sort.py` |
| Thêm/xóa giỏ và kéo-thả | `test_a2_cart.py` |
| Cuộn, ảnh toàn màn hình/phần tử | `test_a3_scroll.py` |
| Phiên Appium và menu | `test_a4_session_menu.py` |
| Chuẩn bị phiên/hàm dùng chung | `conftest.py`, `helpers.py` |
| Test case và báo cáo tài liệu | `testcases.md`, `bao-cao-chuyen-de.md` |
| Kiểm tra bài A1 nguồn | `review-a1.md` |

Không thay thế bài tuần 4–5. Mỗi test reset dữ liệu Swag Labs demo; dùng app tiếng Anh.
Đọc `bao-cao-chuyen-de.md` để chuẩn bị trình bày nội dung tài liệu.

## Chạy từ thư mục gốc repository

Bật máy ảo đã cài Swag Labs. Terminal 1 (bỏ qua nếu Appium đã chạy):

```powershell
$env:ANDROID_HOME = 'E:\Android_SDK'
$env:JAVA_HOME = 'E:\java'
$env:APPIUM_HOME = "$PWD\.appium"
$env:Path = "$env:ANDROID_HOME\platform-tools;$env:JAVA_HOME\bin;$env:Path"
npx.cmd --no-install appium --address 127.0.0.1 --port 4723
```

Terminal 2:

```powershell
& 'E:\Android_SDK\platform-tools\adb.exe' devices
$env:ANDROID_UDID = 'emulator-5554'
.\.venv\Scripts\python.exe -m pytest tuan-06 -v --tb=short --color=no
```

Chạy riêng phần A2: thay `tuan-06` bằng `tuan-06/test_a2_cart.py`.
Không chạy song song nhiều bài trên cùng một máy ảo.

Ảnh test thành công nằm ở `anh/`; lỗi có thể có ảnh và XML trong `debug/`.
`session-info.json` ghi capabilities của phiên A4, không dùng lại session_id đó
cho lần chạy sau. Log kiểm chứng lưu trong `ket-qua-pytest.txt`.
Chụp thêm terminal nếu cần ảnh tổng kết các bài PASSED; không dùng ảnh từ nhánh
tác giả A1 làm minh chứng cho lần chạy của mình.
