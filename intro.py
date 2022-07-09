#!pip install flask
from flask import Flask# import numpy as np
# from sklearn.linear_model import LinearRegression
#-------------------------------------------------------------
#reg = LinearRegression()
#creating a instance of class ---object(reg)
#reg.fit(x,y)

### This is just for your refrence#Intialization of flask
app = Flask(__name__)#dir structure is required .and__name__ take care of the dir struct
#created a instance of flask so that we can use any functionality 

@app.route("/")# it binds the website with sepcific url
def hello():
    return "Hurray to the AKASH'S Session "
print(__name__)
            
if __name__=="__main__":
    app.run(debug=True)