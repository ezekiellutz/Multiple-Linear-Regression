'''
Author: Ezekiel Lutz
Contact Info: xxZeke77xx@gmail.com
Time: 12:05 UTC
Date: 06-03-2021
Data Source: https://www.nrcan.gc.ca/sites/nrcan/files/oee/files/csv/MY2021%20Fuel%20Consumption%20Ratings.csv
Recommended IDE: Spyder 4.2.5 [conda (Python 3.8.8)]
NOTE: Compatability issues with this code are known to exist, please use the IDE listed above.
'''

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from sklearn import linear_model


#opens the .csv file with relevant vehicle information and places it in a dataframe (NOTE: .csv file must be saved in the same directory as this script)
with open ('MY2021 Fuel Consumption Ratings.csv','r') as csv_file:
    df = pd.read_csv(csv_file)
    df = df[['Engine Size','Cylinders','Fuel Consumption','CO2 Emissions']]

#formats the dataframe to only include cells with data
df = df.iloc[1:884]

#defines the datatype in each column of the dataframe
df = df.astype({'Engine Size': float, 'Cylinders': int, 'Fuel Consumption': float, 'CO2 Emissions': int})

#creates a histogram with all of the data that will be used to build the models
df.hist(figsize=(7,5))
plt.suptitle('THE ENTIRE DATASET: VISUALIZED')
plt.show()

#creates variables to hold the results of the following 'for' loop
theta_0 = []
theta_1 = []
theta_2 = []
intercept = []
CoMD = []

#prints a wait message to the console prior to building the model
print('\nOne moment, please wait while the regression model is being built...\n')

#creates a loop to find the value of theta 0, theta 1, and theta 2 for 5000 iterations of the model
#also finds the variance score of the model for 5000 iterations
for i in range (5000):
    mask = np.random.rand(len(df)) < 0.8
    train = df[mask]
    test = df[~mask]
    mlr_model = linear_model.LinearRegression() 
    x_train = np.asanyarray(train[['Engine Size','Cylinders','Fuel Consumption']])
    y_train = np.asanyarray(train[['CO2 Emissions']])
    mlr_model.fit(x_train,y_train)
    coeff = mlr_model.coef_
    inter = mlr_model.intercept_
    theta_0.append(coeff[0,0])
    theta_1.append(coeff[0,1])
    theta_2.append(coeff[0,2])
    intercept.append(inter)
    CoMD.append(mlr_model.score(x_train,y_train))

#finds the average value for theta 0, theta 1, theta 2 and variance score
avg_theta_0 = (sum(theta_0))/len(theta_0)
avg_theta_1 = (sum(theta_1))/len(theta_1)
avg_theta_2 = (sum(theta_2))/len(theta_2)
avg_intercept = (sum(intercept))/len(intercept)
avg_CoMD = round(sum(CoMD)/len(CoMD), 4)
avg_CoMD_percent = avg_CoMD*100

#creates a function to allow the user to use the model to predict CO2 emissions
def calculator():
    
    startup_message = """\
\nWelcome to PyBOT New Vehicle Emissions Calculator!
    
    This calculator uses the ordinary least squares approach for 
    multiple linear regression modeling to accurately predict the
    CO2 emissions of newly manufactured vehicles.
    
    This PyBOT was created by Ezekiel Lutz
    """
    print(startup_message)
    time.sleep(4)
    x_0 = input('To begin, please enter the engine displacement size of the vehicle in liters (L): ')
    time.sleep(1)
    x_1 = input('\nPlease enter the number of cylinders (#): ')
    time.sleep(1)
    x_2 = input('\nPlease enter the fuel consumption in liters per 100 kilometers (L/100km): ')
    predicted_emissions = (float(x_0)*avg_theta_0)+(float(x_1)*avg_theta_1)+(float(x_2)*avg_theta_2)+float(avg_intercept)
    pred_lower = round(predicted_emissions*0.95, 2)
    pred_upper = round(predicted_emissions*1.05, 2)
    time.sleep(2)
    results_message = f"""\
\n\nBased upon the vehicle data entered, the predicted CO2 emissions for this vehicle are expected to be between {pred_lower} and {pred_upper} g/km.
    """
    print(results_message)
    time.sleep(4)
    while True:
        response = input('Would you like to use the calculator again? (Y/N): ')
        if response == 'Y':
            print('\n')
            time.sleep(2)
            return calculator()
        if response == 'y':
            print('\n')
            time.sleep(2)
            return calculator()
        if response == 'Yes':
            print('\n')
            time.sleep(2)
            return calculator()
        if response == 'yes':
            print('\n')
            time.sleep(2)
            return calculator()
        if response == 'YES':
            print('\n')
            time.sleep(2)
            return calculator()
        if response == 'N':
            time.sleep(1)
            break
        if response == 'n':
            time.sleep(1)
            break
        if response == 'No':
            time.sleep(1)
            break
        if response == 'no':
            time.sleep(1)
            break
        if response == 'NO':
            time.sleep(1)
            break
        else:
            time.sleep(1)
            print('\nWell that was not an applicable response! Please try again!')

#calls the function to predict CO2 emissions based on user input
calculator()

#prints an exit message to the console
print('\nThank you for using this calculator!')
time.sleep(1.5)
print('\nGoodbye!')
time.sleep(10)
print('\nAre you still there?')
time.sleep(5)
print('\nWell, since you are still here, let me discuss the model itself in more detail...')
time.sleep(3)
metrics_message = f"""\
\nThe model had a coefficient of multiple determination of {avg_CoMD}. This means that the model explains {avg_CoMD_percent}% of the variability of the response data around its mean. 

In most cases, the higher the coefficient of multiple determination is, the better the model fits the data. This does not necessarily imply that the model will have high out-of-sample accuracy, but it could.
    """
print(metrics_message)



