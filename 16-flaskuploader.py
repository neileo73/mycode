#!/usr/bin/python3
import re
import json

# this works if you "python3 -m pip install flask"
from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/upload")
def upload_file():
    return render_template("upload.html")

@app.route("/uploader", methods =["post"])
def uploader():
    if request.method == "POST": # if we get a post
        mysteryfile = request.files["file"] # pull off the file attachment on the post
        mysteryfile.save(secure_filename(mysteryfile.filename)) # save the file
        if "cap" in mysteryfile.filename:
            return redirect(url_for("sip", filetoparse=mysteryfile.filename))
        else:
            return "That format is not yet supported. Please check back soon."

@app.route("/sip/<filetoparse>")
def sip(filetoparse):
    sipjson = []
    with open(filetoparse) as capture:
        for line in capture:
            matchobj = re.search(r"sip:\+(\d+)@\[(.*)\]:?(\d+)", line)
            if matchobj:
                tinylist = []
                tinylist.append(matchobj.group())
                tinylist.append(matchobj.group(1))
                tinylist.append(matchobj.group(2))
                tinylist.append(matchobj.group(3))
                sipjson.append(tinylist)
        return json.dumps(sipjson)

if __name__ == "__main__":

    app.run(port = 5006)



