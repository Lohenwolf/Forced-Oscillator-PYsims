# Forced Oscillator Phase Space Simulation

## Overview
This repository contains a brief Python simulation of a forced harmonic oscillator, specifically designed to visualize and compare the behavior of **rational** versus **irrational** frequency ratios in phase space.

The project demonstrates a fundamental concept in nonlinear dynamics:
* **Rational Frequency:** The trajectory repeats itself, forming a closed loop.
* **Irrational Frequency:** The trajectory is quasi-periodic; it never closes and eventually fills the phase space (ergodicity).

## Maths
The simulation models the position $x(t)$ as a superposition of a natural frequency $\omega_0$ and a forcing frequency $\omega_f$:

$$x(t) = \cos(\omega_0 t) + \cos(\omega_f t)$$

The velocity $v(t)$ is the time derivative:

$$v(t) = -\omega_0 \sin(\omega_0 t) - \omega_f \sin(\omega_f t)$$

The code compares two scenarios where $\omega_0 = 1.0$:
1.  **Rational Ratio:** $\omega_f = 1.5$ (Closed loop)
2.  **Irrational Ratio:** $\omega_f = \sqrt{2}$ (Space-filling curve)

## Contents

### 1. `ForcedOscillator.py`
A standalone Python script that performs the simulation over a defined number of steps.
* **Output:** Generates a static side-by-side plot of the Phase Space ($x$ vs $v$) for both rational and irrational ratios.
* **Usage:** Best for a quick snapshot of the final trajectory.

### 2. `FOanim.ipynb`
A Jupyter Notebook implementation.
* **Output:** Generates an interactive HTML5 animation using `matplotlib.animation`.
* **Usage:** Best for visualizing *how* the trajectory evolves over time and watching the irrational curve slowly fill the plane.

## Dependencies
To run the code, you will need **Python 3** and the following libraries:

* `numpy`
* `matplotlib`
* `jupyter` (to run the notebook)

```bash
pip install numpy matplotlib jupyter
