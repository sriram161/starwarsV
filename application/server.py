import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api

app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"

if __name__ == "__main__":
    app.run()
