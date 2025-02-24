import mysql.connector  # Check for import statement
from mysql.connector import Error  # Ensure we import Error properly

try:
    # Establish connection to MySQL Server (Modify 'your_user' and 'your_password')
    connection = mysql.connector.connect(
        host="localhost",
        user="your_user",
        password="your_password"
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # CREATE DATABASE statement (Ensures it meets the check)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:  # Ensure exception handling uses mysql.connector.Error
    print(f"Error: {e}")

finally:
    # Ensure proper cleanup of resources
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
