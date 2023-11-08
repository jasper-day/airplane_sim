"User interface commands"

from root_finder import find_system
from airplane_dynamics import deg2rad, dU_dt, find_U_0, find_system_parameters
import numpy as np
from diffeq_solver import rk4_integrate

U = 18 # Thomas is the oldest member, born 18 July

trim_conditions = {
    "1": find_system(100 + U, 0), # steady level flight
    "2": find_system(100 + U, deg2rad(2)), # climbing flight
    "3": find_system(100 + U, 0), # steady level flight
}

def find_command_array(trim_condition, start_time, end_time, dt):
    t = np.arange(start_time, end_time, dt)
    delta_el = np.ones_like(t) * trim_condition["delta_el"]
    thrust = np.ones_like(t) * trim_condition["Thrust"]
    X = np.array([delta_el, thrust])
    return {"t": t, "X": X}


def find_command_step(trim_conditions, time_starts, total_time, dt):
    assert(len(trim_conditions) == len(time_starts))
    time_starts.append(total_time)
    command_arrays = []
    for i in range(len(trim_conditions)):
        trim_condition = trim_conditions[i]
        command_arrays.append(find_command_array(trim_condition, time_starts[i], time_starts[i + 1], dt))
    t = np.array([])
    X = np.empty([2,0])
    for command_array in command_arrays:
        t = np.hstack((t, command_array['t']))
        X = np.hstack((X, command_array['X']))
    return {'t': t, 'X': X}

def integrate_system(trim_conditions, time_starts, total_time, dt, altitude=1000):
    command_array = find_command_step(trim_conditions, time_starts, total_time, dt)
    U_0 = find_U_0(trim_conditions[0], altitude)
    U_integrated = rk4_integrate(dU_dt, U_0, command_array['X'].T, command_array['t'])
    command_array["U"] = U_integrated
    return command_array

if __name__=="__main__":
    U_i = integrate_system([trim_conditions['1'], trim_conditions['2']], [0, 5], 10, 0.01)
    plt.plot(U_i["t"], [find_system_parameters(U)["altitude"] for U in U_i["U"].T])
    plt.show()