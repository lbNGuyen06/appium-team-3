# Ghi chú tuần 4 — Lê Bá Nguyên

Bài thực hành cá nhân trên ứng dụng Android Swag Labs.

## Ghi chú cá nhân

- Ảnh minh chứng: anh/image.png
- Điều đã học: Tôi hiểu cách dùng Python để điều khiển
  Swag Labs trên máy ảo thông qua Appium.
- Tôi hiểu bài test: Mở ứng dụng, chờ ô Username xuất hiện,
  kiểm tra ô đang hiển thị, rồi đóng phiên.
- Cài APK: Tôi kéo file APK vào cửa sổ máy ảo.
- Sử dụng AI: AI hỗ trợ chuẩn bị code và giải thích lỗi.
  Tôi đã tự chạy lại bài và xem kết quả trên terminal.

### Kết quả thực hành có hỗ trợ AI ngày 07/10/2026

Các kết quả dưới đây do trợ lý chạy trên máy cá nhân. Ảnh `anh/image.png`
là minh chứng lần tự chạy lại.

- Thiết bị: máy ảo Android `emulator-5554`; SDK ở `E:\Android_SDK`.
- Môi trường quan sát được: Python 3.13.3, pytest 8.4.2, Appium 2.19.0,
  UiAutomator2 4.2.9.
- Lần đầu dùng locator đúng `test-Username`: `1 passed in 9.87s`.
- Cố ý đổi locator thành `test-Username-SAI`: `1 failed in 24.29s`.
  WebDriverWait chờ tối đa 20 giây nhưng không tìm thấy phần tử hiển thị,
  nên phát sinh `TimeoutException`; thông tin kèm theo có `NoSuchElementError`.
  Tổng thời gian chạy còn bao gồm mở ứng dụng và đóng phiên.
- Khôi phục `test-Username`: `1 passed in 4.66s`.
- Log: `ket-qua-smoke.txt`, `ket-qua-co-y-sai.txt`, `ket-qua-sau-khi-sua.txt`.
- Nhận xét kỹ thuật: locator sai làm bài kiểm thử thất bại dù ứng dụng vẫn
  hiện ô Username. Cần kiểm tra cách tìm phần tử trước khi kết luận app bị lỗi.

## Câu hỏi phần đọc

Cần bổ sung 1–2 câu trả lời bằng lời của mình theo yêu cầu bài học.
