from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def parse_response():
    if request.method == 'POST':
        print(request.form)
        return 'received post'
    return 'woo2'

if __name__ == '__main__':
    app.run()
