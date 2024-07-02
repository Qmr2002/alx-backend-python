#!/usr/bin/env python3

import unittest

from typing import Dict, Tuple, Union

# run the test method with different sets of parameters.
from parameterized import parameterized

# Access nested map with key path.
from utils import access_nested_map

# Get JSON from remote URL.
from utils import get_json

# patch():Allows patching module and class-level attributes within the scope of a test.
# Mock: Basic mock object where you define behaviors and assertions.
from unittest.mock import patch, Mock


from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict,
                                               int],
                               ) -> None:
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

# nested_map={"a": 1}, path=("a",)
# nested_map={"a": {"b": 2}}, path=("a",)
# nested_map={"a": {"b": 2}}, path=("a", "b")

# @parameterized.expand([
#     (input1, input2, expected_output),
#     (input3, input4, expected_output),
#     ...
# ])


# @parameterized.expand([
#     ({"a": 1}, ("a",), 1),
#     ({"a": {"b": 2}}, ("a",), {"b": 2}),
#     ({"a": {"b": 2}}, ("a", "b"), 2)
# ])


    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
# nested_map={}, path=("a",)
# nested_map={"a": 1}, path=("a", "b")
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception,
    ) -> None:
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)

        # # The KeyError message should be the string representation of
        # #  the last key in the path tuple.
        # self.assertEquel(str(error.exception), str(path[-1]))

# task 2
# Explanation
#   Mocking HTTP Calls:

#   Use unittest.mock.patch to mock requests.get and return a mock response.
#   The mock response should have a json method that returns a predefined payload.
#   Parameterizing Tests:

#   Use @parameterized.expand to run the test with different sets of inputs (URL and payload).
# Assertions:
# Ensure the mocked get method is called once with the correct URL.
# Verify that the output of utils.get_json matches the expected payload.
# Steps:
#   Define the Test Class: Ensure the TestGetJson class inherits from unittest.TestCase.
#   Mock requests.get: Use unittest.mock.patch to mock requests.get.
#   Set Up the Mock Response: Define the mock response and its json method to return the test payload.
#   Assertions: Check that requests.get is called once and that get_json
#   returns the expected payload.


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected result.
        """
        with patch('utils.requests.get') as mock_get:
            # Create a mock response object
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Assert that requests.get was called exactly once with the test
            # URL
            mock_get.assert_called_once_with(test_url)

            # Assert that the output of get_json is equal to the test_payload
            self.assertEqual(result, test_payload)


# task 4
# Steps:
    # Define the TestMemoize Class: Create a test class inheriting from unittest.TestCase.
    # Define TestClass: Inside the test method, define a class TestClass with:
    #   a_method that returns a value.
    #   a_property decorated with @memoize, which calls a_method.
    # Mock a_method: Use unittest.mock.patch to mock a_method.
    # Test a_property: Call a_property twice and verify:
    #   The correct result is returned.
    #   a_method is only called once.


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_obj = TestClass()

        # Patch a_method to track its calls
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # Call a_property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Assert that the correct result is returned
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that a_method was only called once
            mock_method.assert_called_once()



# TASK 5
# Step-by-Step Guide
# Familiarize with GithubOrgClient Class:

# The GithubOrgClient class likely has a method org which retrieves information
#  about a GitHub organization.
#  This method might internally call a get_json function to fetch data
# from a URL.
# Setup test_client.py:

# Create a new file named test_client.py.
# Import Necessary Modules:

# Import unittest, patch, parameterized, and GithubOrgClient.
# Define TestGithubOrgClient Class:

# This class will inherit from unittest.TestCase.
# Implement test_org Method:

# Use @patch to mock get_json so no actual HTTP requests are made.
# Use @parameterized.expand to test multiple organization names.
# Test that GithubOrgClient.org returns the correct value and that
# get_json is called with the expected arguments.



from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class to test GithubOrgClient.org method.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        # Set up the mock to return a specific value
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()

        # Assert that get_json was called once with the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Assert that the result is what we expect
        self.assertEqual(result, {"login": org_name})
