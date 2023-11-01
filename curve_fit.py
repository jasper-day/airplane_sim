# Fit curves to data.
# Given: numpy array of linear or quadratic data
# Return: Coefficients of best-fit line

import numpy as np
import math
# import data to fit curves
from aero_table import CD, CL, CM, CL_el, CM_el, alpha, delta_el
import matplotlib.pyplot as plt

def _plot_curve_fit_helper(ax, xscatter, yscatter, xline, yline, linelabel=None, xlabel=None, ylabel=None):
    ax.scatter(xscatter, yscatter, label='Data')
    ax.plot(xline, yline, color='red', label=linelabel)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

def plot_curve_fit(ax, xdata, ydata, degree, linelabel=None, xlabel=None, ylabel=None):
    coefficients = fit_curve(xdata,ydata,degree)
    poly_model = np.poly1d(coefficients)
    xline = np.linspace(min(xdata), max(xdata), 1000)
    yline = poly_model(xline)
    _plot_curve_fit_helper(ax, xdata, ydata, xline, yline, linelabel=linelabel, xlabel=xlabel, ylabel=ylabel)

def fit_curve(xdata, ydata, degree):
    # fixme!
    return np.polyfit(xdata,ydata, degree)

if __name__ == "__main__":
    fig,axs = plt.subplots(3,2)
    plot_curve_fit(axs[0,0], alpha, CD, 2, xlabel=r"\alpha", ylabel=r"CD")
    plot_curve_fit(axs[1,0], alpha, CL, 1, xlabel=r"\alpha", ylabel=r"CL")
    plot_curve_fit(axs[2,0], alpha, CM, 1, xlabel=r"\alpha", ylabel=r"CM")
    plot_curve_fit(axs[0,1], delta_el,CL_el, 1, xlabel=r"\delta_{el}", ylabel=r"CL_{el}")
    plot_curve_fit(axs[1,1], delta_el, CM_el, 1, xlabel=r"\delta_{el}", ylabel=r"CM_{el}")
    plt.show()
