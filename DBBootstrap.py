from sqlalchemy import *
from sqlalchemy.exc import OperationalError

import os

username = 'postgres'
password = 'password'
# host = 'localhost'
host = 'postgres'
# port = '5555'
port = '5432'
database = 'test'


def get_connection_to_database():
    return (create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, database))).connect()


def verify_database_exists():
    try:
        (get_connection_to_database()).close()
        return True
    except OperationalError:
        return False


if __name__ == "__main__":
    print("Checking to see if %s database table exists" % (database))

    if verify_database_exists():
        print("Database %s exists!" % (database))
    else:
        print("Was unable to find %s on host %s" % (database, host))
        result = input("Would you like to create %s on host%s:%s ? [y/n]" % (database, host, port))
        if result.lower() == 'y':
            conn = (create_engine(
                "postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, 'postgres')
            )).connect()
            # Have to commit to end the transaction
            conn.execute('COMMIT')
            conn.execute("CREATE DATABASE %s" % database)
            conn.close()
            print("Database %s created!" % database)

    print("Checking to see if the required tables exist")
    conn = get_connection_to_database()
    queryResult = conn.execute("""
    SELECT 1 AS "exists"
       FROM   information_schema.tables 
       WHERE  table_name = 'example_table'
    """).fetchone()

    if queryResult is None:
        conn.execute("""
        CREATE TABLE example_table (
          input_value varchar,
          select_value varchar
        );
        """)
        conn.close()
        print("Created example_table table in %s" % (database))
    else:
        print('Table already exists! You\'re ready to go!')