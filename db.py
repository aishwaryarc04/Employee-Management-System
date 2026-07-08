import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aishu@2004",
        database="employee_management"
    )

    return conn