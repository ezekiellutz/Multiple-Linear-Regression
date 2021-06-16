# Multiple Linear Regression
An ordinary least squares regression model that accurately predicts the Co2 emissions of new vehicles.

# Installation Instructions
Download both the .py and .csv files and place them in the same directory on your PC. Run the code from your IDE.

It is recommended that this script be run in Spyder 4.2.5 [conda (Python 3.8.8)]. 

# Description
This python script builds an ordinary least squares multiple linear regression model that accurately predicts Co2 emissions for newly manufactured vehicles. In order to do this, the model predicts the Co2 emissions of a vehicle based on three different independent variables. In this model, the three independent variables are engine size, number of cylinders, and fuel consumption. The model trains itelf using 80% of the data, randomly selected, and calculates the coefficients and intercept of the fitted regression line. The model does this 5,000 times, averages the calculated coefficients and intercept, and then uses these averaged values to predict the Co2 emissions of a vehicle using user input parameters.

The python code creates a basic user interface using the console that allows the user to calculate multiple vehicles at one time and exit once complete. 

# How the Model Works
As mentioend before, the model here uses ordinary least squares regression to predict the Co2 emissions of new vehicles. At a high level, ordinary least squares regresson (OLSR) minimizes the sum of the squared residual errors. Given a fitted regression line through the data, the model calculates the distance from each data point to the fitted regression line, squares it, and finds the sum of the squared residual errors. This quantity is what the model minimizes in order to make itself accurate.

OLSR treats the data as a matrix and uses linear algebra to estimate the optimal values for the coefficients. While building a model using OLSR results in a highly repeatable model that is reasonably accurate, it can take a very long time for the CPU of the PC to perform all of the matrix operations required. As a general rule, data sets with 10,000 rows or less are suitable for OLSR. Otherwise an optimization approach, such as a gradient descent model, is more appropriate. 

# The Data Set
The data set used to build this model comes from the Natural Resources Canada website (https://www.nrcan.gc.ca/). This website provides .csv files of new vehicle information for a variety of model years. For this model, data collected for 2021 model year vehicles was used. However, the code can be easily modified to analyze data collected for other model years as well.

# Metrics for the Model
One metric for assessing the accuracy of the model is by examining its coefficient of multiple determination. The coefficient of multiple determination is a decimal number, between 0 and 1, that defines how much of the variability of the response data around its mean the model explains.

In most cases, the higher the coefficient of multiple determination is, the better the model fits the data. This does not necessarily mean that the model will have high out-of-sample accuracy, but it could.

This model has a coefficient of multiple determination of 0.9433. This means that the model can explain 94.33% the variability of the response data around its mean.

# Example

To illustrate what the model is capable of, let's use data from the .csv file provided in this repository. For this example, let's use the data for a 2021 Toyota Tacoma (4WD):

    Welcome to PyBOT New Vehicle Emissions Calculator!
    
    This calculator uses the ordinary least squares approach for 
    multiple linear regression modeling to accurately predict the
    CO2 emissions of newly manufactured vehicles.
    
    This PyBOT was created by Ezekiel Lutz
    
    
    To begin, please enter the engine displacement size of the vehicle in liters (L): 3.5

    Please enter the number of cylinders (#): 6

    Please enter the fuel consumption in liters per 100 kilometers (L/100km): 13


    Based upon the vehicle data entered, the predicted CO2 emissions for this vehicle are expected to be between 253.70 and 280.41 g/km.
    
    
    Would you like to use the calculator again? (Y/N): 
    
The model predicted that the CO2 emissions for this vehicle would be between 253.70 g/km and 280.41 g/km. Looking at the .csv file itself, the vehicle had a measured CO2 emissions of 278.4 g/km. In this case, the measured value fell within the model's predicted range and was successful in predicting the CO2 emissions of the vehicle. 
