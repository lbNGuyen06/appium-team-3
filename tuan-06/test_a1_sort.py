"""A1: phát triển từ ý tưởng đọc/cuộn sản phẩm của Phạm Đức Tài, nhánh 7ec8731."""
import pytest
from selenium.common.exceptions import TimeoutException
from helpers import collect_catalog, sort_by, visible


@pytest.mark.parametrize("label,by_price", [
    ("Price (low to high)", True),
    ("Name (Z to A)", False),
], ids=["price_low_high", "name_z_a"])
def test_a1_sort(logged_in, evidence, label, by_price):
    sort_by(logged_in, label)
    products = collect_catalog(logged_in)
    values = list(products.values()) if by_price else list(products)
    assert values == sorted(values, reverse=not by_price), products
    evidence()


def test_a1_missing_element_timeout(logged_in, evidence):
    # Lỗi cố ý: chỉ TimeoutException là kết quả được chấp nhận.
    with pytest.raises(TimeoutException):
        visible(logged_in, "test-intentionally-missing", timeout=1)
    evidence()
