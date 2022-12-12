from flask import Flask

from test import my_function

app = Flask(__name__)

@app.route('/')
def create_app():
    return my_function()
