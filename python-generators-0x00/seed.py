import csv
import uuid
import mysql.connector
from mysql.connector import errorcode

# ------------------ CONNECT TO MYSQL SERVER ------------------ #
def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password"  # remplace par ton mot de passe
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# ------------------ CREATE DATABASE ------------------ #
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

# ------------------ CONNECT TO ALX_prodev DB ------------------ #
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_mysql_password",
            database="ALX_prodev"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to ALX_prodev: {err}")
        return None

# ------------------ CREATE TABLE user_data ------------------ #
def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(5, 2) NOT NULL,
        INDEX(user_id)
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Table user_data created successfully")
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Failed to create table: {err}")

# ------------------ INSERT DATA FROM CSV ------------------ #
def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                user_id = str(uuid.UUID(row['user_id']))  # assure valid UUID
                name = row['name']
                email = row['email']
                age = float(row['age'])

                # insert if not exists (assume user_id is unique)
                cursor.execute("""
                    INSERT IGNORE INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s);
                """, (user_id, name, email, age))
        connection.commit()
        print("Data inserted successfully")
        cursor.close()
    except Exception as e:
        print(f"Error inserting data: {e}")
