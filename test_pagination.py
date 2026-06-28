import pytest
from pagination import paginate


def test_first_page():
    items = list(range(10))
    result = paginate(items, page=1, limit=3)
    assert result["data"] == [0, 1, 2]
    assert result["page"] == 1
    assert result["total"] == 10
    assert result["total_pages"] == 4


def test_last_page_partial():
    items = list(range(10))
    result = paginate(items, page=4, limit=3)
    assert result["data"] == [9]


def test_empty_list():
    result = paginate([], page=1, limit=10)
    assert result["data"] == []
    assert result["total"] == 0
    assert result["total_pages"] == 1


def test_single_page():
    items = list(range(5))
    result = paginate(items, page=1, limit=10)
    assert result["data"] == items
    assert result["total_pages"] == 1


def test_out_of_bounds_page():
    items = list(range(5))
    result = paginate(items, page=99, limit=10)
    assert result["data"] == []
