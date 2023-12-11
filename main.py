import mysql.connector
from mysql.connector import Error
import datetime

def create_connection(host_name, user_name, user_password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=user_password,
        database=database
    )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
connection = create_connection("localhost", "sqluse", "password", "human_friends")

select_students_query = "SELECT * FROM animals"
with connection.cursor() as cursor:
    cursor.execute(select_students_query)
    result = cursor.fetchall()
    for row in result:
        print(row)
