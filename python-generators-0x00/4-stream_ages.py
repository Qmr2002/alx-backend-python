#!/usr/bin/python3
"""
4-stream_ages.py - Memory-efficient aggregation with Python generators.
"""

import mysql.connector
from seed import connect_to_prodev  # Import connect_to_prodev from seed.py


def stream_user_ages():
    """
    Generator that streams user ages from the user_data table.
    Yields:
        int: The age of a user.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT age FROM user_data;")
        for row in cursor:
            yield int(row[0])  # Extract age as an integer
    finally:
        cursor.close()
        connection.close()


def calculate_average_age():
    """
    Calculates the average age of users using the stream_user_ages generator.
    Prints:
        str: Average age of users.
    """
    total_age = 0
    count = 0
    for age in stream_user_ages():
        total_age += age
        count += 1
    if count > 0:
        print(f"Average age of users: {total_age / count}")
    else:
        print("No users found to calculate average age.")


if __name__ == "__main__":
    calculate_average_age()
