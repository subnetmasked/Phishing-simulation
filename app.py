from flask import Flask, request, redirect, render_template
import csv
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
