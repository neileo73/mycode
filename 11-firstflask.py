#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def endoftheday():
    return "Class is nearing the end of the Wednesday"

if __name__ == "__main__":
    app.run(port=5006)
