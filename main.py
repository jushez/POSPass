from flask import Flask
from admin.second import second
from back.index import indexgg

app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")
app.register_blueprint(indexgg, url_prefix="/gg")


@app.route("/")
def test():
    return "<h1>Test..</h1>"


if __name__ == "__main__":
    app.run(debug=True)