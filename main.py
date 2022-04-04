import flask
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def Student():
    return render_template("StudInfo.html")

@app.route("/search")
def SearchByAdno():
    return render_template("Search.html")

@app.route("/delete")
def DeletebyAdno():
    return render_template("Delete.html")

if __name__=="__main__":
    app.run()