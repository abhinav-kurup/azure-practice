from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    key = os.environ.get('key')
    return f"<html><body><h1>Flask Deployment successful, Key: {key}</h1></body></html>\n"