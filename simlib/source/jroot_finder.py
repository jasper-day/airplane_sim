"Jasper's iterable-based root-finding library"

from root_finder import minimizing_function, get_system_parameters
import math



def converge_rel_error(iterable, e_c, max_terms = 1_000_000_000):
    """Converge an iterable until relative error is less than e_c

Given an iterable that converges on a number, computes successive values of the iterable until the fractional error term `e_a` is less than `e_c`

`e_a` is calculated as the relative difference between terms: `e_a` = (`A_curr` - `A_prev`)/(`A_curr`)

Halts if max_terms is exceeded (default value 1E9)

Returns a tuple `(result, terms)` of the result and the number of terms in the series taken to get there.
    """
    curr = next(iterable)
    # Test whether relative fractional error is acceptable
    pred = lambda A_prev, A_curr: abs((A_curr - A_prev)/A_curr) < abs(e_c)
    for terms in range(1, max_terms):
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return prev, terms
        if pred(prev, curr):
            break
    return curr, terms

def converge_abs_error(iterable, e_c, max_terms=1_000_000_000):
    """Converge a sequence until the absolute error is less than e_c

Given an iterable that converges on a number, computes successive terms until the absolute difference between successive terms is less than some number `e_c`. 

Halts if max_terms is exceeded (default value 1E9)

Returns a tuple `(result, terms)` of the result and the number of terms in the series taken to get there.
    """
    curr = next(iterable)
    pred = lambda A_prev, A_curr: abs(A_curr - A_prev) < abs(e_c)
    for terms in range(1, max_terms):
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return curr, terms
        if pred(prev, curr):
            break
    return curr, terms

def abs_errors_seq(iterable):
    """Get a sequence of absolute errors

Given an iterable, returns a sequence of absolute errors (the difference between successive terms of the sequence)
    """
    curr = next(iterable)
    while True:
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return curr - prev
        yield curr - prev

def rel_errors_seq(iterable):
    """Get a sequence of relative errors

Given an iterable, returns a sequence of relative errors
    """
    curr = next(iterable)
    error = lambda prev, curr: abs((curr - prev)/curr)
    while True:
        prev = curr
        try:
            curr = next(iterable)
        except StopIteration:
            return error(prev, curr)
        yield error(prev, curr)


def converge_terms(iterable, n):
    """Given an iterable, returns the value after `n` iterations."""
    curr = next(iterable)
    for terms in range(1, n):
        try:
            curr = next(iterable)
        except StopIteration:
            break
    return (curr, terms)

# Math Utilities

def sign(x):
    """Returns the sign of a number x

    Raises TypeError on failure"""
    try:
        if x == 0:
            # Note: sign(-0) = 0
            return 0
        if x > 0:
            return 1
        if x < 0:
            return -1
    except TypeError:
        raise TypeError(f"Attempted to calculate sign of {x}")

def test_endpoints(y1, y2):
    if sign(y1) == sign(y2):
        raise Exception(f"Cannot find root between {x1} and {x2}: function has same sign")

def bisection_seq(f, x1, x2):
    """Calculate roots by bisection method

Given a function `f` of one variable and points `x1` and `x2` where `f(x)` has opposite signs, returns a sequence of points that converges to a root using the bisection method."""
    y1, y2 = f(x1), f(x2)
    test_endpoints(y1, y2)
    while True:
        midpoint = (x1 + x2)/2
        y_midpoint = f(midpoint)
        if y_midpoint == 0:
            return midpoint
        if sign(y_midpoint) != sign(y1):
            x1, x2 = x1, midpoint
            # avoid unnecessary function calls
            y1, y2 = y1, y_midpoint 
        else:
            # guaranteed to be one or the other
            x1, x2 = midpoint, x2
            y1, y2 = y_midpoint, y2
        yield midpoint

