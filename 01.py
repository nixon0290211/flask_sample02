from flask import Flask
n

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Member!"


if __name__ == "__main__":
    app.run(debug=True)

