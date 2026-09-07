import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def f(t, y):
    return y - t**2 + 1

t = np.linspace(0, 2, 100)

solution = solve_ivp(
    f, # the equation
    [0, 2], # the domain 
    [0.5], # the initial value
    t_eval=t
)

plt.plot(t, solution.y[0])

plt.xlabel("t")
plt.ylabel("y")
plt.title("Solution of the ODE")
plt.grid()

plt.show()