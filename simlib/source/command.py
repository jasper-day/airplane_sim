"User interface commands"

from dynamics import deg2rad, dU_dt, find_U_0, find_system_parameters
import numpy as np
from diffeq import rk4_integrate

def find_command_fn(initial_condition, trim_list):
    """Returns a function that gives the correct command at a given time t.
    Input:
    trim_list: list of trim conditions (dictionary with at least "delta_el" and "Thrust")
    time_starts: the time each successive trim condition starts
    total_time: the time the simulation should run for
    Output:
    X: X(t) = [delta_el, Thrust] at time t"""
    time_starts = [trim["t_start"] for trim in trim_list]
    time_starts.append(initial_condition["t_total"])
    # time_starts is monotonically increasing
    assert(np.all(np.sign(np.diff(time_starts))))
    X_commands = []
    def find_trim(t):
        for i in range(len(trim_list)):
            if time_starts[i] <= t < time_starts[i + 1]:
                return [trim_list[i]["delta_el"], trim_list[i]["Thrust"]]
        raise RuntimeError(f"Out of bounds access at t={t}")
    return find_trim

def integrate_system(initial_condition, trim_conditions, dt=0.1, starting_altitude=1000):
    """Integrate a system with step changes in commands.
    Returns:
    {"X": Command function, "U_0": Initial conditions, "U": Integrated state, "t": time step}
    """
    X = find_command_fn(initial_condition, trim_list)
    t = np.arange(time_starts[0], total_time, dt)
    U_0 = find_U_0(initial_condition, starting_altitude)
    U_integrated = rk4_integrate(dU_dt, U_0, X, t)
    return {"X": X, "U_0": U_0, "U": U_integrated, "t": t}

extract_param = lambda name: [find_system_parameters(U)[name] for U in U_i["U"]]
extract_command = lambda name: [X[0] if name=="delta_el" else X[1] for X in U_i["X"]]


if __name__=="__main__":
    from plot import make_sample_plot
    print("Comparison: page 14 of project.pdf")
    import matplotlib.pyplot as plt
    trim_conditions = [
        {"Thrust": 2755.17, "delta_el": -0.0520, "V": 100, "alpha": 0.0164, "gamma": 0},
        {"Thrust": 2755.17, "delta_el": -0.0572},
    ]

    U_i = integrate_system(trim_conditions , [0, 100], 300, 0.1, starting_altitude=2000)
    from pprint import pformat
    print(f"""
    Initial system: {pformat(find_system_parameters(U_i['U'][0]))}
    Initial commands: {pformat(trim_conditions[0])}
    """)
    fig, axs = plt.subplots(4,2)
    make_sample_plot(fig,axs)
    plt.show()
    print(trim_conditions[0])