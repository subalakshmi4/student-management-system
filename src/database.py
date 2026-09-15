import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def create_connection():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="student_management",
        connection_timeout=5,
        use_pure=True
    )

    return connection