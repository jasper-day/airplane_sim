"User interface commands"

from root_finder import find_system
from airplane_dynamics import deg2rad, dU_dt, find_U_0, find_system_parameters
import numpy as np
from diffeq_solver import rk4_integrate

# U = 18 # Thomas is the oldest member, born 18 July
U = 0 # testing

trim_conditions = {
    "1": find_system(100 + U, 0), # steady level flight
    "2": find_system(100 + U, deg2rad(2)), # climbing flight
    "3": find_system(100 + U, 0), # steady level flight
}

def find_command_array(trim_condition, start_time, end_time, dt):
    t = np.arange(start_time, end_time, dt)
    delta_el = np.ones_like(t) * trim_condition["delta_el"]
    thrust = np.ones_like(t) * trim_condition["Thrust"]
    X = np.array([delta_el, thrust]).T
    return {"t": t, "X": X}


def find_command_step(trim_conditions, time_starts, total_time, dt):
    assert(len(trim_conditions) == len(time_starts))
    time_starts.append(total_time)
    command_arrays = []
    for i in range(len(trim_conditions)):
        trim_condition = trim_conditions[i]
        command_arrays.append(find_command_array(trim_condition, time_starts[i], time_starts[i + 1], dt))
    t = np.empty([0])
    X = np.empty([0,2])
    for command_array in command_arrays:
        t = np.hstack((t, command_array['t']))
        X = np.vstack((X, command_array['X']))
    return {'t': t, 'X': X}

def integrate_system(trim_conditions, time_starts, total_time, dt, starting_altitude=1000):
    command_array = find_command_step(trim_conditions, time_starts, total_time, dt)
    U_0 = find_U_0(trim_conditions[0], starting_altitude)
    U_integrated = rk4_integrate(dU_dt, U_0, command_array['X'], command_array['t'])
    command_array["U"] = U_integrated
    return command_array

if __name__=="__main__":
    print("Comparison: page 14 of project.pdf")
    import matplotlib.pyplot as plt
    U_i = integrate_system([
        trim_conditions['1'], 
        {"Thrust": 2755.17, "delta_el": -0.0572}], [0, 100], 300, 0.1, starting_altitude=2000)
    from pprint import pformat
    print(f"""
    Initial system: {pformat(find_system_parameters(U_i['U'][0]))}
    Initial commands: {pformat(trim_conditions['1'])}
    """)
    extract_param = lambda name: [find_system_parameters(U)[name] for U in U_i["U"]]
    extract_command = lambda name: [X[0] if name=="delta_el" else X[1] for X in U_i["X"]]
    fig, axs = plt.subplots(4,2)
    axs[0,0].plot(U_i["t"], extract_param("u_B"))
    axs[0,0].set_ylabel("$u_B$")
    axs[0,1].plot(U_i["t"], extract_param("w_B"))
    axs[0,1].set_ylabel("$w_B$")
    axs[1,0].plot(U_i["t"], extract_param("q"))
    axs[1,0].set_ylabel("q")
    axs[1,1].plot(U_i["t"], extract_param("theta (deg)"))
    axs[1,1].set_ylabel(r'$\theta$')
    axs[2,0].plot(U_i["t"], extract_param("gamma (deg)"))
    axs[2,0].set_ylabel(r"$\gamma$")
    axs[2,1].plot(U_i["t"], extract_param("z_B"))
    axs[2,1].set_ylabel(r"$z_B$")
    axs[3,0].plot(U_i["t"], extract_param("alpha (deg)"))
    axs[3,0].set_ylabel(r"$\alpha$")
    axs[3,1].plot(U_i["t"], extract_param("z_E"))
    axs[3,1].set_ylabel(r"$z_E$")
    fig.tight_layout()
    plt.show()