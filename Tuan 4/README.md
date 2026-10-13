# Tuần 4 – Kiểm thử tự động Android với Appium

## 1. Mục tiêu

Thực hiện bài kiểm thử tự động đầu tiên trên ứng dụng Swag Labs bằng Python, Appium và máy ảo Android.

Bài kiểm thử kiểm tra xem ô nhập Username có tồn tại và đang hiển thị trên màn hình đăng nhập hay không.

## 2. Công cụ sử dụng

* Python
* Appium Server
* Appium-Python-Client
* UiAutomator2
* Android Studio Emulator
* Ứng dụng Swag Labs

## 3. Yêu cầu môi trường

Cần cài đặt các công cụ sau trước khi chạy:

* Python
* Node.js và npm
* JDK 17
* Android Studio và Android SDK
* Appium Server cùng driver UiAutomator2

Cài thư viện Python:

```powershell
python -m pip install Appium-Python-Client
```

Nếu chưa cài Appium và driver UiAutomator2, chạy:

```powershell
npm install -g appium
appium driver install uiautomator2
```

## 4. Cách chạy kiểm thử

### Bước 1: Khởi động máy ảo Android

Mở Android Studio, vào Device Manager và khởi động máy ảo đã cài ứng dụng Swag Labs.

Kiểm tra kết nối thiết bị bằng lệnh:

```powershell
adb devices
```

Thiết bị cần xuất hiện với trạng thái `device`.

### Bước 2: Khởi động Appium Server

Khởi động Appium Server và bảo đảm driver UiAutomator2 đã được cài đặt, tải thành công.

Server mặc định sử dụng địa chỉ:

```text
http://127.0.0.1:4723
```

Giữ cửa sổ chạy Appium Server mở trong suốt quá trình kiểm thử.

### Bước 3: Chạy file kiểm thử

Mở PowerShell tại thư mục chứa `test_smoke.py`, sau đó chạy:

```powershell
python test_smoke.py
```

Nếu máy tính không nhận lệnh `python`, hãy sử dụng đường dẫn đầy đủ đến trình thông dịch Python đã cài đặt.

## 5. Kết quả mong đợi

Nếu kiểm thử thành công, màn hình PowerShell hiển thị:

```text
PASS: Ô Username tồn tại và đang hiển thị
```

Kết quả này cho biết Appium đã tìm thấy ô Username và xác nhận phần tử đang hiển thị.

## 6. Lưu ý

* Các đường dẫn cài đặt Android SDK, JDK và Appium có thể khác nhau trên từng máy.
* Cần cập nhật biến môi trường và cấu hình phù hợp với máy tính đang sử dụng.
* Máy ảo Android phải được khởi động và Appium Server phải hoạt động trước khi chạy test.
