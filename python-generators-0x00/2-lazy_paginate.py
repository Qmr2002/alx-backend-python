#!/usr/bin/python3
"""
2-lazy_paginate.py - Lazy loading paginated data with Python generators.
"""

import mysql.connector
from seed import connect_to_prodev  # Import connect_to_prodev from seed.py


def paginate_users(page_size, offset):
    """
    Fetch a single page of user data from the user_data table.
    Args:
        page_size (int): Number of rows per page.
        offset (int): Offset for the SQL query.
    Returns:
        list[dict]: A list of rows as dictionaries.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
        rows = cursor.fetchall()
        return rows
    finally:
        cursor.close()
        connection.close()


def lazy_paginate(page_size):
    """
    Generator that lazily loads paginated data from the user_data table.
    Args:
        page_size (int): Number of rows per page.
    Yields:
        list[dict]: A page of rows as dictionaries.
    """
    offset = 0
    while True:
        page = paginate_users(page_size, offset)
        if not page:  # Stop if the page is empty
            break
        yield page
        offset += page_size  # Move to the next page
