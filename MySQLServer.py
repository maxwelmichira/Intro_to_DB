import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="alx_user",
        password="alx_pass"
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error while connecting to MySQL: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

