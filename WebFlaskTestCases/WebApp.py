#1.Library
from flask import Flask

#2.Prepare app object
app=Flask(__name__)

#3.Add Routing & Function Defination
@app.route("/")
def indexPage():
    return "Welcome to Python Project"

@app.route("/about")
def aboutPage():
    return "My name is Mujahed"

#4.Run app Object
if __name__ ==  '__main__':
    app.run(host="0.0.0.0",port=5000)