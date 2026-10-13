# Test Cases – Đăng nhập Swag Labs

## TC01 – Đăng nhập thành công

* **Mục tiêu:** Kiểm tra đăng nhập thành công với tài khoản hợp lệ.
* **Các bước thực hiện:**

  1. Mở ứng dụng Swag Labs.
  2. Nhập Username: `standard_user`.
  3. Nhập Password: `secret_sauce`.
  4. Nhấn nút Login.
* **Dữ liệu kiểm thử:**

  * Username: `standard_user`
  * Password: `secret_sauce`
* **Kết quả mong đợi:** Đăng nhập thành công và chuyển đến màn hình Products.

## TC02 – Đăng nhập bằng tài khoản bị khóa

* **Mục tiêu:** Kiểm tra hệ thống xử lý khi người dùng sử dụng tài khoản bị khóa.
* **Các bước thực hiện:**

  1. Mở ứng dụng Swag Labs.
  2. Nhập Username: `locked_out_user`.
  3. Nhập Password: `secret_sauce`.
  4. Nhấn nút Login.
* **Dữ liệu kiểm thử:**

  * Username: `locked_out_user`
  * Password: `secret_sauce`
* **Kết quả mong đợi:** Không đăng nhập được và hiển thị thông báo tài khoản bị khóa.

## TC03 – Đăng nhập khi bỏ trống mật khẩu

* **Mục tiêu:** Kiểm tra thông báo lỗi khi người dùng không nhập mật khẩu.
* **Các bước thực hiện:**

  1. Mở ứng dụng Swag Labs.
  2. Nhập Username: `standard_user`.
  3. Để trống ô Password.
  4. Nhấn nút Login.
* **Dữ liệu kiểm thử:**

  * Username: `standard_user`
  * Password: Để trống.
* **Kết quả mong đợi:** Không đăng nhập được và hiển thị thông báo `Password is required`.
