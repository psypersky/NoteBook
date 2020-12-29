import psycopg2.extras
from psycopg2.pool import ThreadedConnectionPool
import logging
from contextlib import contextmanager
from errors import ConnectionPoolExhausted

SQL_CONFIG = {
    'host': 'database',
    'port': '5432',
    'database': 'test_database',
    'user': 'test_user',
    'password': 'changethis'
}

'''
New minconn connections are created automatically.
The pool will support a maximum of about maxconn connections.
*args and **kwargs are passed to the connect() function.
'''
MINCONN = 1
MAXCONN = 20

pool = ThreadedConnectionPool(MINCONN, MAXCONN, **SQL_CONFIG)


@contextmanager
def get_db_connection():
    logging.info('get_db_connection: getting connection')
    connection = None
    try:
        connection = pool.getconn()
        yield connection
    except psycopg2.pool.PoolError as error:
        if (str(error) == 'connection pool exhausted'):
            logging.warning('get_db_connection: connection pool exhausted')
            raise ConnectionPoolExhausted()
    finally:
        if (connection is not None):
            pool.putconn(connection)


@contextmanager
def get_db_cursor(commit=True):
    logging.info('get_db_cursor: getting cursor')
    with get_db_connection() as connection:
        cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
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
        logging.info('get_users: users:')
        logging.info(data)
        # TODO:
        # except psycopg2.ProgrammingError:
        # data = None

    return data
