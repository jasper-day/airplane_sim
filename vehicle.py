# importing modules
import numpy as np
import math

# Airplane Characteristics

# Wing surface
Sref = 20.0  

# airfoil chord
cbar = 1.75 

# Mass of the airplane
acMass = 1300.0 

# Moment of inertia
inertia_yy = 7000

# Commands before trim (only a definitionion, the numbers do not matter)
# After trim, these variable store the trim value
Thrust = 1.0
delta_el = 0.0

# Dummy definition of coeff
# Properly defined should come from curve fitting
# The current values are close, but just placeholders
C_L_0 = 0.1
C_L_alpha = 0.05
C_L_delta_E = 0.0002
C_M_0 = -0.005
C_M_alpha = -0.005
C_M_delta_E = -4e-5
C_D_0 = 0.005
K_CD = 0.02




# Command for manoeuvre
com_Thrust   = 1.0
com_delta_el = 0.0
