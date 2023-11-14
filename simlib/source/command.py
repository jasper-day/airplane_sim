"User interface commands"

from dynamics import deg2rad, dU_dt, find_U_0, find_system_parameters
import numpy as np
from diffeq import rk4_integrate

def find_command_fn(trim_list, time_starts, total_time):
    """Returns a function that gives the correct command at a given time t.
    Input:
    trim_list: list of trim conditions (dictionary with at least "delta_el" and "Thrust")
    time_starts: the time each successive trim condition starts
    total_time: the time the simulation should run for
    Output:
    X: X(t) = [delta_el, Thrust] at time t"""
    assert(len(trim_list) == len(time_starts))
    # time_starts is monotonically increasing
    assert(np.all(np.sign(np.diff(time_starts))))
    time_starts.append(total_time)
    X_commands = []
    def find_trim(t):
        for i in range(len(trim_list)):
            if time_starts[i] <= t < time_starts[i + 1]:
                return [trim_list[i]["delta_el"], trim_list[i]["Thrust"]]
        raise RuntimeError(f"Out of bounds access at t={t}")
    return find_trim

def integrate_system(trim_conditions, time_starts, total_time, dt=0.1, starting_altitude=1000):
    """Integrate a system with step changes in commands.
    Returns:
    {"X": Command function, "U_0": Initial conditions, "U": Integrated state, "t": time step}
    """
    X = find_command_fn(trim_conditions, time_starts, total_time)
    t = np.arange(time_starts[0], total_time, dt)
    U_0 = find_U_0(trim_conditions[0], starting_altitude)
    U_integrated = rk4_integrate(dU_dt, U_0, X, t)
    return {"X": X, "U_0": U_0, "U": U_integrated, "t": t}

extract_param = lambda name: [find_system_parameters(U)[name] for U in U_i["U"]]
extract_command = lambda name: [X[0] if name=="delta_el" else X[1] for X in U_i["X"]]

def make_sample_plot(fig, axs):
    "Plot system results on a 4x2 subplot"
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
    axs[2,1].plot(U_i["t"], extract_param("z_E"))
    axs[2,1].set_ylabel(r"$z_E$")
    axs[3,0].plot(U_i["t"], extract_param("alpha (deg)"))
    axs[3,0].set_ylabel(r"$\alpha$")
    axs[3,1].plot(U_i["t"], extract_param("altitude"))
    axs[3,1].set_ylabel("altitude")
    fig.tight_layout()
    return fig

if __name__=="__main__":
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