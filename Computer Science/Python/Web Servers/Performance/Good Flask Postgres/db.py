import psycopg2

SQL_CONFIG = {
    'host': 'database',
    'port': '5432',
    'database': 'test_database',
    'user': 'test_user',
    'password': 'changethis'
}

def get_users():
    connection = psycopg2.connect(**SQL_CONFIG)
    cursor = connection.cursor()

    sql = 'SELECT * FROM users'

    cursor.execute(sql)

    try:
        result = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # no results of sql statement
        result = None
    finally:
        connection.commit()
        cursor.close()
        connection.close()
    return result

class DataReader(object):
    def __init__(self):
        self.connection = psycopg2.connect(**SQL_CONFIG)
        self.cursor = self.connection.cursor()

    def get_users(self):
        sql = 'SELECT * FROM users'
        self.cursor.execute(sql)

        try:
            result = self.cursor.fetchall()
        except psycopg2.ProgrammingError:
            # no results of sql statement
            result = None
        return result

    def close_connection(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

