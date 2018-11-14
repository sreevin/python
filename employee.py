from flask import Flask, render_template, request
from data import Employees

app=Flask(__name__)

getEmployees = Employees()

@app.route('/employees')
def stud():
    return render_template('empdetails.html',myEmployeelist=getEmployees)

@app.route('/')
def home():
    return render_template('home.html')


if(__name__=='__main__'):
    app.run(debug=True)