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


# Command for manoeuvre
com_Thrust   = 1.0
com_delta_el = 0.0
