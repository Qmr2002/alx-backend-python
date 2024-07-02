#!/usr/bin/env python3

from client import GithubOrgClient
import unittest
from typing import Any, Dict, Tuple, Union
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
from fixtures import TEST_PAYLOAD

from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int],
                               ) -> None:
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception,
    ) -> None:
        """
        Test that access_nested_map raises the expected exception.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), str(path[-1]))

# task 2


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


class TestMemoize(unittest.TestCase):
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


class TestGithubOrgClient(unittest.TestCase):
    """Github Org Client test class
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """Test TestGithubOrgClient.org return the correct value
        """
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock.called_with_once(test_class.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test TestGithubOrgClient.public_repos_url
        return the correct value based on the given payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "something"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Test TestGithubOrgClient.test_public_repos
        return the correct value
        """
        payloads = [{"name": "google"}, {"name": "Twitter"}]
        mock_json.return_value = payloads

        with patch('client.GithubOrgClient._public_repos_url') as mock_public:
            mock_public.return_value = "hey there!"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected = [p["name"] for p in payloads]
            self.assertEqual(result, expected)

            mock_json.called_with_once()
            mock_public.called_with_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test TestGithubOrgClient.has_license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integeration test for Fixtures
    """
    @classmethod
    def setUpClass(cls):
        """Run set up before the actual test
        """
        config = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}

        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repo(self):
        """Integration test: public_repo
        """
        test_class = GithubOrgClient('Google')

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Run after the actual test
        """
        cls.get_patcher.stop()
