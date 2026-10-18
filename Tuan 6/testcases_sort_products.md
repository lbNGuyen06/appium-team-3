# Test Cases – Sắp xếp sản phẩm Swag Labs

## TC01 – Đăng nhập thành công

* **Mục tiêu:** Kiểm tra đăng nhập thành công để vào màn hình Products trước khi sắp xếp sản phẩm.
* **Các bước thực hiện:**

  1. Mở ứng dụng Swag Labs.
  2. Nhập Username: `standard_user`.
  3. Nhập Password: `secret_sauce`.
  4. Nhấn nút Login.
  5. Chờ màn hình Products hiển thị.
* **Dữ liệu kiểm thử:**

  * Username: `standard_user`
  * Password: `secret_sauce`
* **Kết quả mong đợi:** Đăng nhập thành công và chuyển đến màn hình Products.

## TC02 – Chọn sắp xếp giá từ thấp đến cao

* **Mục tiêu:** Kiểm tra người dùng mở được menu sắp xếp và chọn được kiểu sắp xếp giá từ thấp đến cao.
* **Các bước thực hiện:**

  1. Tại màn hình Products, nhấn nút sắp xếp (Modal Selector Button).
  2. Chọn `Price (low to high)`.
  3. Chờ menu sắp xếp đóng lại.
  4. Chờ danh sách sản phẩm hiển thị lại.
* **Dữ liệu kiểm thử:**

  * Kiểu sắp xếp: `Price (low to high)`
* **Kết quả mong đợi:** Menu sắp xếp đóng lại và danh sách sản phẩm hiển thị trên màn hình.

## TC03 – Lấy đầy đủ danh sách sản phẩm khi cuộn

* **Mục tiêu:** Kiểm tra có thể lấy toàn bộ sản phẩm trong danh sách mà không cần biết trước số lượng.
* **Các bước thực hiện:**

  1. Đọc tên và giá các sản phẩm đang hiển thị trên màn hình.
  2. Cuộn danh sách xuống.
  3. Đọc thêm các sản phẩm mới xuất hiện (sản phẩm đã đọc rồi thì không đếm lại).
  4. Lặp lại bước 2 và 3 cho đến khi không cuộn được nữa (hết danh sách).
  5. Đọc thêm một lần cuối sau lần cuộn cuối cùng.
* **Dữ liệu kiểm thử:**

  * Không ghi cứng số lượng sản phẩm.
  * Giới hạn tối đa 20 lần cuộn để tránh lặp vô hạn.
* **Kết quả mong đợi:** Lấy được ít nhất 1 sản phẩm và in ra tổng số sản phẩm đã lấy.

## TC04 – Kiểm tra giá được sắp xếp tăng dần

* **Mục tiêu:** Kiểm tra danh sách giá hiển thị trên app đã được sắp xếp từ thấp đến cao.
* **Các bước thực hiện:**

  1. Lấy danh sách giá theo thứ tự hiển thị trên app (kết quả của TC03).
  2. Tạo danh sách giá đã sắp xếp đúng bằng `sorted()`.
  3. So sánh hai danh sách.
* **Dữ liệu kiểm thử:**

  * Danh sách giá lấy từ app sau khi chọn `Price (low to high)`.
* **Kết quả mong đợi:** Hai danh sách bằng nhau, tức là giá sản phẩm tăng dần. Hiển thị `PASS: Sap xep gia tu thap den cao thanh cong`.
