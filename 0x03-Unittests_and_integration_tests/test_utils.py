#!/usr/bin/env python3
"""First Task"""
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any, ClassVar
from unittest import main, TestCase
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(TestCase):
    """Test cases for the access_nested_map function.

    This class contains tests to ensure the access_nested_map function
    works correctly for various inputs.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """Test access_nested_map with different nested maps and paths.

        Args:
            nested_map (Mapping): A nested dictionary from which to access
            a value.
            path (Sequence): A sequence of keys representing the path to
            the value.
            expected (Any): The expected value at the end of the path.

        Asserts:
            That access_nested_map(nested_map, path) returns the expected value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """_summary_

        Args:
            nested_map (Mapping): _description_
            path (Sequence): _description_
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """_summary_

    Args:
        TestCase (_type_): _description_
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: object, url_get: Any):
        """_summary_

        Args:
            test_url (_type_): _description_
            test_payload (_type_): _description_
        """
        response = Mock()
        response.json.return_value = test_payload
        url_get.return_value = response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(TestCase):
    """Test cases for the memoize decorator.

    This class contains tests to ensure the memoize decorator works correctly,
    caching the result of a method call and returning the cached result on
    subsequent calls.

    Args:
        TestCase (unittest.TestCase): The base class for all unit test cases.
    """

    def test_memoize(self) -> Any:
        """Test memoization of a property method.

        This test defines a nested class `TestClass` with a method `a_method`
        and a memoized property `a_property`. The `a_property` method is
        decorated with `memoize` to cache its result. The test verifies that
        the memoization works as expected by asserting that:

        1. The result of `a_property` is cached and the same on subsequent call
        2. The result of `a_property` is equal to the expected value `42`.

        Returns:
            None
        """
        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()
        instance = TestClass()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            result_1 = instance.a_property
            result_2 = instance.a_property

            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    """Entry Point"""
    main()
