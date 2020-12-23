from psycopg2.pool import ThreadedConnectionPool
import logging
from contextlib import contextmanager

SQL_CONFIG = {
    'host': 'database',
    'port': '5432',
    'database': 'test_database',
    'user': 'test_user',
    'password': 'changethis'
}

pool = ThreadedConnectionPool(1, 20, **SQL_CONFIG)


@contextmanager
def get_db_connection():
    logging.info('get_db_connection: getting connection')
    try:
        connection = pool.getconn()
        yield connection
    finally:
        pool.putconn(connection)


@contextmanager
def get_db_cursor(commit=True):
    logging.info('get_db_cursor: getting cursor')
    with get_db_connection() as connection:
        cursor = connection.cursor()
        try:
            yield cursor
            if commit:
                connection.commit()
        finally:
            cursor.close()


def get_users():
    sql_query = 'SELECT * FROM users'

    with get_db_cursor() as cursor:
        cursor.execute(sql_query)
        data = cursor.fetchall()
        # TODO:
        # except psycopg2.ProgrammingError:
        # data = None

    return data

# class Test:
#     def __init__(self):
#         self.counter = 0

#     def sum_one(self):
#         self.counter += 1

#     def get_counter(self):
#         return self.counter

# class DataReader(object):
#     def __init__(self):
#         self.connection = psycopg2.connect(**SQL_CONFIG)
#         self.cursor = self.connection.cursor()

#     def get_users(self):
#         sql = 'SELECT * FROM users'
#         self.cursor.execute(sql)

#         try:
#             result = self.cursor.fetchall()
#         except psycopg2.ProgrammingError:
#             # no results of sql statement
#             result = None
#         return result

#     def close_connection(self):
#         self.connection.commit()
#         self.cursor.close()
#         self.connection.close()
