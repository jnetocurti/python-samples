import os
from mysql.connector import connect
from contextlib import contextmanager

params = {
    "host": os.getenv('MYSQL_HOST'),
    "port": os.getenv('MYSQL_PORT'),
    "user": os.getenv('MYSQL_USER'),
    "password": os.getenv('MYSQL_PASSWORD'),
    "database": os.getenv('MYSQL_DATABASE')
}


@contextmanager
def connection():
    conn = connect(**params)
    try:
        yield conn
    finally:
        if conn and conn.is_connected():
            conn.close()
