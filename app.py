import os

from flask import Flask, request, Response
from sqlalchemy import *
from ModelRepository import ModelRepository
from dotenv import load_dotenv
from pathlib import Path
from model import Model

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

username = os.getenv('POSTGRES_USERNAME')
password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST')
port = os.getenv('POSTGRES_PORT')
database = os.getenv('POSTGRES_DATABASE')

repository = ModelRepository(
            create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, database))
        )

@app.route('/model', methods=['POST'])
def insert_model():
    if request.method == 'POST':

        repository.put(
            Model(request.form['text_value'], request.form['select_value'])
        )
        return Response(status=200)


if __name__ == '__main__':
    app.run()
