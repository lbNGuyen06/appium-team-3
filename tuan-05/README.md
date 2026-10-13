# Chạy và nộp bài tuần 5

## File cần nộp theo đề

- `testcases.md`: ba test case đăng nhập viết bằng lời trước khi có code.
- `test_login.py`: ba bài kiểm thử, có chú thích tiếng Việt và chạy thành công.
- `anh/`: ảnh kết quả cho thấy ba bài thành công.
- `notes.md`: ghi chú cá nhân, trả lời 1–2 câu hỏi phần đọc,
  ghi việc sử dụng AI và cách kiểm tra câu trả lời.
- Đưa lên nhánh `week-05`, sau đó gộp vào `main` trước buổi học tiếp theo.

## Chạy trên máy cá nhân

Bật máy ảo Android đã cài Swag Labs. Mở PowerShell tại thư mục gốc dự án.
Nếu Appium đã chạy thì bỏ qua bước bật server; không chạy hai server cùng cổng.

Terminal 1:

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
$env:ANDROID_UDID = 'emulator-5554' # thay theo kết quả adb devices
.\.venv\Scripts\python.exe -m pytest tuan-05/test_login.py -v --tb=short --color=no
```

Không thao tác trên máy ảo khi đang chạy. Test sẽ đặt lại dữ liệu app Swag Labs
trước mỗi trường hợp. Mong đợi `3 passed`, kể cả hai tình huống bị từ chối
đăng nhập: chúng thành công khi ứng dụng hiển thị đúng thông báo lỗi mong đợi.

Code chụp ảnh màn ứng dụng sau khi các kiểm tra của từng test thành công.
Chụp thêm màn hình terminal thể hiện cả ba test PASSED và dòng `3 passed`,
lưu trong `anh/image.png`. Ảnh của lần chạy cũ không chứng minh lần chạy mới;
luôn đối chiếu với kết quả terminal hiện tại.

## Giải thích code

- Fixture `driver`: mỗi test có phiên riêng, luôn đóng phiên khi xong.
- `visible`: tìm phần tử theo accessibility id và chờ nó hiển thị.
- `login`: nhập tài khoản, mật khẩu và bấm LOGIN.
- `assert_login_error`: so sánh thông báo lỗi và kiểm tra vẫn ở trang đăng nhập.
- Các hàm `test_login_*`: thực hiện ba test case tương ứng TC01–TC03.

Khi chạy trên máy khác, thay đường dẫn SDK/JDK và mã thiết bị cho phù hợp.
