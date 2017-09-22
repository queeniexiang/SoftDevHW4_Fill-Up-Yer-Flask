"""
Queenie Xiang
SoftDev1 pd7
HW4 -- Fill Up Yer Flask
2017-09-22
""" 

#import from the Flask module (Class) the flask function(?) 
from flask import Flask
app = Flask(__name__)


#assign following fxn to run when root route requested 
@app.route("/") 
def hello_world():
    retStr = ""
    retStr += "<center>Hello, nice to meet you! Click on the picture for a surprise!<br>" 
    retStr += "<a href = /dogs>"
    retStr += "<img src = /static/quokka.jpg> </a> <br>  </center>" 
    
    return retStr 

@app.route("/dogs")
def hello_world2():
    retStr = "";
    retStr += "<center> Click one below!!<br>" 
    retStr += "<a href = /cats>"
    retStr += "<img src = /static/dog1.jpg height='300' width='400'>"
    retStr += "<img src = /static/dog4.gif> <br>"
    retStr += "<img src = /static/dog2.jpg> <br>"
    retStr += "<img src = /static/dog3.jpg> <br> </a> </center>"
    return retStr


@app.route("/cats")
def hello_world3():
    retStr = ""
    retStr += "<center> Have a great day! <br>"
    retStr += "<img src = /static/cat1.gif> <br>"
    retStr += "<img src = /static/cat2.gif> <br> </center>"

    return retStr


if __name__ == "__main__":
    app.debug = True
    app.run()

