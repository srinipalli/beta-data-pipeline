import os
from dotenv import load_dotenv

load_dotenv()

H = os.getenv("MYSQL_HOST")
U = os.getenv("MYSQL_USER")
P = os.getenv("MYSQL_PASSWORD")
D = os.getenv("MYSQL_DB")

import mysql.connector

mydb = mysql.connector.connect(
    host = H,
    user = U,
    password = P,
    database = D
)
cursor = mydb.cursor()
cursor.execute(f"select * from stage{input("enter stage name: ")};")
print(type(cursor.fetchone()[0]))