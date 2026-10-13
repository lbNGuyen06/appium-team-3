# Ghi chú tuần 5 — Lê Bá Nguyên

## Tình trạng bài nộp

- Đã soạn ba test case trong `testcases.md` trước khi viết `test_login.py`.
- Code có chú thích tiếng Việt, chờ phần tử và tạo phiên độc lập cho mỗi test.
- Đã chạy trên Android `emulator-5554` ngày 13/10/2026: `3 passed in 41.84s`.
- Log thực tế: `ket-qua-pytest.txt`; ba ảnh màn ứng dụng nằm trong `anh/`.
- Đã bổ sung ảnh terminal `anh/image.png` từ lần tự chạy lại:
  cả ba test PASSED, tổng kết `3 passed in 26.81s`.
- Phần nhận xét và câu trả lời cá nhân bên dưới cần bổ sung.

## Ghi chú cá nhân

- Phần tôi đã thực hiện: [điền đúng việc thực tế]
- Điều tôi hiểu về tìm phần tử, nhập dữ liệu, bấm nút và assert: [điền]
- Kết quả chạy và lỗi/cách sửa: [điền]
- Câu hỏi đọc 1 — Làm thế nào tìm accessibility id bằng Appium Inspector? [tự trả lời]
- Câu hỏi đọc 2 — Nếu kết quả thực tế khác mong đợi, pytest báo gì? [tự trả lời]
- Tôi đã hỏi AI điều gì, kiểm tra câu trả lời thế nào, học thêm được gì? [điền]

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

Trợ lý hỗ trợ soạn test case, code Appium/pytest, hướng dẫn và khung ghi chú.
Phần nhận xét cá nhân cần phản ánh cách hiểu và trải nghiệm thực hành thực tế.
