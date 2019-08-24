from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'API for the management of accesses to BITZ'
