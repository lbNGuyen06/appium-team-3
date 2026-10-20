# Báo cáo chuyên đề tuần 6 — App A1 đến A4

Người thực hiện: Lê Bá Nguyên. Ứng dụng: Swag Labs Android, Appium Python Client.
Phạm vi mới: thực hiện đủ A1–A4 theo sheet T6–T11 v3.

## 1. Cách hệ thống hoạt động

pytest chạy Python → Appium Python Client gửi HTTP đến `127.0.0.1:4723` →
Appium server nạp UiAutomator2 driver → ADB/chuyển tiếp cổng →
UiAutomator2 trên Android thao tác Swag Labs → trả kết quả cho Python.

Server đang chạy cục bộ, không cần đưa lên Internet. Swag Labs không tự kết nối
đến Appium. Mỗi test tạo phiên, thao tác, kiểm tra bằng assert và đóng phiên.

## 2. A1 — Sắp xếp sản phẩm và cơ chế chờ

Tài liệu phân công: 5.1 Explicit Waits, 5.2 Implicit Waits,
7.5 Locate elements By, 7.1 Exceptions.

- `webdriver.Remote`: mở phiên trên Appium server.
- `AppiumBy.ACCESSIBILITY_ID`: tìm bằng định danh accessibility của app.
- `WebDriverWait(...).until(...)`: chờ điều kiện cụ thể trong thời gian tối đa.
- `visibility_of_element_located`: phần tử tồn tại và hiển thị.
- `element_to_be_clickable`: phần tử hiển thị và được bật; không đảm bảo không bị
  lớp phủ che, nên vẫn cần kiểm tra trạng thái màn hình phù hợp.
- `implicitly_wait`: thời gian chờ chung cho tìm phần tử; bài dùng 0 để không
  cộng dồn với explicit wait.
- `find_elements`: trả danh sách; rỗng khi không có kết quả sau thời gian chờ.
- `TimeoutException`: hết hạn chờ điều kiện; bài lỗi có chủ đích dùng
  `pytest.raises(TimeoutException)` để xác nhận loại lỗi đúng.

Đọc đủ 6 tên và giá qua các viewport rồi kiểm tra thứ tự; dùng Decimal để xử lý
giá tiền. Chỉ đọc được một sản phẩm chưa chứng minh danh sách được sắp đúng.
Hai test nghiệp vụ: giá thấp–cao và tên Z–A. Một test kỹ thuật: timeout có chủ đích.

## 3. A2 — Giỏ hàng, kéo-thả và ngoại lệ

Tài liệu phân công: 3.3 Drag and drop, 3.5 Popup dialogs,
7.1 Exceptions, 7.2 Action Chains, 7.3 Alerts.

- `click`, `text`, `find_elements`: thêm/xóa, đọc tên và đếm sản phẩm.
- Trên web, `ActionChains` có thể tạo chuỗi
  `click_and_hold → move_to_element → release → perform`.
- Trên app Android native, bài dùng `execute_script("mobile: dragGesture", ...)`
  từ tay nắm sản phẩm đến vùng thả của app. Tọa độ đích lấy từ phần tử thực tế.
- Xác minh kéo-thả bằng huy hiệu giỏ và tên sản phẩm trong giỏ, không chỉ dựa
  vào việc lệnh không báo lỗi.
- `NoSuchElementException`: `find_element` không tìm được phần tử.
  Bài giỏ trống xác nhận lỗi này bằng `pytest.raises`.
- Popup JavaScript (`switch_to.alert`, accept/dismiss) thuộc ngữ cảnh web.
  Không tự coi menu hay thông báo React Native là JavaScript alert; dùng locator
  cho UI native. Luồng giỏ hàng này không phát sinh popup cần accept.

## 4. A3 — Cuộn và chụp màn hình

Tài liệu phân công: 8.3 Scroll, 8.4 Auto save files, 8.5 Upload files,
8.6 Firebug, 8.7 Screenshot, 7.19 Remote WebDriver, 7.20 WebElement.

