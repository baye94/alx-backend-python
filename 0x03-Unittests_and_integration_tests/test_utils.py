#!/usr/bin/env python3
"""
a class to test the utils.py file
"""
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    a class to test the utils.py file
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        a test to test the access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        a test to test the access_nested_map function
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    a class to test get json method
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, payload):
        """
        a test to test the get_json function
        """
        with patch("utils.requests.get") as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(get_json(test_url), payload)
            self.assertEqual(mock_get.call_count, 1)


class TestMemoize(unittest.TestCase):
    """
    a class to test memoize method
    """

    def test_memoize(self):
        """
        a test to test the memoize function
        """

        class TestClass:
            """
            a test to test the memoize function
            """

            def a_method(self):
                """
                a test to test the memoize function
                """
                return 42

            @memoize
            def a_property(self):
                """
                a test to test the memoize function
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            test_object = TestClass()
            test_object.a_property()
            test_object.a_property()
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
