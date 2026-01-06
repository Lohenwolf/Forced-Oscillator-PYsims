import numpy as np
import matplotlib.pyplot as plt

# --- 1. Simulation parameters ---
t_max = 500         # Duration (increase this value to see the second graph fill out more)
dt = 0.01           # Step size, decrease to increase precision
t = np.arange(0, t_max, dt)

# Natural frequency
w0 = 1.0

# --- 2. Two scenarios ---

# A: Rational ratio (e.g. 3/2 = 1.5)
# The trajectory will repeat and will be a closed line.
wf_rational = 1.5 * w0 

# B: Irrational ratio (e.g. sqrt(2))
# the trajectory will not close and will fill out the space.
wf_irrational = np.sqrt(2) * w0 

# --- 3. Trajectory calculation ---

def motion(w_forced, time_array):
    # x(t) = A*cos(w0*t) + B*cos(wf*t) (let's assume A=1, B=1)
    x = np.cos(w0 * time_array) + np.cos(w_forced * time_array)
    
    # v(t) = derivative of x(t)
    v = -w0 * np.sin(w0 * time_array) - w_forced * np.sin(w_forced * time_array)
    return x, v

x_rat, v_rat = motion(wf_rational, t)
x_irr, v_irr = motion(wf_irrational, t)

# --- 4. visualization ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Rational
ax1.plot(x_rat, v_rat, lw=0.8, color='blue', alpha=0.8)
ax1.set_title(r"Rational ratio ($\omega_f / \omega_0 = 1.5$)" + "\nClosed periodic trajectory")
ax1.set_xlabel("Position $x$")
ax1.set_ylabel("Velocity $v$")
ax1.grid(True, linestyle='--', alpha=0.6)

# Irrational
ax2.plot(x_irr, v_irr, lw=0.5, color='red', alpha=0.6)
ax2.set_title(r"Irrational ratio ($\omega_f / \omega_0 = \sqrt{2}$)" + "\nDense, closed, quasi-periodic trajectory")
ax2.set_xlabel("Position $x$")
ax2.set_ylabel("Velocity $v$")
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()