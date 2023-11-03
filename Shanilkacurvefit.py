# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:49:21 2023

@author: HP
"""

# Fit curves to data.
# Given: numpy array of linear or quadratic data
# Return: Coefficients of best-fit line

import numpy as np
import math
#Cd=Cd0+KCl^2
import numpy as np
import matplotlib.pyplot as plt

# Sample data
alpha = np.array([-16,-12,-8,-4,-2,0,2,4,8,12])
delta_el  = np.array([-20,-10,0,10,20])

CD_wing = np.array([
    0.115000000000000
  , 0.079000000000000
  , 0.047000000000000
  , 0.031000000000000
  , 0.027000000000000
  , 0.027000000000000
  , 0.029000000000000
  , 0.034000000000000
  , 0.054000000000000
  , 0.089000000000000
  ])


CL_wing = np.array([
   -1.421000000000000
  ,-1.092000000000000
  ,-0.695000000000000
  ,-0.312000000000000
  ,-0.132000000000000
  , 0.041000000000000
  , 0.218000000000000
  , 0.402000000000000
  , 0.786000000000000
  , 1.186000000000000
  ])

CM_wing = np.array([
    0.077500000000000
  , 0.066300000000000
  , 0.053000000000000
  , 0.033700000000000
  , 0.021700000000000
  , 0.007300000000000
  ,-0.009000000000000
  ,-0.026300000000000
  ,-0.063200000000000
  ,-0.123500000000000
  ])

CL_el = np.array([
   -0.051000000000000
  ,-0.038000000000000
  ,                 0
  , 0.038000000000000
  , 0.052000000000000
  ])

CM_el = np.array([
    0.084200000000000
  , 0.060100000000000
  ,-0.000100000000000
  ,-0.060100000000000
  ,-0.084300000000000
  ])


# Degree of the polynomial
degree = 2  # You can change this to fit a polynomial of a different degree

# Fit a polynomial regression model
coefficients = np.polyfit(alpha, CL_wing, degree)

# Create a polynomial regression model function
poly_model = np.poly1d(coefficients)

# Generate a range of x values for the curve
alpha_values = np.linspace(min(alpha), max(alpha), 100)

# Calculate corresponding y values using the polynomial regression model
CL_wing_values = poly_model(alpha_values)

# Plot the data points and the polynomial regression curve
plt.scatter(alpha, CL_wing, label='Data')
plt.plot(alpha_values, CL_wing_values, color='red', label=f'Polynomial Regression (Degree {degree})')
plt.xlabel('alpha')
plt.ylabel('CL_wing')
plt.legend()
plt.show()

# Output the coefficients of the polynomial regression model
print(f"Polynomial Coefficients: {coefficients}")
# Degree of the polynomial

# Degree of the polynomial
degree2 = 2  # You can change this to fit a polynomial of a different degree

# Fit a polynomial regression model
coefficients = np.polyfit(alpha, CM_wing, degree2)

# Create a polynomial regression model function
poly_model = np.poly1d(coefficients)

# Generate a range of x values for the curve
alpha_values = np.linspace(min(alpha), max(alpha), 100)

# Calculate corresponding y values using the polynomial regression model
CM_wing_values = poly_model(alpha_values)

# Plot the data points and the polynomial regression curve
plt.scatter(alpha, CM_wing, label='Data')
plt.plot(alpha_values, CM_wing_values, color='red', label=f'Polynomial Regression (Degree {degree})')
plt.xlabel('alpha')
plt.ylabel('CM_wing')
plt.legend()
plt.show()

# Output the coefficients of the polynomial regression model
print(f"Polynomial Coefficients: {coefficients}")
# Degree of the polynomial




