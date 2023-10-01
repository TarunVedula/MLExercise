# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request, jsonify
from model import predict_receipts

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API route for predictions
@app.route('/api/predict', methods=['POST'])
def predict_api():
    try:
        date = request.form['date']
        predicted_value = predict_receipts(date)
        return jsonify({'predicted_value': predicted_value})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
