# Ghi chú tuần 4 — nhóm App

Mỗi thành viên bổ sung một mục riêng và viết bằng lời của mình sau khi thực hành.
Hiện file có ghi chú của Lê Bá Nguyên; các thành viên khác cần bổ sung.

## Thành viên: Lê Bá Nguyên

- Ảnh minh chứng: anh/image.png
- Điều đã học: Tôi hiểu cách dùng Python để điều khiển
  Swag Labs trên máy ảo thông qua Appium.
- Tôi hiểu bài test: Mở ứng dụng, chờ ô Username xuất hiện,
  kiểm tra ô đang hiển thị, rồi đóng phiên.
- Cài APK: Tôi kéo file APK vào cửa sổ máy ảo.
- Sử dụng AI: AI hỗ trợ chuẩn bị code và giải thích lỗi.
  Tôi đã tự chạy lại bài và xem kết quả trên terminal.

## Theo dõi của nhóm trưởng

### Kết quả thực hành có hỗ trợ AI ngày 07/10/2026

Các kết quả dưới đây do trợ lý chạy trên máy của nhóm trưởng; từng thành viên
vẫn cần tự thực hành và viết nhận xét riêng ở phần của mình.

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
- Đã có ảnh và ghi chú của Lê Bá Nguyên; chưa có phần của các thành viên khác.

| Thành viên | Cài xong      | Tự chạy PASS  | Có ảnh  | Có ghi chú |
| ---------- | ------------- | ------------- | ------- | ---------- |
| Lê Bá Nguyên | Đã cài | Đã chạy PASS | anh/image.png | Đã có; cần bổ sung câu hỏi phần đọc |
