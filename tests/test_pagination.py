"""Tests for pagination.paginate. Run: python -m unittest discover -s tests -v"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from pagination import paginate  # noqa: E402


class Paginate(unittest.TestCase):
    def test_first_page(self):
        r = paginate(list(range(120)), page=1, limit=50)
        self.assertEqual(r["data"], list(range(50)))
        self.assertEqual((r["page"], r["limit"], r["total"], r["total_pages"]), (1, 50, 120, 3))

    def test_last_partial_page(self):
        self.assertEqual(paginate(list(range(120)), page=3, limit=50)["data"], list(range(100, 120)))

    def test_page_beyond_range_is_empty(self):
        r = paginate(list(range(10)), page=5, limit=5)
        self.assertEqual(r["data"], [])
        self.assertEqual(r["total_pages"], 2)

    def test_empty_list_has_one_page(self):
        r = paginate([], page=1, limit=50)
        self.assertEqual((r["data"], r["total"], r["total_pages"]), ([], 0, 1))

    def test_exact_multiple(self):
        self.assertEqual(paginate(list(range(100)), limit=50)["total_pages"], 2)

    def test_defaults(self):
        r = paginate(list(range(3)))
        self.assertEqual((r["page"], r["limit"], r["data"]), (1, 50, [0, 1, 2]))


if __name__ == "__main__":
    unittest.main()
