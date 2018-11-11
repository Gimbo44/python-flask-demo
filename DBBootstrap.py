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

    metadata = MetaData(get_engine())
    table = Table('example', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('text_value', String),
                  Column('select_value', String)
                  )

    metadata.create_all()