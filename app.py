from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "website content"


@app.route('/about/')
def about():
    return "this is the about us page"


if __name__ == "__main__":
    app.run(debug=True)
