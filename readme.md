# How to Use This Repository

- Install Git
    - For apple users: Included in Apple development pack
    - Should be included in Windows and Linux by default
        - Windows: `winget install Git.Git` or download from online
    - Check installed with `git --version` in terminal
- Commands:
    1. Go to the directory where you want to copy the files to (`cd ~/Documents/` or similar) and run
      `git clone https://github.com/jasper-day/airplane_sim` to copy the assignment into a new folder
    1. Before starting to work: `git pull` to update to the latest version of the code
    2. After making changes: `git add -A` to add your work to the index, then `git commit -a` to make a new commit (you'll be prompted to write a commit message - say what changes you've made)
    3. To make your work seen by everyone else: `git push` to push to github.

# Tasks

- Coding
    - Curve fitting (linear and polynomial) for experimental data
        - Mehmet
        - Kaartic
    - Differential Equations numerical solver with state variables
        - Thomas
        - Jasper
        - Niketa
    - Equation solver (root finder) for trim conditions
        - Shanilka
        - Xavier
- User Interface
    - Graphs and charts
    - Input desired values, commands
    - Would be really nice to have a GUI application
- Project Report

# Thomas has been here :)
# niketa was here :)
# Xaier here

# Files in this repository

Files containing the airplane characteristics, aerodynamics, and the environment:
- aero_table.py
    - python files with the aerodynamics coefficients at discrete values of the angle of attack alpha and elevator angle delta_el
- env.py
    - Gravity and air density
- vehicle.py
    - Some airplane characteristics (Sref, airfoil chord, moment of inertia, mass) 

Code files:
- aero_analytical_build_ToBeCompleted.py


# Design Project Tasks

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
