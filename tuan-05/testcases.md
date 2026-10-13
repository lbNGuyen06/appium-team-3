# Test case đăng nhập Swag Labs — tuần 5

Soạn trước khi viết code kiểm thử tuần 5. Phạm vi: ứng dụng Android Swag Labs.
Tiền điều kiện chung: máy ảo đang chạy, đã cài Swag Labs, Appium và UiAutomator2
sẵn sàng. Mỗi test bắt đầu từ màn đăng nhập với dữ liệu ứng dụng được đặt lại.

## TC01 — Đăng nhập thành công

- Dữ liệu: username `standard_user`, password `secret_sauce`.
- Bước 1: nhập username vào ô Username.
- Bước 2: nhập password vào ô Password.
- Bước 3: bấm LOGIN.
- Mong đợi: màn Products hiển thị danh sách sản phẩm.

## TC02 — Tài khoản bị khóa

- Dữ liệu: username `locked_out_user`, password `secret_sauce`.
- Bước 1: nhập username vào ô Username.
- Bước 2: nhập password vào ô Password.
- Bước 3: bấm LOGIN.
- Mong đợi: hiện `Sorry, this user has been locked out.`;
  vẫn ở màn đăng nhập, không vào danh sách sản phẩm.

## TC03 — Bỏ trống mật khẩu

- Dữ liệu: username `standard_user`, password để trống.
- Bước 1: nhập username vào ô Username.
- Bước 2: để ô Password trống.
- Bước 3: bấm LOGIN.
- Mong đợi: hiện `Password is required`;
  vẫn ở màn đăng nhập, không vào danh sách sản phẩm.

Hai trường hợp đăng nhập bị từ chối vẫn phải PASSED nếu ứng dụng báo đúng lỗi.
