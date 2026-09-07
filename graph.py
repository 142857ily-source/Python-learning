import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 1000)
y = np. cos(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("y = cos(x)")
plt.grid()
plt.show()


h = 0.1
t = np.arange(0, 5, h)

y = [1]

for i in range(len(t) - 1):
    new_y = y[i] - h * y[i]
    y.append(new_y)

plt.plot(t, y)
plt.xlabel("t")
plt.ylabel("y")
plt.title("Solution of y' = -y")
plt.grid()

plt.show()