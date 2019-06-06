#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def endoftheday():
    return "Class is nearing the end of the Wednesday"

@app.route("/hello/<name>", defaults={'position': 'Administrative Assistant'})
@app.route("/hello/<name>/<position>")
def hellostudents(name, position):
    return "Hello {1} {0} I am pleased to meet you {0}".format(name, position)
    return "Welcome to class..." + name

if __name__ == "__main__":
    app.run(port=5006)
