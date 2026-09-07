import numpy as np
import matplotlib.pyplot as plt


x=int(input(f'Enter your initial value:',))
positions=[x]
def f(x):
    while x!=1:
        if x % 2 == 0:
            x=x//2
        else:
            x=3*x+1
        positions.append (x)
f(x)
print(len(positions))
print(max(positions))
plt.plot(positions)
plt.show()