- `mobile: scrollGesture`: cuộn vùng danh sách, trả khả năng còn cuộn tiếp.
  Giới hạn vòng lặp để tránh treo; đọc lại viewport sau lần cuộn cuối.
- `AppiumBy.ANDROID_UIAUTOMATOR` và `UiScrollable`: tìm sản phẩm ngoài màn hình
  bằng selector Android, ví dụ Sauce Labs Onesie.
- `save_screenshot(path)`: ảnh toàn màn hình của thiết bị.
- `element.screenshot(path)`: ảnh riêng phần tử; kiểm tra file được tạo và có dữ liệu.
- “Auto save files”/“Upload files” trong tài liệu Selenium nói về trình duyệt.
  Swag Labs PRODUCTS native không có ô HTML chọn file; không dùng `send_keys`
  đường dẫn lên một ô bất kỳ để giả lập upload.
- Firebug là công cụ cũ dành cho Firefox, không dùng để inspect Android.
  Với app này dùng Appium Inspector và cây giao diện Android.

Ảnh minh chứng phản ánh giao diện; ảnh riêng lẻ không thay thế tổng kết pytest.
Test A3-01 đọc đủ catalog ở cuối danh sách; A3-02 tìm Onesie và lưu hai loại ảnh.

## 5. A4 — Phiên Remote WebDriver và menu

Tài liệu phân công: 1 Installation, 2.5 Remote WebDriver, 7.6 Desired Capabilities,
7.17 Chrome Options, 8.1 ChromeDriver, 3.6 History and location.

- `UiAutomator2Options` chứa capabilities chọn Android, driver, udid, appPackage,
  appActivity và chính sách reset. Truyền qua `options=` khi tạo Remote.
- `session_id`: mã phiên server cấp, có giá trị trong vòng đời phiên.
- `capabilities`: thông tin phiên đã được server chấp nhận, dùng để kiểm tra
  đúng Android, UiAutomator2 và thiết bị.
- `back()` trên Android gửi thao tác quay lại thiết bị; không phải lúc nào
  cũng là lịch sử URL như trong trình duyệt.
- Menu: mở Menu → ALL ITEMS, mở chi tiết → back; xác nhận cùng phiên và
  trở lại PRODUCTS. Test riêng Menu → LOGOUT kiểm tra ô Username xuất hiện.
- ChromeOptions/ChromeDriver phục vụ Chrome hoặc ngữ cảnh WebView tương thích;
  không cần dùng trong các màn native của tuần 6.

## 6. Demo và cách đọc kết quả

1. Bật máy ảo và Appium, kiểm tra `adb devices`.
2. Chạy `python -m pytest tuan-06 -v`.
3. Giải thích một ca mỗi nhóm A1–A4 và mở ảnh tương ứng.
4. Mở `ket-qua-pytest.txt` để xem tổng kết; đối chiếu `review-a1.md`.
5. Một test nghiệp vụ lỗi phải báo FAILED/ERROR. Các test lỗi có chủ đích
   chỉ PASS khi đúng loại ngoại lệ dự kiến.

## Nguồn

- [Sheet mới](https://docs.google.com/spreadsheets/d/1iOs5fvOxvkHQwqh_QQYTblzJ-Vl1I9mt/edit)
- [Tài liệu Selenium Python theo sheet](https://selenium-python.readthedocs.io/)
- [Appium Python Client](https://github.com/appium/python-client)
- [UiAutomator2 gestures](https://appium.github.io/appium-uiautomator2-driver/latest/reference/execute-methods/#gestures)
- [Mã nguồn Swag Labs](https://github.com/saucelabs/sample-app-mobile)
- A1 tham khảo ý tưởng từ bài Phạm Đức Tài tại commit `7ec8731`; chi tiết trong
  `review-a1.md`. Các thay đổi và phần A2–A4 có hỗ trợ AI, cần đọc hiểu trước demo.
