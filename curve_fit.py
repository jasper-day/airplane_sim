# Fit curves to data.
# Given: numpy array of linear or quadratic data
# Return: Coefficients of best-fit line

import numpy as np
import math
# import data to fit curves
from aero_table import CD, CL, CM, CL_el, CM_el, alpha, delta_el

def plot_curve_fit(ax, xscatter, yscatter, xline, yline, linelabel=None, xlabel=None, ylabel=None):
    ax.scatter(xscatter, yscatter, label='Data')
    ax.plot(xline, yline, color='red', label=linelabel)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

def fit_curve(xdata, ydata, degree):eeee
    # fixme!
    return np.polyfit(xdata,ydata, degree)


