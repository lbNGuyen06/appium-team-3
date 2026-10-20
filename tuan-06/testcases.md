# Tuần 6 — test case A1 đến A4

Tiền điều kiện: Swag Labs Android tiếng Anh, tài khoản standard_user / secret_sauce,
Appium 2 + UiAutomator2; mỗi test đặt lại app và có phiên riêng.
Soạn bộ test case này trước khi triển khai code tuần 6.

| Mã | Bước thực hiện | Kết quả mong đợi |
|---|---|---|
| A1-01 | Đăng nhập, chọn Price (low to high), đọc và cuộn hết danh sách | Đủ 6 sản phẩm mẫu, tên/giá đúng, giá tăng dần |
| A1-02 | Chọn Name (Z to A), đọc và cuộn hết danh sách | Đủ 6 sản phẩm, tên giảm dần |
| A1-03 | Chờ một accessibility id cố ý không tồn tại trong 1 giây | Phát sinh TimeoutException, test vẫn PASS vì lỗi được dự kiến |
| A2-01 | Thêm Backpack và Bike Light, mở giỏ, xóa Backpack | Huy hiệu đổi 1 → 2 → 1; giỏ chỉ còn Bike Light |
| A2-02 | Kéo tay nắm của Backpack lên vùng thả, mở giỏ | Huy hiệu 1 và giỏ chứa đúng Backpack |
| A2-03 | Từ giỏ trống, tìm Item không tồn tại | NoSuchElementException; không có dòng sản phẩm |
| A3-01 | Cuộn bằng mobile: scrollGesture đến cuối danh sách | Đọc đủ 6 tên, lưu ảnh toàn màn hình ở cuối |
| A3-02 | Dùng UiScrollable tìm Sauce Labs Onesie | Tên đúng, lưu ảnh riêng phần tử và toàn màn hình |
| A4-01 | Tạo phiên, đọc session_id và capabilities | Có session_id; Android / UiAutomator2 / đúng udid |
| A4-02 | Đăng nhập, mở menu, chọn ALL ITEMS; mở chi tiết Backpack rồi back | Menu đóng, màn PRODUCTS trở lại, session_id giữ nguyên |
| A4-03 | Đăng nhập, mở menu rồi LOGOUT | Ô Username xuất hiện, PRODUCTS không còn |

Không coi lỗi kết nối/Appium hoặc đọc thiếu sản phẩm là PASS.
Ảnh/log được tạo từ lần chạy thật; lỗi được ghi rõ và sửa trước khi nộp.
