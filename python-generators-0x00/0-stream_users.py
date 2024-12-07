#!/usr/bin/python3
"""
0-stream_users.py - A generator that streams rows from the user_data table
"""

from itertools import islice
import mysql.connector
from mysql.connector import Error


def stream_users():
    """Generator that streams rows from the user_data table."""
    try:
        # Connect to the ALX_prodev database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)  # Return rows as dictionaries
        cursor.execute("SELECT * FROM user_data;")  # Execute the query

        # Yield rows one by one
        for row in cursor:
            yield row

        # Consume all remaining results (important for cleanup)
        cursor.fetchall()
    except Error as e:
        print(f"Database error: {e}")
    finally:
        # Ensure proper cleanup
        try:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
        except Error as e:
            print(f"Error during cleanup: {e}")




for user in islice(stream_users(), 6):
    print(user)


