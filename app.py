import pickle
lr = pickle.load(open("lr_c33.pkl",'rb'))


import numpy as np
from flask import Flask,request,jsonify,render_template
app = Flask(__name__)

@app.route("/")
def homepage():
	return render_template("index.html")
	
	
@app.route("/predict",methods=['POST']) 
def predict(): 
    #li=[]
    #for x in request.form.values():
    #    li.append(int(x)
    pre = lr.predict([[int(x) for x in request.form.values()]])
    return render_template("index.html",prediction_text="your salary would be"+str(pre))
    
    
if __name__=="__main__":
    app.run(port=5001,debug=True)