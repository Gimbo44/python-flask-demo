from flask import Flask, request, Response
from sqlalchemy import *
from ModelRepository import ModelRepository
from model import Model

app = Flask(__name__)

username = 'postgres'
password = 'password'
host = 'postgres'
port = '5432'
database = 'test'

repository = ModelRepository(
            create_engine("postgresql://%s:%s@%s:%s/%s" % (username, password, host, port, database))
        )

@app.route('/', methods=['POST'])
def insert_model():
    if request.method == 'POST':
        print(request.form)

        repository.put(
            Model(request.form['text_value'], request.form['select_value'])
        )
        return Response(status=200)

@app.route('/list', methods=['GET'])
def get_all_models():
    print(repository.get_all())
    return Response(status=200)

if __name__ == '__main__':
    app.run()
