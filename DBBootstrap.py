from sqlalchemy import *
from sqlalchemy.exc import OperationalError


username = 'postgres'
password = 'password'
host = 'postgres'
port = '5432'
database = 'test'


def get_engine():
    return create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, database))


def get_connection_to_database():
    return (get_engine()).connect()


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

    metadata = MetaData(get_engine())
    table = Table('example', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('text_value', String),
                  Column('select_value', String)
                  )

    metadata.create_all()