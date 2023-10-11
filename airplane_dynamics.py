# 3-DOF simulation for airplane
# State vector U is chosen as:
# U[0] = x_B (body-relative forward location)
# U[1] = u_B (body-relative forward velocity)
# U[2] = z_B (body-relative downward location)
# U[3] = w_B (body-relative downward velocity)
# U[4] = theta (angle to the ground)
# U[5] = q (angular velocity, d(theta)/dt)

def dU_dt(U, delta_E, T):
    """
    Given a state, the elevator trim angle, and the thrust T, returns dU_dt
    """
    [x_B, u_B, z_B, w_B, theta, q] = U
