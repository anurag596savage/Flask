from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

app.run(port=5006)
