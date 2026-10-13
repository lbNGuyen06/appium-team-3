# Ghi chú tuần 5 — Lê Bá Nguyên

## Tình trạng bài nộp

- Đã soạn ba test case trong `testcases.md` trước khi viết `test_login.py`.
- Code có chú thích tiếng Việt, chờ phần tử và tạo phiên độc lập cho mỗi test.
- Đã chạy trên Android `emulator-5554` ngày 13/10/2026: `3 passed in 41.84s`.
- Log thực tế: `ket-qua-pytest.txt`; ba ảnh màn ứng dụng nằm trong `anh/`.
- Đã bổ sung ảnh terminal `anh/image.png` từ lần tự chạy lại:
  cả ba test PASSED, tổng kết `3 passed in 26.81s`.

## Ghi chú cá nhân

- Phần tôi đã thực hiện: Bật máy ảo, tự chạy lại ba test đăng nhập bằng pytest
  và chụp ảnh kết quả `3 passed in 26.81s`.
- Kiến thức chính: Tìm phần tử bằng accessibility id, dùng `send_keys` để nhập,
  `click` để bấm và `assert` để đối chiếu kết quả với mong đợi.
- Lỗi/cách sửa: Kết nối ADB từng bị treo; AI hỗ trợ khởi động lại ADB,
  kiểm tra Android sẵn sàng rồi chạy lại thành công.
- Câu hỏi đọc 1 — Tìm accessibility id bằng Appium Inspector thế nào?
  Mở phiên kết nối, chọn phần tử trong ảnh/cây giao diện và xem thuộc tính
  `content-desc` trên Android; giá trị này được dùng làm accessibility id.
- Câu hỏi đọc 2 — Nếu kết quả khác mong đợi, pytest báo gì?
  Khi `assert` không đúng, test báo FAILED kèm AssertionError để xem nguyên nhân.
- Sử dụng AI: Tôi hỏi về vai trò Appium, biến `driver`, kết nối cục bộ và cách
  test thao tác giao diện. Tôi kiểm tra bằng cách tự chạy lại, xem kết quả và ảnh.
  Hai ca đăng nhập bị từ chối vẫn PASSED khi ứng dụng báo đúng lỗi mong đợi.

## Hỗ trợ AI trong quá trình chuẩn bị

### Kết quả thực hành có hỗ trợ AI

- TC01 đăng nhập `standard_user`: PASSED, hiển thị danh sách sản phẩm.
- TC02 đăng nhập `locked_out_user`: PASSED, hiện đúng thông báo tài khoản bị khóa.
- TC03 bỏ trống mật khẩu: PASSED, hiện `Password is required`.
- Lỗi môi trường đã gặp: ADB nhận máy ảo nhưng lệnh shell không phản hồi.
  Khởi động lại ADB bằng `adb kill-server` rồi `adb start-server`;
  kiểm tra `sys.boot_completed` trả về `1`, sau đó chạy lại thành công.
- Các kết quả này do trợ lý chạy trên máy cá nhân; lần tự chạy lại được lưu
  riêng trong ảnh `anh/image.png`.

Trợ lý hỗ trợ soạn test case, code Appium/pytest, hướng dẫn và ghi chú ngắn gọn
dựa trên quá trình thực hành và trao đổi thực tế.
