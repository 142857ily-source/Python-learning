import numpy as np
import matplotlib.pyplot as plt

def random_walk(steps):
    position = 0
    positions = [0]
    for i in range(steps):
        step = int(np.random.choice([-1, 1]))
        position = position + step
        positions.append(position)
    for k in range (1,steps):
        if positions[k]==0:
            print (k)
    distance=(abs((positions[-1])))
    print (distance)
    return positions 
steps = int(input ("Enter your steps:",))
walk = random_walk(steps)
plt.plot(walk)
plt.show()




