#!/usr/bin/env python3
"""
seed.py - Setup MySQL database and seed it with data from user_data.csv
"""
import uuid 
import mysql.connector
from mysql.connector import Error
import csv
import os


def connect_db():
    """Connect to the MySQL server."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password=""  # Replace with your MySQL password
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_database(connection):
    """Create the ALX_prodev database if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        print("Database ALX_prodev created successfully (if not exists).")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()


def connect_to_prodev():
    """Connect to the ALX_prodev database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="ALX_prodev"
        )
        return connection
    except Error as e:
        print(f"Error connecting to ALX_prodev database: {e}")
        return None


def create_table(connection):
    """Create the user_data table if it does not exist."""
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL(3,0) NOT NULL
            );
        """)
        print("Table user_data created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")
    finally:
        cursor.close()


def insert_data(connection, csv_file):
    """Insert data into the user_data table from a CSV file."""
    if not os.path.exists(csv_file):
        print(f"File {csv_file} not found.")
        return

    try:
        cursor = connection.cursor()
        with open(csv_file, mode="r") as file:
            csv_reader = csv.DictReader(file)

            # Check if headers are present
            if not csv_reader.fieldnames or {'name', 'email', 'age'} - set(csv_reader.fieldnames):
                print(f"CSV file headers must include: name, email, age")
                return

            for row in csv_reader:
                user_id = str(uuid.uuid4())  # Generate a unique user_id
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE 
                    name=VALUES(name), email=VALUES(email), age=VALUES(age);
                """, (user_id, row["name"], row["email"], row["age"]))
            connection.commit()
            print("Data inserted successfully.")
    except Error as e:
        print(f"Error reading or inserting data from CSV: {e}")
    finally:
        cursor.close()



# Example usage of the module
if __name__ == "__main__":
    connection = connect_db()
    if connection:
        create_database(connection)
        connection.close()

        connection = connect_to_prodev()
        if connection:
            create_table(connection)
            insert_data(connection, "user_data.csv")
            connection.close()
