"User interface commands"

from simlib.root_finder import find_system
from simlib.dynamics import deg2rad, dU_dt, find_U_0, find_system_parameters
import numpy as np
from simlib.diffeq import rk4_integrate

U = 18 # Thomas is the oldest member, born 18 July

trim_conditions = {
    "1": find_system(100 + U, 0), # steady level flight
    "2": find_system(100 + U, deg2rad(2)), # climbing flight
    "3": find_system(100 + U, 0), # steady level flight
}

def find_command_fn(trim_conditions, time_starts, total_time, dt):
    assert(len(trim_conditions) == len(time_starts))
    # time_starts is monotonically increasing
    assert(np.all(np.sign(np.diff(time_starts))))
    time_starts.append(total_time)
    X_commands = []
    def find_trim(t):
        for i in range(len(trim_conditions)):
            if time_starts[i] <= t < time_starts[i + 1]:
                return [trim_conditions[i]["delta_el"], trim_conditions[i]["Thrust"]]
        raise RuntimeError(f"Out of bounds access at t={t}")
    return find_trim

def integrate_system(trim_conditions, time_starts, total_time, dt, starting_altitude=1000):
    X = find_command_fn(trim_conditions, time_starts, total_time, dt)
    t = np.arange(time_starts[0], total_time, 0.1)
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
    fig, axs = plt.subplots(4,2)
    make_sample_plot(fig,axs)
    plt.show()