def false_pos_seq(f, x1, x2):
    """Calculate roots by false position method

Given a function `f` of one variable and points `x1` and `x2` where `f(x)` has opposite signs, returns a sequence of points that converges to a root using the false position method."""
    y1, y2 = f(x1), f(x2)
    test_endpoints(y1, y2)
    while True:
        false_root = (x1 * y2 - x2 * y1)/(y2 - y1)
        y_false_root = f(false_root)
        if y_false_root == 0:
            return false_root
        if sign(y_false_root) != sign(y1):
            x1, x2 = x1, false_root
            y1, y2 = y1, y_false_root
        else:
            x1, x2 = false_root, x2
            y1, y2 = y_false_root, y2
        yield false_root

def false_illinois_seq(f, x1, x2):
    """Modified false position root solver, using the Illinois algorithm
    
    See https://en.wikipedia.org/wiki/Regula_falsi#The_Illinois_algorithm"""
    y1, y2 = f(x1), f(x2)
    test_endpoints(y1, y2)
    y_false_root_prev = 0
    while True:
        false_root = (x1 * y2  - x2 * y1)/(y2 - y1)
        y_false_root = f(false_root)
        if y_false_root == 0:
            return false_root
        if sign(y_false_root) != sign(y1):
            x1, x2 = x1, false_root
            if sign(y_false_root_prev) == sign(y_false_root):
                # Illinois addition: halve retained root
                y1, y2 = 0.5*y1, y_false_root
            else:
                y1, y2 = y1, y_false_root
        else:
            x1, x2 = false_root, x2
            if sign(y_false_root_prev) == sign(y_false_root):
                # Illinois addition
                y1, y2 = y_false_root, 0.5*y2
            else:
                y1, y2 = y_false_root, y2
        yield false_root
        y_false_root_prev = y_false_root
        
def false_bjorck_seq(f, x1, x2):
    """Modified false position root solver, using the Anderson-Bjorck algorithm
    
See: https://en.wikipedia.org/wiki/Regula_falsi#Anderson%E2%80%93Bj%C3%B6rck_algorithm"""
    y1, y2 = f(x1), f(x2)
    test_endpoints(y1, y2)
    while True:
        false_root = (x1 * y2  - x2 * y1)/(y2 - y1)
        y_false_root = f(false_root)
        if y_false_root == 0:
            return false_root
        if sign(y_false_root) != sign(y1):
            x1, x2 = x1, false_root
            mod_term_p = 1 - y_false_root/y2
        else:
            x1, x2 = false_root, x2
        yield false_root

def find_root_rel_error(f, x1, x2, e_c, method, **kwargs):
    seq = method(f, x1, x2)
    return converge_rel_error(seq, e_c, **kwargs)

def find_root_abs_error(f, x1, x2, e_c, method, **kwargs):
    seq = method(f, x1, x2)
    return converge_abs_error(seq, e_c, **kwargs)

def find_root_num_terms(f, x1, x2, method, nterms):
    seq = method(f, x1, x2)
    return converge_terms(seq, nterms)

def find_system(V, gamma, method, err_type, e, **kwargs):
    """Given velocity and flight path angle, calculates the angle of attack
    Input:
    method: root finding method to use
    err_type: error convergence to use (relative, absolute, nterms)
    e: error threshold or number of terms"""
    f = minimizing_function(V, gamma)
    alpha, nterms = find_root(f, -math.pi/2 + 0.1, math.pi/2, method, err_type, e, **kwargs)
    system = get_system_parameters(V, gamma, alpha)
    system["nterms"] = nterms
    return system

def find_root(f, x1, x2, method, error_type, e, **kwargs):
    if error_type == "relative" or error_type == "rel":
        return find_root_rel_error(f, x1, x2, e, method, **kwargs)
    elif error_type == "absolute" or error_type == "abs":
        return find_root_abs_error(f, x1, x2, e, method, **kwargs)
    elif error_type == "n" or error_type == "nterms":
        return find_root_num_terms(f, x1, x2, method, e, **kwargs)

methods = {
    "bisection": bisection_seq,
    "false position": false_pos_seq,
    "false position (illinois variation)": false_illinois_seq,
    "false position (anderson-bjorck variation)": false_bjorck_seq
}

err_types = ["absolute", "relative", "nterms"]