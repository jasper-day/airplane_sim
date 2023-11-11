import numpy as np
from airplane_dynamics import deg2rad
Vinput = 0
Ginput = 0
U = 21

V = Vinput + U
Gamma = deg2rad(Ginput)

print(f'The input velocity is {V}, and the input velocity is {Gamma}.')

