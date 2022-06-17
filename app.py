from flask import Flask
from flask import Flask, render_template, request
import pickle
import sklearn
import numpy as np
try:

    model_RFC = pickle.load(open('loan_approve.pkl', 'rb'))

except FileNotFoundError as e:
    print(e)
app = Flask(__name__)
@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        Self_Employed = float(request.form['Self_Employed'])
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        Credit_History = float(request.form['Credit_History'])
        Property_Area = float(request.form['Property_Area'])

        output = model_RFC.predict(np.array([[Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]]))
        res = ""
        if output == 1:
            res = "Approved"
            return render_template('Prediction.html', predict_res=res)
        else:
            res = "Not allow"
            return render_template('Prediction_RF.html',predict_res = res)
@app.route("/result", methods=['GET'])
def result():
    pass
if __name__ == "__main__":
    app.debug = True
    app.run()