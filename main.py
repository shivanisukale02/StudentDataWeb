import flask
from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def Student():
    return "student info"

@app.route("/search")
def SearchByAdno():
    return "search by admn no"

@app.route("/delete")
def DeletebyAdno():
    return "delete by admo no"

if __name__=="__main__":
    app.run()