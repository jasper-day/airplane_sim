from aero_table import CD, CL, CM, CL_el, CM_el, alpha, delta_el
import numpy as np
import math
import matplotlib.pyplot as plt

CD_wing=CD
CL_wing=CL
CM_wing=CM

# generate x and y
x = delta_el
y = CM_el

# Direct least square regression for a single unknown
a = np.dot(np.dot(np.linalg.inv(np.dot(x[:, np.newaxis].T, x[:, np.newaxis])), x[:, np.newaxis].T), y)

# Create a dictionary with the variable name and its value
coefficients = {'CM_delta_el': a[0]}

# Print the variable name and its value
for var_name, var_value in coefficients.items():
    print(f"{var_name}: {var_value}")

# plot the results
plt.figure(figsize=(10, 8))
plt.plot(x, y, 'b.')
plt.plot(x, a[0] * x, 'r')  # Removed the "+ a[1]" part
plt.xlabel('Delta el')
plt.ylabel('CM_el')
plt.show()