import numpy as np
import matplotlib.pyplot as plt
import math

n=int(input(f'Enter your input:'))
x=np.random.random(n)
y=np.random.random(n)

def monte_carlo(x,y):
    count=0
    for i,j in zip(x,y):
        if (i**2 + j**2)<1:
            count+=1
    return count
count=monte_carlo(x,y)
pi=4*count/n
print (f"monte_carlo_pi={pi}")
print (f'Error={abs(100*(pi - math.pi)/math.pi)}%')

inside = x**2 + y**2 < 1
plt.scatter(x[inside], y[inside], s=2)
plt.scatter(x[~inside], y[~inside], s=2)
theta = np.linspace(0, np.pi/2, 100)
plt.plot(np.cos(theta), np.sin(theta))
plt.axis("equal")
plt.show()





