Stock Correlation Calculator
This project contains a Python program that calculates the correlation of a given stock compared to a benchmark index. The program takes in the opening price of the stock and a CSV file containing the daily closing prices of the stock. It then calculates the daily returns of both the stock and the benchmark index, finds the dispersion of the benchmark index's returns from the mean, calculates the covariance between the two sets of returns, and ultimately outputs the correlation coefficient.

Prerequisites
To use this program, you will need to have Python 3 installed on your computer. Additionally, you will need to have the following Python modules installed:

csv
statistics
Getting Started
To use the program, simply download the correlation_calculator.py file and save it in a directory on your computer.

Next, create a CSV file that contains the daily closing prices of the benchmark index. The first row should contain column headers, and the following rows should contain the closing prices for each day. The program expects the data to be in descending order (i.e., the most recent date should be at the top of the file).

Create another CSV file that contains the daily closing prices of the stock you want to compare to the benchmark index. Again, the first row should contain column headers, and the following rows should contain the closing prices for each day in descending order.

In your Python environment, import the correlation_calculator.py file and call the co() function, passing in the correlation() function and the two CSV files as arguments. The co() function will return the correlation coefficient between the stock and the benchmark index
