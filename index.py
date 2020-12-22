from flask import Flask, flash, request, redirect, url_for, render_template
from Encoder import encod
from decoder import decod

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def up():
    return render_template("index.html", flag=0)


@app.route("/enc", methods=["GET", "POST"])
def op():
    if request.method == "POST":
        opt = request.form["option"]
        if opt == "e":
            return render_template("index.html", flag=1, img=0)
        if opt == "d":
            return render_template("index.html", flag=2, img=0)
    return render_template("index.html", flag=0, img=0)


@app.route("/enci", methods=["GET", "POST"])
def enc():
    if request.method == "POST":
        m = request.form["inptxt"]
        f = open("static\data.txt", "w")
        f.write(m)
        f.close()
        encod()
    return render_template("index.html", flag=1, img=1)


@app.route("/deci", methods=["GET", "POST"])
def dei():
    if request.method == "POST":
        f = request.files["file"]
        f.save("static\enimg.tiff")
        data = decod()
    return render_template("index.html", flag=2, img=1, data=data)


if __name__ == "__main__":

    app.run(threaded=Tree, port=5000)

