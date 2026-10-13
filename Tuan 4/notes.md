# Notes

## 1. Những điều đã học

* Hiểu được cách sử dụng Appium để điều khiển và kiểm thử ứng dụng Android tự động.
* Biết rằng Appium Server cần chạy trước khi chương trình Python kết nối và thực hiện kiểm thử.
* Biết cách sử dụng Android Studio Emulator để chạy ứng dụng trên máy ảo.
* Hiểu cách sử dụng `UiAutomator2Options` để cấu hình nền tảng Android, thiết bị và ứng dụng cần kiểm thử.
* Biết cách tìm một phần tử giao diện bằng Accessibility ID và sử dụng `is_displayed()` để kiểm tra phần tử có đang hiển thị hay không.
* Biết sử dụng câu lệnh `assert` để kiểm tra điều kiện và `try...finally` để đảm bảo phiên kiểm thử được đóng bằng `driver.quit()`.

## 2. Kết quả thực hành

Đã chạy thành công file `test_smoke.py` trên máy ảo Android với ứng dụng Swag Labs.

Kết quả nhận được:

`PASS: Ô Username tồn tại và đang hiển thị`

Kết quả cho thấy chương trình đã kết nối được với Appium Server, tìm thấy ô Username và xác nhận ô này đang hiển thị.

## 3. Câu hỏi đọc tài liệu

**Câu hỏi 1:** [Điền nguyên văn câu hỏi đọc tài liệu thứ nhất của giảng viên]

**Trả lời:** [Điền câu trả lời dựa trên tài liệu được giao]

**Câu hỏi 2:** [Điền nguyên văn câu hỏi đọc tài liệu thứ hai của giảng viên]

**Trả lời:** [Điền câu trả lời dựa trên tài liệu được giao]

## 4. Sử dụng AI

**Đã sử dụng AI:** Có.

**Nội dung đã hỏi AI:**

* Hướng dẫn thiết lập môi trường Appium và kết nối với máy ảo Android.
* Hướng dẫn xử lý lỗi cấu hình môi trường và driver UiAutomator2.
* Giải thích cách viết và chạy bài kiểm thử tự động bằng Python.
* Hướng dẫn kiểm tra ô Username trên giao diện ứng dụng.

**Câu trả lời của AI có chính xác không?**

Các hướng dẫn đã được kiểm chứng bằng cách chạy thử trên máy tính. Sau khi xử lý cấu hình Appium và UiAutomator2, bài kiểm thử đã chạy thành công và in ra kết quả `PASS`.

**Tôi hiểu được gì sau khi sử dụng AI?**

Tôi hiểu rõ hơn mối liên hệ giữa máy ảo Android, Appium Server, driver UiAutomator2 và chương trình Python. Tôi cũng hiểu cách tìm phần tử giao diện bằng Accessibility ID, kiểm tra phần tử đang hiển thị và đọc kết quả kiểm thử. Tôi nhận ra rằng cần kiểm tra log và môi trường thực tế thay vì chỉ sao chép lệnh mà không hiểu nguyên nhân lỗi.
