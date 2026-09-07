import numpy as np
import matplotlib.pyplot as plt

def random_walk(steps):
    position = 0
    positions = [0]
    for i in range(steps):
        step = int(np.random.choice([-1, 1]))
        position = position + step
        positions.append(position)
    k_list=[0]
    for k in range (1,steps):
        if positions[k]==0:
            k_list.append(k)
    print (k_list)
    displacement=(abs((positions[-1])))
    print (f"displacement={displacement}")
    return positions 
steps = int(input ("Enter your steps:",))
walk = random_walk(steps)
plt.plot(walk)
plt.show()





