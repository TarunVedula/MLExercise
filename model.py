# -*- coding: utf-8 -*-
import csv
import numpy as np
 

# Load data from the CSV file
def load_data(file_path):
    dates = []
    receipts = []

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            dates.append(row[0])
            receipts.append(int(row[1]))

    return dates, receipts

# Convert dates to numeric values (days since the start)
def convert_dates_to_numeric(dates):
    numeric_dates = [i for i in range(1, len(dates) + 1)]
    return numeric_dates

# Simple linear regression model
def simple_linear_regression(x, y):
    n = len(x)
   
    # Calculate the mean of x and y
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate the slope (m) and y-intercept (b) of the regression line
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean)**2 for i in range(n))

    m = numerator / denominator
    b = y_mean - m * x_mean

    return m, b

# Predict values using the regression model
def predict_values(x, m, b):
    return [m * xi + b for xi in x]

# Function to predict receipts for a given date
def predict_receipts(input_date):
    # Load data from the CSV file
    file_path = 'data_daily.csv'
    dates, receipts = load_data(file_path)

    # Convert dates to numeric values
    numeric_dates = convert_dates_to_numeric(dates)

    # Perform simple linear regression
    m, b = simple_linear_regression(numeric_dates, receipts)

    # Convert the input date to a numeric value
    input_numeric_date = len(dates) + 1 + numeric_dates[-1]

    # Predict value for the input date
    prediction = m * input_numeric_date + b

    return prediction


