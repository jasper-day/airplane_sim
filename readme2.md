# SimuPlane
# Project Description
The aim of this project is to simulate the longitudinal dynamics of a small airplane. The airplane encounters aerodynamic forces and moments when in motion, this program provides the facilities to find the trim conditions of the airplane (where all forces are balanced, leading to no change over time), as well as  input commands to the airplane.

This project includes a Graphical User interface (GUI), wherein the user can input the trim conditions and the the flight commands, and obtain the response of the airplane. The response of the system can be a depicted by a series of graphs, in which the user can use a drop down menu to choose their desired graph.

Due to the complexity of this simultaion, various nuerical methods were employed to predict the response of the airplane. Python is used for this simulation, as it has a diverse set of packages and libraris that offer features for different simulation components.  

The GUI is written in PyQt, a binder for the original Qt, which was written in C++. PyQt was chosen for its Python flexibility and its robust Qt framework.

# Files in this repository

Files containing the airplane characteristics, aerodynamics, and the environment:
- aero_table.py
    - python files with the aerodynamics coefficients at discrete values of the angle of attack alpha and elevator angle delta_el
- env.py
    - Gravity and air density
- vehicle.py
    - Some airplane characteristics (Sref, airfoil chord, moment of inertia, mass) 

Code files:
- curve_fit.py
    - Linear and quadratic curve fitting
- diffeq.py
    - Solve ODEs
- root_finder.py
    - Find roots of equations
- command.py
    - User interface commands
- dynamics.py
    - code for the flight mechanics of the airplane
- gui_root_find.py
    - []
- gui_root_finder_iterables.py
    - iterable-based root-finding library with various options
- gui_t_climb.py
    - calculate the time for climb
- plot.py
    - Plotting functionality for various questions
- main.py
    - []     

# How to use the project
# Credits
This project was coded by Jasper Day, Kaartic Ramana Vengidesh, Mehmet Tasman, Niketa Silva Walichchoru Evayage, Shanilka Kannangara, Thomas Wang and Xavier Yi.
# Design Project Tasks

- Coding
    - Curve fitting (linear and polynomial) for experimental data (part 1 of part A)
        - Input: table of values (e.g., from `aero_tables.py`)
        - Output: list of coefficients for a linear or quadratic line of best fit
        - File: `curve_fit.py`
        - Method: Linear regression

    - Differential Equations numerical solver with state variables (part 3 of part A)
        - Input: State change equation, commands
        - Output: 2D array of state integrated through time
        - File: `diffeq_solver.py`
        - Method: Runge-Kutta

    - Equation solver (root finder) for trim conditions (part 2 of part A)
        - Input: Multivariate equation
        - Output: Roots of that equation
        - File: `root_finder.py`
        - Method: Newton-Raphson

- User Interface
    - Graphs and charts
    - Input desired values, commands
    - Would be really nice to have a GUI application
- Project Report

## Part A. 

Develop python code with the following functionality

- Compute the coefficients for the simplified models of CL, CD, and CM from a set of
experimental data.
- Trim the airplane: For given values of the velocity V and flight path angle γ, compute the angle of attack α, the value of the commands T (thrust) and δE (elevator angle), and all the other state variables. 
- Solve the 3 DoF equations of motion of the airplane. The simulation should start from a trim initial condition and then compute the response of the system to time-dependent commands such as a variation of the thrust T and elevator angle δE , or a combination of the two. 
## Part B1.

Use the python code you developed to perform the following engineering design
simulations:

- Trim the airplane for a range of values of the velocity Vmin < V < Vmax and flight path angle γmin < γ < γmax to find the value of the commands T (thrust) and δE (elevator angle) for several combinations of V and γ in the range above. Plot the T and δE vs V and γ. 
- Pay attention at the min and max values of the ranges for V and γ. Limit the ranges such that physical constrains are not violated. For example, the thrust T should always be positive, α and δE should be in the ranges of the experimental data provided for the aerodynamics coefficients CL, CD, and CM, etc. 

## Part B2. 

Use your python code to analyse the climb from horizontal flight at an altitude h1 = 1000m to horizontal flight at another altitude h2 = 2000m.
- First, consider the following 3 equilibrium conditions:
    - Trim condition 1: Consider a trim condition at constant altitude h1 = 1000m (flight path angle γ = 0) with a velocity V = (100 + U) m/s, where U is the day of birth (1-31) of the oldest member of your group.
        - In this conditions the commands are T1 and δE1.
    - Trim condition 2: Compute another trim condition with the same velocity and a flight path angle γ = 2 degrees.
        -  In this conditions the commands are T2 and δE2.
    - Trim condition 3: Same as Trim condition 1, but at different altitude h2 = 2000m (in our model, altitude has no effect on trim)
        - In this conditions the commands are T3 = T1 and δE3 = δE1.
- Then:
    - Simulate the system for 10 seconds starting from Trim condition 1 (commands at T1 and δE1)
    - Change commands to T2 and δE2 and simulate the system for an additional interval of tclimb
seconds.
    - Change commands to T3 and δE3 and simulate the system for a time long enough that
oscillations are dumped.
- Question: how long should the commands T2 and δE2 be applied (in other words, find the appropriate tclimb), such that the altitude at the end of the simulation is approximately h2 = 2000m?
- To this end, run steps 1,2,3 several times for different values of tclimb to identify the
appropriate tclimb.

## Part C

Develop a user interface that allows the following:

- Prescribe a desired flight trim condition (the velocity V and flight path angle γ) and see the resulting angle of attack α, the value of the commands T (thrust) and δE (elevator angle).
- Starting from the trim condition computed above, prescribe a step change of commands (T and δE ) and a total solution time, to see the resulting time evolution. For example the software could output the plots of some variables vs time.