from flask import Flask
from flask-restplus import Api

app = Flask(__name__)

@app.route("/")
def hello():
        return "Hello World!"

if __name__ == "__main__":
    app.run()
