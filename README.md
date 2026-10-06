# Thực hành kiểm thử tự động — nhóm App — tuần 4

Mục tiêu: mở Swag Labs trên Android và kiểm tra có ô tên đăng nhập.
Code được chuẩn bị với hỗ trợ AI; đã chạy trên máy ảo emulator-5554 của nhóm trưởng
và đạt `1 passed in 9.87s`. Kết quả này không thay thế phần thực hành của từng thành viên.
Mỗi thành viên cần tự gõ, chạy, giải thích code và viết ghi chú riêng theo đề bài.

## 1. Chuẩn bị

- Python, Node.js và npm, JDK 17.
- Android Studio, Android SDK Platform-Tools và một máy ảo đã khởi động.
- Appium 2 và UiAutomator2 phiên bản 4 (phiên bản 5 trở lên yêu cầu Appium 3).
- Tải APK Android Swag Labs từ https://github.com/saucelabs/sample-app-mobile/releases.
  Chọn Android.SauceLabs.Mobile.Sample.app…apk, không chọn bản iOS.

Mở PowerShell tại thư mục dự án. Chạy từng lệnh và kiểm tra lỗi trước khi tiếp tục:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
npm.cmd install --save-dev appium@2
```

Trong mỗi terminal dùng Appium/ADB, thiết lập biến cho phiên làm việc.
Thay đường dẫn SDK/JDK nếu máy bạn cài ở nơi khác:

```powershell
$env:ANDROID_HOME = 'E:\Android_SDK'
$env:JAVA_HOME = 'E:\java'
$env:APPIUM_HOME = "$PWD\.appium"
$env:Path = "$env:ANDROID_HOME\platform-tools;$env:JAVA_HOME\bin;$env:Path"
```

Cài driver vào thư mục riêng của dự án:

```powershell
npx.cmd --no-install appium driver install uiautomator2@4
npx.cmd --no-install appium driver doctor uiautomator2
adb devices -l
```

Máy ảo phải xuất hiện với trạng thái `device`. Lấy đúng mã thiết bị từ kết quả,
ví dụ `emulator-5554`; không mặc định mọi máy đều có mã này.

## 2. Cài Swag Labs

```powershell
$env:ANDROID_UDID = 'emulator-5554' # thay bằng mã thực tế
adb -s $env:ANDROID_UDID install 'C:\duong-dan-thuc-te\SwagLabs.apk'
```

Đường dẫn APK trên là ví dụ, phải thay bằng file đã tải.
Mở Swag Labs trên máy ảo để kiểm tra màn đăng nhập xuất hiện.

## 3. Chạy bài kiểm thử

Terminal thứ nhất, sau khi thiết lập biến ở bước 1:

```powershell
npx.cmd --no-install appium --address 127.0.0.1 --port 4723
```

Giữ terminal này chạy. Mở terminal thứ hai tại thư mục dự án:

```powershell
$env:ANDROID_UDID = 'emulator-5554' # thay bằng mã thực tế
.\.venv\Scripts\python.exe -m pytest tuan-04/test_smoke.py -v
```

Kết quả mong đợi là `1 passed`, chỉ đánh dấu hoàn thành khi đã chạy thực tế.
Test đưa dữ liệu ứng dụng Swag Labs demo về trạng thái ban đầu.
Chụp ảnh terminal có kết quả và máy ảo, lưu vào `tuan-04/anh/`.

## 4. Hiểu code và thử lỗi

Luồng lệnh: pytest chạy hàm test → Appium Python client gửi yêu cầu → Appium
server nhận yêu cầu → UiAutomator2 điều khiển Android → trả kết quả về test.

- `UiAutomator2Options`: khai báo thiết bị và ứng dụng cần mở.
- `webdriver.Remote`: bắt đầu phiên điều khiển qua Appium server.
- `WebDriverWait`: chờ điều kiện hiển thị, tối đa 20 giây.
- `ACCESSIBILITY_ID`: tìm ô có nhãn kiểm thử `test-Username`.
- `assert`: kiểm tra kết quả.
- `finally` và `quit`: kết thúc phiên cả khi có lỗi.

Sau lần chạy thành công, cố ý đổi `test-Username` thành `test-Username-SAI`,
chạy lại và đọc lỗi timeout. Ghi nhận lỗi rồi sửa lại locator đúng, chạy lại PASS.
Mỗi người tự viết chú thích tiếng Việt và hoàn thành `tuan-04/notes.md`.

## 5. Nộp bài nhóm

Nhóm trưởng tạo repository GitHub và mời thành viên. Nếu đã có repository,
dùng repository đó, không tạo bản trùng. Khi đã có nhánh main, tạo nhánh
`week-04`, đưa các file bài làm vào đó rồi gộp vào main trước buổi tiếp theo.

Nộp `README.md`, `requirements.txt`, `package.json`, `package-lock.json` (sau cài),
`.gitignore`, `tuan-04/test_smoke.py`, ghi chú và ảnh của mọi thành viên.
Không nộp `.venv`, `node_modules`, `.appium` hoặc APK.

## Xử lý lỗi thường gặp

- Không nhận `adb`: kiểm tra SDK Platform-Tools đã cài và đường dẫn SDK đúng.
- `adb devices` trống: khởi động máy ảo trong Device Manager.
- Connection refused cổng 4723: Appium server chưa chạy hoặc đã dừng vì lỗi.
- Không tìm thấy driver: kiểm tra hai terminal dùng cùng `APPIUM_HOME`.
- Không tìm thấy ứng dụng: kiểm tra đã cài đúng APK Swag Labs trên đúng máy ảo.
- Timeout tìm ô: xem màn hình máy ảo có đang ở trang đăng nhập hay không.
- `KeyError: ANDROID_UDID`: đặt biến mã thiết bị trong terminal chạy pytest.

## Tài liệu

- https://appium.io/docs/en/2.19/quickstart/
- https://github.com/appium/appium-uiautomator2-driver
- https://github.com/appium/python-client
- https://developer.android.com/studio/run/managing-avds
- https://github.com/saucelabs/sample-app-mobile/releases
