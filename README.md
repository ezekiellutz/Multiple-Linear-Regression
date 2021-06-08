# Multiple Linear Regression
An ordinary least squares regression model that accurately predicts the Co2 emissions of new vehicles.

# Installation Instructions
Download both the .py and .csv files and place them in the same directory on your PC. Run the code from your IDE.

It is recommended that this script be run in Spyder 4.2.5 [conda (Python 3.8.8)]. 

# Description
This python script builds an ordinary least squares multiple linear regression model that accurately predicts Co2 emissions for newly manufactured vehicles. In order to do this, the model predicts the Co2 emissions of a vehicle based on three different independent variables. In this model, the three independent variables are engine size, number of cylinders, and fuel consumption. The model trains itelf using 80% of the data, randomly selected, and calculates the coefficients and intercept of the fitted regression line. The model does this 5,000 times, averages the calculated coefficients and intercept, and then uses these averaged values to predict the Co2 emissions of a vehicle using user input parameters.

The python code creates a basic user interface using the console that allows the user to calculate multiple vehicles at one time and exit once complete. 

# How the Model Works
As mentioend before, the model here uses Ordinary least squares regression to predict the Co2 emissions of new vehicles. At a high level, ordinary least squares regresson (OLSR) minimizes the sum of the squared residual errors. Given a fitted regression line through the data, the model calculates the distance from each data point to the fitted regression line, squares it, and finds the sum of the squared residual errors. This quantity is what the model minimizes in order to make itself accurate.

OLSR treats the data as a matrix and uses linear algebra to estimate the optimal values for the coefficients. While building a model using OLSR results in a highly repeatable model that is reasonably accurate, it can take a very long time for the CPU of the PC to perform all of the matrix operations required. As a general rule, data sets with 10,000 rows or less are suitable for OLSR. Otherwise an optimization approach, such as a gradient descent model. 



