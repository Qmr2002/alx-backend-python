#!/usr/bin/python3
"""
1-batch_processing.py - Batch processing large data with Python generators.
"""

import mysql.connector
from mysql.connector import Error


def stream_users_in_batches(batch_size):
    """
    Generator that streams rows from the user_data table in batches.
    Args:
        batch_size (int): Number of rows per batch.
    Yields:
        list[dict]: A batch of rows as dictionaries.
    """
    connection = None
    cursor = None
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        # Fetch rows in batches
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    except Error as e:
        print(f"Database error: {e}")
    finally:
        # Ensure proper cleanup
        if cursor:
            try:
                cursor.close()
            except Error as e:
                print(f"Error closing cursor: {e}")
        if connection and connection.is_connected():  # Fixed the typo here
            try:
                connection.close()
            except Error as e:
                print(f"Error closing connection: {e}")


def batch_processing(batch_size):
    """
    Processes each batch to filter users over the age of 25.
    Args:
        batch_size (int): Number of rows per batch.
    """
    for batch in stream_users_in_batches(batch_size):
        # Filter users with age > 25
        filtered_users = (user for user in batch if user["age"] > 25)
        for user in filtered_users:
            print(user)


if __name__ == "__main__":
    batch_processing(50)
